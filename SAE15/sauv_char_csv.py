import csv
import numpy as np

# Fixation de la graine aléatoire pour obtenir les mêmes résultats quelque soit l'ordinateur
np.random.seed(0)

# Méthode tirage_loto qui génère les séquences de numéros tirés
def tirage_loto(n_donnees):#Argument = longueur de la séquence
    donnees = []
    for i in range(n_donnees):
        sequence = np.random.choice(range(1, 46), 5, replace=False)
        #Génération des séquences de numéros aléatoires sans remise (replace=False) 
        donnees.append({'sequence':sequence.tolist(), 'Num':i+1})
    return donnees

# Méthode de sauvegarde des séquences dans un fichier CSV
def sauvegarder_csv(donnees, fichier):
    with open(fichier, 'w', newline='') as f:
        writer = csv.writer(f) #Permet d'écrire les séquences
        writer.writerow(['Num', 'sequence'])
        for seq in donnees:
            writer.writerow([seq['Num'], ','.join(map(str, seq['sequence']))])

# Méthode de chargement des séquences à partir du fichier CSV
def charger_csv(fichier):
    donnees = []
    with open(fichier, 'r') as f:
        reader = csv.reader(f) #Lit les séquences
        next(reader) # On saute la première ligne qui contient les en-têtes
        for row in reader:
            donnees.append({'Num': int(row[0]), 'sequence': [int(x) for x in row[1].split(',')]})
    return donnees

donnees = tirage_loto(50) #Nombre de tirages
sauvegarder_csv(donnees, 'donnees.csv')
donnees_chargees = charger_csv('donnees.csv')
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