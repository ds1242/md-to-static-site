import os
import shutil

def copy_files(source_path, destination):
    path_list = []
    check_destination(destination)    

    if not os.path.exists(source_path):
        raise Exception('not a valid path')
        
    for current_path in os.listdir(source_path):
        curr_path = os.path.join(source_path, current_path)
        if os.path.isfile(curr_path):
            shutil.copy(curr_path, destination)
        else:
            destination = destination + curr_path[len(source_path):]            
            copy_files(curr_path, destination)
    





def check_destination(destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    
        
