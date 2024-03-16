import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', "bold")
        node2 = TextNode('This is a text node', "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode('This is a text node', "bold")
        node2 = TextNode('something else', 'italic')
        self.assertNotEqual(node, node2)

    def test_eq_full(self):
        node = TextNode('This is a text node', "bold", 'boot.dev')
        node2 = TextNode('This is a text node', "bold", 'boot.dev')
        self.assertEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()