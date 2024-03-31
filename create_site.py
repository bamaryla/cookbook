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

    try:
        image_filename = [image for image in images if image.startswith(recipe_file_no_ext)][0]
    except IndexError:
        image_filename = "default.jpg"

    with open(f'recipes_json/{recipe_file}') as f:
        try:
            recipe = json.load(f)
        except:
            print(f'Error while reading {recipe_file}')

    with open(f'recipes/{recipe_file.replace("json", "html")}', 'w') as f:
        f.write(template_recipe.render(recipe=recipe, image_filename=image_filename))

    recipes[recipe_file_no_ext] = recipe.get('title')


with open('index.html', 'w') as f:
    f.write(template_main.render(recipes=recipes))