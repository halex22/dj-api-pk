from django.contrib.auth.models import User
from rest_framework.serializers import (CharField, ModelSerializer, SlugField,
                                        StringRelatedField)

from .models import (Ability, BaseStats, FriendShipCategory,
                     GrowthRateCategory, Pokemon, PokemonType, Training)


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

        

class PokemonSerializer(BaseSerializer):
    hidden_ability = AbilitySerializer()
    abilities = AbilitySerializer(many=True)
    types = PokemonTypeSerializer(many=True)
    stats = BaseStatsSerializer()
    training = TrainingSerializer()

    class Meta:
        model = Pokemon
        exclude = [ 'id']



