jour = 14
heure = 9
minute = 34

i = 0
j = 0
k = 0
compteur = 0
while i != jour:
    i += 1
compteur = 3600 * i
while j != heure:
    j += 1
compteur += (60 * i) + minute
print("Depuis le début du mois,", compteur, "minutes se sont écoulées")