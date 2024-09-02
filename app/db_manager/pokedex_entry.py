from typing import Dict

from pokemon.models import PokedexEntry, Pokemon, PokemonGame


def fetch_pkmn_game(name: str) -> PokemonGame:
    model, state = PokemonGame.objects.get_or_create(name= name.lower())
    return model


def create_entry(pokemon_game: PokemonGame, pokemon_instance: Pokemon, text: str) -> PokedexEntry:
    entry = PokedexEntry(
        pokemon = pokemon_instance,
        pokemon_game = pokemon_game,
        entry = text
    )
    return entry


def create_pokedex_entries(stats:Dict[str, str], pokemon: Pokemon):
    for game, entry_text in stats.items():
        pkmn_game = fetch_pkmn_game(name=game.lower())
        pkmn_pokedex_entry = create_entry(
            pokemon_game=pkmn_game,
            pokemon_instance=pokemon,
            text= entry_text
        )
        pkmn_pokedex_entry.save()