# -*-coding:utf-8 -*
import os, sys
import pygame
from Map import*


TILESIZE = 20
MAPWIDTH = 15
MAPHEIGHT = 15

pygame.init()
screen = pygame.display.set_mode((TILESIZE*MAPWIDTH,TILESIZE*MAPHEIGHT),0,32)




ground=pygame.image.load("/home/ben/Documents/Projet_OpenClassroom/Projet3/Sprites/floor-tiles.png").convert().subsurface(pygame.Rect(160,100,20,20)),
wall=pygame.image.load("/home/ben/Documents/Projet_OpenClassroom/Projet3/Sprites/structures.png").convert().subsurface(pygame.Rect(160,100,20,20)),  
wallVertical=pygame.image.load("/home/ben/Documents/Projet_OpenClassroom/Projet3/Sprites/structures.png").convert().subsurface(pygame.Rect(160,100,20,20))




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.update()

