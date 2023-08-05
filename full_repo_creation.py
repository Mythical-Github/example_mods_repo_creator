import os
import sys
import time
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

create_repo_py = f"{script_dir}/create_repo.py"
clone_repo_py = f"{script_dir}/clone_repo.py"
add_submodules_py = f"{script_dir}/add_submodules.py"
delete_repo_files_on_disk = f"{script_dir}/delete_repo_files_on_disk.py"

subprocess.run(["python", create_repo_py])
subprocess.run(["python", clone_repo_py])
subprocess.run(["python", add_submodules_py])
subprocess.run(["python", delete_repo_files_on_disk])
subprocess.run(["python", clone_repo_py])

sys.exit()
