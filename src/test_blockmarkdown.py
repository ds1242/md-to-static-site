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
    def test_paragraph(self):
        md = "This is a heading"
        self.assertEqual(
            block_to_block_type(md),
            block_type_paragraph
        )
    def test_quote(self):
        md = "> this is a quote"
        self.assertEqual(
            block_to_block_type(md),
            block_type_quote
        )
    def test_unordered_list_star(self):
        md = """* this is an unordered list
* second part of unordered list """
        self.assertEqual(
            block_to_block_type(md),
            block_type_unordered_list
        )
    def test_unordered_list_dash(self):
        md = """- this is an unordered list
- second part of unordered list
- third part of unordered list"""
        self.assertEqual(
            block_to_block_type(md),
            block_type_unordered_list
        )
    def test_ordered_list(self):
        md = """1. this is an unordered list
2. second part of unordered list
3. third part of unordered list"""
        self.assertEqual(
            block_to_block_type(md),
            block_type_ordered_list
        )



if __name__ == "__main__":
    unittest.main()