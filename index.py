import yaml
from jinja2 import Environment, FileSystemLoader

# Step 1: Load data/data from the YAML file
with open('data/data.yml', 'r', encoding="utf-8") as file:
    data = yaml.safe_load(file)

# Step 2: Setup Jinja2 environment and load template
env = Environment(loader=FileSystemLoader('templates'))

# Load the template (assuming you have 'template.html' in the 'templates' directory)
template = env.get_template('base.html')

# Step 3: Render the template with data from the YAML file
output = template.render(data)

with open('index.html', 'w', encoding="utf-8") as file:
    file.write(output)

print("index.html has been generated successfully.")
