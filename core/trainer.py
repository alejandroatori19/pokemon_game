


class Trainer:
    # ATTRIBUTES of the class
    """
    name = None
    pokemonTeam = None   
    """
    
    def __init__ (self, name = None, pokemonTeam = None):
        self.name = name
        self.pokemonTeam = [] if pokemonTeam is None else pokemonTeam
    
    def get_pokemon (self, index):
        return self.pokemonTeam[index]
    
    def add_pokemon (self, pokemon):
        if len (self.pokemonTeam) < 6:
            self.pokemonTeam.append(pokemon)
        else:
            print ("The pokemon team is full")
            
    def remove_pokemon (self, index):
        self.pokemonTeam.pop(index)
    
    def print_information_trainer (self):
        print (f" ---------- TRAINER INFORMATION ({self.name}) ---------- ")
        for pokemon in self.pokemonTeam:
            pokemon.print_information_pokemon ()