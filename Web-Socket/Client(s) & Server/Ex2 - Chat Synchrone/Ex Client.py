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

def programme_client():
    try:
        port = 5000
        socket_client = socket.socket()
        socket_client.connect(('localhost', port))
        arret = False

        while not arret:
            message = input(" -> ")
            socket_client.send(message.encode())
            data = socket_client.recv(1024).decode()
            if data.lower().strip() == 'arret':
                socket_client.close()
                arret = True
            elif data.lower().strip() == 'bye':
                print("Déconnexion demandée par le serveur.")
                socket_client.close()
                arret = True
            else:
                print('Reçu du serveur : ' + data)

    except ConnectionRefusedError:
        print("Erreur de connexion : le serveur n'est pas disponible.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
    finally:
        socket_client.close()

if __name__ == '__main__':
    programme_client()



