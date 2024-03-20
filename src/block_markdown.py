import re

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
    if re.match(r"^(#{1,6})\s(.*)", block):
        return block_type_heading
    lines = block.split('\n')
    if all(line.startswith('* ') or line.startswith('- ') for line in lines):
        return block_type_unordered_list
    if all(line.startswith('> ') for line in lines):
        return block_type_quote
    if all(line.startswith('{line}. ') for line in lines):
        return block_type_ordered_list
    else:
        return block_type_paragraph

