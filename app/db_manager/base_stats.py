from pokemon.models import BaseStats, Pokemon


def create_pokemon_bs_model(stats_dict: dict, pokemon_model: Pokemon):
    stats = unpack_stats_dict(stats_dict)
    pokemon_base_stats = BaseStats(**stats)
    pokemon_base_stats.pokemon = pokemon_model
    pokemon_base_stats.save()


def unpack_stats_dict(stats: dict):
    unpacked_stats = {}
    for outer_key, values in stats.items():
        for inner_key, value in values.items():
            unpacked_stats[f'{outer_key}_{inner_key}'] = value
    return unpacked_stats