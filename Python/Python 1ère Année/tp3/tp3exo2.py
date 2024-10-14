import time
print("Veuillez saisir une valeur :")
x=int(input())
if x < 0 :
    print("Veuillez saisir une valeur superieur à 0 :")
    x=int(input())
else:
    while x!=0:
        x=x-1
        print(x)
        time.sleep(0.5)
