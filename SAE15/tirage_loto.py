#1– Écrire le programme du tirage du loto (5 nombres entre 1 et 45).
#2– Utiliser un générateur aléatoire uniforme (voir la bibliothèque numpy).
#3– Possibilité d’effectuer plusieurs tirages succéssifs en utilisant la même graine aléatoire.
import numpy as np

# Fixation de la graine aléatoire
np.random.seed(0)

# Génération des séquences de numéros tirés
def tirage_loto(n_donnees):
    donnees = []
    for i in range(n_donnees):
        sequence = np.random.choice(range(1, 46), 5, replace=False)
        donnees.append(sequence)
    return donnees


donnees = tirage_loto(10)
print(donnees)

donnees2 = tirage_loto(5)
print(donnees2)
