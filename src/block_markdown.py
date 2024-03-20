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
    word_list = []
    split_block = block.split(" ")
    count = len(split_block[0])

    value = block[count:]
    value = value.strip(" ")
    print(value)
    tag = 'h' + str(count)
    return HTMLNode(tag, value, None, None)