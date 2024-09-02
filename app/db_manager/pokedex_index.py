from typing import Dict

from pokemon.models import Pokedex, PokedexLocalIndex, Pokemon


def fetch_pokedex_model(name:str) -> Pokedex:
    model, state = Pokedex.objects.get_or_create(
        name=name.lower()
    )
    return model


def create_local_index(stats: Dict[str, int], pokemon_instance: Pokemon):
    for podex_name, index in stats.items():
        local_index = PokedexLocalIndex(
            pokedex = fetch_pokedex_model(name=podex_name),
            pokemon = pokemon_instance,
            index = index
        )
        local_index.save()
