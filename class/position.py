from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

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

        if direction == KEY_UP:
            x,y = self.position
            return Position(x-1,y)

        elif direction == KEY_DOWN : 
            x,y = self.position
            return Position(x+1,y)

        elif direction == KEY_RIGHT :
            x,y = self.position
            return Position(x,y+1)

        elif direction == KEY_LEFT: 
            x,y = self.position
            return Position(x,y-1)


