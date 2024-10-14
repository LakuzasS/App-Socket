class Tasse:
    """
    Création d'une classe tasse 
    """
    def __init__(self, mat : str, coul : str, con : float, mar : str):
        """
        fonction qui permet d'initialiser les attributs d'instance de la classe Tasse
        """
        self.matiere = mat
        self.couleur = coul
        self.contenance = con
        self.marque = mar

    # def getMatiere(self):
    #     return self.matiere
    
    # def getCouleur(self):
    #     return self.couleur

    # def getcontenance(self):
    #     return self.contenance

    # def getMarque(self):
    #     return self.marque
    
    # def setMatiere(self):
    #     self.matiere = matiere
    
    # def setCouleur(self):
    #     self.couleur = couleur

    # def setcontenance(self):
    #     self.contenance = contenance

    # def setMarque(self):
    #     self.marque = marque
    
    def __str__(self):
        """
        fonction qui permet de retourner des chaines de caractères dans les appels print
        """
        print(f"La tasse de matière", self.matiere ,"est de couleur", self.couleur ,"et de marque", self.marque ,"a une contenance de", self.contenance ,"ml.")

    def __del__(self):
        """
        fonction qui permet d'éliminer les attributs de la tasse créée précédemment ssi la tasse est vide, autrement dit si la contenance est égale à 0 ml
        """
        if self.contenance == 0: 
            matiere.__del__(self)
            couleur.__del__(self)
            contenance.__del__(self)
            marque.__del__(self)

Tasse1 = Tasse(mat="céramique", coul="bleue", mar="duralex", con="50")
Tasse1.__str__()

