import unittest
from benzaiten.graph import GraphBuilder

class GraphTest(unittest.TestCase):
    
    def setUp(self):
        self.builder = GraphBuilder()
        self.short_text = "There's nothing like the laughter of a baby. Unless it's early morning and you're home alone."
        
    def test_build_short_text(self):
        graph = self.builder.buildGraph(self.short_text)
        self.assertEqual(2, len(graph.verteces))
    
    def test_k_highest_short(self):
        graph = self.builder.buildGraph(self.short_text)
        self.assertEqual(["There's nothing like the laughter of a baby.", "Unless it's early morning and you're home alone."], graph.k_highest(10))
    
    def test_vertexes(self):
        sentences = ["There's nothing like the laughter of a baby.", "Unless it's early morning and you're home alone."]
        verteces = self.builder._create_verteces(sentences)
        for vertex in verteces:
            self.assertTrue(vertex.sentence in sentences)
            self.assertEqual(1, len(vertex.connected))
