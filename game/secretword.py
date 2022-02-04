#Emer
#The puzzle is a secret word randomly chosen from a list.
<<<<<<< HEAD

import random

class Secretword():
=======
import random

class secretword():
>>>>>>> 0f1d825a98fa1eebf05f744e3697c831cf49e1e2
    def __init__(self):
        self.word= ""

    def secretword(self):
        
        list = [
            "water",
            "apple",
            "star",
            "table"
<<<<<<< HEAD
            
=======
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
>>>>>>> 0f1d825a98fa1eebf05f744e3697c831cf49e1e2
        ]
        
        word = random.choice(list)
        self.word = word
        return word
    
    def displayword(self, word):
        display = []
        for letter in range(len(word)):
            display += "_"
        return display
