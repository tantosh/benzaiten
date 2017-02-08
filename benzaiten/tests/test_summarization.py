import unittest
import os
from benzaiten.summarization import TextRankSummarizer

class SummarizationTest(unittest.TestCase):
    
    def setUp(self):
        self.summarizer = TextRankSummarizer()
    
    def test_summarize_short_text(self):
        text = "Graph-based ranking algorithms are essentially a way of deciding the importance of a vertex within a graph, based on global information recursively drawn from the entire graph. The basic idea implemented by a graph-based ranking model is that of 'voting' or 'recommendation'"
        #the given text is already short
        self.assertEqual(text, self.summarizer.summarize(text))
        