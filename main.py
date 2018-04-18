#coding utf-8

import pygame
from pygame.locals import *
import os
import time
from random import randrange
from math import *
from monstre import *
from personnage import *
from Arbre_Comp_Options import *
from arme import *

pygame.init()
# pygame.key.set_repeat(80, 22) elvevé car j'ai remplacé if KEYDOWN par pygame.get_pressed.

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
boutoncomp = pygame.image.load("TEXTURES/boutoncomp.png").convert_alpha()

arbre_comp = Arbre_Comp_Options()
arme = arme()



class menu():

    continuer = True
    mouse_x, mouse_y = 0, 0

    boutonPlay_x = 500
    boutonPlay_y = 220
    boutonPlay_w = 330
    boutonPlay_h = 132

    boutoncomp_x = 565
    boutoncomp_y = 400
    boutoncomp_w = 217
    boutoncomp_h = 84

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
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if mouse_x > boutoncomp_x and mouse_x < boutoncomp_x+boutoncomp_w and mouse_y > boutoncomp_y and mouse_y < boutoncomp_y+boutoncomp_y:
                    arbre_comp.arbrecomp()
                    continuer = True
            pass

        win.blit(fondmenu, (0,0))
        win.blit(boutoncomp, (boutoncomp_x,boutoncomp_y))
        win.blit(boutonJouer, (boutonPlay_x,boutonPlay_y))
        win.blit(logo, (logo_x,logo_y))
        if mouse_x > boutonPlay_x and mouse_x < boutonPlay_x + boutonPlay_w and mouse_y > boutonPlay_y and mouse_y < boutonPlay_y + boutonPlay_h:
            win.blit(bulleJouer, (bullePlay_x,bullePlay_y))
            pass
        win.blit(viseur, (mouse_x-(cursor_w/2),mouse_y-(cursor_h/2)))
        pygame.display.flip()
        continue
    pass

time.sleep(1)

class play():

    global rectBalle_w, rectBalle_h
    global BallesPos_x, BallesPos_y
    global vitesseBalle_x, vitesseBalle_y
    global alpha, imax
    cursor_w = 54
    cursor_h = 54
    rectPlayer_x = 20
    rectPlayer_y = 20
    rectPlayer_w = 13
    rectPlayer_h = 34

    rectBalle_w = 5
    rectBalle_h = 3
    playerVitess_x = 0
    playerVitess_y = 0
    orientation = "Defaut"
    niveau = 1
    continuer = True
    i = 0
    imax = 150 # nombre maximal de balles à l'écran
    BallesPos_x = []
    BallesPos_y = []
    vitesseBalle_x = []
    vitesseBalle_y = []
    alpha = []
    tirer = False

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


    for i in range(0, imax):
        BallesPos_x.append(0)
        BallesPos_y.append(0)
        vitesseBalle_x.append(0)
        vitesseBalle_y.append(0)
        alpha.append(0)
        pass


    def fafficherBalle():
        for elt in range(0, imax):
            BallesPos_x[elt] += vitesseBalle_x[elt]
            BallesPos_y[elt] += vitesseBalle_y[elt]
            win.blit(balle, (BallesPos_x[elt]-(rectBalle_w/2),BallesPos_y[elt]-(rectBalle_h/2)))
            pygame.transform.rotate(balle, degrees(alpha[elt]))
            pass
        pass


    while continuer == True:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x, mouse_y = mouse_x, mouse_y
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    continuer = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                tirer = True

            if event.type == MOUSEBUTTONUP and event.button == 1:
                tirer = False
        if tirer == True:
            i += 1
            alpha[i] = asin((mouse_x - rectPlayer_x)/(sqrt((rectPlayer_x - mouse_x)**2+(rectPlayer_y - mouse_y)**2))) - (pi / 2)
            vitesseBalle_x[i] = (cos(alpha[i])*10)+(randrange(-100,100,1)/200)
            vitesseBalle_y[i] = (sin(alpha[i])*10)+(randrange(-100,100,1)/200)
            BallesPos_x[i], BallesPos_y[i] = rectPlayer_x, rectPlayer_y
            if rectPlayer_y < mouse_y:
                vitesseBalle_y[i] -= 2*vitesseBalle_y[i]
                BallesPos_x[i], BallesPos_y[i] = rectPlayer_x, rectPlayer_y

        k = pygame.key.get_pressed()
        if k[K_RIGHT] or k[K_g]:
            playerVitess_x += 1.2
            orientation = "Droite"
        if k[K_LEFT] or k[K_d]:
            playerVitess_x -= 1.2
            orientation = "Gauche"
        if (k[K_LEFT] == False or k[K_d] == False) and (k[K_RIGHT] == False or k[K_g] == False):
            orientation = "Defaut"
        if ((k[K_RIGHT] or k[K_g]) and k[K_UP]) and rectPlayer_y + rectPlayer_h == pygame.display.Info().current_h:
            playerVitess_y = -9
            playerVitess_x += 1.2
        if ((k[K_LEFT] or k[K_d]) and k[K_UP]) and rectPlayer_y + rectPlayer_h == pygame.display.Info().current_h:
            playerVitess_y = -9
            playerVitess_x -= 1.2

        rectPlayer_x += playerVitess_x
        rectPlayer_y += playerVitess_y
        playerVitess_x = playerVitess_x / 1.25
        if rectPlayer_y + rectPlayer_h <= pygame.display.Info().current_h:
            playerVitess_y += 0.75
        else:
            playerVitess_y = 0
            rectPlayer_y = pygame.display.Info().current_h - rectPlayer_h


        ffond(niveau)
        fafficherBalle()
        win.blit(viseur, (mouse_x-(cursor_w/2),mouse_y-(cursor_h/2)))
        if orientation == "Defaut":
            win.blit(personnage, (rectPlayer_x,rectPlayer_y))
        if orientation == "Droite":
            win.blit(personnageD, (rectPlayer_x,rectPlayer_y))
        if orientation == "Gauche":
            win.blit(personnageG, (rectPlayer_x,rectPlayer_y))
            win.blit(viseur, (mouse_x-(cursor_w/2),mouse_y-(cursor_h/2)))
        pygame.display.flip()
        if i >= imax-1:
            i = 0
            pass
        pass

    pass
