from constantes import*
from position import*

class Level:

    def __init__(self,file):
        self.file = file

        #self.level=list() pr affichage
        self.ground=list()
        self.wall=list()
        self.start=list()
        self.finish=list()
        #self.level.append(self.ground) pr affichage 

    def load_level(self):
        with open(self.file) as my_level:
            for  x,line in enumerate(my_level):
                for y,column in enumerate(line):
                    if column == GROUND :
                        self.ground.append(Position(x,y))                        
                    elif column == WALL:
                        self.wall.append(Position(x,y))
                    elif column == START:
                        self.start.append(Position(x,y))
                        self.ground.append(Position(x,y))
                    else:
                        self.finish.append(Position(x,y))
                        self.ground.append(Position(x,y))
    
    def is_valid_position(self,position):
        return position in self.ground
        

test = Level('data/level/level1.txt')
test.load_level()
p = Position(0,0)

print(test.is_valid_position(p))