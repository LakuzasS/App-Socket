from random import *
while True :
    print("Pile ou face ?")
    a = input()
    x = int(randint(0,101))
    if x < 50:
        print("pile")
        break
    else:
        print("face")
        break
