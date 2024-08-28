import json
from pathlib import Path
from typing import Dict, TypedDict


class PokemonStats(TypedDict):
    base_stats = dict
    breeding = dict
    img_link = str | None
    other_languages = dict
    pokédex_data = dict
    pokédex_entries = dict
    training = dict
    types_effect = dict
    where_to_find = dict



def fetch_json_pokemon_data(path_to_file: Path):
    pokemon_dict = {}
    for stat in path_to_file.iterdir():  
        stat_name, stat_info = parse_stat(stat)
        pokemon_dict[stat_name] = stat_info
    return pokemon_dict

def parse_stat(path_to_file: Path) -> Dict[str, dict]:
    with open(file=path_to_file, mode='r', encoding='utf8') as file:
        return path_to_file.stem, json.load(file)