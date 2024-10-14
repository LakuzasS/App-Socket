class Personnage:
    """
    Classe décrivant le format générique de Personnage.

    Attributs:
        pseudo (str): Le pseudo du personnage.
        niveau (int): Le niveau du personnage.
        pointsDeVie (int): Les points de vie du personnage.
        initiative (int): L'initiative du personnage.
    """
    def __init__(self, pseudo: str, niveau: int = 1):
        """
        Constructeur de la classe Personnage.

        Arguments:
            pseudo (str): Le pseudo du personnage.
            niveau (int): Le niveau du personnage (par défaut 1).
        """
        self.__pseudo = pseudo
        if isinstance(niveau, int):
            self.__niveau = niveau
            self.__pointsDeVie = niveau
            self.__initiative = niveau
        else:
            raise TypeError(" /!\ Le niveau doit être un entier /!\ ")

    # Les accesseurs
    @property 
    def pointsDeVie(self) -> int:
        """
        Propriété qui permet d'obtenir les points de vie du personnage.

        Returns:
            int: Les points de vie du personnage.
        """
        return self.__pointsDeVie

    @pointsDeVie.setter  
    def pointsDeVie(self, pv: int):   
        """
        Setter pour les points de vie du personnage.

        Arguments:
            pv (int): Les nouveaux points de vie du personnage.

        Raises:
            ValueError: Si pv est inférieur à zéro.
            TypeError: Si pv n'est pas un entier.
        """  
        if isinstance(pv, int):
            if pv >= 0:
                self.__pointsDeVie = pv
            # else:
            #     raise ValueError(" /!\ Pas de PV négatifs /!\ ")
        else:
            raise TypeError(" /!\ Les PV doivent être des entiers /!\ ")

    @property
    def initiative(self) -> int:
        """
        Propriété qui permet d'obtenir l'initiative du personnage.

        Returns:
            int: L'initiative du personnage.
        """
        return self.__initiative

    @initiative.setter
    def initiative(self, ini: int):
        """
        Setter pour l'initiative du personnage.

        Arguments:
            ini (int): La nouvelle initiative du personnage.

        Raises:
            ValueError: Si l'initiative est inférieure à zéro.
            TypeError: Si l'initiative n'est pas un entier.
        """
        if isinstance(ini, int):
            if ini >= 0:
                self.__initiative = ini
            # else:
            #     raise ValueError(" /!\ Pas d'initiative négative /!\ ")
        else:
            raise TypeError(" /!\ L'initiative doit être un entier /!\ ")

    def degats(self) -> int:
        """
        Méthode qui permet de définir le nombre de dégâts causés par une
        attaque.

        Returns:
            int: Le nombre de dégâts causés.
        """
        return self.__niveau

    def attaque(self, adversaire: 'Personnage'):
        """
        Méthode qui teste les initiatives pour déterminer la priorité
        d'attaque des personnages.

        Arguments:
            adversaire (Personnage): Le personnage adversaire.
        """
        if self.__initiative > adversaire.__initiative:
            if adversaire.pointsDeVie > 0:  
                adversaire.pointsDeVie -= self.degats()
            if adversaire.pointsDeVie > 0:
                self.pointsDeVie -= adversaire.degats()
        elif adversaire.__initiative > self.__initiative:
            if self.pointsDeVie > 0: 
                self.pointsDeVie -= adversaire.degats()
            if self.pointsDeVie > 0:
                adversaire.pointsDeVie -= self.degats()
        else:
            if adversaire.pointsDeVie > 0:
                adversaire.pointsDeVie -= self.degats()
            if self.pointsDeVie > 0:
                self.pointsDeVie -= adversaire.degats()

    def combat(self, adversaire):
        """
        Méthode qui permet de mener toutes les attaques nécessaires à
        la mort d'un des deux assaillants.

        Arguments:
            adversaire: Le personnage adversaire.
        """
        while self.pointsDeVie > 0 and adversaire.pointsDeVie > 0:
            self.attaque(adversaire)
            adversaire.attaque(self)
        if self.pointsDeVie <= 0:
            print(f"{self.__pseudo} a perdu le combat !")
        if adversaire.pointsDeVie <= 0:
            print(f"{adversaire.__pseudo} a perdu le combat !")

    def soigner(self, adversaire):
        """
        Méthode qui permet de restaurer les points de vie du personnage
        jusqu'à son niveau.

        Arguments:
            adversaire: Le personnage à soigner.
        """
        self.pointsDeVie = self.__niveau
        adversaire.pointsDeVie = adversaire.__niveau
    
    def __eq__(self,adversaire):
        """
        Compare deux éléments en utilisant l'opérateur ==.

        Returns:
            bool: True si les deux éléments sont égaux, False sinon.
        """
        if (self.__pseudo == adversaire.__pseudo and self.__niveau == adversaire.__niveau):
            return True
        else:
            return False

    def __str__(self):
        """
        Méthode spéciale pour représenter le personnage sous forme de chaîne de caractères.

        Returns:
            str: Une chaîne de caractères représentant le personnage.
        """
        return f"Pseudo: {self.__pseudo}, Niveau: {self.__niveau}, Points de Vie: {self.__pointsDeVie}, Initiative: {self.__initiative}"


