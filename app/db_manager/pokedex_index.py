from typing import Dict

from django.db import IntegrityError
from pokemon.models import Pokedex, PokedexLocalIndex, Pokemon


def fetch_pokedex_model(name: str) -> Pokedex:
    model, state = Pokedex.objects.get_or_create(
        name=name.lower()
    )
    return model


def create_local_index(stats: Dict[str, int], pokemon_instance: Pokemon):
    """Creates a local index instance for the given pokemon instance

    Args:
        stats (Dict[str, int]): dict with all the pokedex name and number
        pokemon_instance (Pokemon): The pokemon that will have it's local indexes created
    """
    print(stats)
    for pokedex_name, index in stats.items():
        pokedex_instance = fetch_pokedex_model(name=pokedex_name)
        
        try:
            local_index, created = PokedexLocalIndex.objects.get_or_create(
                pokedex=pokedex_instance,
                pokemon=pokemon_instance,
                defaults={'index': index}
            )
            if created:
                print(f"Created new local index for {pokemon_instance.name} in {pokedex_name}")
            else:
                print(f"Local index already exists for {pokemon_instance.name} in {pokedex_name}")

        except IntegrityError as e:
            print(f'Failed to create local index for {pokemon_instance.name} in pokedex {pokedex_name}: {e}')
            raise IntegrityError()

