#Joseph
#If the guess is correct, the letter is revealed.
#If the guess is incorrect, a line is cut on the player's parachute.

# defines the Check() class.
class Check():
    def __init__(self):
        self.word = ""
        self.display = []

    # the check method takes four arguement.
    def check(self, guess, word, display ):
        self.word = word
        self.display = display
        if guess in self.word:
            return True
        else:
            print(f"{guess} not in word")
            return False