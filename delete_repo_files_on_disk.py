import os
import sys
import stat
import json
import shutil

settings_json = f"{os.getcwd()}/settings.json"

with open(settings_json, 'r') as json_file:
    data = json.load(json_file)
    
settings = data['settings']

repo_name = settings['repo_name']

def onerror(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)

local_directory = f"{os.getcwd()}/{repo_name}"

shutil.rmtree(local_directory, onerror=onerror)

sys.exit()
