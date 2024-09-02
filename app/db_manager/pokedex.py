from typing import Dict, List

from django.db.models import Model
from pokemon.models import (Ability, EffectCategory, Pokemon, PokemonType,
                            PokemonTypeEffec)

from .dicts import CleanedPokedexData


def fetch_model(name: str, model: Model) -> Model:
    instance, state = model.objects.get_or_create(
        name = name.lower()
    )
    return instance


def fetch_type(type_name: str) -> PokemonType:
    model, state = PokemonType.objects.get_or_create(
        name=type_name.lower()
    )
    return model


def fetch_ability(ability_name: str) -> Ability:
    model, state = Ability.objects.get_or_create(name=ability_name.lower())
    return model


def create_pokemon_effect_type(stats: Dict[str, Dict[str, int]], pokemon_instance: Pokemon):
    for _type, cat_and_value in stats.items():
        for category, value in cat_and_value.items():

            type_instance = fetch_model(name=_type, model=PokemonType)
            category_instance = fetch_model(name=category, model=EffectCategory)

            type_effect = PokemonTypeEffec(
                type = type_instance,
                effect_category = category_instance,
                pokemon = pokemon_instance,
                value = value
            )
            type_effect.save()


def fetch_types(types_array:List[str] ) -> List[PokemonType]:
    return [fetch_model(_type, PokemonType) for _type in types_array if _type]


def fetch_normal_abilities(abilities_dict: dict) -> List[Ability]:
    abilities_list = []
    for ability in abilities_dict['normal']:
        abilities_list.append(fetch_model(ability, Ability))
    return abilities_list


def create_pkmn_model(stats: CleanedPokedexData, pokemon_name: str, gen_num:int) -> Pokemon:
    
    pkmn = Pokemon(
        name=pokemon_name,
        heigth=stats['height'],
        weigth=stats['weight'],
        hidden_ability= fetch_model(name=stats['abilities']['hidden'],model= Ability),
        national_index=stats['national'],
        generation_number = gen_num
    )
    pkmn.save()

    abilities_models = fetch_normal_abilities(
        abilities_dict=stats['abilities'])
    
    pokemon_types = fetch_types(stats['type'])

    for _pokemon_type in pokemon_types:
        pkmn.types.add(_pokemon_type)

    for ability in abilities_models:
        pkmn.abilities.add(ability)

    return pkmn
