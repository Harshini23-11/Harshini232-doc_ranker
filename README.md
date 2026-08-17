# Document Search and Ranking System

## 1. Project Overview

This project implements a simple document search and ranking system using the TF-IDF technique.

The system accepts a user's search query, compares it with a collection of text documents, calculates similarity scores, and ranks the documents according to their relevance.

## 2. Objective

The main objectives of this project are:

- Create a collection of text documents
- Process the document contents
- Convert text into TF-IDF representations
- Compare a search query with the documents
- Rank documents based on similarity
- Identify the most and least relevant documents

## 3. Technologies Used

- Python
- TF-IDF
- Cosine Similarity
- Regular Expressions
- Python Unittest
- Text File Dataset

## 4. Project Structure

```text
232-DOC_RANKER/
│
├── dataset/
│   ├── document01.txt
│   ├── document02.txt
│   ├── ...
│   └── document30.txt
│
├── create_dataset.py
├── tfidf_ranker.py
├── test_tfidf_ranker.py
└── README.md