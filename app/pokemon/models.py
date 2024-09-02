import uuid

from django.db import models
from django.utils.text import slugify

# Create your models here.

class MyBaseModel(models.Model):
    name = ...
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    slug = models.SlugField(db_index=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    
    class Meta:
        abstract = True


class PokemonType(MyBaseModel):
    name = models.CharField(unique=True, max_length=20, null=False, blank=False)

    class Meta:
        db_table = 'types'


class Ability(MyBaseModel):
    name = models.CharField(unique=True, max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'abilities'


class Pokemon(MyBaseModel):
    name = models.CharField(unique=True, max_length=100, null=False, blank=False)
    heigth = models.DecimalField(decimal_places=2, max_digits=8, null=False, blank=False)
    weigth = models.DecimalField(decimal_places=2, max_digits=8, null=False, blank=False)
    national_index = models.PositiveIntegerField(null= False, blank=False)
    types = models.ManyToManyField(PokemonType, related_name='types')
    abilities = models.ManyToManyField(Ability, related_name='abilities')
    hidden_ability = models.ForeignKey(Ability, on_delete=models.SET_NULL, related_name='hidden_ability', null=True)
    generation_number = models.PositiveIntegerField(null=False, blank=False)
    
    class Meta:
        db_table = 'pokemons'


    def __str__(self) -> str:
        return f'Pokemon: {self.name} - National id: {self.national_index}'


class BaseStats(models.Model):
    pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE, related_name='stats')
    hp_base = models.PositiveIntegerField(null= False, blank=False)
    hp_min = models.PositiveIntegerField(null= False, blank=False)
    hp_max = models.PositiveIntegerField(null= False, blank=False)
    attack_base = models.PositiveIntegerField(null= False, blank=False)
    attack_min = models.PositiveIntegerField(null= False, blank=False)
    attack_max = models.PositiveIntegerField(null= False, blank=False)
    defense_base= models.PositiveIntegerField(null= False, blank=False)
    defense_min= models.PositiveIntegerField(null= False, blank=False)
    defense_max= models.PositiveIntegerField(null= False, blank=False)
    sp_atk_base= models.PositiveIntegerField(null= False, blank=False)
    sp_atk_min = models.PositiveIntegerField(null= False, blank=False)
    sp_atk_max = models.PositiveIntegerField(null= False, blank=False)
    sp_def_base = models.PositiveIntegerField(null= False, blank=False)
    sp_def_min = models.PositiveIntegerField(null= False, blank=False)
    sp_def_max = models.PositiveIntegerField(null= False, blank=False)
    speed_base = models.PositiveIntegerField(null= False, blank=False)
    speed_min = models.PositiveIntegerField(null= False, blank=False)
    speed_max = models.PositiveIntegerField(null= False, blank=False)

    class Meta:
        db_table = 'base_stats'


# class SmallNameModel(models.Model):
#     name = models.CharField(unique=True, max_length=25, null=False, blank=False)

#     class Meta:
#         abstract = True


class FriendShipCategory(MyBaseModel):
    name = models.CharField(unique=True, max_length=25, null=False, blank=False)
    
    class Meta:
        db_table = 'friendship_categories'


class GrowthRateCategory(MyBaseModel):
    name = models.CharField(unique=True, max_length=25, null=False, blank=False)
    
    class Meta:
        db_table = 'growth_rate_category'


class Training(models.Model):
    pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE, related_name='training')
    base_exp = models.PositiveIntegerField(null= False, blank=False)
    catch_rate = models.DecimalField(decimal_places=2, max_digits=4, null=False, blank=False)
    friendship_category = models.ForeignKey(FriendShipCategory, on_delete=models.SET_NULL, related_name='friendship_category', null=True)
    base_friendship = models.PositiveIntegerField()
    growth_rate = models.ForeignKey(GrowthRateCategory, on_delete=models.SET_NULL, related_name='growth_rate', null=True)

    class Meta:
        db_table = 'training_stats'


class EggGroup(MyBaseModel):
    name = models.CharField(unique=True, max_length=25, null=False, blank=False)
    
    class Meta:
        db_table = 'egg_groups'


class EggCyclesCategory(MyBaseModel):
    name = models.CharField(max_length=50, unique=True, blank=False, null=False)

    class Meta:
        db_table = 'egg_cycles_categories'

class Breeding(models.Model):
    pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE, related_name='breeding')
    genderless = models.BooleanField(default=False, blank=True)
    male = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    female = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    egg_groups = models.ManyToManyField(EggGroup, related_name='egg_groups')
    egg_cycles_category = models.ForeignKey(EggCyclesCategory, on_delete=models.SET_NULL, related_name='egg_cycles_category', null=True)
    egg_cycles_value = models.PositiveIntegerField()

    class Meta:
        db_table = 'breeding_stats'


class PokemonGame(MyBaseModel):
    name = models.CharField(unique=True, max_length=50, null=False, blank=False)
    
    class Meta:
        db_table = 'pokemon_games'


class PokedexEntry(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokedex_entries')
    pokemon_game = models.ForeignKey(PokemonGame, on_delete=models.CASCADE, related_name='game_pokemon_entries')
    entry = models.TextField(null=False, blank=False)


    class Meta:
        db_table = 'pokedex_entries'


class Pokedex(MyBaseModel):
    name = models.CharField(unique=True, max_length=50, null=False, blank=False,)

    class Meta:
        db_table = 'pokedex'


class PokedexLocalIndex(models.Model):
    pokedex = models.ForeignKey(Pokedex, on_delete=models.SET_NULL, related_name='local_pokedex', null=True)
    pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE, related_name='pokemon_local')
    index = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        db_table = 'local_pokedex'


class EffectCategory(models.Model):
    name = models.CharField(unique=True, null=False, blank=False, max_length=50)

    class Meta:
        db_table = 'effect_category'


class PokemonTypeEffec(models.Model):
    type = models.ForeignKey(PokemonType, on_delete=models.SET_NULL, null=True, related_name='type_effects')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_type_effect')
    effect_category = models.ForeignKey(EffectCategory, on_delete=models.SET_NULL, null=True)
    value = models.DecimalField(max_digits=2, decimal_places=1, null=False, blank=False)

    class Meta:
        db_table = 'pokemon_type_effect'