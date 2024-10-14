print("Pour 4 personnes la fondu Fribourgeoise nécessite : ")
fromage = 800
print("Il nous faut", fromage, "grammes de fromages")
eau = 2
print("Il nous faut", eau, "dl d'eau .")
ail = 2
print("Il nous faut", ail, "gouse d'ail")
pain = 400
print( "Il nous faut", pain , "grammes de pain")
print (" veuillez saisir le nombre de convive : ")
Base = int(input())
print("Pour faire une fondue ribourgeoise pour " , Base ," personnes , il vous faut :")
fromage = 800*Base/4
print( fromage, "grammes de fromages")
eau = 2*Base/4
print( eau, "dl d'eau .")
ail = 2*Base/4
print(ail, "gouse d'ail")
pain = 400*Base/4
print(pain , "grammes de pain")