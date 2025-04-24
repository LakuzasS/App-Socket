# 1 Une socket simple
#   Reprendre les codes du cours et les implémenter
import socket

def programme_serveur():
    try:
        port = 5000
        socket_serveur = socket.socket()
        socket_serveur.bind(('localhost', port))
        socket_serveur.listen(2)
        conn, adresse = socket_serveur.accept()
        print("Connexion depuis : " + str(adresse))

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("De l'utilisateur connecté : " + str(data))
            data = input(' -> ')
            conn.send(data.encode())

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



