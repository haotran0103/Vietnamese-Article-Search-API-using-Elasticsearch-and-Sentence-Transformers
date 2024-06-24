from flask import Flask, request, jsonify
from flask_cors import CORS
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

app = Flask(__name__)
CORS(app)

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "DU6CcWicaYxZuMJTHvB+"),
    verify_certs=False
)
index_name = 'articles'

model = SentenceTransformer('model.h5')

def encode_text(text):
    embeddings = model.encode(text, convert_to_tensor=False) 
    return embeddings

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')
    
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    
    query_embedding = encode_text(query)

    bm25_query = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "content"]
            }
        }
    }
    bm25_results = es.search(index=index_name, body=bm25_query)
    
    embedding_query = {
        "query": {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": query_embedding}
                }
            }
        }
    }
    embedding_results = es.search(index=index_name, body=embedding_query)

    combined_results = bm25_results['hits']['hits'] + embedding_results['hits']['hits']
    combined_results = sorted(combined_results, key=lambda x: x['_score'], reverse=True)

    results = []
    for result in combined_results:
        title = result['_source'].get('title')
        if title:
            results.append(title)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
