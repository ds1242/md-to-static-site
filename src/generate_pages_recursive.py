import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for path in os.listdir(dir_path_content):
        set_source_path = os.path.join(dir_path_content, path)
        set_dest_path = os.path.join(dest_dir_path, path)
        if os.path.isfile(set_source_path):
            generate_page(set_source_path, template_path, set_dest_path)
        else:
            generate_pages_recursive(set_source_path, template_path, set_dest_path)