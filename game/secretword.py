#Emer
#The puzzle is a secret word randomly chosen from a list.
import random

class secretword():
    def __init__(self):
        self.word= ""

    def secretword(self):
        
        list = [
            "water",
            "apple",
            "star",
            "table"
            "nun"
            "burn"
            "sustain"
            "shelf"
            "reveal"
            "cheap"
            "bold"
            "promote"
            "matrix"
            "production"
        ]
        
        word = random.choice(list)
        self.word = word
        return word
    
    def displayword(self, word):
        display = []
        for letter in range(len(word)):
            display += "_"
        return display
