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
    def __init__(self, filename="", thirst=0, energy=0, accuracy=0, strength=0, painTolerence=0, speed=0, perception=0,
                    foodMods="", bonusTraits="", occupationTraits=""):
        questions = []
        if filename != "": self.load(filename)
        self.statblock = [thirst, energy, accuracy, strength, painTolerence, speed, perception, foodMods, bonusTraits, occupationTraits]

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

    def getStatName(self, index):
        l = ["thirst", "energy", "accuracy", "strength", "painTolerence", "speed", "perception", "foodMods", "bonusTraits", "occupationTraits"]
        return l[index]

    def printStatBlock (self):
        foodMods = "\t" + self.getFoodMods().replace("\n","\n\t")
        occupationTraits = "\t" + self.getOccupationTraits().replace("\n","\n\t")
        bonusTraits = "\t" + self.getBonusTraits().replace("\n","\n\t")

        output = "\nName:\tPlayer:\nThirst: {}/{}\tEnergy: {}/{}\nPain Tolerence: {}\nAcc: {}\tPerc: {}\nStr: {}\tSpd : {}\n\nFood Mods:{}\n\nOccupation Traits:{}\n\nBonus Traits:{}\n"

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

            question.append(file.pop(0).strip())    # question[0] is the actual question, the rest are answers

            line = file.pop(0)                      # We don't strip() here so we can test for newlines

            while line != "\n" and len(file) > 0:
                line = line.strip().split(';')

                question.append(line)
                line = file.pop(0)

            questions.append(question)

        self.questions = questions
        return questions

    def clear(error=""):
        import platform
        import os
        if platform.system() == 'Windows':
            _=os.system('cls')
        else:
            _=os.system('clear')

        if error: print(error)

    def input(self, promptText, indexRange):
        try:
            n = int(input(promptText))
        except ValueError:
            n = self.input("Please enter a number.\n> ", indexRange)

        if n > (indexRange):
            n = self.input("Please enter one of the choices above.\n> ", indexRange)

        return n

    def addStatBlock(self, statSet):
        """
        Adds the recieved statSet to the global stat block.
        Dynamically summs numbers and concatenates strings
        """
        if len(statSet) != len(self.statblock):
            exc = "{}\nStatSet incorrect length. Expected {}, got {}.".format(statSet, str(len(self.statblock)), str(len(statSet)))
            raise Exception(exc)

        for i in range(len(statSet)):          # Convert all the numbers in the array to usable integers
            try:
                statSet[i] = int(statSet[i])
            except ValueError:
                statSet[i] = "\n" + statSet[i]    # Adds a newline to the beginning of all strings
                # pass

        for i in range(len(statSet)):
            # If statSet[i] is an integer, this performs integer division
            # If statSet[i] is a string, this concatenates
            try:
                self.statblock[i] += statSet[i]
            except TypeError:
                print("Set {} corrupted\nTried to add disparate types '{}' and {}: {}.".format(statSet, statSet[i].strip(), type(self.statblock[i]), self.getStatName(i)))
                quit()

    def ask(self, qIndex):
        """
        Prints a question and a series of answers, then prompts for an answer.
        Adds the relevant stats from the answer to the global stat block.
        """
        q = self.questions[qIndex]
        
        print(q[0])
        for i in range(1, len(q)):
            print("\t{}. {}".format(i,q[i][0]))

        answer = self.input("> ",len(q)-1)

        self.addStatBlock(q[answer][1:])            # Sends everything but the answer text to the statblock


########
# Main #
########
def main():
    character = Character()
    character.load("character")
    character.printStatBlock()
    character.ask(0)
    character.ask(1)
    character.ask(2)
    character.printStatBlock()

if __name__ == '__main__':
    main()
