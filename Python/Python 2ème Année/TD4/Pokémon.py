# +-------------------+       +---------------------+
# |     Pokemon       |       |       PokemonMer    |
# +-------------------+       +---------------------+
# | -nom: str         |       | -nom: str           |
# | -poids: float     |       | -poids: float       |
# | -nb_pattes: int   |       | -nb_nageoires: int  |
# | -taille: float    |       | +vitesse(): float   |
# | +__init__(...):   |       | +__init__(...):     |
# | +__str__(): str   |       | +__str__(): str     |
# +-------------------+       +---------------------+
#        |                          ^
#        |                          |
#        |                          |
#        v                          |
# +-------------------+       +---------------------+
# | PokemonSportif    |       | PokemonCroisiere    |
# +-------------------+       +---------------------+
# | -freq_cardiaque:  |       | +vitesse(): float   |
# |   int             |       +---------------------+
# | +vitesse(): float |
# | +__init__(...):   |
# | +__str__(): str   |
# +-------------------+
#        ^
#        |
#        |
#        v
# +-------------------+
# | PokemonCasanier   |
# +-------------------+
# | -heures_tv: int   |
# | +vitesse(): float |
# | +__init__(...):   |
# | +__str__(): str   |
# +-------------------+

import json
import pickle

class Pokemon:
    def __init__(self, nom : str, poids : float, nb_pattes : int, taille : float):
        """
        Initialise un objet Pokemon.

        Args:
            nom (str): Le nom du Pokémon.
            poids (float): Le poids du Pokémon en kilogrammes.
            nb_pattes (int): Le nombre de pattes du Pokémon.
            taille (float): La taille du Pokémon en mètres.
        """
        self.nom = nom
        self.poids = poids
        self.nb_pattes = nb_pattes
        self.taille = taille

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du Pokémon.

        Returns:
            str: Une chaîne de caractères représentant le Pokémon.
        """
        return f"Je suis le Pokémon {self.nom}, mon poids est de {self.poids} kg, j'ai {self.nb_pattes} pattes, ma taille est de {self.taille} mètres."

class PokemonSportif(Pokemon):
    def __init__(self, nom : str, poids : float, nb_pattes : int, taille : float, freq_cardiaque : int):
        """
        Initialise un objet PokemonSportif.

        Args:
            nom (str): Le nom du Pokémon.
            poids (float): Le poids du Pokémon en kilogrammes.
            nb_pattes (int): Le nombre de pattes du Pokémon.
            taille (float): La taille du Pokémon en mètres.
            freq_cardiaque (int): La fréquence cardiaque du Pokémon en pulsations par minute.
        """
        super().__init__(nom, poids, nb_pattes, taille)
        self.freq_cardiaque = freq_cardiaque

    def vitesse(self):
        """
        Calcule la vitesse du Pokémon sportif.

        Returns:
            float: La vitesse du Pokémon en km/h.
        """
        return (self.poids * 3) / (self.taille * 0.1)

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du Pokémon sportif.

        Returns:
            str: Une chaîne de caractères représentant le Pokémon sportif.
        """
        return super().__str__() + f" Ma fréquence cardiaque est de {self.freq_cardiaque} pulsations à la minute."

class PokemonCasanier(Pokemon):
    def __init__(self, nom : str, poids : float, nb_pattes : int, taille : float, heures_tv : int):
        """
        Initialise un objet PokemonCasanier.

        Args:
            nom (str): Le nom du Pokémon.
            poids (float): Le poids du Pokémon en kilogrammes.
            nb_pattes (int): Le nombre de pattes du Pokémon.
            taille (float): La taille du Pokémon en mètres.
            heures_tv (int): Le nombre d'heures par jour où le Pokémon regarde la télévision.
        """
        super().__init__(nom, poids, nb_pattes, taille)
        self.heures_tv = heures_tv

    def vitesse(self):
        """
        Calcule la vitesse du Pokémon casanier.

        Returns:
            float: La vitesse du Pokémon en km/h.
        """
        return (self.poids * 3) / (self.taille * 0.1)

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du Pokémon casanier.

        Returns:
            str: Une chaîne de caractères représentant le Pokémon casanier.
        """
        return super().__str__() + f" Je regarde la télé {self.heures_tv} heures par jour."

class PokemonMer:
    def __init__(self, nom : str, poids : float, nb_nageoires : int):
        """
        Initialise un objet PokemonMer.

        Args:
            nom (str): Le nom du Pokémon.
            poids (float): Le poids du Pokémon en kilogrammes.
            nb_nageoires (int): Le nombre de nageoires du Pokémon.
        """
        self.nom = nom
        self.poids = poids
        self.nb_nageoires = nb_nageoires

    def vitesse(self):
        """
        Calcule la vitesse du Pokémon de mer.

        Returns:
            float: La vitesse du Pokémon en km/h.
        """
        return (self.nb_nageoires / 25) * ((self.poids * 3) / 10)

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du Pokémon de mer.

        Returns:
            str: Une chaîne de caractères représentant le Pokémon de mer.
        """
        return f"Je suis le Pokémon {self.nom}, mon poids est de {self.poids} kg, j'ai {self.nb_nageoires} nageoires."

class PokemonCroisiere(PokemonMer):
    def vitesse(self):
        """
        Calcule la vitesse du Pokémon de croisière.

        Returns:
            float: La vitesse du Pokémon en km/h.
        """
        return (self.nb_nageoires / 25) * ((self.poids * 3) / 10) / 2

    def __str__(self):
        """
        Renvoie une représentation en chaîne de caractères du Pokémon de croisière.

        Returns:
            str: Une chaîne de caractères représentant le Pokémon de croisière.
        """
        return super().__str__() + f" Ma vitesse de croisière est de {self.vitesse()} km/h."

if __name__ == "__main__":
    p1 = PokemonSportif("Pikachu", 18, 2, 0.85, 120)
    p2 = PokemonCasanier("Salamèche", 12, 2, 0.65, 8)
    p3 = PokemonMer("Rondoudou", 45, 2)
    p4 = PokemonCroisiere("Bulbizarre", 15, 3)

    pokemons = [p1, p2, p3, p4]
    for pokemon in pokemons:
        print(pokemon)

    with open("pokémon.txt","w") as f:
        print(json.dump(p1.__dict__,f))
    
    with open("pokémon.txt","w") as f2:
        print(json.dump(p2.__dict__,f2))
    

    with open ("pokémon.txt","r") as f3:
        res = json.load(f3)
        print(f"dicionnaire issu de json {res}")
        p3 = Pokemon(res["nom"],res["poids"],res["nb_pattes"],res["taille"])

    with open("data.bin","wb") as fb:
        pickle.dump(p1,fb)

    with open("data.bin","rb") as fb2:
        p3 = pickle.load(fb2)
        

