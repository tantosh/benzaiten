import unittest
from benzaiten.graph import GraphBuilder

class SentenceExtractionTest(unittest.TestCase):
    
    def setUp(self):
        self.builder = GraphBuilder()
    
    def test_two_sentences_fullstop(self):
        sentences = self.builder._extract_sentences("History is a wheel. The nature of man is fundamentally unchanging.")
        self.assertEqual(["History is a wheel.", "The nature of man is fundamentally unchanging."], sorted(sentences))
        
    def test_two_sentences_question(self):
        sentences = self.builder._extract_sentences("What? That can't be!")
        self.assertEqual(sorted(["What?", "That can't be!"]), sorted(sentences))
    
    def test_two_sentences_exclamation(self):
        sentences = self.builder._extract_sentences("No! Don't do that!")
        self.assertEqual(sorted(["No!", "Don't do that!"]), sorted(sentences))
        
    def test_multiple_questions_exclamations(self):
        sentences = self.builder._extract_sentences("What??!! You can't be serious!!!!")
        self.assertEqual(sorted(["What??!!", "You can't be serious!!!!"]), sorted(sentences))
        
    def test_one_sentence(self):
        self.assertEqual(["What are you doing?"], self.builder._extract_sentences("What are you doing?"))
        self.assertEqual(["History is a wheel"], self.builder._extract_sentences("History is a wheel"))
        self.assertEqual(["History is a wheel."], self.builder._extract_sentences("History is a wheel."))