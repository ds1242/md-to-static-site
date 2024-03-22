import os


def copy_static():
    current_path = "."
    path_list = os.listdir(path=current_path)
    print(path_list)


copy_static()