def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst
lst1 =  [0, 1, 2]

lst2 = ajouter_elt(lst1, len(lst1))

print(f"La liste 1 : {lst1} a pour id {id(lst1)} et comme type {type(lst1)}")
print(f"La liste 2 : {lst2} a pour id {id(lst2)} et comme type {type(lst2)}\n")
