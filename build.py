import yaml
import os
import shutil
from jinja2 import Environment, FileSystemLoader

# Step 1: Load data from the YAML file
with open('data/data.yml', 'r', encoding="utf-8") as file:
    data = yaml.safe_load(file)

# Step 2: Setup Jinja2 environment and load template
env = Environment(loader=FileSystemLoader('templates'))

# Load the template (assuming you have 'base.html' in the 'templates' directory)
template = env.get_template('base.html')

# Step 3: Render the template with data from the YAML file
output = template.render(data)

# Ensure the 'website' directory exists
os.makedirs('website', exist_ok=True)

# Write the output to the 'website' directory as 'index.html'
output_file_path = os.path.join('website', 'index.html')

with open(output_file_path, 'w', encoding="utf-8") as file:
    file.write(output)

# Step 4: Copy 'css' and 'assets' directories into 'website'
def copy_directory(src_dir, dest_dir):
    """Copy the contents of a directory to a destination directory."""
    if os.path.exists(src_dir):
        shutil.copytree(src_dir, os.path.join(dest_dir, os.path.basename(src_dir)), dirs_exist_ok=True)

# Copy the 'css' and 'assets' directories into the 'website' directory
copy_directory('css', 'website')
copy_directory('assets', 'website')

print("index.html has been generated successfully in the 'website' directory.")
