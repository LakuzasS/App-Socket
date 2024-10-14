import math

class Point:
    """
    Création de la classe Point.
    """
    nom = "Point"
    def __init__(self, x : float = 0, y : float = 0):
        """
        (Constructeur) Fonction qui permet d'initialiser les 
        attributs de la classe Point.
        """
        self.__x = x
        self.__y = y 

    def distanceCoord(self, x : float, y : float) -> float:
        """
        (Méthode) Fonction qui permet de calculer la distance 
        par rapport à un autre point via les coordonnées.
        """
        if isinstance(x, (float, int)) and isinstance(y, (float, int)):
            return math.sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)
        else:
            raise TypeError("Mauvaise valeur de coordonnée !")

    def distancePoint(self, p : 'Point') -> float:
        """
        (Méthode) Fonction qui permet de calculer la distance 
        par rapport à l'objet Point associé à l'autre point.
        """
        return math.sqrt((self.__x - p.__x) ** 2 + (self.__y - p.__y) ** 2)

if __name__ == "__main__":
    p = Point()
    p2 = Point(1, 5)
    print(p2.distanceCoord(2, 4))

class Cercle:
    """ 
    Création de la classe Cercle.
    """

    def __init__(self, r: float = 0, c: 'Point' = Point()):
        """
        (Constructeur) Fonction qui permet d'initialiser les attributs
        de la classe Cercle.
        """
        if isinstance(c, Point):
            self.__centre = c
            self.__rayon = r
        else:
            raise TypeError("Le centre doit être une instance de la classe Point")

    def diametre(self) -> float:
        """
        (Méthode) Fonction qui permet de calculer le diamètre du cercle.
        """
        return 2 * self.__rayon

    def perimetre(self) -> float:
        """
        (Méthode) Fonction qui permet de calculer le périmètre du cercle.
        """
        return 2 * math.pi * self.__rayon

    def surface(self) -> float:
        """
        (Méthode) Fonction qui permet de calculer la surface du cercle.
        """
        return math.pi * self.__rayon ** 2

    def Intersection(self, autreCercle: 'Cercle') -> bool:
        """
        (Méthode) Fonction qui permet de déterminer si un autre cercle
        est en intersection avec celui-ci.
        """
        distance_centres = self.__centre.distancePoint(autreCercle.__centre)
        somme_rayons = self.__rayon + autreCercle.__rayon
        return distance_centres <= somme_rayons

    def Appartient(self, point: 'Point') -> bool:
        """
        (Méthode) Fonction qui permet de déterminer si un Point A fait
        partie du cercle.
        """
        distance_centre_point = self.__centre.distancePoint(point)
        return distance_centre_point <= self.__rayon

if __name__ == "__main__":
    c1 = Cercle(3) 
    c2 = Cercle(4, Point(2, 2))
    
    print("Cercle 1 - Rayon:", c1.diametre(), "Diamètre:", c1.diametre(), "Périmètre:", c1.perimetre(), "Surface:", c1.surface())
    print("Cercle 2 - Rayon:", c2.diametre(), "Diamètre:", c2.diametre(), "Périmètre:", c2.perimetre(), "Surface:", c2.surface())
    
    if c1.Intersection(c2):
        print("Les cercles c1 et c2 sont en intersection.")
    else:
        print("Les cercles c1 et c2 ne sont pas en intersection.")
    
    point_A = Point(3, 3)
    if c1.Appartient(point_A):
        print("Le Point A appartient au cercle c1.")
    else:
        print("Le Point A n'appartient pas au cercle c1.")

