from pathlib import Path
import math
import re
from collections import Counter


DATASET_FOLDER = Path("dataset")


def tokenize(text):
    """Convert text into lowercase words."""
    return re.findall(r"\b[a-zA-Z]+\b", text.lower())


def load_documents():
    """Load all .txt documents from the dataset folder."""
    documents = {}

    for file_path in sorted(DATASET_FOLDER.glob("*.txt")):
        documents[file_path.name] = file_path.read_text(
            encoding="utf-8"
        )

    return documents


def calculate_tf(tokens):
    """Calculate term frequency for a document."""
    word_count = Counter(tokens)
    total_words = len(tokens)

    if total_words == 0:
        return {}

    return {
        word: count / total_words
        for word, count in word_count.items()
    }


def calculate_idf(documents_tokens):
    """Calculate inverse document frequency."""
    total_documents = len(documents_tokens)

    document_frequency = Counter()

    for tokens in documents_tokens.values():
        for word in set(tokens):
            document_frequency[word] += 1

    idf = {}

    for word, frequency in document_frequency.items():
        idf[word] = math.log(
            total_documents / frequency
        )

    return idf


def calculate_tfidf(tf, idf):
    """Calculate TF-IDF vector."""
    return {
        word: tf_value * idf.get(word, 0)
        for word, tf_value in tf.items()
    }


def cosine_similarity(vector1, vector2):
    """Calculate cosine similarity between two vectors."""

    common_words = set(vector1) | set(vector2)

    dot_product = sum(
        vector1.get(word, 0) * vector2.get(word, 0)
        for word in common_words
    )

    magnitude1 = math.sqrt(
        sum(value ** 2 for value in vector1.values())
    )

    magnitude2 = math.sqrt(
        sum(value ** 2 for value in vector2.values())
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)


def rank_documents(query, documents):
    """Rank documents according to the user query."""

    documents_tokens = {
        name: tokenize(text)
        for name, text in documents.items()
    }

    query_tokens = tokenize(query)

    all_tokens = dict(documents_tokens)
    all_tokens["__query__"] = query_tokens

    idf = calculate_idf(all_tokens)

    document_vectors = {}

    for name, tokens in documents_tokens.items():
        tf = calculate_tf(tokens)
        document_vectors[name] = calculate_tfidf(tf, idf)

    query_tf = calculate_tf(query_tokens)
    query_vector = calculate_tfidf(query_tf, idf)

    results = []

    for name, vector in document_vectors.items():
        score = cosine_similarity(query_vector, vector)
        results.append((name, score))

    results.sort(key=lambda item: item[1], reverse=True)

    return results


def main():

    print("=" * 70)
    print("          TF-IDF DOCUMENT RANKING SYSTEM")
    print("=" * 70)

    documents = load_documents()

    print(f"\nTotal documents loaded: {len(documents)}")

    if not documents:
        print("No documents found in the dataset folder.")
        return

    query = input("\nEnter your search query:\nQuery: ").strip()

    if not query:
        print("Query cannot be empty.")
        return

    results = rank_documents(query, documents)

    print("\n" + "=" * 70)
    print("RANKED DOCUMENT RESULTS")
    print("=" * 70)

    for rank, (document, score) in enumerate(results, start=1):
        print(
            f"{rank:2}. {document:<20} Score: {score:.4f}"
        )

    highest_document, highest_score = results[0]
    lowest_document, lowest_score = results[-1]

    print("\n" + "=" * 70)

    print("MOST RELEVANT DOCUMENT")
    print(f"Document : {highest_document}")
    print(f"Score    : {highest_score:.4f}")

    print("\nLEAST RELEVANT DOCUMENT")
    print(f"Document : {lowest_document}")
    print(f"Score    : {lowest_score:.4f}")

    print("=" * 70)


if __name__ == "__main__":
    main()