# Wade

# Bring together all classes



from game.gameover import Gameover
from game.parachute import Parachute
from game.playerguess import Playerguess
from game.secretword import Secretword
from game.check import Check
from game.display import Display

class Director():

    def __init__(self):
        self.word = ""
        self.displayword = []
        self.parachute = ""
        self.game = True

    def start_game(self):
        
        word = Secretword().secretword()
        self.word = word

        self.displayword = Secretword().displayword(word)
            
        i = 1
        print(Parachute().parachute(i))

        while self.game:
            print()
            print(self.displayword)

            guess = Playerguess().get_input()
            check = Check().check(guess, self.word, self.displayword)
            
            if check:
                self.displayword  = Display().display(guess, self.word, self.displayword)   

            else:
                i += 1
                print(Parachute().parachute(i))

            game = Gameover().gameover(self.displayword ,i)
            
            if game or game == False:
                print(self.displayword)
                break
