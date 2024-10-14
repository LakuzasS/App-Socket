from random import *
while True :
    print("Pile ou face ?")
    x = int(randint(1,3))
    if x < 3:
        print("pile")
        break
    else:
        print("face")
        break

