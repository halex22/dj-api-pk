from django.db.models import Model, QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Pokemon
from .serializers import PokemonSerializer


class SingleObjectAPIView(RetrieveAPIView):
    model: Model = ...
    filter_name: str = ...

    def get_query_args(self):
        return {self.filter_name: self.kwargs[self.filter_name]}

    def get_queryset(self) -> QuerySet:
        queryset_result = self.model.objects.filter(**self.get_query_args())
        return queryset_result

    def get_object(self):
        result = self.get_queryset()
        return result.first()
    

class PokemonAPIView(SingleObjectAPIView):
    model = Pokemon
    serializer_class = PokemonSerializer
    filter_name = 'name'

    def get(self, *args, **kwargs):
        print(self.request)
        return super().get(*args, **kwargs)
    

class OnePokeView(APIView):

    permission_class = [AllowAny]

    def get(self, *args, **kwargs):
        pokemon = Pokemon.objects.filter(name='charizard').first()
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)
    
    
def home(request):
    return HttpResponse('it is ok')