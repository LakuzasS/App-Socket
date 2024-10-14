print("veuillez saisir un nombre :")
a = int(input())
if a%2==0:
    if a > 0:
        print( a , " est positif et paire")
    elif a==0:
        print(a , " est égal à 0 et positif")
    elif a < 0:
        print(a, " est négatif et paire")
elif a%2!=0:
    if a > 0:
        print( a , " est positif et impaire")
    elif a < 0:
        print(a, " est négatif et impaire")