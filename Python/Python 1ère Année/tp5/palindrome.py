chain = str.lower(input("Entrez une chaine de caractères : "))
alphachain = ""
death = 0

for i in chain:
    if i.isalpha() == True:
        alphachain = alphachain + i

lenalpha = len(alphachain)
lenalphamin = lenalpha - 1
for j in range(int(lenalpha / 2)):
    if alphachain[j] != alphachain[lenalphamin - j]:
        print("Ce n'est pas un palindrome !")
        death = 1
        break

if death == 0:
    print("C'est un palindrome !")
