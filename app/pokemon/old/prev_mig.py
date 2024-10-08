# Generated by Django 5.0.7 on 2024-09-02 20:27

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'abilities',
            },
        ),
        migrations.CreateModel(
            name='EffectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'effect_category',
            },
        ),
        migrations.CreateModel(
            name='EggCyclesCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'egg_cycles_categories',
            },
        ),
        migrations.CreateModel(
            name='EggGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'db_table': 'egg_groups',
            },
        ),
        migrations.CreateModel(
            name='FriendShipCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'db_table': 'friendship_categories',
            },
        ),
        migrations.CreateModel(
            name='GrowthRateCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'db_table': 'growth_rate_category',
            },
        ),
        migrations.CreateModel(
            name='Pokedex',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'pokedex',
            },
        ),
        migrations.CreateModel(
            name='PokemonGame',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'pokemon_games',
            },
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'types',
            },
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('heigth', models.DecimalField(decimal_places=2, max_digits=8)),
                ('weigth', models.DecimalField(decimal_places=2, max_digits=8)),
                ('national_index', models.PositiveIntegerField()),
                ('generation_number', models.PositiveIntegerField()),
                ('abilities', models.ManyToManyField(related_name='abilities', to='pokemon.ability')),
                ('hidden_ability', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hidden_ability', to='pokemon.ability')),
                ('types', models.ManyToManyField(related_name='types', to='pokemon.pokemontype')),
            ],
            options={
                'db_table': 'pokemons',
            },
        ),
        migrations.CreateModel(
            name='PokedexLocalIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField()),
                ('pokedex', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='local_pokedex', to='pokemon.pokedex')),
                ('pokemon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_local', to='pokemon.pokemon')),
            ],
            options={
                'db_table': 'local_pokedex',
            },
        ),
        migrations.CreateModel(
            name='Breeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genderless', models.BooleanField(blank=True, default=False)),
                ('male', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('female', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('egg_cycles_value', models.PositiveIntegerField()),
                ('egg_cycles_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='egg_cycles_category', to='pokemon.eggcyclescategory')),
                ('egg_groups', models.ManyToManyField(related_name='egg_groups', to='pokemon.egggroup')),
                ('pokemon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='breeding', to='pokemon.pokemon')),
            ],
            options={
                'db_table': 'breeding_stats',
            },
        ),
        migrations.CreateModel(
            name='BaseStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hp_base', models.PositiveIntegerField()),
                ('hp_min', models.PositiveIntegerField()),
                ('hp_max', models.PositiveIntegerField()),
                ('attack_base', models.PositiveIntegerField()),
                ('attack_min', models.PositiveIntegerField()),
                ('attack_max', models.PositiveIntegerField()),
                ('defense_base', models.PositiveIntegerField()),
                ('defense_min', models.PositiveIntegerField()),
                ('defense_max', models.PositiveIntegerField()),
                ('sp_atk_base', models.PositiveIntegerField()),
                ('sp_atk_min', models.PositiveIntegerField()),
                ('sp_atk_max', models.PositiveIntegerField()),
                ('sp_def_base', models.PositiveIntegerField()),
                ('sp_def_min', models.PositiveIntegerField()),
                ('sp_def_max', models.PositiveIntegerField()),
                ('speed_base', models.PositiveIntegerField()),
                ('speed_min', models.PositiveIntegerField()),
                ('speed_max', models.PositiveIntegerField()),
                ('pokemon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='pokemon.pokemon')),
            ],
            options={
                'db_table': 'base_stats',
            },
        ),
        migrations.CreateModel(
            name='PokedexEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokedex_entries', to='pokemon.pokemon')),
                ('pokemon_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_pokemon_entries', to='pokemon.pokemongame')),
            ],
            options={
                'db_table': 'pokedex_entries',
            },
        ),
        migrations.CreateModel(
            name='PokemonTypeEffec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=1, max_digits=2)),
                ('effect_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon.effectcategory')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_type_effect', to='pokemon.pokemon')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_effects', to='pokemon.pokemontype')),
            ],
            options={
                'db_table': 'pokemon_type_effect',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_exp', models.PositiveIntegerField()),
                ('catch_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('base_friendship', models.PositiveIntegerField()),
                ('friendship_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='friendship_category', to='pokemon.friendshipcategory')),
                ('growth_rate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='growth_rate', to='pokemon.growthratecategory')),
                ('pokemon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='training', to='pokemon.pokemon')),
            ],
            options={
                'db_table': 'training_stats',
            },
        ),
    ]
