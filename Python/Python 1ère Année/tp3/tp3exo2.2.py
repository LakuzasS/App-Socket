import time
print("Veuillez saisir une valeur :")
x=int(input())
if x < 0 :
    print("Veuillez saisir une valeur superieur à 0 :")
    x=int(input())
else:
    for i in range ( x , -1 , -1):
        print(i)
        time.sleep(0.5)