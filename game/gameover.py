#Lucca

#Everytime the loop is over, the Gameover class should check if
#the world is done, or the lives are over

class Gameover():

    #If the puzzle is solved the game is over.
    #If the player has no more parachute the game is over.
   
    def gameover(self, playerguess, turn):
        if '_' not in playerguess:
            print("Congratulations, you solved the secret word")
            return True
        elif turn == 6:
<<<<<<< HEAD
            print("Thanks for playeing, try again")
            return False    
=======
            print("Thanks for playing, try again")
>>>>>>> 0f1d825a98fa1eebf05f744e3697c831cf49e1e2
