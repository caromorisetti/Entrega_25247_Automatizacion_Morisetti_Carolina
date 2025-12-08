import json
from pathlib import Path
# Lee un archivo JSON y devuelve su contenido como un diccionario.
def read_json_products(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
