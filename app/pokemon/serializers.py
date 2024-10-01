from django.contrib.auth.models import User
from rest_framework.serializers import (CharField, ModelSerializer, SlugField,
                                        StringRelatedField)

from .models import (Ability, BaseStats, Breeding, EffectCategory,
                     EggCyclesCategory, EggGroup, FriendShipCategory,
                     GrowthRateCategory, PokedexEntry, Pokemon, PokemonGame,
                     PokemonType, PokemonTypeEffec, Training)


class BaseSerializer(ModelSerializer):
    name = CharField()
    # id = UUIDField()
    slug = SlugField()


class PokemonTypeSerializer(BaseSerializer):

    class Meta:
        model = PokemonType
        exclude = ['id']

class AbilitySerializer(BaseSerializer):
    
    class Meta:
        model = Ability
        exclude = ['id']



class BaseStatsSerializer(ModelSerializer):

    class Meta:
        model = BaseStats
        exclude = ['id', 'pokemon']


class FriendshipSerializer(ModelSerializer):

    class Meta:
        model = FriendShipCategory
        exclude = ['id']


class GrowRateSerializer(ModelSerializer):

    class Meta:
        model = GrowthRateCategory
        exclude = ['id']


class TrainingSerializer(ModelSerializer):

    friendship_category = FriendshipSerializer()
    growth_rate = GrowRateSerializer()

    class Meta:
        model = Training
        exclude = ['pokemon']


class EggCyclesCategorySerializer(ModelSerializer):

    class Meta:
        model = EggCyclesCategory
        exclude = ['id']


class EggGroupSerializer(ModelSerializer):

    class Meta:
        model = EggGroup
        exclude = ['id']


class BreedingSerializer(ModelSerializer):
    egg_groups = EggGroupSerializer(many=True)
    egg_cycles_category = EggCyclesCategorySerializer()


    class Meta:
        model = Breeding
        exclude = ['pokemon']


class PokemonGameSerializer(ModelSerializer):
    
    class Meta:
        model = PokemonGame
        exclude = ['id']


class PokedexEntrySerializer(ModelSerializer):
    pokemon_game = PokemonGameSerializer()

    class Meta:
        model = PokedexEntry
        fields = ['pokemon_game', 'entry']


class EffectCategorySerializer(ModelSerializer):

    class Meta:
        model = EffectCategory
        fields = ['name']


class PokemonTypeEffectSerializer(ModelSerializer):
    effect_category = EffectCategorySerializer()
    type = PokemonTypeSerializer()

    class Meta:
        model = PokemonTypeEffec
        exclude = ['pokemon', 'id']


class BasePokemonSerializer(BaseSerializer):
    types = PokemonTypeSerializer(many=True)
    abilities = AbilitySerializer(many=True)
    hidden_ability = AbilitySerializer()

    
    class Meta:
        model = Pokemon
        # fields = '__all__'
        exclude = ['id', 'heigth', 'weigth']


class PokemonSerializer(BasePokemonSerializer):

    stats = BaseStatsSerializer()
    training = TrainingSerializer()

    breeding = BreedingSerializer()
    pokedex_entries = PokedexEntrySerializer(many=True)
    pokemon_type_effect = PokemonTypeEffectSerializer(many=True)

    # class Meta:
    #     model = Pokemon
    #     exclude = [ 'id']


class PokemonHintSerializer(ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ['name',  'slug']


class AbilityByPokemon(BasePokemonSerializer):
    ...



