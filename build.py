import yaml
import os
import shutil
from jinja2 import Environment, FileSystemLoader

with open('data/data.yml', 'r', encoding="utf-8") as file:
    data = yaml.safe_load(file)

env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('base.html')

output = template.render(data)

os.makedirs('website', exist_ok=True)

output_file_path = os.path.join('website', 'index.html')

with open(output_file_path, 'w', encoding="utf-8") as file:
    file.write(output)

def copy_file_or_directory(src, dest):
    """Copy files or directories to the destination."""
    if os.path.isdir(src):  
        dest_dir = os.path.join(dest, os.path.basename(src))
        shutil.copytree(src, dest_dir, dirs_exist_ok=True)  
    elif os.path.isfile(src):  
        shutil.copy2(src, dest)  

files_to_copy = ['static', 'assets', 'CNAME']

for item in files_to_copy:
    copy_file_or_directory(item, 'website')

print("index.html has been generated successfully in the 'website' directory.")
