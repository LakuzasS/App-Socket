print("veuillez saisir une valeur :")
x=int(input())
print("Voulez vous que la boucle s'effectue en while ( tapez 1 )ou en for ( tapez 2) ")
c=int(input())
n=1
if c == 2 :
    for i in range ( 1 , x+1):
        n=n*i
        print(n)
elif c == 1:
    while x>0 :
        n=n*x
        x=x-1
        print(n)