from map import*
from game import*
import random
class Item :

    def __init__(self,level,name):
        self.level = level
        self.position = self.level.random_position_item()
        self.name = name
        self.item_counter = 1

 

        

    def __repr__(self):
    
        return str(self.name)

