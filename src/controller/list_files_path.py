import os
import json
from urllib import response

def list_files_path():

    id = 0
    data = {}
   
    target = os.getcwd() + '/files'
    list_files = os.listdir(target)

    if '.gitkeep' in list_files:
        list_files.remove('.gitkeep')

    for item in list_files:
        id += 1
        key = "id_"+ str(id)
        d = {key: str(item)}
        data.update(d)

    response = data

    return response