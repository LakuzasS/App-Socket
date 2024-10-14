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
# Présenter l’algorithme de recherche dichotomique (récursif)
"""
Données : lst, la liste à trier
	      x, élément que l’on cherche dans la liste
	      gauche, début de la liste
	      droite, fin de la liste
Fonction recherche_dichotomique_recursive(lst, x, gauche, droite)
  Debut
   Si gauche > droite:
     Retourner -1
     milieu ←  (gauche + droite) divisé par 2
   Si x < lst[milieu]:
     Retourner recherche_dichotomique_recursive(lst, x, gauche, milieu - 1)
   Sinon Si x > lst[milieu]:
     Retourner recherche_dichotomique_recursive(lst, x, milieu + 1, droite)
   Sinon:
     Retourner milieu
  Fin
Fonction recherche_dichotomique(lst, x)
  Début
   Retourner recherche_dichotomique_recursive(lst, x, 0, longueur de lst - 1)
  Fin

"""


# Implémentation en python
def recherche_dichotomique_recursive(lst, x, gauche, droite):
  if gauche > droite:
    return -1
  milieu = (gauche + droite) // 2
  if x < lst[milieu]:
    return recherche_dichotomique_recursive(lst, x, gauche, milieu - 1)
  elif x > lst[milieu]:
    return recherche_dichotomique_recursive(lst, x, milieu + 1, droite)
  else:
    return milieu

def recherche_dichotomique(lst, x):
  return recherche_dichotomique_recursive(lst, x, 0, len(lst) - 1)

lst = [1, 3, 5, 7, 9]
x = 5
indice = recherche_dichotomique(lst, x)
if indice != -1:
  print(f"L'élément {x} se trouve à l'indice {indice} de la séquence {lst}")
else:
  print(f"L'élément {x} n'est pas dans la séquence {lst}")
