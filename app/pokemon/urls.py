from django.urls import path

from .views import OnePokeView, PokemonAPIView, home

urlpatterns = [
    path('pokemon/<name>', view=PokemonAPIView.as_view()),
    path('', home),
    path('one', view=OnePokeView.as_view())
]
