import os
import sys
import json
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

settings_json = f"{os.getcwd()}/settings.json"

with open(settings_json, 'r') as json_file:
    data = json.load(json_file)
    
settings = data['settings']

USERNAME = settings['github_username']
TOKEN = settings['access_token']


repo_description = settings['repo_description']

license_template = settings['license_template']
homepage = settings['homepage']
private_repo = False

topics = settings['topics']

submodules = settings['submodules']

repo_name = settings['repo_name']
REPO_PATH = f"{os.getcwd()}/{repo_name}"

os.chdir(REPO_PATH)

for submodule in submodules:
    submodule_url = submodule['submodule_url']
    submodule_path = submodule['submodule_path']
    os.system(f"git submodule add {submodule_url} {submodule_path}")
    os.system(f"git add .")
    os.system(f'git commit -m "Added submodule"')
    os.system(f"git push")

sys.exit()
