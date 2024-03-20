import unittest
from block_markdown import markdown_to_blocks

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text_block = """ 
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items      
        """
        list_of_text = markdown_to_blocks(text_block)
        print(list_of_text)