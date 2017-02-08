import unittest
from benzaiten.summarization import summarize, sentences

class SummarizationTest(unittest.TestCase):
        
    def test_two_sentences_fullstop(self):
        self.assertEqual(["History is a wheel.", "The nature of man is fundamentally unchanging."], sorted(sentences("History is a wheel. The nature of man is fundamentally unchanging.")))
        
    def test_two_sentences_question(self):
        self.assertEqual(sorted(["What?", "That can't be!"]), sorted(sentences("What? That can't be!")))
    
    def test_two_sentences_exclamation(self):
        self.assertEqual(sorted(["No!", "Don't do that!"]), sorted(sentences("No! Don't do that!")))
        
    def test_multiple_questions_exclamations(self):
        self.assertEqual(sorted(["What??!!", "You can't be serious!!!!"]), sorted(sentences("What??!! You can't be serious!!!!")))
        
    def test_one_sentence(self):
        self.assertEqual(["What are you doing?"], sentences("What are you doing?"))
        self.assertEqual(["History is a wheel"], sentences("History is a wheel"))
        self.assertEqual(["History is a wheel."], sentences("History is a wheel."))
