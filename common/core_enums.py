from enum import Enum

# Types of Pokemon & movements
class Type(Enum):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    GRASS = "Grass"
    ELECTRIC = "Electric"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DARK = "Dark"
    DRAGON = "Dragon"
    STEEL = "Steel"
    FAIRY = "Fairy"

# Catgory of Movements
class MoveCategory(Enum):
    PHYSICAL = "Physical"
    SPECIAL = "Special"
    STATUS = "Status"

# Types of the stats
class Stat(Enum):
    HP = "HP"
    ATTACK = "Physical Attack"
    DEFENSE = "Physical Defense"
    SPECIAL_ATTACK = "Special Attack"
    SPECIAL_DEFENSE = "Special Defense"
    SPEED = "Speed"
    
class StatType(Enum):
    BASE = "Base"
    EV = "EVs"
    IV = "IVs"
    FINAL = "Final"