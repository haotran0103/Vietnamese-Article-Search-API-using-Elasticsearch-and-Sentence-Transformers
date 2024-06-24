
# Vietnamese Article ElasticSearch API

This project provides an API for searching Vietnamese articles using Elasticsearch and Sentence Transformers. The system combines BM25 search and embedding-based search to deliver accurate and semantically relevant search results.

## Features

- Search for articles based on titles and content.
- Return a list of article titles that match the search query.
- Use a combination of BM25 and vector embeddings to improve search accuracy.

## Technology Stack

- Python
- Flask
- Elasticsearch
- Sentence Transformers
- PyVi (for Vietnamese NLP)

## Installation

### Requirements

- Python 3.10 or higher
- Elasticsearch 7.x or 8.x

### Install Required Libraries

```sh
pip install flask flask-cors elasticsearch sentence-transformers pyvi
```

## Data Preparation

1. Load and clean your data.
2. Normalize and tokenize Vietnamese text.
3. Remove stop words from the text.

## Model and Index Setup

1. Load the Sentence Transformer model.
2. Encode text data into vector embeddings.
3. Create an Elasticsearch index to store the articles and their embeddings.

## Running the API

1. Connect to Elasticsearch.
2. Create a Flask API to handle search requests.
3. Implement search logic combining BM25 and embedding-based search.

## Usage

### Endpoint

- `POST /search`

### Request Body

```json
{
    "query": "your search query"
}
```

### Response

A list of article titles that match the search query.

### Example

To search for articles, send a POST request to `http://localhost:5000/search` with the following JSON payload:

```json
{
    "query": "Vietnamese cuisine"
}
```

The API will respond with a list of titles of articles that are relevant to the search query.

## Results

The Vietnamese Article Search API effectively combines traditional BM25 search with semantic search using vector embeddings. This approach ensures that search results are both relevant and contextually accurate, providing a better user experience when searching for Vietnamese articles.
![Sentiment Analysis]([https://github.com/haotran0103/sentiment-app/blob/master/image.png](https://github.com/haotran0103/Vietnamese-Article-Search-API-using-Elasticsearch-and-Sentence-Transformers/blob/master/image.png)
