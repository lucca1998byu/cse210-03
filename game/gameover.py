#Lucca

#Everytime the loop is over, the Gameover class should check if
#the world is done, or the lives are over

class Gameover():
    def gameover(self, playerguess, turn):
        if '_' not in playerguess:
            print("""
            
Yb  dP  dP"Yb  88   88     Yb        dP 88 88b 88 
 YbdP  dP   Yb 88   88      Yb  db  dP  88 88Yb88 
  8P   Yb   dP Y8   8P       YbdPYbdP   88 88 Y88 
 dP     YbodP  `YbodP'        YP  YP    88 88  Y8 

            
            
            """)
            return True
        elif turn == 6:
            print("""
            
█▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀█ █░█ █▀▀ █▀█
█▄█ █▀█ █░▀░█ ██▄   █▄█ ▀▄▀ ██▄ █▀▄
            
            """)
            print("***********************")
            print("--------You Die-------")
            print("************************")
            return False
    
