#coding utf-8

class arme():
    """docstring for [object Object]."""
    def __init__(self):
        """Différents attributs pour chacunes des armes :
        - rand : combien l'arme est précise. (de 500 à 32 000) (+ pour plus de préscision.)
        - name : nom de l'arme commes le nom du fichier image de l'arme. (str)
        - balle : balle utilisée. (chemin en str de l'image)
        - repeat : si l'arme tire en raffale ou pas.
        - speed : vitesse de l'arme à tirer. (tours de boucles à attendre avant un nouveau tour.)
        - type_arme : selon la classe du joueur : Explosive, Electricité, Rapide ou Defaut.
        - reload : vitesse de l'arme à être rechargée. (tours de boucles à attendre avant un nouveau tour.)
        """

    def Glock_12(self):
        """ Arme de niveau 1 """
        self.rand = 5000
        self.name = "Glock 12"
        self.balle = "TEXTURES/Balle.png"
        self.repeat = False
        self.speed = 0
        self.type_arme = "Defaut"
        self.relaod = 0
        pass

    def Glock_18(self):
        """ Arme de niveau 2 """
        self.rand = 0
        self.name = 0
        self.balle = 0
        self.repeat = 0
        self.speed = 0
        self.type_arme = 0
        pass
