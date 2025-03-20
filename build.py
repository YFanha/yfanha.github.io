import yaml
import os
import shutil
from jinja2 import Environment, FileSystemLoader

def remove_extension(filename):
    name, _ = os.path.splitext(filename)
    return name

def getInformations(directory="data"):
    data = {}
    for file in os.listdir(directory):
        if file.endswith(".yml") or file.endswith(".yaml"):
            subject = remove_extension(file)

            with open(os.path.join(directory, file), 'r', encoding="utf-8") as f:
                content = yaml.safe_load(f)

            if isinstance(content, dict):
                data[subject] = content[subject]

    return data


env = Environment(loader=FileSystemLoader('templates'))

base_template = env.get_template('base.html')
cv_section = env.get_template('cv.html')
cv_portfolio = env.get_template('portfolio.html')

data = getInformations()

# Render sub-sections
cv_content = cv_section.render(data)
portfolio_content = cv_portfolio.render(data)

output = base_template.render(data, cv_content=cv_content, portfolio_content=portfolio_content)

output_file_path = os.path.join('website', 'index.html')

os.makedirs('website', exist_ok=True)

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
