nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []
somme = 0.0
for i in range(nombreEtudiants):
    print("Note de l'etudiant :".format(i))
    a = float(input())
    if 0 <= a <= 20:
        notes.append(a)
    else:
        print("veuillez saisir une note comprise entre 0 et 20 : ")
        a = float(input())
for i in range(nombreEtudiants):
    somme += notes[i]
    moyenne = somme/nombreEtudiants
for i in range(nombreEtudiants):
    b = notes[i] - moyenne
    print("L'etudiant",i,"a obtenu la note de",notes[i],", la moyenne de la classe est de",moyenne,"et l'ecart de sa note avec la moyenne et de",b,".")
