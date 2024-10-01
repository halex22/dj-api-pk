from django.urls import path

from .views import (AbilitiesListView, AbilityByPokemon, AbilityView,
                    AllPokemonView, DetailTypeView, EggGroupListView,
                    EggGroupView, GenerationView, OnePokeView, PokemonHintView,
                    PokemonView, home)

urlpatterns = [
    # path('pokemon/<name>', view=PokemonAPIView.as_view()),
    path('<slug:pokemonSlug>', PokemonView.as_view()),
    path('one', view=OnePokeView.as_view()),
    # path('by-ability/<slug:slug>', view=AbilityView.as_view()),
    path('by-generation/gen-id-<int:gen_id>/', view=GenerationView.as_view()),
    path('by-ability/<slug:ability_slug>/', view=AbilityView.as_view()),
    path('by-egg-group/<egg_group_slug>/', view=EggGroupView.as_view()),
    path('by-type/<type>/', DetailTypeView.as_view()),
    path('all-abilities/', view=AbilitiesListView.as_view()),
    path('all-egg-groups/', view=EggGroupListView.as_view()),
    path('all-pokemon/', view=AllPokemonView.as_view()),
    path('pokemon-hint/<hint>/', view=PokemonHintView.as_view())
]
