nMax = 10
v1 = []
v2 = []
produit_scalaire = 0
n = int(input("veuillez saisir la taille effective des valeurs :"))
if n < 1 or n > nMax:
    n = int(input("Faux, veuillez rentrer une valeur comprise entre 1 et nMax :"))
print("Saisie du premier vecteur :")
for i in range(n):
    v1.append(int(input("Veuillez saisir les composantes de v1 :")))
print("Saisie du second vecteur :")
for i in range(n):
    v2.append(int(input("Veuillez saisir les composantes de v2 :")))
produit_scalaire = v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
print("Le produit scalaire de v1 par v2 vaut", produit_scalaire)