from typing import List

from pokemon.models import Breeding, EggCyclesCategory, EggGroup, Pokemon

from .dicts import CleanedBreeding


def fetch_egg_group_model(name: str) -> EggGroup:
    model, state = EggGroup.objects.get_or_create(name= name.lower())
    return model


def fetch_egg_cycles_model(name: str) -> EggCyclesCategory:
    model, state = EggCyclesCategory.objects.get_or_create(name=name.lower()) 
    return model 


def fetch_egg_groups(groups: List[str]) -> List[EggGroup]:
    models_list = []
    for group in groups:
        models_list.append(fetch_egg_group_model(name=group))
    return models_list


def create_breeding_model(stats: CleanedBreeding, pokemon_instance: Pokemon = None) ->  Breeding:
    pkmn_breeding_stats = Breeding(
        egg_cycles_category = fetch_egg_cycles_model(
            name= getattr(stats['egg_cycles'], 'category', 'n/a') 
        ),
        egg_cycles_value = getattr(stats['egg_cycles'], 'value', 0), 
        pokemon = pokemon_instance
    )
    if len(stats['gender']) < 2:
        pkmn_breeding_stats.genderless = True
    else:
        pkmn_breeding_stats.male = stats['gender']['male']
        pkmn_breeding_stats.female = stats['gender']['female']
    egg_group_models = fetch_egg_groups(stats['egg_groups'])

    pkmn_breeding_stats.save()

    for model in egg_group_models:
        pkmn_breeding_stats.egg_groups.add(model)
