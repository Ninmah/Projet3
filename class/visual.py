from game import *
from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT
import curses




def update(screen):

    for x in range(game.map.width):
        for y in range(game.map.width):
            if (x,y) in game.map.finish:
                screen.addstr(x,y,'F')
            elif (x,y) in game.map.ground:
                screen.addstr(x,y,'G')
            else:
                screen.addstr(x,y,"*")

    screen.addstr(game.hero.position[0][0],game.hero.position[0][1],'H')

def main(screen):
    while True:
        key = screen.getch()
        if key == curses.KEY_UP:
            #game.hero.position
            update(screen)
            
            


game = Game()
game.start()
curses.wrapper(main)

