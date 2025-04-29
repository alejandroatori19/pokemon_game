# Import classes
from pokemon import Pokemon
from constants import MAX_POKEMON_TEAM

class Trainer:
    # Attributes of the Trainer
    name = None
    pokemonTeam = None
    
    # Constructor of the Trainer class
    def __init__ (self, name, pokemonTeam):
        self.name = name
        self.pokemonTeam = pokemonTeam
    
    @classmethod
    def from_dict(cls, data):
        listPokemon = []
        for dataPokemon in data['PokemonTeam']:
            listPokemon.append (Pokemon.from_dict(dataPokemon))
 
        return cls(data['Name'], listPokemon)
    
    # --------------------------------------
    
    # Adders & Removers of Pokemons
    def add_pokemon_to_team (self, pokemon):
        if len (self.pokemonTeam) < MAX_POKEMON_TEAM:
            self.pokemonTeam.append(pokemon)
            print (f"The pokemon {pokemon.name} has been added to the pokemon team.")
        else:
            print (f"The pokemon team is full! (Pokemon team size -> {len (self.pokemonTeam)})")
        
    # ------------------------------------------------

    def remove_pokemon_from_team (self, indexPokemon):
        if len (self.pokemonTeam) < indexPokemon:
            self.pokemonTeam.pop(indexPokemon)
            print (f"The pokemon {indexPokemon} has been removed from the pokemon team.")
        else:
            print (f"The pokemon team is empty! (Pokemon team size -> {len (self.pokemonTeam)})")
        
    # ---------------------------------------------------
    
    def replace_pokemon_from_team (self, index, pokemon):
        if index < len(self.pokemonTeam) and index >= 0:
            self.pokemonTeam[index] = pokemon
            print (f"The pokemon {index} has been replaced.")
        else:
            print (f"The pokemon team is not available! (Pokemon team size -> {len (self.pokemonTeam)})")
        
        
    def choose_movement (self, player):
        print (f"-------- MOVEMENTS PLAYER {player} --------")
        self.pokemonTeam[0].print_movements ()
        # It suposes that user never introduce a wrong input
        return input (f"Choose a movement to use[1-{len(self.pokemonTeam[0].movements)}]: ")
        
    # ---------------------------
    
    def print_information (self):
        print (f"Trainer name: {self.name}")
        for index, pokemon in enumerate(self.pokemonTeam):
            print (f"-------- POKEMON {index + 1} --------")
            pokemon.print_information()
            print ("\n")
            
        
