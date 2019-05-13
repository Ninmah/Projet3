from map import*
from items import *
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT

class Character :

    def __init__(self, map):
        self.map = map
        self.position = None
        

    def start_hero(self):
        self.position = self.map.start

    def position_guardian(self):
        self.position = self.map.finish

    def move(self,direction) :
        new_position = Position(self.position[0],self.position[1]).deplacement(direction)
        if new_position in self.map:
            self.position = new_position
    
    def exit(self):
        return self.position in self.map.finish 


hero1 = Character(map)
hero1.start_hero()
#hero1.move(KEY_LEFT)

