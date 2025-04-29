



class Movement:
    # Attributes of the Movement
    name = None
    id = None
    category = None
    type = None
    power = None
    description = None
    
    # Constructor of the Movement class
    def __init__ (self, name, id, category, type, power, description):
        self.name = name
        self.id = id
        self.category = category
        self.type = type
        self.power = power
        self.description = description
        
    @classmethod
    def from_dict(cls, data):
        return cls(data['Name'], data['Id'], data['Category'], data['Type'], data['Power'], data['Description'])
    
    def print_movement (self):
        print (f"{self.name}[PP/PP] - POWER:{self.power} - DESCRIPTION:{self.description}")
    
    # ---------------------------
    def print_information (self):
        print (f"Name: {self.name}")
        print (f"ID: {self.id}")
        print (f"Category: {self.category}")
        print (f"Type: {self.type}")        
        print (f"Power: {self.power}")
        print (f"Description: {self.description}")