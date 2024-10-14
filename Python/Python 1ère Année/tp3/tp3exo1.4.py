print("Veuillez saisir un nombre :")
x=int(input())
n=0
if x<1:
    print("Veuillez saisir un nombre :")
    x=int(input())
for c in range(x):
    n=n+c
    if n<=x :
        total=c
    else:
        print( x ," est composé de la somme des " , total ," premier entier naturel ")
        break