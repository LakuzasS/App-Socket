grade = []
weight = []
death = 0
total = 0
totco = 0

while True:
    S = str(input("Entrez votre note et coefficient séparés d'un espace (0 pour sortir) : ")).split(" ")

    if (len(S) == 1) & (S[0] == "0"):
        break
    elif len(S) != 2:
        print("La valeur saisie est invalide, veuillez réessayer !")     
    
    elif float(S[0]) < 8:
        print("L'étudiant à une note inférieure à 8, il n'est donc pas admis.")
        death = 1
        break
    else:
        grade.append(float(S[0]))
        weight.append(int(S[1]))

if death == 0:
    for i in range(len(grade)):
        total = total + (grade[i] * weight[i])
        totco = totco + weight[i]

    moy = total / totco
    
    if moy < 10:
        print(f"La moyenne générale de l'étudiant {moy} étant inférieure à 10, l'étudiant n'est pas admis.")
    else:
        print(f"La moyenne générale de l'étudiant {moy} étant supérieure à 10, l'étudiant est admis.")
