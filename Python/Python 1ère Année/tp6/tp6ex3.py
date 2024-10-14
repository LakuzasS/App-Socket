def ajouter_elt(lst = [0, 1, 2], elt = 3):
    lst.append(elt)
    return lst

print(f"Le résultat de 'print(ajouter_elt())' serait : [0, 1, 2, 3], nous pouvons le vérifier : {ajouter_elt()}")

print(f"Si nous rappelons la fonction, nous trouverons le même résultat suivi de 3 à nouveau :, {ajouter_elt()}")


def ajouter_carac(ch = "abc", elt = "d"):
    return ch + elt

print(f"\nLe résultat de 'print(ajouter_carac())' serait : 'abcd', nous pouvons le vérifier : {ajouter_carac()}")

print(f"Si nous rappelons la fonction, nous trouverons le même résultat :", {ajouter_carac()})