import os
from pathlib import Path
from time import sleep

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

from db_manager import CleanedPokemonDict, fetch_json_pokemon_data
from db_manager.base_stats import create_pokemon_bs_model
from db_manager.breeding import create_breeding_model
from db_manager.pokedex import create_pkmn_model, create_pokemon_effect_type
from db_manager.pokedex_entry import create_pokedex_entries
from db_manager.pokedex_index import create_local_index
from db_manager.training import create_training_st_model
from pokemon.models import Pokemon

APP_DIR = Path('./').absolute()
DATA_DIR = APP_DIR / 'data'




def fetch_pokemon_instance(name: str) -> Pokemon | None:
    pokemon = Pokemon.objects.filter(name= name.lower())
    if pokemon:
        return pokemon.first()
    return None


if __name__ == '__main__':

    for generation in DATA_DIR.iterdir():
        gen_number = generation.stem[-1]
        print('\n', f'generation {gen_number}', '\n')

        # if generation.stem != 'gen_9':
        #     continue

        for pokemon_dir in generation.iterdir():
            pokemon_dict: CleanedPokemonDict = fetch_json_pokemon_data(path_to_file=pokemon_dir)
            print('looking for: ', pokemon_dir.stem)
            instance = fetch_pokemon_instance(pokemon_dir.stem)
            if not instance:
                instance = create_pkmn_model(stats=pokemon_dict['pokédex_data'], pokemon_name=pokemon_dir.stem,
                                             gen_num= gen_number)
                
                print('creating ', instance.name, 'stats')
                create_pokemon_effect_type(pokemon_dict['types_effect'], pokemon_instance=instance)
                create_local_index(pokemon_dict['pokédex_data']['local'], pokemon_instance=instance)
                create_pokemon_bs_model(pokemon_dict['base_stats'], pokemon_model=instance)
                create_training_st_model(pokemon_dict['training'], pokemon_instance=instance)
                create_breeding_model(pokemon_dict['breeding'], pokemon_instance=instance)

                if not hasattr(pokemon_dict['pokédex_entries'], 'pokédex_entries' ):
                    create_pokedex_entries(pokemon_dict['pokédex_entries'], pokemon=instance)

