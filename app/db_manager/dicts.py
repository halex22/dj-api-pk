from typing import Dict, List, TypedDict, Union


class CleanedPokedexData(TypedDict):
    national: int
    type: List[Union[str, None]]
    species: str
    height: float
    weight: float
    abilities: List[str]
    local: Dict[str, int]


class CleanedTraining(TypedDict):
    ev_yield: Dict[str, int]
    catch_rate: str
    base_friendship: int
    base_exp: int
    growth_rate: str


class CleanedBreeding(TypedDict):
    egg_groups: List[str]
    gender: List[float]
    egg_cycles: str


class CleanedPokemonDict(TypedDict):
    pokedex_data: CleanedPokedexData
    base_stats: str
    trainig: CleanedTraining
    breeding: CleanedBreeding
    pokedex_entries: str
    types_effect: dict
    img_link: str | None
    other_languages: dict
    where_to_find: dict
