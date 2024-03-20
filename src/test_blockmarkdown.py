import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,

    block_type_heading,
    block_type_paragraph,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_heading_single_check(self):
        md = "# This is a heading"
        self.assertEqual(
            block_to_block_type(md),
            block_type_heading
        )
    def test_heading_three_check(self):
        md = "### This is a heading"
        self.assertEqual(
            block_to_block_type(md),
            block_type_heading
        )
    def test_heading_six(self):
        md = "###### This is a heading"
        self.assertEqual(
            block_to_block_type(md),
            block_type_heading
        )
    def test_not_heading(self):
        md = "####### This is a heading"
        self.assertNotEqual(
            block_to_block_type(md),
            block_type_heading
        )



if __name__ == "__main__":
    unittest.main()