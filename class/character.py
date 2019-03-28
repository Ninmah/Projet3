from level import*
class Character:

    def __init__(self,level):
        self.level= level
        self.position = self.level.start

    def __repr__(self):
        return str(self.position)  

test = Level('data/level/level1.txt')
hero = Character(test)
print(hero)
    