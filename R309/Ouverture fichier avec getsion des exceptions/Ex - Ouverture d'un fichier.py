nom_fichier = 'fichier.txt'

try:
    fichier = open(nom_fichier, 'r')
    
    try:
        lignes = fichier.readlines()
        for ligne in lignes:
            ligne_propre = ligne.rstrip()
            print(ligne_propre)
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'a pas été trouvé.")
    
    except IOError as e:
        print(f"Erreur d'entrée/sortie : {e}")
    
    except FileExistsError:
        print(f"Erreur : Le fichier '{nom_fichier}' existe déjà.")
    
    except PermissionError:
        print(f"Erreur de permission : Vous n'avez pas la permission d'accéder au fichier '{nom_fichier}'.")
    
    finally:
        fichier.close()
        print("Le fichier a été fermé.")
        
except FileNotFoundError:
    print(f"Erreur : Le fichier '{nom_fichier}' n'a pas été trouvé lors de la tentative d'ouverture.")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")

#############################################################################################

nom_fichier = "inexistant.txt"

try:
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            ligne_propre = ligne.rstrip()
            print(ligne_propre)
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
except FileNotFoundError:
    print(f"Erreur : Le fichier '{nom_fichier}' n'a pas été trouvé.")
except IOError as e:
    print(f"Erreur d'entrée/sortie : {e}")
except FileExistsError:
    print(f"Erreur : Le fichier '{nom_fichier}' existe déjà.")
except PermissionError:
    print(f"Erreur de permission : Vous n'avez pas la permission d'accéder au fichier '{nom_fichier}'.")
finally:
    print("Fin du programme.")

###############################################################################################

nom_fichier = 'fichier.txt' 

try:
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            ligne_propre = ligne.rstrip()
            print(ligne_propre)
# Le fichier est automatiquement fermé à la fin du bloc 'with' grâce à la gestion de contexte.
except Exception as e:
    print(f"Une erreur s'est produite : {e}")
except FileNotFoundError:
    print(f"Erreur : Le fichier '{nom_fichier}' n'a pas été trouvé.")
except IOError as e:
    print(f"Erreur d'entrée/sortie : {e}")
except FileExistsError:
    print(f"Erreur : Le fichier '{nom_fichier}' existe déjà.")
except PermissionError:
    print(f"Erreur de permission : Vous n'avez pas la permission d'accéder au fichier '{nom_fichier}'.")
finally:
    print("Fin du programme.")
