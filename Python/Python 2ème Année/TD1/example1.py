class Example: 
    """
    création d'une classe de test "Example"
    """
    def __init_(self, c :str):
        """
        focntion qui permet d'initialiser les attributs de la classe Exmaple
        """
        self.chaine = c

    def bonjour(nom : str) -> None:
        """
        fonction permettant de dire bonjour à une personne dont le nom est passé en argument
        """
        print(f"bonjour {nom}")
    
    if __name__ == "__main__":
        bonjour("Maxime")
        print(f"documentation fonction bonjour {bonjour.__doc__}")

    def Affiche(self):
        """
        fonction qui prend en argument une chaine de caractère puis qui l'affiche précédé de "Texte à afficher"
        """
        print("Texte à afficher :", self.c )

class Vélo:
    """
    création d'une classe Vélo
    """
    def __init__(self, m : str, t : float, c : str, v : int):
        self.marque = m
        self.taille = t
        self.couleur = c
        self.vitesse = v
    
    def gear_up(self):
        self.v += 1 
        return self.v

    def gear_down(self, v):
        self.v -= 1 
        return self.v

    def __str__(self):
        print("Le vélo est de marque", self.m,"possède une taille de pneus de", self.t, "est de couleur", self.c, "et a", self.v, "vitesses.")

v1 = Vélo(m="Orbea", t=1.20, c="blanc", v=24)
v1.__str__()

if v < 1 or v > 25:
    print("Oops, cette vitesse n'existe pas, essaye entre 1 et 25 !")
    v = int(input("Choisis ta nouvelle vitesse :"))
