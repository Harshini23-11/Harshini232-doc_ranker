import unittest

from tfidf_ranker import load_documents, rank_documents


class TestTFIDFRanker(unittest.TestCase):

    def test_document_count(self):
        documents = load_documents()
        self.assertEqual(len(documents), 30)

    def test_results_count(self):
        documents = load_documents()
        results = rank_documents("solar energy", documents)
        self.assertEqual(len(results), 30)

    def test_results_are_sorted(self):
        documents = load_documents()
        results = rank_documents("renewable energy", documents)

        scores = [score for _, score in results]

        self.assertEqual(
            scores,
            sorted(scores, reverse=True)
        )

    def test_solar_energy_ranking(self):
        documents = load_documents()
        results = rank_documents("solar energy", documents)

        highest_document, highest_score = results[0]

        self.assertEqual(
            highest_document,
            "document03.txt"
        )

        self.assertGreater(highest_score, 0)

    def test_agriculture_ranking(self):
        documents = load_documents()
        results = rank_documents("agriculture", documents)

        highest_document, highest_score = results[0]

        self.assertEqual(
            highest_document,
            "document01.txt"
        )

        self.assertGreater(highest_score, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)