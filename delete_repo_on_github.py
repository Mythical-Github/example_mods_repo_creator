import os
import sys
import stat
import json
import shutil
import requests

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

settings_json = f"{os.getcwd()}/settings.json"

with open(settings_json, 'r') as json_file:
    data = json.load(json_file)
    
settings = data['settings']

github_username = settings['github_username']
repository_name = settings['repo_name']
access_token = settings['access_token']

def delete_github_repo(username, repo_name, access_token):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully.")
    else:
        print(f"Failed to delete repository '{repo_name}'.")
        print(f"Response status code: {response.status_code}")
        print("Response content:", response.content)

if __name__ == "__main__":
    delete_github_repo(github_username, repository_name, access_token)
