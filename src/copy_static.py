import os

def create_file_path(path, output_list):
    path_list = []
    if os.path.exists(path):
        if os.path.isfile(path):
            output_list.append(path)
        else:
            path_list = os.listdir(path=path)

        for current_path in path_list:
            curr_path = os.path.join(path, current_path)
            if os.path.isfile(curr_path):
                output_list.append(curr_path)
            else:
                create_file_path(curr_path, output_list)
        return output_list
    else:
        raise Exception('not a valid path')

