#Lucca
class Gameover():
    def gameover(self, secretword, playerguess):
        if secretword == playerguess:
            print("Congratulations, you solved the secret word")
        else:
            print("Thanks for playeing, try again")    


#If the puzzle is solved the game is over.
#If the player has no more parachute the game is over.