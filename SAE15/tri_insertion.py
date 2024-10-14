#Présentation du tri par insertion
"""
Le tri par insertion considère chaque élément du tableau 
et l'insère à la bonne place parmi les éléments déjà triés. 
Ainsi, au moment où on considère un élément, les éléments qui 
le précèdent sont déjà triés, tandis que les éléments qui le 
suivent ne sont pas encore triés.

Pour trouver la place où insérer un élément parmi les 
précédents, il faut le comparer à ces derniers, et les décaler 
afin de libérer une place où effectuer l'insertion. Le décalage 
occupe la place laissée libre par l'élément considéré. En 
pratique, ces deux actions s'effectuent en une passe, qui 
consiste à faire « remonter » l'élément au fur et à mesure 
jusqu'à rencontrer un élément plus petit.
"""
# Présenter l’algorithme du tri par insertion (itératif)
"""
Données : lst, la liste à trier
Fonction tri_insertion(lst) :
  n ← longueur de la séquence
  Début
    Pour i allant de 1 à n - 1 faire:
      x ← lst[i]
      j ← i
      Tant que j > 0 & lst[j - 1] > x faire:
        lst[j] ← lst[j - 1]
        j ← j - 1
      FinTq
      lst[j] ← x
    FinPour
 Retourner lst
  Fin
"""


# Implémentation en python
def tri_insertion(lst):
  n = len(lst)
  for i in range(1, n):
    x = lst[i]
    j = i
    while j > 0 and lst[j - 1] > x:
      lst[j] = lst[j - 1]
      j = j - 1
    lst[j] = x
  return lst

tirage = [3, 7, 4, 1, 9, 6]
print("Tirage de départ :", tirage)
tirage_trie = tri_insertion(tirage)
print("Voici le tirage trié :", tirage_trie)
