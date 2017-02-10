import os
import unittest

from benzaiten.graph import GraphNode
from benzaiten.summarization import TextRankSummarizer

class SummarizationTest(unittest.TestCase):
    
    def setUp(self):
        self.short_text =  "Graph-based ranking algorithms are essentially a way of deciding the importance of a vertex within a graph, based on global information recursively drawn from the entire graph. The basic idea implemented by a graph-based ranking model is that of 'voting' or 'recommendation'."
        self.long_text = "Have you ever had a desire to go far, far away, to where there’s not a soul, to be alone? If yes, then you’re extremely clever, and scientists have something to say about it. Scientists from Singapore Management University and the London School of Economics and Political Science conducted a study to find a connection between the place where people live and how satisfied they are with their lives. It turned out that the higher the level of intelligence people living in big cities have, the less happy they are. While most people feel happier when they’re surrounded by friends, highly intelligent individuals are more comfortable being alone. Why does it happen? The scientists suggest that we feel uncomfortable in large communities since our brain is evolutionarily adapted to work in groups of no more than 150 people. Which means the smarter a person is, the more uncomfortable they feel in large communities. Friendship makes us happy, satisfies our psychological need for affection, gives a feeling of being needed, and provides an opportunity to share experiences. However, people with high intelligence have an inverse relationship: clever people feel happier being alone, not when surrounded by other people — even good friends."

    def test_summarize_short_text(self):
        self.assertEqual(len(self.long_text), len(TextRankSummarizer().summarize(self.long_text)))
    
    def test_summarize_long_text(self):
        summarized_text = TextRankSummarizer(k_sentences = 3).summarize(self.long_text)
        expected_text = "Scientists from Singapore Management University and the London School of Economics and Political Science conducted a study to find a connection between the place where people live and how satisfied they are with their lives. The scientists suggest that we feel uncomfortable in large communities since our brain is evolutionarily adapted to work in groups of no more than 150 people. Which means the smarter a person is, the more uncomfortable they feel in large communities."
        
        self.assertEqual(len(expected_text), len(summarized_text))
        self.assertEqual(expected_text, summarized_text)
    
    def test_order_of_sentences_summarize_long_text(self):
        summarized_text = TextRankSummarizer(k_sentences = 3).summarize(self.long_text)
        expected_text = "Scientists from Singapore Management University and the London School of Economics and Political Science conducted a study to find a connection between the place where people live and how satisfied they are with their lives. The scientists suggest that we feel uncomfortable in large communities since our brain is evolutionarily adapted to work in groups of no more than 150 people. Which means the smarter a person is, the more uncomfortable they feel in large communities."
        
        summarized_sentences = summarized_text.split(".")
        expected_sentences = expected_text.split(".")

        self.assertEqual(len(expected_text), len(summarized_text))
        self.assertEqual(expected_sentences[0], summarized_sentences[0])
        self.assertEqual(expected_sentences[1], summarized_sentences[1])
        self.assertEqual(expected_sentences[2], summarized_sentences[2])
        self.assertEqual(expected_text, summarized_text)
    
    def test_calculate_connected(self):
        node1 = GraphNode('One', 0, 2.5)
        node2 = GraphNode('Two', 1, 0.5)
        node1.connect(node2, 1.0)
           
        connected_weight = TextRankSummarizer()._calculate_connected_weight(node1.connected)
        self.assertEqual(0.5, connected_weight)
        