import re
from htmlnode import HTMLNode

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


def is_ordered_list(lines):
    for i, line in enumerate(lines, start=1):
        expected_start = f"{i}"
        if not line.startswith(expected_start):
            return False
    return True


def create_heading_node(block, block_type):
    if block_type != block_type_heading:
        raise Exception('wrong block type')
    tag = ""
    count = block.count('#')

    value = block[count:]
    value = value.strip(" ")

    tag = 'h' + str(count)
    return HTMLNode(tag, value)

def create_blockquote_node(block, block_type):
    if block_type != block_type_quote:
        raise Exception('wrong block type')
    tag = ""
    if block.startswith(">"):
        tag = "blockquote"
    value = block[1:]
    value = value.lstrip(" ")
    return HTMLNode(tag, value)

def create_paragraph_node(block, block_type):
    if block_type != block_type_paragraph:
        raise Exception('wrong block type')
    tag = "p"
    return HTMLNode(tag, block)

def create_ul_node(block, block_type):
    if block_type != block_type_unordered_list:
        raise Exception('Not unordered list. wrong block type')
    children = []
    split_block = block.split('\n')
    for line in split_block:
        children.append(HTMLNode('li', line.strip('-*+ ')))
    tag = 'ul'
    return HTMLNode(tag, None, children)

def create_ol_node(block, block_type):
    if block_type != block_type_ordered_list:
        raise Exception('Not unordered list. wrong block type')
    children = []
    split_block = block.split('\n')
    for line in split_block:
        children.append(HTMLNode('li', line.strip('-*+ ')))
    tag = 'ol'
    return HTMLNode(tag, None, children)

def create_code_node(block, block_type):
    if block_type != block_type_code:
        raise Exception('Not a code block. Wrong block type')
    tag = 'pre'
    return HTMLNode(tag, None, HTMLNode('code', block))

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            children.append(create_heading_node(block, block_type))
        elif block_type == block_type_quote:
            children.append(create_blockquote_node(block, block_type))
        elif block_type == block_type_code:
            children.append(create_code_node(block, block_type))
        elif block_type == block_type_ordered_list:
            children.append(create_ol_node(block, block_type))
        elif block_type == block_type_unordered_list:
            children.append(create_ul_node(block, block_type))

    return HTMLNode('div', None, children)