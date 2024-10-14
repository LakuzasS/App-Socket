import json
import numpy as np

# Fixation de la graine aléatoire pour obtenir les mêmes résultats quelque soit l'ordinateur
np.random.seed(0)

# Méthode tirage_loto qui génère les séquences de numéros tirés
def tirage_loto(n_donnees):
    donnees = []
    for i in range(n_donnees):
        sequence = np.random.choice(range(1, 46), 5, replace=False)
        #Génération des séquences de numéros aléatoires sans remise (replace=False)
        donnees.append({'num':i+1, 'sequence':sequence.tolist()})
    return donnees

# Méthode de sauvegarde des séquences dans un fichier JSON
def sauvegarder_json(donnees, fichier):
    with open(fichier, 'w') as f:
        json.dump(donnees, f) #Ecrit les objets dans un fichier JSON 

# Méthode de chargement des séquences à partir du fichier JSON
def charger_json(fichier):
    with open(fichier, 'r') as f:
        donnees = json.load(f) #Charge les données
    return donnees

donnees = tirage_loto(10) #nombre de tirages
sauvegarder_json(donnees, 'donnees.json')
donnees_chargees = charger_json('donnees.json')
print(donnees_chargees)

import matplotlib.pyplot as plt

# Calcul de l'histogramme des numéros tirés
def histogramme(donnees):
    compteur = np.zeros(45) # Tableau de comptage de chaque nombre de 1 à 45
    for sequence in donnees:
        for num in sequence['sequence']:
            compteur[num-1] += 1 # Incrémente le compteur correspondant au nombre tiré
    return compteur

# Tracé de l'histogramme
def plot_histogramme(compteur):
    plt.bar(range(1, 46), compteur)
    plt.xlabel('Numéro')
    plt.ylabel('Compteur')
    plt.title('histogramme des numéros tirés')
    plt.show()

compteur = histogramme(donnees_chargees)
plot_histogramme(compteur)