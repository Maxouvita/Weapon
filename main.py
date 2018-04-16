#coding utf-8

import pygame
from pygame.locals import *
import os
import math
from monstre import *
from personnage import *

pygame.init()

win = pygame.display.set_mode((1280,720), FULLSCREEN)
fondmenu = pygame.image.load("TEXTURES/menu principal.jpg")
level1 = pygame.image.load("TEXTURES/level_1-2.png")
astro = personnage()
personnage = pygame.image.load(astro.path).convert_alpha()
personnageD = pygame.image.load(astro.pathD).convert_alpha()
personnageG = pygame.image.load(astro.pathG).convert_alpha()
boutonJouer = pygame.image.load("TEXTURES/Bouton Jouer.png").convert_alpha()
bulleJouer = pygame.image.load("TEXTURES/Bulle Jouer.png").convert_alpha()
logo = pygame.image.load("TEXTURES/Logo.png").convert_alpha()
viseur = pygame.image.load("TEXTURES/Viseur.png").convert_alpha()
balle = pygame.image.load("TEXTURES/Balle.png").convert_alpha()

def ffond(niveau):
    if niveau == 1 or niveau == 2:
        win.blit(level1, (0,0))
    if niveau == 3:
        win.blit(level3, (0,0))
    if niveau == 4:
        win.blit(level4, (0,0))
    if niveau == 5:
        win.blit(level5, (0,0))
    if niveau == 6:
        win.blit(level6, (0,0))
    if niveau == 7:
        win.blit(level7, (0,0))
    if niveau == 8:
        win.blit(level8, (0,0))
    if niveau == 9:
        win.blit(level9, (0,0))
    pass

class menu():


    continuer = True
    mouse_x, mouse_y = 0, 0

    boutonPlay_x = 500
    boutonPlay_y = 220
    boutonPlay_w = 330
    boutonPlay_h = 132

    bullePlay_x = 390
    bullePlay_y = boutonPlay_y+15
    bullePlay_w = 110
    bullePlay_h = 57

    cursor_w = 54
    cursor_h = 54

    logo_x = 529
    logo_y = 25






    while continuer == True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer = False
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if mouse_x > boutonPlay_x and mouse_x < boutonPlay_x+boutonPlay_w and mouse_y > boutonPlay_y and mouse_y < boutonPlay_y+boutonPlay_y:
                    continuer = False
            pass

        win.blit(fondmenu, (0,0))
        win.blit(boutonJouer, (boutonPlay_x,boutonPlay_y))
        win.blit(logo, (logo_x,logo_y))
        if mouse_x > boutonPlay_x and mouse_x < boutonPlay_x + boutonPlay_w and mouse_y > boutonPlay_y and mouse_y < boutonPlay_y + boutonPlay_h:
            win.blit(bulleJouer, (bullePlay_x,bullePlay_y))
            pass
        win.blit(viseur, (mouse_x-(cursor_w/2),mouse_y-(cursor_h/2)))
        pygame.display.flip()

        continue
    pass



class play():

    cursor_w = 54
    cursor_h = 54
    rectPlayer_x = 20
    rectPlayer_y = 20
    rectPlayer_w = 13
    rectPlayer_h = 34
    rectBalle_x = 0
    rectBalle_y = 5
    rectBalle_w = 5
    rectBalle_h = 3
    orientation = "Defaut"
    niveau = 1
    continuer = True






    while continuer == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer = False
        mouse_x, mouse_y = pygame.mouse.get_pos()



        ffond(niveau)
        win.blit(balle, (rectBalle_x-(rectBalle_w/2), rectBalle_y-(rectBalle_h/2)))
        win.blit(viseur, (mouse_x,mouse_y))
        if orientation == "Defaut":
            win.blit(personnage, (rectPlayer_x,rectPlayer_y))
        if orientation == "Droite":
            win.blit(personnageD, (rectPlayer_x,rectPlayer_y))
        if orientation == "Gauche":
            win.blit(personnageG, (rectPlayer_x,rectPlayer_y))
            win.blit(viseur, (mouse_x-(cursor_w/2),mouse_y-(cursor_h/2)))
        pygame.display.flip()

        pass

    pass
