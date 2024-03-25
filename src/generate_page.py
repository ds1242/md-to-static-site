from extract_title import extract_title
from block_markdown import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as original_markdown:
        content = original_markdown.read()
        title = extract_title(content)        
        content = markdown_to_html_node(content)

        
    with open(template_path, "r") as template:
        template_path_data = template.read()
        template_path_data = template_path_data.replace("{{ Title }}", title)
        template_path_data = template_path_data.replace("{{ Content }}", content.to_html())
        if not os.path.exists(dest_path):
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            with open(dest_path, 'w') as final:
                final.write(template_path_data)
