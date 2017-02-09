import unittest
from benzaiten.graph import GraphBuilder

class GraphTest(unittest.TestCase):
    
    def setUp(self):
        self.builder = GraphBuilder()
        self.short_text = "There's nothing like the laughter of a baby. Unless it's 1 a.m. and you're home alone."
        self.long_text = "Have you ever had a desire to go far, far away, to where there’s not a soul, to be alone? If yes, then you’re extremely clever, and scientists have something to say about it. Scientists from Singapore Management University and the London School of Economics and Political Science conducted a study to find a connection between the place where people live and how satisfied they are with their lives. It turned out that the higher the level of intelligence people living in big cities have, the less happy they are. While most people feel happier when they’re surrounded by friends, highly intelligent individuals are more comfortable being alone. Why does it happen? The scientists suggest that we feel uncomfortable in large communities since our brain is evolutionarily adapted to work in groups of no more than 150 people. Which means the smarter a person is, the more uncomfortable they feel in large communities. Friendship makes us happy, satisfies our psychological need for affection, gives a feeling of being needed, and provides an opportunity to share experiences. However, people with high intelligence have an inverse relationship: clever people feel happier being alone, not when surrounded by other people — even good friends."
        
    def test_build_short_text(self):
        graph = self.builder.buildGraph(self.short_text)
        self.assertEqual(2, len(graph.verteces))
    
    def test_k_highest_short(self):
        graph = self.builder.buildGraph(self.short_text)
        self.assertEqual(["There's nothing like the laughter of a baby.", "Unless it's 1 a.m. and you're home alone."], graph.k_highest(10))
    
    def test_order_of_k_highest_sentences_long_text(self):
        _summarizer = TextRankSummarizer(k_sentences = 3)
        summarized_text = _summarizer.summarize(self.long_text)
        expected_text = "Scientists from Singapore Management University and the London School of Economics and Political Science conducted a study to find a connection between the place where people live and how satisfied they are with their lives. The scientists suggest that we feel uncomfortable in large communities since our brain is evolutionarily adapted to work in groups of no more than 150 people. However, people with high intelligence have an inverse relationship: clever people feel happier being alone, not when surrounded by other people — even good friends."

        summarized_sentences = summarized_text.split(".")
        expected_sentences = expected_text.split(".")

        self.assertEqual(len(expected_text), len(summarized_text))
        self.assertEqual(expected_sentences[0], summarized_sentences[0])
        self.assertEqual(expected_sentences[1], summarized_sentences[1])
        self.assertEqual(expected_sentences[2], summarized_sentences[2])
        self.assertEqual(expected_text, summarized_text)
    
    def test_vertexes(self):
        sentences = ["There's nothing like the laughter of a baby.", "Unless it's 1 a.m. and you're home alone."]
        verteces = self.builder._create_verteces(sentences)
        for vertex in verteces:
            self.assertTrue(vertex.sentence in sentences)
            self.assertEqual(1, len(vertex.connected))
