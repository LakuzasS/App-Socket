print("Donnez un nom suivi d'un prénonom 2 fois de suite :")
nom1 = str(input())
nom2 = str(input())
prenom1 = str(input())
prenom2 = str(input())
if nom1<nom2:
    print(str.upper(nom1), str.capitalize(prenom1))
    print(str.upper(nom2), str.capitalize(prenom2))
elif nom1==nom2:
    if prenom1<prenom2:
        print(str.upper(nom1), str.capitalize(prenom1))
        print(str.upper(nom2), str.capitalize(prenom2))
    else:
        print(str.upper(nom2), str.capitalize(prenom2))
        print(str.upper(nom1), str.capitalize(prenom1))
else:
    print(str.upper(nom2), str.capitalize(prenom2))
    print(str.upper(nom1), str.capitalize(prenom1))
