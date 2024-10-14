L1 = [0] * 3
print(f"La liste {L1} a pour id {id(L1)} et comme type {type(L1)}\n")

for i in range(len(L1)):
    print(f"L'élément {i + 1} a comme type {type(L1[i])} et comme id {id(L1[i])}")
print("\nOn remarque que les ids sont identiques si les variables sont égales (type et valeur)\n")

L1[1] += 1
print(f"La liste {L1} a pour id {id(L1)} et comme type {type(L1)}")
print("On remarque que ni le type ni l'id de la list n'a changé\n")

for i in range(len(L1)):
    print(f"L'élément {i + 1} a comme type {type(L1[i])} et comme id {id(L1[i])}")
