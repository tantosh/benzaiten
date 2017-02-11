import unittest
from benzaiten.graph import GraphBuilder

class SentenceExtractionTest(unittest.TestCase):
    
    def setUp(self):
        self.builder = GraphBuilder()
    
    def test_two_sentences_fullstop(self):
        sentences = self.builder._extract_sentences("History is a wheel. The nature of man is fundamentally unchanging.")
        self.assertCountEqual(["History is a wheel.", "The nature of man is fundamentally unchanging."], sentences)
        
    def test_two_sentences_question(self):
        sentences = self.builder._extract_sentences("What? That can't be!")
        self.assertCountEqual(["What?", "That can't be!"], sentences)
    
    def test_two_sentences_exclamation(self):
        sentences = self.builder._extract_sentences("No! Don't do that!")
        self.assertCountEqual(["No!", "Don't do that!"], sentences)
    
    def test_two_sentences_exclamation(self):
        sentences = self.builder._extract_sentences("No! Don't do that!")
        self.assertCountEqual(["No!", "Don't do that!"], sentences)
        
    def test_multiple_questions_exclamations(self):
        sentences = self.builder._extract_sentences("What??!! You can't be serious!!!!")
        self.assertCountEqual(["What??!!", "You can't be serious!!!!"], sentences)
        
    def test_newlines_no_fullstops(self):
        sentences = self.builder._extract_sentences("""There are plenty of various definitions what actually text summarization means.\n
        “A brief but accurate representation of the contents of a document”\n
        “A distilling the most important information from a source to produce an abridged version for a particular user/users and task/tasks”""")

        self.assertCountEqual(["There are plenty of various definitions what actually text summarization means.",
                               "“A brief but accurate representation of the contents of a document”",
                               "“A distilling the most important information from a source to produce an abridged version for a particular user/users and task/tasks”"], sentences)
    
    def test_ul_invalid_sentences(self):
        sentences = self.builder._extract_sentences(" • coherence (express the way how the parts of the summary create together an integrated sequence) As the oldest publication, describing an implementation of an automatic summarizer is often cited.")
        self.assertCountEqual(["As the oldest publication, describing an implementation of an automatic summarizer is often cited."], sentences)
        
    def test_one_sentence(self):
        self.assertEqual(["What are you doing?"], self.builder._extract_sentences("What are you doing?"))
        self.assertEqual(["That cannot happen!"], self.builder._extract_sentences("That cannot happen!"))
        self.assertEqual(["History is a wheel."], self.builder._extract_sentences("History is a wheel."))
