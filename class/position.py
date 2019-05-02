class Position : 

    def __init__(self,x,y):
        self.position = (x,y)
        

    
    def __repr__(self):
        
        return str(self.position)

    def __eq__(self,other):
        return self.position == other

    def __getitem__(self, i):
        return self.position[i]
        

    def up(self):
        x,y = self.position
        return Position(x,y+1)
    
    def down(self):
        x,y = self.position
        return Position(x,y-1)
    
    def right(self):
        x,y = self.position
        return Position(x+1,y)
        
    def left(self):
        x,y = self.position
        return Position(x-1,y)


