import pygame
from game import * 

class GameVisual :


    def update(self,screen,game):
        for x in range(game.map.width):
            for y in range(game.map.width):
                if (x,y) in game.map.ground:
                    screen.blit(ground,(x*TILESIZE,y*TILESIZE))
                elif(x,y) in game.map.wall:
                    screen.blit(wall,(x*TILESIZE,y*TILESIZE))

        screen.blit(hero,(game.hero.position[0]*TILESIZE,game.hero.position[1]*TILESIZE))
        screen.blit(guardian,(game.guardian.position[0]*TILESIZE,game.guardian.position[1]*TILESIZE)) 
        
        if game.needle.item_counter == 1 : 
            screen.blit(needle,(game.needle.position[0]*TILESIZE,game.needle.position[1]*TILESIZE))
        if game.tube.item_counter == 1:
            screen.blit(tube,(game.tube.position[0]*TILESIZE,game.tube.position[1]*TILESIZE))
        if game.ether.item_counter == 1:
            screen.blit(ether,(game.ether.position[0]*TILESIZE,game.ether.position[1]*TILESIZE))

        if game.win_condition():
            screen.blit(win_text,(320 - win_text.get_width() // 2, 240 - win_text.get_height() // 2))
        if game.loose_condition():
            screen.blit(loose_text,(320 - loose_text.get_width() // 2, 240 - loose_text.get_height() // 2))