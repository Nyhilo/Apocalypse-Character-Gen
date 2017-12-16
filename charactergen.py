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

from random import randint

class Character (object):
    """docstring for Character  """
    def __init__(self, filename = "", thirst=0, energy=0, accuracy=0, strength=0, painTolerence=0, speed=0, perception=0,
                    foodMods="", bonusTraits="", occupationTraits=""):
        self.statblock = [thirst, energy, accuracy, strength, painTolerence, speed, perception, foodMods, bonusTraits, occupationTraits]
        if filename != "": self.load(filename)

    def getThirst (self): return self.statblock[0]

    def getRandomThrist (self): return randint(0,self.getThirst())

    def getEnergy (self): return self.statblock[1]

    def getRandomEnergy (self): return randint(0,self.getEnergy())

    def getAccuracy (self): return self.statblock[2]

    def getStrength (self): return self.statblock[3]

    def getPainTolerence (self): return self.statblock[4]

    def getSpeed (self): return self.statblock[5]

    def getPerception (self): return self.statblock[6]

    def getFoodMods (self): return self.statblock[7]

    def getBonusTraits (self): return self.statblock[8]

    def getOccupationTraits (self): return self.statblock[9]

    def printStatBlock (self):
        foodMods = "\t" + self.getFoodMods().replace("\n","\n\t")
        occupationTraits = "\t" + self.getOccupationTraits().replace("\n","\n\t")
        bonusTraits = "\t" + self.getBonusTraits().replace("\n","\n\t")

        output = "\nName:\tPlayer:\nThirst: {}/{}\tEnergy: {}/{}\nPain Tolerence: {}\nAcc: {}\tPerc: {}\nStr: {}\tSpd : {}\n\nFood Mods:\n{}\n\nOccupation Traits:\n{}\n\nBonus Traits:\n{}\n"
        print(output.format(self.getRandomThrist(), self.getThirst(), self.getRandomEnergy(), self.getEnergy(),
                self.getPainTolerence(),
                self.getAccuracy(), self.getPerception(),
                self.getStrength(), self.getSpeed(),
                foodMods, occupationTraits, bonusTraits))

    def load(self, filename):
        with open(filename,'r') as f:
            file = f.readlines()

        questions = []

        while len(file) > 0:
            question = []

            # question[0] is the actual question
            question.append(file.pop(0).strip())

            # The other indices are the answers
            line = file.pop(0)
            while line != "\n" and len(file) > 0:
                line = file.pop(0)
                question.append(line.strip())

            questions.append(question)

        return questions


########
# Main #
########
def main():
    character = Character()
    character.load("character")
    character.printStatBlock()

if __name__ == '__main__':
    main()
