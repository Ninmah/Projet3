from position import Position
import random
class Map : 

    def __init__(self,file) :
        self.file = file
        self.start = []
        self.finish = []
        self.ground = []
        self.width = 15
        self.height = 15

    def load_map(self):
        
        with open(self.file,'r') as f :
            map = [line.strip() for line in f.readlines() if line.strip()]
        for x,line in enumerate(map) :
            for y, col in enumerate(line):
                if y != '\n':
                    if col == 'G': 
                        self.ground.append(Position(x,y))
                    if col == 'S':
                        self.start.append(Position(x,y))
                    if col == 'F':
                        self.finish.append(Position(x,y))


    def __contains__(self,position):
        return position in self.ground

   
    def random_position_item(self):
        return random.choice(self.ground[:])

     



