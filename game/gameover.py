#Lucca

#Everytime the loop is over, the Gameover class should check if
#the world is done, or the lives are over

class Gameover():

    #If the puzzle is solved the game is over.
    #If the player has no more parachute the game is over.
   
    def gameover(playerguess, turn):
        if '_' not in playerguess:
            print("Congratulations, you solved the secret word")
            return True
        elif turn == 6:
            print("Thanks for playing, try again")
