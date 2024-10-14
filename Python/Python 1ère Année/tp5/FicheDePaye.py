heure = int(input("Saisir le nombre d'heures de travail :"))
salaire = int(input("Définir le salaire horaire :"))
salaire_depart = salaire
a = 0
b = 0
if heure <= 160:
    salaire *= heure
    print("l'ouvrier aura gagné",salaire,"€ en",heure,"heures")

if heure >= 161 and heure <= 200:
    a = heure - 160
    salaire *= ((heure-a) + (a * 1.25))
    print("l'ouvrier aura gagné",salaire,"€ en",heure,"heures")


if heure > 200:
    a = 200 - 160
    salaire *= ((200-a) + (a * 1.25))
    b = heure - 200
    salaire += salaire_depart * b * 1.5
    print("l'ouvrier aura gagné", salaire, "€ en", heure, "heures")






