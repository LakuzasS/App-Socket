print("à quelle heure avez vous pris le vélo :")
a=int(input())
print("à quelle heure avez vous rendu votre vélo :")
b=int(input())
while True :
    while b < 0 or a >24 or a < 0 or b >24 or b < a or b == a:
        print("l'heure à laquelle vous avez pris votre velo doit correspondre aux prérequis  :")
        a = int(input())
        print("l'heure à laquelle vous avez rendu votre vélo doit doit correspondre aux prérequis :")
        b = int(input())
    break
if 0<=a<b<=7 :
    heure= b-a
    print("Vous avez loué votre vélo pendant \n " , heure , " heure à un tarif à 1€/h . \n Le montant total est de", heure , "€")
elif 17<a<b<=24 :
    heure = b - a
    print("Vous avez loué votre vélo pendant \n ", heure , " heure à un tarif à 1€/h . \n Le montant total est de", heure , "€")
elif 7<a<b<=17 :
    heure = (b-a)
    tarif = (b-a)*2
    print("Vous avez loué votre vélo pendant \n ", heure , " heure à un tarif à 2€/h . \n Le montant total est de", tarif , "€")
elif 0<=a<=7 and 7<b<=17 :
    heure : (7 - a ) - ( b - 7 ) * 2
    c = (7 - a )
    d = ( b - 7 ) * 2
    e= (b-7)
    tarif = c + d
    print("Vous avez loué votre vélo pendant \n ", e, " heure à un tarif à 2€/h . \n " , c , " heure à un tarif à 1€/h .\n Le montant total est de",
    tarif, "€")
elif 7<a<=17 and 24>=b>17 :
    heure: (17 - a) * 2  - (b - 17)
    c = (17 - a)
    d = ( 17 - a ) *2
    e = (b - 17)
    tarif = e + d
    print("Vous avez loué votre vélo pendant \n ", c, " heure à un tarif à 2€/h . \n ",e,
          " heure à un tarif à 1€/h .\n Le montant total est de",
          tarif, "€")
elif 0<=a<=7 and 17<b<=24 :
    heure: (b-a)
    c = 10
    e = 10*2
    d = (b-a) - 10
    tarif = e+d
    print("Vous avez loué votre vélo pendant \n ", c, " heure à un tarif à 2€/h . \n ", d,
          " heure à un tarif à 1€/h .\n Le montant total est de",
          tarif, "€")