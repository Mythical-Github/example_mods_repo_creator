import os
import sys
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

settings_json = f"{os.getcwd()}/settings.json"

with open(settings_json, 'r') as json_file:
    data = json.load(json_file)

settings = data['settings']

repo_dir = settings['repo_name']
USERNAME = settings['github_username']
repo_url = f"https://github.com/{USERNAME}/{repo_dir}"

os.system (f"git clone --recursive {repo_url} {repo_dir}")

sys.exit()
