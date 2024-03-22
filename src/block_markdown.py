import re
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = 'paragraph'
block_type_heading = 'heading'
block_type_code = 'code'
block_type_quote = 'quote'
block_type_unordered_list = 'unordered_list'
block_type_ordered_list = 'ordered_list'

def markdown_to_blocks(markdown):
    output = []
    split_block = markdown.split("\n\n")
    for block in split_block:
        if block == "":
            continue
        else:
            block = block.strip()
            output.append(block)
    return output


def block_to_block_type(block):
    lines = block.split('\n')
    if re.match(r"^(#{1,6})\s(.*)", block):
        return block_type_heading
    if block.startswith('```') and block.endswith('```'):
        return block_type_code
    elif all(line.startswith('* ') or line.startswith('- ') for line in lines):
        return block_type_unordered_list
    elif all(line.startswith('> ') for line in lines):
        return block_type_quote
    elif is_ordered_list(lines):
        return block_type_ordered_list
    else:
        return block_type_paragraph
    
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return create_paragraph_node(block)
    if block_type == block_type_heading:
        return create_heading_node(block)
    if block_type == block_type_code:
        return create_code_node(block)
    if block_type == block_type_ordered_list:
        return create_ol_node(block)
    if block_type == block_type_unordered_list:
        return create_ul_node(block)
    if block_type == block_type_quote:
        return create_blockquote_node(block)
    raise ValueError("Invalid block type")


def is_ordered_list(lines):
    for i, line in enumerate(lines, start=1):
        expected_start = f"{i}"
        if not line.startswith(expected_start):
            return False
    return True

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def create_heading_node(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f'Invalid heading level: {level}')
    text = block[level + 1: ]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def create_blockquote_node(block):
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        if not line.startswith('>'):
            raise ValueError('Invalid quote block')
        new_lines.append(line.lstrip('>').strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def create_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def create_ul_node(block):
    html_items = []
    split_block = block.split('\n')
    for line in split_block:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def create_ol_node(block):
    html_items = []
    split_block = block.split('\n')
    for line in split_block:
        text = line[3:]
        children = text_to_children(text)
        html_items.append(ParentNode('li',children))
    return ParentNode('ol', html_items)

def create_code_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode('div', children, None)
