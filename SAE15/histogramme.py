# Écrire l’algorithme du calcul de l’histogramme des numéros sortis
"""
Fonction histogramme(donnees):
  Debut
    compteur <- tableau de zéro avec 45 cases
    Pour chaque séquence dans les données faire:
      Pour chaque numéro dans la séquence faire:
        compteur[numéro] <- compteur[numéro] + 1
      FinPour
    FinPour
  retourner compteur
  Fin
"""
#Implémenation en python
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



