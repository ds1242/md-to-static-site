import unittest
from block_markdown import (
    block_type_heading,
    block_type_paragraph,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,

    markdown_to_blocks,
    block_to_block_type,
    create_heading_node,
    create_blockquote_node,
    create_paragraph_node,
    create_ul_node,
    create_ol_node,
    create_code_node,
    markdown_to_html_node,
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
    def test_block_code(self):
        md = '''``` a block of code goes here
more stuff goes into this
```'''
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
    

if __name__ == "__main__":
    unittest.main()