def PlusGrandNombreReel(a : float, b : float) -> float :
    """ 
    fonction qui détermine le plus grand nombre réel parmi ceux rentrés en argument
    """
    if a > b:
        return 'Le plus grand nombre réel de la liste est',a
    else: 
        return 'Le plus grand nombre réel de la liste est',b

print(PlusGrandNombreReel(12.2, 11.7))

def ControleSeuil(Seuil : int, x : float):
    """
    fonction qui indique si la valeur passée en argument est supérieure au seuil
    """
    if x > Seuil:
        return(x,'est supérieur au seuil')
    else:
        return(x,'est compris dans le seuil')

print(ControleSeuil(10, 13.3))

def PlusGrandeValeur(Lst, maxi : int):
    """
    fonction qui permet de déterminer la valeur la plus grande d'une liste donnée en argument
    """
    for i in range(len(Lst)):
        if maxi < Lst[i]:
            maxi = Lst[i]
    return maxi

Lst = [1,2,3,4,5,6,7,8]
print(PlusGrandeValeur(Lst, 0))

def ValeursInférieurSeuil(Liste, Seuil2 = 3):
    """
    fonction qui permet de déterminer le nombre de valeurs d'une liste inférieures à un seuil donné en argument
    """
    compteur = 0
    for j in range(len(Liste)):
        if Liste[j] < Seuil2:
            compteur += 1
    return compteur

Liste = [1,2,3,4,5,6,7,8]
print(ValeursInférieurSeuil(Liste,3))

def DonneesDico(dico):
    """
    fonction qui affiche l'ensemble des données d'un dictionnaire passé en argument
    """
    for key in dico:
        print(f"{key}:{dico[key]}")
    
dico = {"bus":"bus","voiture":"voiture","camion":"camion"}
print(DonneesDico(dico))

