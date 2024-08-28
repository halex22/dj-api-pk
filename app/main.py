import json
import os
from pathlib import Path

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

from db_manager import CleanedPokemonDict, fetch_json_pokemon_data
from pokemon import models

APP_DIR = Path('./').absolute()
DATA_DIR = APP_DIR / 'data'

def create_pokemon_model(data: CleanedPokemonDict) -> None:
    
    ...


if __name__ == '__main__':

    for generation in DATA_DIR.iterdir():
        for pokemon_dir in generation.iterdir():
            pokemon_dict = fetch_json_pokemon_data(path_to_file=pokemon_dir)
            print(pokemon_dict)
            break
        break
