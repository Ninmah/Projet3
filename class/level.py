from parameter import*
from position import*

class Level:

    def __init__(self,file):
        self.file = file

        
        self.ground=list()
        self.wall=list()
        self.start=list()
        self.finish=list()
        


    def load_level(self):
        with open(self.file,) as my_level:
            for  x,line in enumerate(my_level):
                for y,column in enumerate(line):
                    if column == GROUND :
                        self.ground.append(Position(x,y))
                    elif column == WALL:
                        self.wall.add(Position(x,y))
                    elif column == START:
                        self.start.add(Position(x,y))
                        self.ground.add(Position(x,y))
                    else:
                        self.finish.add(Position(x,y))
                        self.ground.add(Position(x,y))


test = Level('data/level/level1.txt')
print(test.wall)