from map import*
class Character :

    def __init__(self, map):
        self.map = map
        self.position = None
        

    def start_hero(self):
        self.position = self.map.start

    def position_guardian(self):
        self.position = self.map.finish

    def move(self, deplacement) : 
        new_position = getattr(self.position, str(deplacement))()
        if new_position in self.map:
            self.position = new_position

