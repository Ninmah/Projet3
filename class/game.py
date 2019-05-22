from map import*
from character import*
from items import*

class Game : 

    def __init__(self):

        self.map = None
        self.hero = None
        self.guardian = None
        self.needle = None
        self.ether = None
        self.tube = None
        self.win_counter = 0
    def start(self):

        self.map = Map("/home/ben/Documents/Projet_OpenClassroom/Projet3/data/level/level1.txt")
        self.map.load_map()
        self.hero = Character(self.map)
        self.hero.start_hero()
        self.guardian = Character(self.map)
        self.guardian.position_guardian()
        self.needle = Item(self.map,'needle')
        self.tube = Item(self.map,'tube')
        self.ether = Item(self.map,'ether')

    def move(self,direction):
        self.hero.move(direction)


    def take_item(self):
        if self.hero.position == self.needle.position :
            if self.needle.item_counter ==1:
                self.win_counter +=1
            self.needle.item_counter = 0
            
        elif self.hero.position == self.tube.position:
            if self.tube.item_counter ==1:
                self.win_counter +=1
            self.tube.item_counter = 0
            
        elif self.hero.position == self.ether.position:
            if self.ether.item_counter ==1:
                self.win_counter +=1
            self.ether.item_counter = 0
            
    
    def exit(self):
        if self.hero.position == self.guardian.position and self.win_counter == 3:
            print("tu as gg")
        elif self.hero.position == self.guardian.position and self.win_counter != 3:
            print("tu as loose")