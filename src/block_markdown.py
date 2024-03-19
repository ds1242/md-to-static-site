
def markdown_to_blocks(markdown):
    output = []
    split_block = markdown.split("\n\n")
    for block in split_block:
        block = block.strip(" ")
        output.append(block)
    return output



