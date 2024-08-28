from django.db import models

# Create your models here.


class PokemonType(models.Model):
    name = models.CharField(unique=True, max_length=20, null=False, blank=False)

    class Meta:
        db_table = 'types'


class Ability(models.Model):
    name = models.CharField(unique=True, max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'abilities'


class Pokemon(models.Model):
    name = models.CharField(unique=True, max_length=100, null=False, blank=False)
    heigth = models.DecimalField(decimal_places=2, max_digits=4, null=False, blank=False)
    weigth = models.DecimalField(decimal_places=2, max_digits=4, null=False, blank=False)
    types = models.ManyToManyField(PokemonType, related_name='types')
    abilities = models.ManyToManyField(Ability, related_name='abilities')
    hidden_ability = models.ForeignKey(Ability, on_delete=models.SET_NULL, related_name='hidden_ability', null=True)

    class Meta:
        db_table = 'pokemons'


class BaseStats(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='stats')
    hp= models.PositiveIntegerField(null= False, blank=False)
    attack= models.PositiveIntegerField(null= False, blank=False)
    defense= models.PositiveIntegerField(null= False, blank=False)
    sp_atk= models.PositiveIntegerField(null= False, blank=False)
    sp_def= models.PositiveIntegerField(null= False, blank=False)
    speed= models.PositiveIntegerField(null= False, blank=False)

    class Meta:
        db_table = 'base_stats'


class SmallNameModel(models.Model):
    name = models.CharField(unique=True, max_length=25, null=False, blank=False)

    class Meta:
        abstract = True


class FriendShipCategory(SmallNameModel):
    
    class Meta:
        db_table = 'friendship_categories'


class GrowthRateCategory(SmallNameModel):
    
    class Meta:
        db_table = 'growth_rate_category'


class Training(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='traning')
    base_exp = models.PositiveIntegerField(null= False, blank=False)
    catch_rate = models.DecimalField(decimal_places=2, max_digits=3, null=False, blank=False)
    friendship_category = models.ForeignKey(FriendShipCategory, on_delete=models.SET_NULL, related_name='friendship_category', null=True)
    base_friendship = models.PositiveIntegerField()
    growth_rate = models.ForeignKey(GrowthRateCategory, on_delete=models.SET_NULL, related_name='growth_rate', null=True)

    class Meta:
        db_table = 'training_stats'


class EggGroup(SmallNameModel):
    
    class Meta:
        db_table = 'egg_groups'


class EggCyclesCategory(models.Model):
    name = models.CharField(max_length=35, unique=True, blank=False, null=False)

    class Meta:
        db_table = 'egg_cycles_categories'

class Breeding(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='breeding')
    genderless = models.BooleanField(default=False, blank=True)
    male = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    female = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    egg_groups = models.ManyToManyField(EggGroup, related_name='egg_groups')
    egg_cycles_category = models.ForeignKey(EggCyclesCategory, on_delete=models.SET_NULL, related_name='egg_cycles_category', null=True)
    egg_cycles_value = models.PositiveIntegerField()

    class Meta:
        db_table = 'breeding_stats'


class PokemonGame(SmallNameModel):
    
    class Meta:
        db_table = 'pokemon_games'


class PokedexEntry(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokedex_entries')
    pokemon_game = models.ForeignKey(PokemonGame, on_delete=models.CASCADE, related_name='game_pokemon_entries')
    entry = models.TextField(null=False, blank=False)


    class Meta:
        db_table = 'pokedex_entries'

