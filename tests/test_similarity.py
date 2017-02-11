import unittest
from math import log10
from benzaiten.graph import GraphBuilder, GraphNode

class SimilarityTest(unittest.TestCase):
    
    def setUp(self):
        self.builder = GraphBuilder()
    
    def test_similarity_identical(self):
        sentence = "It was a nice day.".split(" ")
        words_count = 5
        expected_similarity = round(words_count / (2 * log10(words_count)), 4)
        
        self.assertEqual(expected_similarity, self.builder._similarity(sentence, sentence))
    
    def test_dissimilar(self):
        first = "It was a nice day."
        other = "Don't be scared of the monsters, just look for them."
        first_words = first.split(" ")
        other_words = other.split(" ")
        
        self.assertEqual(0, self.builder._similarity(first_words, other_words))
        
    
    def test_similarity(self):
        eleanor = "The future belongs to those who believe in the beauty of their dreams.".split(" ")
        michelle = "We want our children — and all children in this nation — to know that the only limit to the height of your achievements is the reach of your dreams and your willingness to work for them.".split(" ")
        malania = "We want our children in this nation to know that the only limit to your achievements is the strength of your dreams and your willingness to work for them.".split(" ")
        
        similarity_similar = self.builder._similarity(michelle, malania)
        similarity_not_so_similar = self.builder._similarity(michelle, eleanor)
        
        self.assertGreater(similarity_similar, similarity_not_so_similar)
    
    def test_extract_words(self):
        self.assertCountEqual(["It", "was", "a", "nice", "day"], GraphNode("It was a nice day.", 0).words)