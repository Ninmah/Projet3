from game import*
import curses

def update(screen):

    for x in range(game.map.width):
        for y in range(game.map.width):
            if (x,y) in game.map.start:
                screen.addstr(x,y,'S')
            if (x,y) in game.map.finish:
                screen.addstr(x,y,'F')
            elif (x,y) in game.map.ground:
                screen.addstr(x,y,'g')
            else:
                screen.addstr(x,y,"*")

def main(screen):
    while True:
        c = screen.getch()
        if c == ord('a'):
            update(screen)


game = Game()
game.start()
curses.wrapper(main)

