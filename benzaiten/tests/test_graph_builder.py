import unittest
from benzaiten.graph import GraphBuilder

class GraphBuilderTest(unittest.TestCase):
    
    def setUp(self):
        self.builder = GraphBuilder()

    def test_build_short_text(self):
        graph = self.builder.buildGraph("There's nothing like the laughter of a baby. Unless it's 1 a.m. and you're home alone.")
        self.assertEqual(2, graph.vertex_count())
    
    def test_vertexes(self):
        sentences = ["There's nothing like the laughter of a baby.", "Unless it's 1 a.m. and you're home alone."]
        verteces = self.builder._create_verteces(sentences)
        for vertex in verteces:
            self.assertTrue(vertex.sentence in sentences)
            self.assertEqual(1, len(vertex.connected))
