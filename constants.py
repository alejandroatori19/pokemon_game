# constants.py

from enum import Enum

# ----------------------------------------
# Pokémon Types Enumeration
# ----------------------------------------

class PokemonType(Enum):
    NORMAL = 0
    FIRE = 1
    WATER = 2
    GRASS = 3
    ELECTRIC = 4
    ICE = 5
    FIGHTING = 6
    POISON = 7
    GROUND = 8
    FLYING = 9
    PSYCHIC = 10
    BUG = 11
    ROCK = 12
    GHOST = 13
    DRAGON = 14
    DARK = 15
    STEEL = 16
    FAIRY = 17

# ----------------------------------------
# Move Categories Enumeration
# ----------------------------------------

class MoveCategory(Enum):
    PHYSICAL = 0
    SPECIAL = 1
    STATUS = 2

# ----------------------------------------
# Pokédex Number to Pokémon Name Mapping
# ----------------------------------------

POKEDEX = {
    1: {
        "name": "Bulbasaur",
        "types": ["Grass", "Poison"],
        "base_stats": {
            "hp": 45,
            "attack": 49,
            "defense": 49,
            "sp_attack": 65,
            "sp_defense": 65,
            "speed": 45
        }
    },
    2: {
        "name": "Ivysaur",
        "types": ["Grass", "Poison"],
        "base_stats": {
            "hp": 60,
            "attack": 62,
            "defense": 63,
            "sp_attack": 80,
            "sp_defense": 80,
            "speed": 60
        }
    },
    3: {
        "name": "Venusaur",
        "types": ["Grass", "Poison"],
        "base_stats": {
            "hp": 80,
            "attack": 82,
            "defense": 83,
            "sp_attack": 100,
            "sp_defense": 100,
            "speed": 80
        }
    },
    4: {
        "name": "Charmander",
        "types": ["Fire"],
        "base_stats": {
            "hp": 39,
            "attack": 52,
            "defense": 43,
            "sp_attack": 60,
            "sp_defense": 50,
            "speed": 65
        }
    },
    5: {
        "name": "Charmeleon",
        "types": ["Fire"],
        "base_stats": {
            "hp": 58,
            "attack": 64,
            "defense": 58,
            "sp_attack": 80,
            "sp_defense": 65,
            "speed": 80
        }
    },
    6: {
        "name": "Charizard",
        "types": ["Fire", "Flying"],
        "base_stats": {
            "hp": 78,
            "attack": 84,
            "defense": 78,
            "sp_attack": 109,
            "sp_defense": 85,
            "speed": 100
        }
    },
    7: {
        "name": "Squirtle",
        "types": ["Water"],
        "base_stats": {
            "hp": 44,
            "attack": 48,
            "defense": 65,
            "sp_attack": 50,
            "sp_defense": 64,
            "speed": 43
        }
    },
    8: {
        "name": "Wartortle",
        "types": ["Water"],
        "base_stats": {
            "hp": 59,
            "attack": 63,
            "defense": 80,
            "sp_attack": 65,
            "sp_defense": 80,
            "speed": 58
        }
    },
    9: {
        "name": "Blastoise",
        "types": ["Water"],
        "base_stats": {
            "hp": 79,
            "attack": 83,
            "defense": 100,
            "sp_attack": 85,
            "sp_defense": 105,
            "speed": 78
        }
    }
    # You can continue with the rest as needed...
}






MAX_MOVEMENTS = 4
MAX_POKEMON_TEAM = 6