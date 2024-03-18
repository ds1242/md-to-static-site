import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode('This is a div', 'div', None)
        self.assertEqual(
            node.to_html(),
            '<div>This is a div</div>'
        )