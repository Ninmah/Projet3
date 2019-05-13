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

    screen.addstr(game.hero.position[0],game.hero.position[1],'H')
    screen.addstr(game.items1.position[0],game.items1.position[1],'O')
    #screen.addstr(game.items2.position[0],game.items2.position[1],'O')
    #screen.addstr(game.items3.position[0],game.items3.position[1],'O')
    

def update_control(screen):
    key = screen.getch()
    if key in (KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT):
        game.hero.move(key)
        update(screen)
    if game.hero.exit():
        screen.addstr('tu as win ! ')

    if game.take_item():
        screen.addstr('tu as sdsd! ')
def main(screen):
    while True:
        update_control(screen)
        curses.curs_set(False)
        
            


game = Game()
game.start()
curses.wrapper(main)

