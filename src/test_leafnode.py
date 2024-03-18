import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode('div', 'This is a div', None)
        self.assertEqual(
            node.to_html(),
            '<div>This is a div</div>'
        )
    
    def test_props(self):
        node = LeafNode('a', 'this is a link', {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">this is a link</a>'
        )

    def test_large_props(self):
        node = LeafNode(
            "div",
            "Hello, world!",
            {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="greeting" href="https://boot.dev">Hello, world!</div>'
        )
    
    def test_to_html_no_tag(self):
        node = LeafNode(None,"Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")