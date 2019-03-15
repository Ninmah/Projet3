# -*-coding:utf-8 -*
import os, sys
import pygame

TILESIZE = 20
MAPWIDTH = 15
MAPHEIGHT = 15
G=0
MV=1 
M=33
pygame.init()
screen = pygame.display.set_mode((TILESIZE*MAPWIDTH,TILESIZE*MAPHEIGHT))




textures={
          G: pygame.image.load("/home/ben/Documents/Projet_OpenClassroom/projet3/Sprites/floor-tiles.png").convert().subsurface(pygame.Rect(160,100,20,20)),#Ground
          MV: pygame.image.load("/home/ben/Documents/Projet_OpenClassroom/projet3/Sprites/structures.png").convert().subsurface(pygame.Rect(160,100,20,20)),  
        M : pygame.image.load("/home/ben/Documents/Projet_OpenClassroom/projet3/Sprites/structures.png").convert().subsurface(pygame.Rect(160,100,20,20))

}

level= [
            [M,M,M,M,M,M,M,M,M,M,M,M,M,M,MV],
            [G,G,G,G,G,G,G,G,G,MV,G,G,G,G,MV],
            [MV,M,M,M,M,M,M,G,G,MV,G,G,M,M,MV],
            [MV,G,G,G,G,G,G,G,G,MV,G,G,M,M,MV],
            [MV,G,G,G,M,M,M,M,G,G,G,G,M,M,MV],
            [MV,M,M,M,M,M,G,G,G,M,G,G,G,G,MV],
            [MV,G,G,G,G,G,G,G,M,M,G,M,M,G,MV],
            [MV,G,M,G,G,G,M,G,G,M,G,G,M,G,MV],
            [MV,G,M,M,M,M,M,M,M,M,M,M,M,G,MV],
            [MV,G,M,G,G,G,G,G,G,M,G,G,G,G,MV],
            [MV,G,M,M,G,G,M,G,M,M,G,M,G,G,MV] ,
            [MV,G,G,G,G,G,MV,G,M,M,G,M,M,M,MV], 
            [MV,G,G,G,G,G,MV,G,G,G,G,G,G,G,G],
            [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M], 
           ]


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            screen.blit(textures[level[0][column]], (column*TILESIZE,row*TILESIZE))
    pygame.display.update()

