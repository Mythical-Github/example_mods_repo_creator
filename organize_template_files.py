import os
import sys
import time
import json
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

clone_repo_py = f"{script_dir}/clone_repo.py"
delete_repo_files_on_disk = f"{script_dir}/delete_repo_files_on_disk.py"
remove_submodules = f"{script_dir}/remove_submodules.py"

settings_json = f"{script_dir}/settings.json"

with open(settings_json, 'r') as json_file:
    data = json.load(json_file)
    
settings = data['settings']

repo_name = settings['repo_name']

game_project_name = settings['game_project_name']

template_blueprint_project = f"{os.getcwd()}/{repo_name}/Blueprint/Template_UE4SS_Blueprint_Mods" 
final_blueprint_project = f"{os.getcwd()}/{repo_name}/Blueprint/{game_project_name}"

shutil.move(template_blueprint_project, final_blueprint_project)

template_blueprint_uproject_file = f"{os.getcwd()}/{repo_name}/Blueprint/{game_project_name}/Template.uproject"
final_blueprint_uproject_file = f"{os.getcwd()}/{repo_name}/Blueprint/{game_project_name}/{game_project_name}.uproject"

shutil.move(template_blueprint_uproject_file, final_blueprint_uproject_file)

os.system(f"git add .")
os.system(f'git commit -m "Added submodule"')
os.system(f"git push")

subprocess.run(["python", delete_repo_files_on_disk])
subprocess.run(["python", clone_repo_py])
subprocess.run(["python", removesubmodules])
subprocess.run(["python", delete_repo_files_on_disk])
subprocess.run(["python", clone_repo_py])

time.sleep(999999999)

sys.exit()
