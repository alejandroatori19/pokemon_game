# Import libraries
import json

# Import classes 
from trainer import Trainer
from pokemon import Pokemon



class Battle:
    trainer1 = None
    trainer2 = None
    
    def __init__ (self):
        
        pass
    
    # ------------------------------------------------
    def load_trainer_data_from_file (self, file_path):
        # Read data
        with open(file_path, "r") as file:
            data = json.load(file)['Trainer']
        
        # Now we have to create Pokemons Objects with the movements they have
        self.trainer1 = Trainer.from_dict (data)
        self.trainer2 = Trainer.from_dict (data)        
    
    # ----------------------
    def cycle_battle (self):
        return
    
    # ----------------
    def battle (self):
        # First of all both trainers has to choose a movement (Be sure that movement index is +1)
        indexMovement1 = self.trainer1.choose_movement (1)
        print ("\n")
        indexMovement2 = self.trainer2.choose_movement (2)
        
        # Now we have to get who moves first based on speed
        
        
        return
    
    # ---------------------------
    def print_information (self):
        self.trainer1.print_information()