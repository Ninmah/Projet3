import pygame
from pygame.locals import *
from constantes import*
from game import *


def main():
    #initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode((675,675),RESIZABLE)
    pygame.display.set_caption("Labyrinthe MacGyver")
    font = pygame.font.SysFont("Arial", 72)
    win_text = font.render("You win", True, (51, 100, 255))
    loose_text = font.render("You loose", True, (51, 100, 255))


    continuer = True
    #chargement sprite
    ground = pygame.image.load(ground_sprite).convert_alpha()
    wall = pygame.image.load(wall_sprite).convert_alpha()
    hero = pygame.image.load(hero_sprite).convert_alpha()
    needle = pygame.image.load(needle_sprite).convert_alpha()
    tube = pygame.image.load(tube_sprite).convert_alpha()
    ether = pygame.image.load(ether_sprite).convert_alpha()
    guardian = pygame.image.load(guardian_sprite).convert_alpha()

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
                    

            

        pygame.display.flip()


game = Game()
game.start()
if __name__ == '__main__': main()
