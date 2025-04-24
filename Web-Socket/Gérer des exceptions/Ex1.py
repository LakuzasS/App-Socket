def divEntier(x: int, y: int) -> int:
        if x < 0:
            raise ValueError("x ne peut pas être négatif !")
        if y < 0:
            raise ValueError("y ne peut pas être négatif !")
        elif y == 0:
            raise ZeroDivisionError("x ne peut pas être égal à 0 !")
        elif x < y:
            return 0
        else:
            x = x - y 
            return divEntier(x, y) + 1

# Questions : 
#   1. Que fait ce code ?
#   Ce code instantie deux entiers, x et y. Si la valeur de x est inférieure à celle de y, alors
#   le code renvoie la valeur 0. Sinon la nouvelle valeur de x sera égale à elle même à laquelle
#   on soustrait la valeur de y. Une fois cette la valeur de x changée, on effectue une division
#   x / y à laquelle on ajoute 1. 

#   2. Essayer avec deux valeurs simples (entiers et positifs) ?
# print(divEntier(3, 5)) # Return 0 car 3 < 5
# print(divEntier(9, 4)) # Return ((9 - 4)/4) + 1 = 2 

# Exercices : 
#   1. Ajouter un main permettant de saisir les valeurs de x et de y.
if __name__ == '__main__':
    try :
        x = int(input("x : "))
        y = int(input("y : "))
        assert x > 0
        assert y >= 0
#   2. Ajouter l'exeption ValueError
    except ValueError as err:
        print("Merci d'entrer une valeur de type int.")
    except AssertionError as err:
        print("Merci d'entrer une valeur positive pour les deux entrées.")
#       a. Pourquoi devez vous gérer ValueError ?
#       Cela nous permet de respecter la consigne qui dit que l'on doit saisir des valeurs 
#       simples de type int et positives. Si cette condition n'est pas respectée, cela renvoie
#       un message d'erreur. 
#   3. Essayer de saisir la valeur 0 pour y
#       a. Que se passe-t'il ?
#       On a affaire à une RecursionError car on fait tourner le programme à l'infini. En effet,
#       ici on divise par 0 ce qui est impossible.
#       b. Gérer l'exception en mettant un message correspondant à l'erreur
    except ZeroDivisionError as err:
        print("Impossible de diviser par 0, veuillez changer la valeur de y.")
    else:
        print(divEntier(x, y))
#   4. Ajouter dans la fonction divEntier une exception :
#       a. si l’un des nombres passés par argument est négatif
#       b. si y est égale à 0