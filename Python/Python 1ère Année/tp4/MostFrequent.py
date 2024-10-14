L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 6, 7]
L2 = L1
""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
occurences = 0
x = 0
for i in L1:
    nombre = i
    x = 0
    for i in L2:
        if nombre == L2[i]:
            x += 1
        if x > occurences:
            occurences = x
            nombre2 = i
print("Le nombre le plus frequent dans la liste est le",nombre2,"et on le retrouve",occurences,"fois.")





"""
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
