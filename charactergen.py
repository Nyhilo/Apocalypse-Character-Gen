"""
TODO
Quiz the user
Have setting for full randomness

Source files will have a question and several answers
Each answer has and aswer text and a semi-colon deliminated stat block
Stats in the block are addative. Numbers accumulate, Text concatenates
Format:

    text; thirst; energy; accuracy; strength; pain tolerance; speed; perception; food mods; bonus traits; occupation traits
"""

class Character (object):
    """docstring for Character  """
    def __init__(self, thirst=0, energy=0, accuracy=0, strength=0, painTolerence=0, speed=0, perception=0,
                    foodMods="", bonusTraits="", occupationTraits=""):
        statblock = [thirst, energy, accuracy, strength, painTolerence, speed, perception, foodMods, bonusTraits, occupationTraits]

    def getThirst (self): return self.stablock[0]

    def getEnergy (self): return self.stablock[1]

    def getAccuracy (self): return self.stablock[2]

    def getStrength (self): return self.stablock[3]

    def getPainTolerence (self): return self.stablock[4]

    def getSpeed (self): return self.stablock[5]

    def getPerception (self): return self.stablock[6]

    def getFoodMods (self): return self.stablock[7]

    def getBonusTraits (self): return self.stablock[8]

    def getOccupationTraits (self): return self.stablock[9]

