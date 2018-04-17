#coding utf-8

class personnage():
    """docstring for [object Object]."""
    def __init__(self):
        """Attributs initiaux du personnage, comprenant :
        - la vie du personnage
        - la largeur de l'image
        - la hauteur de l'image
        - le chemin du sprite
        """
        self.vie = 100
        self.width = 13
        self.height = 34
        self.path = "TEXTURES/astro.png"
        self.pathD = "TEXTURES/astroDroite.png"
        self.pathG = "TEXTURES/astroGauche.png"
