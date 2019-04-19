class Hero :

    def __init__(self, level):
        self.level = level
        self.position = self.level.start_position
        
    def move(self, deplacement) : 
        new_position = self.position + deplacement
        if new_position in self.level:
            self.position = new_position

