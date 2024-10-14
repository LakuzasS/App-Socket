from random import *
i = randint(0,100)
x=0
print("Veuillez deviner la valeur choisie :")
n=int(input())
while x!=i :
    if i<n :
        x=x+1
        print("veuillez saisir une valeur plus petite")
        n=int(input())
    elif i>n:
        x=x+1
        print("veuillez saisir une valeur plus grande")
        n = int(input())
    else :
        x=x+1
        break
print(" Vous avez mis" , x , " essaie pour trouver ", i)
