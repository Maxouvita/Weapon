#coding utf-8

import pygame
from pygame.locals import *

class Arbre_Comp_Options():
    """docstring for [object Object]."""
    def __init__(self):
        """Différents attributs :
        -
        -
        -
        -           Tu mets ici tes constantes nésséssaires. (surtout pas l'initialisation de la fenetre ici.)
        -
        -
        -
        """

    def arbrecomp(self):
        """ Commentaire """

        

        fondc = pygame.image.load("TEXTURES/Fond.jpg").convert_alpha()

        arbre = True
        while arbre == True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    arbre = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        arbre = False
            win.blit(fondc,(0,0))
            pygame.display.flip()
            pass

        # code


        pass

    def options(self):

        pass
