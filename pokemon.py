# Import classes
from movement import Movement



class Pokemon:
    # Attributes of the Pokemon
    name = None
    alias = None
    id = None
    pokedex_number = None
    gender = None
    level = None
    type = None
    
    movements = None
    baseStats = {}

    # Constructor of the Pokemon class
    def __init__ (self, name, alias, id, pokedex_number, gender, level, type, movements, base_stats):
        self.name = name
        self.alias = alias if alias != None else name
        self.id = id
        self.pokedex_number = pokedex_number
        self.gender = gender
        self.level = level
        self.type = type
        
        self.movements = movements
        self.baseStats = base_stats
    
    @classmethod
    def from_dict(cls, data):
        listMovements = []
        for dataMovement in data['Movements']:
            listMovements.append (Movement.from_dict(dataMovement))
            
        return cls(data['Name'], data['Alias'], data['Id'], data['PokedexNumber'], data['Gender'], data['Level'], data['Type'], listMovements, data['BaseStats'])
        
    def print_movements (self):
        counter = 1
        for movement in self.movements:
            print (f"[{counter}]", end=" ")
            movement.print_movement ()
            counter += 1
        
    # ---------------------------
    def print_information (self):
        print (f"Name: {self.name}")
        print (f"Alias: {self.alias}")
        print (f"ID: {self.id}")
        print (f"Pokedex number: {self.pokedex_number}")
        print (f"Gender: {self.gender}")
        print (f"Level: {self.level}")
        print (f"Type: {self.type}")
        
        print ("\n-------- INIT STATS ---------")
        print (f"HP: {self.baseStats['hp']}")
        print (f"Attack: {self.baseStats['attack']}")
        print (f"Defense: {self.baseStats['defense']}")
        print (f"Sp. Attack: {self.baseStats['sp_attack']}")
        print (f"Sp. Defense: {self.baseStats['sp_defense']}")
        print (f"Speed: {self.baseStats['speed']}")
        print ("--------- END STATS ---------")
        
        print ("\n--------- INIT MOVEMENTS ---------")
        
        for movement in self.movements:
            movement.print_information()
            print ("\n-----------------------------------\n")
            
        print ("--------- END MOVEMENTS ---------")
    