from map import*
from character import*
from items import*

class Game : 

    def __init__(self):

        self.map = None
        self.hero = None
        self.guardian = None
        self.items = None

    def start(self):

        self.map = Map("/home/ben/Documents/Projet_OpenClassroom/Projet3/data/level/level1.txt")
        self.map.load_map()
        self.hero = Character(self.map)
        self.hero.start_hero()
        self.guardian = Character(self.map).position_guardian()
        self.items1 = Item(self.map)
        self.items1.add_items()
       # self.items2 = Item(self.map)
        #self.items3 = Item(self.map)

    def move(self,direction):
        self.hero.move(direction)

    def take_item(self):
        return self.hero.position == self.items1.position