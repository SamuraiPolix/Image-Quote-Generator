import json
import os


def get_data(json_file):
    with open(f'{json_file}', 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
    verses: str = jsonData['verses']
    refs: str = jsonData['references']
    return verses, refs


def txt_to_json(text_file, output_folder):
    # TODO FINISH TEXT TO JSON
    with open(f'{text_file}', 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