class Rectangle:
    """
    Création de la classe Rectangle.
    """

    def __init__(self, bg: 'Point' = Point(), l: float = 1, h: float = 1):
        """
        (Constructeur) Fonction qui permet d'initialiser les attributs
        de la classe Rectangle.
        """
        if isinstance(bg, Point):
            self.__bas_gauche = bg
            self.__longueur = l
            self.__hauteur = h
        else:
            raise TypeError("Le point bas-gauche doit être une instance de la classe Point")

    def surface(self) -> float:
        """
        (Méthode) Fonction qui permet de calculer la surface du rectangle.
        """
        return self.__longueur * self.__hauteur

    def perimetre(self) -> float:
        """
        (Méthode) Fonction qui permet de calculer le périmètre du rectangle.
        """
        return 2 * (self.__longueur + self.__hauteur)

    def BG(self) -> 'Point':
        """
        (Méthode) Fonction qui retourne le Point bas-gauche du rectangle.
        """
        return self.__bas_gauche

    def BD(self) -> 'Point':
        """
        (Méthode) Fonction qui retourne le Point bas-droit du rectangle.
        """
        x = self.__bas_gauche._Point__x + self.__longueur
        y = self.__bas_gauche._Point__y
        return Point(x, y)
    
    def HG(self) -> 'Point':
        """
        (Méthode) Fonction qui retourne le Point haut-gauche du rectangle.
        """
        x = self.__bas_gauche._Point__x
        y = self.__bas_gauche._Point__y + self.__hauteur
        return Point(x, y)

    def HD(self) -> 'Point':
        """
        (Méthode) Fonction qui retourne le Point haut-droit du rectangle.
        """
        x = self.__bas_gauche._Point__x + self.__longueur
        y = self.__bas_gauche._Point__y + self.__hauteur
        return Point(x, y)

    def VérifiePoint(self, point: 'Point') -> bool:
        """
        (Méthode) Fonction qui vérifie si un Point est situé dans le rectangle.
        """
        x = point._Point__x  
        y = point._Point__y  
        x_min = self.__bas_gauche._Point__x
        x_max = x_min + self.__longueur
        y_min = self.__bas_gauche._Point__y
        y_max = y_min + self.__hauteur
        return x_min <= x <= x_max and y_min <= y <= y_max

if __name__ == "__main__":
    r1 = Rectangle() 
    r2 = Rectangle(Point(1, 2), 3, 4)
    
    print("Rectangle 1 - Surface:", r1.surface(), "Périmètre:", r1.perimetre())
    print("Rectangle 2 - Surface:", r2.surface(), "Périmètre:", r2.perimetre())
    
    point_A = Point(2, 3)
    if r1.VérifiePoint(point_A):
        print("Le Point A est dans le rectangle r1.")
    else:
        print("Le Point A n'est pas dans le rectangle r1.")
    
    print("Coin bas gauche de r2:", r2.BG().distanceCoord(0, 0))
    print("Coin bas droit de r2:", r2.BD().distanceCoord(0, 0))
    print("Coin haut gauche de r2:", r2.HG().distanceCoord(0, 0))
    print("Coin haut droit de r2:", r2.HD().distanceCoord(0, 0))

class TriangleRectangle:
    """
    Création de la classe TriangleRectangle.
    """

    def __init__(self, c1: float = 1, c2: float = 1, ad: 'Point' = Point()):
        """
        (Constructeur) Fonction qui permet d'initialiser les attributs
        de la classe TriangleRectangle.
        """
        if isinstance(ad, Point):
            self.__cote1 = c1
            self.__cote2 = c2
            self.__angle_droit = ad
        else:
            raise TypeError("Le point de l'angle droit doit être une instance de la classe Point")

    def hypothenuse(self) -> float:
        """
        (Méthode) Fonction qui retourne la valeur de l'hypoténuse du triangle.
        """
        return math.sqrt(self.__cote1 ** 2 + self.__cote2 ** 2)

    def perimetre(self) -> float:
        """
        (Méthode) Fonction qui retourne le périmètre du triangle.
        """
        return self.__cote1 + self.__cote2 + self.hypothenuse()

    def surface(self) -> float:
        """
        (Méthode) Fonction qui retourne la surface du triangle.
        """
        return 0.5 * self.__cote1 * self.__cote2

    def Isocèle(self) -> bool:
        """
        (Méthode) Fonction qui vérifie si le triangle est isocèle.
        """
        return self.__cote1 == self.__cote2

if __name__ == "__main__":
    t1 = TriangleRectangle(3, 4) 
    t2 = TriangleRectangle(5, 12, Point(0, 0)) 
    
    print("Triangle 1 - Hypoténuse:", t1.hypothenuse(), "Périmètre:", t1.perimetre(), "Surface:", t1.surface())
    print("Triangle 2 - Hypoténuse:", t2.hypothenuse(), "Périmètre:", t2.perimetre(), "Surface:", t2.surface())
    
    if t1.Isocèle():
        print("Le triangle t1 est isocèle.")
    else:
        print("Le triangle t1 n'est pas isocèle.")
