#Lucca
# The parachute class keeps the lives of the user
#every time the user guess wrong, he misses a live
class Parachute():

    # the method returns a variable, depending of the argument given when its called in Director

    def parachute(check):
        parachute1 = """
     _____    
    /_____\\
    \     /   Lifes: 5
     \   /
      😅 

        """
        parachute2 = """
      
    /_____\\
    \     /   Lifes: 4
     \   /
      😥    
        
        """

        parachute3 = """
        
     _____
    \     /   Lifes: 3
     \   /
      😨        
        

        """
        parachute4 = """
        
     _____
    \     /   Lifes: 2
     \   /
      😖        
        

        """
        parachute5 = """
        
    

     \   /    Lifes: 1
      😵   

        
        """

        parachute6 = """
        
    

     
      👻   
        
        
        """
        if check == 1:
            return parachute1 
        elif check == 2:
            return parachute2
        elif check == 3:
            return parachute3
        elif check == 4:
            return parachute4
        elif check == 5:
            return parachute5
        else:
            return parachute6