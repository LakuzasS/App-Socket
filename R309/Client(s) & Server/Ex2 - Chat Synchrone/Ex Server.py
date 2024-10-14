# 2 Un chat synchrone
#   Ajout de messages de « protocole » :
#       • bye – qui provoque l’arrêt du client mais pas du serveur
#       • arret – qui arrête le client et le serveur
#   De manière synchrone
#       • Le client envoie un message et le serveur répond
#       • Tester votre code avec votre voisin
#       • Attention un client doit pouvoir se reconnecter après la
#         déconnexion du précédent
import socket

def programme_serveur():
    try:
        port = 5000
        socket_serveur = socket.socket()
        socket_serveur.bind(('localhost', port))
        socket_serveur.listen(2)
        conn, adresse = socket_serveur.accept()
        print("Connexion depuis : " + str(adresse))
        arret = False

        while not arret:
            data = conn.recv(1024).decode()
            if not data:
                arret = True
            else:
                print("De l'utilisateur connecté : " + str(data))
                if data.lower().strip() == 'arret':
                    conn.send("arret".encode())
                    conn.close()
                    socket_serveur.close()
                    arret = True
                elif data.lower().strip() == 'bye':
                    conn.send("bye".encode())
                    conn.close()
                    conn, adresse = socket_serveur.accept()
                    print("Reconnexion depuis : " + str(adresse))
                else:
                    message = input(' -> ')
                    conn.send(message.encode())

    except OSError as os_err:
        print(f"Erreur OS : {os_err}")
    except ConnectionResetError:
        print("La connexion a été réinitialisée par le client.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
    finally:
        conn.close()
        socket_serveur.close()

if __name__ == '__main__':
    programme_serveur()