class Guerrier(Personnage):
    """
    Classe décrivant un personnage de type Guerrier, héritant de la classe Personnage.

    Attributs hérités de Personnage:
        pseudo (str): Le pseudo du personnage.
        niveau (int): Le niveau du personnage.
        pointsDeVie (int): Les points de vie du personnage.
        initiative (int): L'initiative du personnage.
    """
    def __init__(self, pseudo: str, niveau: int = 1):
        """
        Constructeur de la classe Guerrier.

        Arguments:
            pseudo (str): Le pseudo du Guerrier.
            niveau (int): Le niveau du Guerrier (par défaut 1).
        """
        super().__init__(pseudo, niveau)
        self.pointsDeVie = niveau * 8 + 4
        self.initiative = niveau * 4 + 6
    
    @property
    def niveau(self) -> int:
        """
        Propriété qui permet d'obtenir le niveau du Guerrier.

        Returns:
            int: Le niveau du Guerrier.
        """
        return self._Personnage__niveau

    def degats(self) -> int:
        """
        Méthode qui permet de définir le nombre de dégâts causés par une
        attaque.

        Returns:
            int: Le nombre de dégâts causés.
        """
        return self.niveau * 2

    def __str__(self):
        """
        Méthode spéciale pour représenter le guerrier sous forme de chaîne de caractères.

        Returns:
            str: Une chaîne de caractères représentant le guerrier.
        """
        return f"Guerrier - {super().__str__()}"


class Mage(Personnage):
    """
    Classe décrivant un personnage de type Mage, héritant de la classe Personnage.

    Attributs hérités de Personnage:
        pseudo (str): Le pseudo du personnage.
        niveau (int): Le niveau du personnage.
        pointsDeVie (int): Les points de vie du personnage.
        initiative (int): L'initiative du personnage.

    Attributs spécifiques aux Mages:
        mana (int): La mana du Mage.
    """
    def __init__(self, pseudo: str, niveau: int = 1):
        """
        Constructeur de la classe Mage.

        Arguments:
            pseudo (str): Le pseudo du Mage.
            niveau (int): Le niveau du Mage (par défaut 1).
        """
        super().__init__(pseudo, niveau)
        self.pointsDeVie = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        self.__mana = niveau * 5

    @property
    def mana(self) -> int:
        """
        Propriété qui permet d'obtenir la mana du Mage.

        Returns:
            int: La mana du Mage.
        """
        return self.__mana

    @mana.setter  
    def mana(self, mana : int):   
        """
        Setter pour la mana du Mage.

        Arguments:
            mana (int): La mana du Mage.

        Raises:
            ValueError: Si mana est inférieur à zéro.
            TypeError: Si mana n'est pas un entier.
        """  
        if isinstance(mana, int):
            if mana >= 0:
                self.__mana = mana
            else : 
                raise ValueError(" /!\ Pas de mana négatif /!\ ")
        else : 
            raise TypeError(" /!\ La mana doit être un entier /!\ ")
        
    @property
    def niveau(self) -> int:
        """
        Propriété qui permet d'obtenir le niveau du Mage.

        Returns:
            int: Le niveau du Mage.
        """
        return self._Personnage__niveau  

    def degats(self) -> int :
        """
        Méthode qui permet de définir le nombre de dégâts causés par une 
        attaque.

        Returns:
            int: Le nombre de dégâts causés.
        """
        if self.mana > 0 :
            return self.niveau + 3  
        else :
            return self.niveau

    def __str__(self):
        """
        Méthode spéciale pour représenter le mage sous forme de chaîne de caractères.

        Returns:
            str: Une chaîne de caractères représentant le mage.
        """
        return f"Mage - {super().__str__()}, Mana: {self.__mana}"


