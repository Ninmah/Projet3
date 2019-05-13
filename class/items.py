from map import*
import random
class Item :

    def __init__(self,level):
        self.level = level
        self.position = self.level.random_position_item()

    def add_items(self):
        self.level.items.append(self.position)