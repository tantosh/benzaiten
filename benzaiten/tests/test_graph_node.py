import unittest
from benzaiten.graph import GraphNode

class GraphNodeTest(unittest.TestCase):
    
    def test_error(self):
        node = GraphNode('What?', 0.2303)
        self.assertEqual(0.2303, node.error)
        
        node.score = 0.2301
        self.assertEqual(0.0002, node.error)
        
    def test_connect(self):
        node = GraphNode('What?', 0.2303)
        other = GraphNode('No!', 0.2301)
        node.connect(other, 1.23)
        
        self.assertEqual(1, len(other.connected))
        self.assertEqual(1, len(node.connected))
        self.assertEqual(1.23, other.connected[node])
        self.assertEqual(1.23, node.connected[other])