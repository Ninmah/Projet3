import pygame
from pygame.locals import *
from constantes import*
from game import *


def main():
    
    pygame.init()
    game = Game()
    game.start()
    
    #initialisation de la fenêtre d'affichage
    screen = pygame.display.set_mode((675,675),RESIZABLE)
    pygame.display.set_caption("Labyrinthe MacGyver")
    font = pygame.font.SysFont("Arial", 72)
    win_text = font.render("You win", True, (51, 100, 255))
    loose_text = font.render("You loose", True, (51, 100, 255))


    
    #chargement sprite
    ground = pygame.image.load(ground_sprite).convert_alpha()
    wall = pygame.image.load(wall_sprite).convert_alpha()
    hero = pygame.image.load(hero_sprite).convert_alpha()
    needle = pygame.image.load(needle_sprite).convert_alpha()
    tube = pygame.image.load(tube_sprite).convert_alpha()
    ether = pygame.image.load(ether_sprite).convert_alpha()
    guardian = pygame.image.load(guardian_sprite).convert_alpha()

    continuer = True
    while continuer:

        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    continuer = False
                elif event.key == K_UP:
                    game.hero.move(K_UP)
                    game.take_item()
                elif event.key == K_DOWN:
                    game.hero.move(K_DOWN)
                    game.take_item()
                elif event.key == K_RIGHT:
                    game.hero.move(K_RIGHT)
                    game.take_item()
                elif event.key == K_LEFT:
                    game.hero.move(K_LEFT)
                    game.take_item()
                    
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
            

        pygame.display.flip()



if __name__ == '__main__': main()
