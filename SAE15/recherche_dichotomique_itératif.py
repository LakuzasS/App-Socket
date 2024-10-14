#Présentation de la recherche dichotomique
"""
Il s'agit d'un algorithme de recherche pour trouver la 
position d'un élément dans un tableau trié. 
Le principe est le suivant : 
Comparer l'élément avec la valeur de la case au milieu 
du tableau ; si les valeurs sont égales, la tâche est 
accomplie, sinon on recommence dans la moitié du tableau 
pertinente.
"""
# Présenter l’algorithme de recherche dichotomique (itératif)
"""
Données : lst, la liste à trier
	        x, élément que l’on cherche dans la liste
Fonction recherche_dichotomique_iteratif(lst, x) :
  Début
    gauche ← 0
    droite ← longueur de la liste - 1
    Tant que gauche <= droite faire:
      milieu ← (gauche + droite) // 2
      Si lst[milieu] == x :
        Retourner milieu
      Sinon Si lst[milieu] < x :
        gauche ← milieu + 1
      Sinon :
        droite ← milieu - 1
    FinTq
    Retourner -1
  Fin

"""


# Implémentation en python
def recherche_dichotomique(lst, x):
  gauche = 0
  droite = len(lst) - 1
  while gauche <= droite:
    milieu = (gauche + droite) // 2
    if x < lst[milieu]:
      droite = milieu - 1
    elif x > lst[milieu]:
      gauche = milieu + 1
    else:
      return milieu
  return -1

lst = [1, 3, 5, 7, 9]
x = 5
indice = recherche_dichotomique(lst, x)
if indice != -1:
  print(f"L'élément {x} se trouve à l'indice {indice} de la séq {lst}")
else:
  print(f"L'élément {x} n'est pas dans la séq {lst}")

