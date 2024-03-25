import os
import shutil
from textnode import TextNode
from copy_static import copy_files
from generate_page import generate_page

destination = './public'
source_path = './static'
md_source = './content'
template = './template.html'




def main():
    # test_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    copy_files(source_path, destination)
    generate_page(os.path.join(md_source, "index.md"), template, os.path.join(destination, "index.html"))

main()
