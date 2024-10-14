tab = [5, 2, 4, 8, 1, 3]
print(tab)

for i in range(len(tab) - 1):
    min = tab[i]
    for j in range(i + 1, len(tab)):
        if tab[j] < min:
            min = tab[j]
            index = j
    if min < tab[i]:
        temp = tab[i]
        tab[i] = tab[index]
        tab[index] = temp
    print(tab)