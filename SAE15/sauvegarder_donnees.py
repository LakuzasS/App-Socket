#Implémenter une méthode relative à la sauvegarde de données binaires
import pickle

def sauvegarder_donnees(donnees, fichier):
  with open(fichier, "wb") as f:
    pickle.dump(donnees, f)

donnees = [1, 2, 3, 4, 5]
sauvegarder_donnees(donnees, "donnees.bin")

"""
Cette fonction prend en entrée une liste de données à sauvegarder
'donnees' et le nom du fichier où enregistrer ces données 'fichier',
et enregistre les données bianires dans le fichier.
"""
