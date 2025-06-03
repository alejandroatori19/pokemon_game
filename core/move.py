

class Move:
    # ATTRIBUTES of the class
    """
    name = None
    description = None
    type = None
    category = None
    power = None
    accuracy = None
    currentPowerPoints = None
    maxPowerPoints = None
    """
    
    
    # Class constructor
    def __init__ (self, name = None, description = None, type = None, category = None, power = None, accuracy = None, maxPowerPoints = None):
        self.name = name
        self.description = description
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.currentPowerPoints = maxPowerPoints
        self.maxPowerPoints = maxPowerPoints
        
    # Check if move can be used
    def can_use (self):
        return True if self.currentPowerPoints > 0 else False
    
    # Reduce pp of the move after use it
    def reduce_pp (self):
        self.currentPowerPoints -= 1
        
    # Reset the Power Points
    def reset_pp (self):
        self.PP = self.maxPP
        
        
    def print_information_single_move (self):
        print (f"{self.name} - Power: {self.power} - Accuracy: {self.accuracy}")
        
    def print_information_move (self):
        print (f" ---------- MOVE INFORMATION ({self.name}) ---------- ")
        print (f"Move Name: {self.name}")
        print (f"Move Description: {self.description}")
        print (f"Move Type: {self.type}")
        print (f"Move Category: {self.category}")
        print (f"Move Power: {self.power}")
        print (f"Move Accuracy: {self.accuracy}")
        print (f"Move Current Power Points: {self.currentPowerPoints}")
        print (f"Move Max Power Points: {self.maxPowerPoints}") 
        
        