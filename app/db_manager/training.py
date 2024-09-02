from pokemon.models import (FriendShipCategory, GrowthRateCategory, Pokemon,
                            Training)

from .dicts import CleanedTraining


def fetch_friendhship_category(name:str) -> FriendShipCategory:
    cat_name = name.lower() if name else 'n/a'
    print(cat_name, 'looking for this cat')
    model, state = FriendShipCategory.objects.get_or_create(
        name = cat_name 
    )
    print(f'model state: {state}')
    return model

def fetch_g_rate_category(name:str)-> GrowthRateCategory:
    model, state = GrowthRateCategory.objects.get_or_create(
        name= name.lower()
    )
    return model


def create_training_st_model(stats: CleanedTraining, pokemon_instance: Pokemon):
    pkmn_training_stats = Training(
        base_exp = stats['base_exp'],
        catch_rate = stats['catch_rate']['percentage'],
        friendship_category = fetch_friendhship_category(
            name=getattr(stats['base_friendship'], 'category', 'n/a')
        ),
        base_friendship = getattr(stats['base_friendship'], 'value', 0),
        growth_rate = fetch_g_rate_category(name=stats['growth_rate']),
        pokemon = pokemon_instance
    )
    pkmn_training_stats.save()
