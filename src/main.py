from textnode import TextNode
from copy_static import copy_files
from generate_page import generate_page

def main():
    test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    # source_path = './static'
    # destination = './public'
    # copy_files(source_path, destination)
    source = './content/index.md'
    template = './template.html'
    destination = './public/index.html'
    generate_page(source, template, destination)

main()
