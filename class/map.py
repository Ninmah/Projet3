from position import*
class Map:

    def __init__(self,fichier):
        self.fichier = fichier
        self.ground = list()
        self.wall = list() 
        self.start = list()
        self.finish = list()
        self.position = list()

    def generate_map(self):
        with open(self.fichier,'r') as map:
            for x,line in enumerate(map):
                    for y,column in enumerate(line):
                        if column == 'G':
                            self.ground.append(Position(x,y))
                        if column == '*':
                            self.wall.append(Position(x,y))
                        if column == 'S':
                            self.start.append(Position(x,y))
                            self.ground.append(Position(x,y))
                        if column == 'F':
                            self.finish.append(Position(x,y))
                            self.ground.append(Position(x,y))
map = Map("/home/ben/Documents/Projet_OpenClassroom/Projet3/data/level/level1.txt")
map.generate_map()
print(map.ground)
#generate map

