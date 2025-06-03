from common.core_enums import Stat, StatType

class Stats:    
    def __init__ (self, hp = -1, attack = -1, defense = -1, specialAttack = -1, specialDefense = -1, speed = -1, typeStat = None):
        self.statsDict = {
            Stat.HP: hp,
            Stat.ATTACK: attack,
            Stat.DEFENSE: defense,
            Stat.SPECIAL_ATTACK: specialAttack,
            Stat.SPECIAL_DEFENSE: specialDefense,
            Stat.SPEED: speed
        }
   
        self.typeStat = typeStat
        
        self.validate()

    @staticmethod
    def from_dict(data, typeStat = None):
        return Stats(
            hp = data[Stat.HP.value],
            attack = data[Stat.ATTACK.value],
            defense = data[Stat.DEFENSE.value],
            specialAttack = data[Stat.SPECIAL_ATTACK.value],
            specialDefense = data[Stat.SPECIAL_DEFENSE.value],
            speed = data[Stat.SPEED.value],
            typeStat = typeStat
        )

    def get_specific_stat (self, nameStat):
        return self.statsDict[nameStat]
    
    def set_specific_stat (self, nameStat, value):
        self.statsDict[nameStat] = value
        
    # Validates if the stats are valid (Single validation will be updated in the FUTURE)
    def validate (self):
        # Base stats must be between 0 and 255
        if self.typeStat == StatType.BASE:
            if not all (0 <= value <= 255 for value in self.statsDict.values()):
                return False
        
        # EVs must be between 0 and 252. Also the sum of all EVs must be less or equal to 510
        if self.typeStat == StatType.EV:
            values = self.statsDict.values()
            if not all (0 <= value <= 252 for value in values):
                return False
            
            if sum(values) > 510:
                return False
        
        # IVs must be between 0 and 31.
        if self.typeStat == StatType.IV:
            if not all (0 <= value <= 31 for value in self.statsDict.values()):
                return False
        
        # Final stats must be over 1.
        if self.typeStat == StatType.FINAL:
            if not all (value > 1 for value in self.statsDict.values()):
                return False
        
        # Reaching this point means that the stats are valid
        return True
        
    def print_information_stats (self):
        print (f" ---------- STATS INFORMATION {self.typeStat}---------- ")
        for key, value in self.statsDict.items():
            print (f"{key.name}: {value}")