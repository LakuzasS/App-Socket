# 1 Une socket simple
#   Reprendre les codes du cours et les implémenter
import socket

def programme_client():
    try:
        port = 5000
        socket_client = socket.socket()
        socket_client.connect(('localhost', port))
        message = input(" -> ")

        while message.lower().strip() != 'bye':
            socket_client.send(message.encode())
            data = socket_client.recv(1024).decode()
            print('Reçu du serveur : ' + data)
            message = input(" -> ")

    except ConnectionRefusedError:
        print("Erreur de connexion : le serveur n'est pas disponible.")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")
    finally:
        socket_client.close()

if __name__ == '__main__':
    programme_client()
