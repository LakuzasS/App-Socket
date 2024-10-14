Temp1 = 0
Temp2 = 0
Temp3 = 0
for i in range(0, 10):
    print("Veuillez saisir une valeur comprise entre 0 et 20 :")
    x = float(input())
    while x < 0 or x > 20:
        print("Veuillez saisir une valeur comprise entre 0 et 20 :")
        x = float(input())
    else:
        if x < 10:
            Temp1 = Temp1 + 1
        elif x >= 10 and x <=15:
            Temp2 = Temp2 + 1
        else :
            Temp3 = Temp3 + 1
print(" Il y a un total de", Temp1, " valeurs en dessous de 10 \n Il y a un total de ", Temp2,
      " valeurs entre 10 (inclus) et 15 ( inclus) \n Il y a un total de ", Temp3, "valeurs au dessus de 15")
