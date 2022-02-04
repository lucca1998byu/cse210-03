#Lucca

class Display():
    def display(self, guess, word, displayword ):
        
        
        for position in range(len(word)):
            letter = word[position]

            if letter == guess:
                displayword[position] = guess
        return displayword