class Joueur:
    """
    Classe représentant un joueur de MMORPG.

    Attributs:
        nom (str): Le nom du joueur.
        personnages (list): Une liste de personnages du joueur.
        max_personnages (int): Le nombre maximum de personnages autorisés pour le joueur.
    """
    def __init__(self, nom: str, max_personnages: int):
        """
        Constructeur de la classe Joueur.

        Arguments:
            nom (str): Le nom du joueur.
            max_personnages (int): Le nombre maximum de personnages autorisés.
        """
        self.__nom = nom
        self.__max_personnages = max_personnages
        self.__personnages = []

    def ajouter_personnage(self, personnage: Personnage):
        """
        Ajoute un personnage à la liste des personnages du joueur.

        Arguments:
            personnage (Personnage): Le personnage à ajouter.
        """
        if len(self.__personnages) < self.__max_personnages:
            self.__personnages.append(personnage)
        else:
            raise IndexError(" /!\ La liste a atteint le nombre maximal de personnages /!\ ")

    def num_perso(self, num: int) -> Personnage:
        """
        Permet l'accès au numéro du personnage.

        Returns:
            int: Le numéro du personnage.
        """
        if 0 <= num < len(self.__personnages):
            return self.__personnages[num]
        else:
            raise IndexError(" /!\ Numéro de personnage invalide /!\ ")

    def pseudo_perso(self, pseudo: str) -> Personnage:
        """
        Permet l'accès au pseudo du personnage.

        Returns:
            str: Le pseudo du personnage.
        """
        for personnage in self.__personnages:
            if personnage._Personnage__pseudo == pseudo:
                return personnage
        raise ValueError(" /!\ Pseudo de personnage introuvable /!\ ")

    def donnes_perso(self, personnage: Personnage) -> list:
        """
        Permet l'accès à toutes les données du personnage.

        Returns:
            list: Les données du personnage.
        """
        return [personnage._Personnage__pseudo, personnage._Personnage__niveau, personnage._Personnage__pointsDeVie, personnage._Personnage__initiative]

    def num_suppr(self, num: int):
        """
        Permet la suppression du numéro du personnage.
        """
        if 0 <= num < len(self.__personnages):
            del self.__personnages[num]
        else:
            raise IndexError(" /!\ Numéro de personnage invalide /!\ ")

    def pseudo_suppr(self, pseudo: str):
        """
        Permet la suppression du pseudo du personnage.
        """
        for personnage in self.__personnages:
            if personnage._Personnage__pseudo == pseudo:
                self.__personnages.remove(personnage)
                return
        raise ValueError(" /!\ Pseudo de personnage introuvable /!\ ")

    def personnage_suppr(self, personnage):
        """
        Permet la suppression du personnage.
        """
        if personnage in self.__personnages:
            self.__personnages.remove(personnage)

if __name__ == "__main__":
    p1 = Personnage("toto")
    p2 = Personnage("titi", 3)
    print(f"{p1}\n{p2}")
    p1.combat(p2)
    print(f"{p1}\n{p2}")
    g1 = Guerrier("guerrier")
    m1 = Mage("mage")
    print(f"{g1}\n{m1}")
    g1.combat(m1)
    print(f"{g1}\n{m1}")
