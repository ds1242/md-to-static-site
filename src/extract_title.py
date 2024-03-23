


def extract_title(markdown):
    split_file = markdown.split("\n")
    print(split_file[0])



f = open('./content/index.md', 'r')
markdown_file = f.read()
extract_title(markdown_file)