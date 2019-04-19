from position import*
class Map : 

    def __init__(self,file):
        self.file = file
        self.start = []
        self.finish = []
        self.ground = []

    def load_map(self):
        
        with open(self.file,'r') as f :
            for x,line in enumerate(f):
                for y, col in enumerate(line):
                    if col == 'G': 
                        self.ground.append(Position(x,y))
                    if col == 'S':
                        self.start.append(Position(x,y))
                    if col == 'F':
                        self.finish.append(Position(x,y))

    def __contains__(self,position):
        return position in self.ground

    

map = Map("/home/ben/Documents/Projet_OpenClassroom/Projet3/data/level/level1.txt")
map.load_map()
p = Position(-8,0)
print(p in map)
