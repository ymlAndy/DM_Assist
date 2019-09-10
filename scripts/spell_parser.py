import json
import os


project_root = "DM_Assist"

myfile = open(f'{project_root}/parsed_data/spell_collection.txt', 'w')
for file_name in os.listdir(f"{project_root}/data"):
    with open(f"{project_root}/data/{file_name}") as file:
        spell_file = json.load(file)
        for spell in spell_file["compendium"]["spell"]:
            spell_name = f"""\"{spell["name"]}\", \"{spell["name"]}\"\n"""
            spell_name = spell_name.replace("(", "")
            spell_name = spell_name.replace(")", "")
            myfile.write(spell_name)

myfile.close()