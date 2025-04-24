# 3 Un chat Asynchrone et serveur de discussion
#   Ajout de messages de « protocole » :
#       • bye – qui provoque l’arrêt du client mais pas du serveur
#       • arret – qui arrête le client et le serveur
#   De manière asynchrone
#       • Le client et le serveur peuvent envoyer des messages quand il le souhaite
#       • En utilisant un mécanisme de Thread
#       • Tester votre code avec votre voisin
#   Si vous en avez la force, créer un serveur qui permet la discussion entre plusieurs clients
#       • Les clients discutent entre eux
#       • Le serveur renvoie les messages aux autres clients en spécifiant l’IP de la machine
import socket
import threading

def ecouter_serveur(socket_client):
    try:
        while True:
            data = socket_client.recv(1024).decode()
            if not data:
                break
            print(f'Reçu du serveur : {data}')
            if data.lower().strip() == 'arret' or data.lower().strip() == 'bye':
                socket_client.close()
                break
    except (ConnectionResetError, ConnectionAbortedError):
        pass

def programme_client():
    try:
        port = 5000
        socket_client = socket.socket()
        socket_client.connect(('localhost', port))

        # Démarrer un thread pour écouter les messages du serveur en parallèle
        thread_ecoute = threading.Thread(target=ecouter_serveur, args=(socket_client,))
        thread_ecoute.start()

        while True:
            message = input(" -> ")
            socket_client.send(message.encode())
            if message.lower().strip() == 'arret' or message.lower().strip() == 'bye':
                break

    except Exception as e:
        pass
    finally:
        socket_client.close()

if __name__ == '__main__':
    programme_client()












