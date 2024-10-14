#Implémenter une méthode relative au chargement de données binaires
import pickle

def charger_donnees(fichier):
  with open(fichier, "rb") as f:
    donnees = pickle.load(f)
  return donnees

donnees = charger_donnees("donnees.bin")
print(donnees)  # Affiche [1, 2, 3, 4, 5]

"""
Cette fonction prend en entrée le nom du fichier contenant 
les données binaires à charger 'fichier', lit et charge ces 
données, et retourne la liste de données chargées
"""