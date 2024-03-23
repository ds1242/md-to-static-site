from textnode import TextNode
from copy_static import copy_files

def main():
    test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    source_path = './static'
    destination = './public'
    copy_files(source_path, destination)

main()
