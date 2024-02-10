import json
import os
from jinja2 import Template


list_of_recipes_json_files = os.listdir('recipes_json')

template_main = Template(open('template_main.html').read())
template_recipe = Template(open('template_recipe.html').read())

images = os.listdir('images')
recipes = {}

for recipe_file in list_of_recipes_json_files:
    recipe_file_no_ext = recipe_file.replace('.json', '')
    image_filename = [image for image in images if image.startswith(recipe_file_no_ext)][0]

    with open(f'recipes_json/{recipe_file}') as f:
        recipe = json.load(f)

    with open(f'recipes/{recipe_file.replace("json", "html")}', 'w') as f:
        f.write(template_recipe.render(recipe=recipe, image_filename=image_filename))

    recipes[recipe_file_no_ext] = recipe.get('title')


with open('index.html', 'w') as f:
    f.write(template_main.render(recipes=recipes))