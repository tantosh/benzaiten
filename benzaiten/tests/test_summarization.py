import os
import unittest

from benzaiten.graph import GraphNode
from benzaiten.summarization import TextRankSummarizer

class SummarizationTest(unittest.TestCase):
    
    def setUp(self):
        self.summarizer = TextRankSummarizer()
    
    def test_summarize_short_text(self):
        text = "Graph-based ranking algorithms are essentially a way of deciding the importance of a vertex within a graph, based on global information recursively drawn from the entire graph. The basic idea implemented by a graph-based ranking model is that of 'voting' or 'recommendation'"
        #the given text is already short
        self.assertEqual(len(text), len(self.summarizer.summarize(text)))
    
    def test_calculate_connected(self):
        node1 = GraphNode('One', 2.5)
        node2 = GraphNode('Two', 0.5)
        node1.connect(node2, 1.0)
           
        connected_weight = self.summarizer._calculate_connected_weight(node1.connected)
        self.assertEqual(0.5, connected_weight)
        