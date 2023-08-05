import os
import sys
import time
import json
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

settings_json = f"{os.getcwd()}/settings.json"

with open(settings_json, 'r') as json_file:
    data = json.load(json_file)
    
settings = data['settings']

USERNAME = settings['github_username']
TOKEN = settings['access_token']

repo_name = settings['repo_name']
repo_description = settings['repo_description']

license_template = settings['license_template']
homepage = settings['homepage']
private_repo = False

topics = settings['topics']

settings['submodules']

def create_github_repo():
    url = f"https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "name": repo_name,
        "description": repo_description,
        "private": private_repo,
        "license_template": license_template,
        "homepage": homepage,
        "topics": topics
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 201:
        print("Repository created successfully!")
        print(f"Repository URL: {response.json()['html_url']}")
        return repo_name
    else:
        print("Failed to create repository.")
        print(f"Response: {response.content}")
        return None

def delete_github_repo(repo_name):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print("Repository deleted successfully!")
    else:
        print("Failed to delete repository.")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")

created_repo_name = create_github_repo()

sys.exit()
