# Libraries needed
from common.core_enums import Stat, StatType
from core.stats import Stats




class Pokemon:
    """
    # ATTRIBUTES of the class
    name = None
    level = None
    types = None
    baseStats = None
    evs = None
    ivs = None
    nature = None
    finalStats = None
    moveSet = None
    """
    
    def __init__ (self, name = None, level = None, types = None, baseStats = None, evs = None, ivs = None, nature = None, moveSet = None):
        self.name = name
        self.types = types
        self.level = level
        self.baseStats = baseStats
        self.evs = evs
        self.ivs = ivs 
        self.nature = nature   
        self.finalStats = self.calculate_stats ()
        self.moveSet = moveSet
     
    # Here the pokemon stats are calculated based on EVs, IVs, baseStats, nature (FUTURE) and level. 
    # Also it will be modifying while the level increase
    def calculate_stats (self):
        finalStats = Stats (typeStat = StatType.FINAL)
        
        for stat in Stat:
            baseStat = self.baseStats.get_specific_stat (stat)
            evStat = self.evs.get_specific_stat (stat)
            ivStat = self.ivs.get_specific_stat (stat)
            
            finalStat = (2 * baseStat + ivStat + (evStat // 4) * self.level) // 100
            
            # Check if the stat that is being calculated is HP. Because this is a special case
            if stat == Stat.HP:
                finalStat = finalStat + self.level + 10
            else:
                finalStat = finalStat + 5
            
            finalStats.set_specific_stat (stat, finalStat)
            
        return finalStats
        
    
    # Get the stat from the class Stats (Must be fixed)
    def get_specific_stat (self, statName):
        return self.finalStats.get_stat (statName)
    
    def set_level (self, newLevel):
        self.level = newLevel
        
    def get_level (self):
        return self.level
    
    def get_types (self):
        return self.types
    
    def get_specific_movement (self, moveID):
        return self.moveSet[moveID]
    
    def get_name (self):
        return self.name
    
    
    
        
    def print_information_pokemon (self):
        print (f" ---------- POKEMON INFORMATION ({self.name}) ---------- ")
        print (f"Pokemon Level: {self.level}")
        print (f"Pokemon Types: {self.types}")        
        print (f"Pokemon Nature: {self.nature}")
        self.baseStats.print_information_stats ()
        self.ivs.print_information_stats ()
        self.evs.print_information_stats ()
        if type (self.finalStats) == Stats:
            self.finalStats.print_information_stats ()

        # Printing the moves
        for move in self.moveSet:
            move.print_information_move ()