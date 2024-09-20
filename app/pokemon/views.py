from django.db.models import Model, QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ability, EggGroup, Pokemon
from .serializers import (AbilityByPokemon, AbilitySerializer,
                          BasePokemonSerializer, EggGroupSerializer,
                          PokemonSerializer)


class OnePokeView(APIView):

    permission_class = [AllowAny]

    def get(self, *args, **kwargs):
        pokemon = Pokemon.objects.filter(name='charizard').first()
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)
    


class PokemonView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PokemonSerializer

    def get_object(self):
        pokemon_slug = self.kwargs.get('pokemonSlug')
        return Pokemon.objects.get(slug=pokemon_slug)
    

class AbilityView(APIView):

    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        pokemons = Pokemon.objects.filter(abilities__slug='blaze')
        serializer = AbilityByPokemon(pokemons, many=True)
        return Response(serializer.data)
    


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AbilityView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BasePokemonSerializer
    # pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        ability_slug = self.kwargs.get('slug')
        print(self.kwargs)
        return Pokemon.objects.filter(abilities__slug=ability_slug)


class EggGroupView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BasePokemonSerializer

    def get_queryset(self):
        slug  = self.kwargs.get('slug')
        return Pokemon.objects.filter(breeding__egg_groups__slug=slug)
    

class GenerationView(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class = BasePokemonSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        gen_id = self.kwargs.get('gen_id')
        return Pokemon.objects.filter(generation_number=gen_id).order_by('national_index')


class AbilitiesListView(ListAPIView):

    permission_classes = [AllowAny]
    serializer_class =  AbilitySerializer

    def get_queryset(self):
        return Ability.objects.all()
    

class EggGroupListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EggGroupSerializer

    def get_queryset(self):
        return EggGroup.objects.all()

    # def get(self, *args, **kwargs):
    #     pokemons = Pokemon.objects.filter(generation_number=1)
    #     serializer = BasePokemonSerializer(pokemons, many= True)
    #     return Response(serializer.data)
    
    
def home(request):
    return HttpResponse('it is ok')