from core.pokemon import Pokemon
from core.trainer import Trainer
from core.stats import Stats
from core.move import Move
from common.core_enums import StatType

import json

# This method will load the data from json file
def load_trainer_data_from_json (filePath):
    with open(filePath, 'r') as file:
        trainerData = json.load(file)["Trainer"]
        
    # First of all, we need to create a Trainer object
    trainer = Trainer(trainerData["Name"])
    
    for pokemonData in trainerData["PokemonTeam"]:
        # Pokemon data
        pokemonName = pokemonData["Name"]
        pokemonLevel = pokemonData["Level"]
        pokemonTypes = pokemonData["Type"]
        pokemonNature = pokemonData["Nature"]
        pokemonMovements = []
        
        # Move data
        for moveData in pokemonData["Movements"]:
            moveName = moveData["Name"]
            moveDescription = moveData["Description"]
            moveType = moveData["Type"]
            moveCategory = moveData["Category"]
            movePower = moveData["Attack"]
            moveAccuracy = moveData["Accuracy"]
            moveMaxPP = moveData["PP"]
            
            move = Move (name=moveName, description=moveDescription, 
                         type=moveType, category=moveCategory, power=movePower, 
                         accuracy=moveAccuracy, maxPowerPoints=moveMaxPP
                         )
            
            pokemonMovements.append(move)
        
        # Stats data 
        pokemonBaseStats = Stats.from_dict(pokemonData["BaseStats"], typeStat=StatType.BASE)
        pokemonIvs = Stats.from_dict(pokemonData["IVs"], typeStat=StatType.IV)
        pokemonEvs = Stats.from_dict(pokemonData["EVs"], typeStat=StatType.EV)
            
        # Creating pokemon object and adding into the trainer team
        pokemon = Pokemon(name=pokemonName, level=pokemonLevel, 
                          types=pokemonTypes, baseStats=pokemonBaseStats, 
                          evs=pokemonEvs, ivs=pokemonIvs, 
                          nature=pokemonNature, moveSet=pokemonMovements
                          )
        
        trainer.add_pokemon(pokemon)
        
    return trainer