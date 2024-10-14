L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 6, 7, 6]
occurence = 0
num = L1[0]
for i in L1:
    x = L1.count(i)
    if x > occurence:
        occurence = x
        num = i
print("Le nombre le plus frequent dans la liste est le",num,"et il apparaît",x,"fois.")

