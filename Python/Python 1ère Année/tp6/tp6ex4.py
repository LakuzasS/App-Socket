import random
## Fonction generer(nbr, vmin, vmax) pour générer un tableau de 'nbr' valeurs comprises entre 'vmin' et 'vmax'
def generer(nbr, vmin, vmax):
    table = []
    for i in range(nbr):
        table.append(random.uniform(vmin, vmax))
    return table


## Fonction combienInferieur(table, vseuil) pour compter le nombre de valeurs d'un tableau 'table' inférieures à la valeur 'vseuil'
def combienInferieur(table, vseuil=30):
    j = 0
    for i in table:
        if i < vseuil:
            j += 1
    return j


nb = int(input("Combien de valeur voulez-vous générer ? : "))
print(f"Générer {nb} nombres entiers entre 0 et 100")

vmin = int(input("Valeur minimum de l'interval : "))
vmax = int(input("Valeur maximum de l'interval : "))

tab = generer(nb, vmin, vmax)
tab.sort()
print(tab)

test = True
while test:
    seuil = input("Voulez-vous préciser le seuil ? (Oui/O ou Non/N) : ")
    if seuil == "O" or seuil == "Oui":
        vs = (input("Quel valeur voulez-vous en tant que seuil ? : "))
        test = False
        total = combienInferieur(tab, vs)
        print(f"Il y en a {total} inférieurs à {vs}")

    elif seuil == "N" or seuil == "Non":
        test = False
        total = combienInferieur(tab)
        print(f"Il y en a {total} inférieurs à 30")