from map import*
class Character :

    def __init__(self, map):
        self.map = map
        self.position = None
        

    def start_hero(self):
        self.position = self.map.start

    def position_guardian(self):
        self.position = self.map.finish

    def move(self) :
        new_position = Position(self.position[0][0],self.position[0][1])
        print(new_position)
        if new_position in self.map:
            self.position = new_position
            print(self.position)
hero1 = Character(map)
hero1.start_hero()

