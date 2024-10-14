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

def gerer_client(conn, adresse, clients):
    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"De l'utilisateur {adresse}: {data}")

            if data.lower().strip() == 'arret':
                for client in clients:
                    if client != conn:
                        try:
                            client.send("arret".encode())
                            client.close()
                        except:
                            continue
                break
            elif data.lower().strip() == 'bye':
                conn.send("bye".encode())
                clients.remove(conn)
                break
            else:
                for client in clients:
                    if client != conn:
                        try:
                            client.send(f"De l'utilisateur {adresse}: {data}".encode())
                        except:
                            continue
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        print(f"Déconnexion de l'utilisateur {adresse}")
        conn.close()

def programme_serveur():
    port = 5000
    socket_serveur = socket.socket()
    socket_serveur.bind(('localhost', port))
    socket_serveur.listen(5)
    clients = []

    try:
        while True:
            conn, adresse = socket_serveur.accept()
            clients.append(conn)
            client_thread = threading.Thread(target=gerer_client, args=(conn, adresse, clients))
            client_thread.start()

    except KeyboardInterrupt:
        print("Arrêt du serveur.")
        for client in clients:
            try:
                client.send("arret".encode())
                client.close()
            except:
                continue

    finally:
        socket_serveur.close()

if __name__ == '__main__':
    programme_serveur()


























