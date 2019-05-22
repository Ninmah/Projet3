from pygame import K_RIGHT, K_LEFT,K_DOWN,K_UP
from constantes import *

class Position : 

    def __init__(self,x,y):
        self.position = (x,y)
        
    def __repr__(self):
        
        return str(self.position)

    def __eq__(self,other):
        return self.position == other

    def __getitem__(self, i):
        return self.position[i]
        



    def deplacement(self,direction):

        if direction == K_UP:
            x,y = self.position
            return Position(x,y-1)

        elif direction == K_DOWN : 
            x,y = self.position
            return Position(x,y+1)

        elif direction == K_RIGHT :
            x,y = self.position
            return Position(x+1,y)

        elif direction == K_LEFT: 
            x,y = self.position
            return Position(x-1,y)


