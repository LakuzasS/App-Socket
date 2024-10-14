T = []
voyelles = ['a','e','i','o','u','y']
chaine = str(input("Ecrire du texte, 100 caractères max :"))
longueur = 0
compteur = 0
pourcentage = 0
occurrence = 0
chaine2 = "wagon"
if len(chaine) > 100:
    str(input("Vous avez plus de 100 caractères, réésayez :"))
for i in range(len(chaine)+1):
    longueur = i
print("La chaine contient",longueur,"caractères.")
for j in range(0, len(chaine)-1):
    for k in range(len(voyelles)):
        if chaine[j] == voyelles[k]:
            compteur += 1
pourcentage = (compteur / longueur) * 100
print("Dans la liste, il y a ",round(pourcentage,1),"% de voyelles.")
for a in range(len(chaine)):
    if chaine2 == chaine[a]+chaine[a+1]+chaine[a+2]+chaine[a+3]+chaine[a+4]:
        print("wagon est bien une sous-chaine de T et apparait la première fois à l'indice", a+1)
        break
    occurrence = chaine.count("wagon")
print("La chaine de caractères wagon apparaît",occurrence,"fois dans la liste.")

