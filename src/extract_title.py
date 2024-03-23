
def extract_title(markdown):
    split_file = markdown.split("\n")
    return split_file[0].strip('# ')
