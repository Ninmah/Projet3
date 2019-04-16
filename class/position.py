class Position :
    
    def __init__(self,x,y):
        self.position = x,y

    def __repr__(self):
        
        return repr(self.position)
        
    def __getitem__(self,position):
        return self.position[position]
