import os
import sys
import json
import time
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

settings_json = f"{os.getcwd()}/settings.json"

with open(settings_json, 'r') as json_file:
    data = json.load(json_file)
    
settings = data['settings']

repo_name = settings['repo_name']

REPO_PATH = f"{os.getcwd()}/{repo_name}"

submodules = settings['submodules']

os.chdir(REPO_PATH)

for submodule in submodules:
    submodule_path = submodule['submodule_path']
    submodule_path = f"{REPO_PATH}/{submodule_path}"

    os.system(f"git submodule deinit -f {submodule_path}")
    os.system(f"git rm -f {submodule_path}")
    os.system(f"rd /s /q {submodule_path}")

    os.system(f'git commit -m "Removed submodule"')

    os.system("git push")

sys.exit()
