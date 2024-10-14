#Présentation du tri coktail 
"""
Le tri cocktail (cocktail sort), ou tri shaker (shaker sort) 
ou tri à bulles bidirectionnel (bidirectional bubble sort) est 
une variante du tri à bulles qui est à la fois un algorithme 
de tri et un tri par comparaison.
"""
# Présenter l’algorithme du tri cocktail (itératif)
"""
Données : lst, la liste à trier
Fonction tri_cocktail(lst) :
  n ← longueur de la séquence
  Début
    échangé = vrai
    droite ← n - 1
    gauche ← 0
    Tant que échangé = vrai faire:
      échangé = faux
      Pour i allant de gauche à droite faire:
        Si lst[i] > lst[i + 1] :
          échanger lst[i] & lst[i + 1]
          échangé = vrai
      droite ← droite - 1
      Si échangé = faux :
        sortir de la boucle
      Sinon :
        échangé = faux
        Pour i allant de droite à gauche faire:
          Si lst[i] < lst[i - 1] :
            échanger lst[i] et lst[i - 1]
            échangé = vrai
        gauche ← gauche + 1
    Retourner lst
  Fin
"""


# Implémentation en python
def tri_cocktail(lst):
  n = len(lst)
  echange = True
  droite = n - 1
  gauche = 0
  while echange:
    echange = False
    for i in range(gauche, droite):
      if lst[i] > lst[i + 1]:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
        echange = True
    droite = droite - 1
    if not echange:
      break
    else:
      echange = False
      for i in range(droite, gauche, -1):
        if lst[i] < lst[i - 1]:
          lst[i], lst[i - 1] = lst[i - 1], lst[i]
          echange = True
      gauche = gauche + 1
  return lst

tirage = [3, 7, 4, 1, 9, 6]
print("Tirage de départ :", tirage)
tirage_trie = tri_cocktail(tirage)
print("Voici le tirage trié :", tirage_trie)
