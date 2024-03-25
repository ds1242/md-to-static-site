
def extract_title(markdown):
    split_file = markdown.split("\n")
    for line in split_file:
        if line.startswith("#"):
            return line.strip('# ')
        else:
            raise Exception('No h1 on the document')
