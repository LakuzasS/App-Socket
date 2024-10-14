#Présentation du tri fusion:
"""
Il s'agit d'un tri suivant le paradigme diviser pour régner. 
Le principe du tri fusion est le suivant :
On divise en deux moitiés la liste à trier (en prenant par 
exemple, un élément sur deux pour chacune des listes).
On trie chacune d'entre elles.
On fusionne les deux moitiés obtenues pour reconstituer 
la liste triée.
"""
# Présenter l’algorithme du tri fusion (récursif)
"""
Données : lst, la liste à trier
Fonction tri_fusion(lst) :
  Début
  n ←  longueur de la séquence
  Si n > 1 :
    milieu ←  n // 2
    gauche ← lst[:milieu]
    droite ← lst[milieu:]
    tri_fusion(gauche)
    tri_fusion(droite)
    i = j = k = 0
    Tant que i < len(gauche) & j < len(droite) faire :
      Si gauche[i] < droite[j] :
        lst[k] ← gauche[i]
        i ← i + 1
      Sinon :
        lst[k] ← droite[j]
        j ← j + 1
      k ← k + 1
    FinTq
    Tant que i < len(gauche) faire:
      lst[k] ← gauche[i]
      i ← i + 1
      k ← k + 1
    FinTq
    Tant que j < len(droite) faire:
      lst[k] ←droite[j]
      j ← j + 1
      k ← k + 1
    FinTq
  Fsi
  Retourner lst
  Fin
"""


# Implémentation en python
def tri_fusion(lst):
  n = len(lst)
  if n > 1:
    milieu = n // 2
    gauche = lst[:milieu]
    droite = lst[milieu:]
    tri_fusion(gauche)
    tri_fusion(droite)
    i = j = k = 0
    while i < len(gauche) and j < len(droite):
      if gauche[i] < droite[j]:
        lst[k] = gauche[i]
        i = i + 1
      else:
        lst[k] = droite[j]
        j = j + 1
      k = k + 1
    while i < len(gauche):
      lst[k] = gauche[i]
      i = i + 1
      k = k + 1
    while j < len(droite):
      lst[k] = droite[j]
      j = j + 1
      k = k + 1
  return lst

tirage = [3, 7, 4, 1, 9, 6]
print("Tirage de départ :", tirage)
tirage_trie = tri_fusion(tirage)
print("Voici le tirage trié :", tirage_trie)
