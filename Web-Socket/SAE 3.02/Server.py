import socket
import threading
import mysql.connector
import hashlib
import time
import os
import json

class Server:
    def __init__(self):
        """
        Initialise la classe du serveur.

        Configurations de la base de données, initialisation des sockets, et des structures de données.
        """
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'IutC_MySQL!68#',
            'database': 'test'
        }

        self.db_connection = mysql.connector.connect(**self.db_config)
        self.cursor = self.db_connection.cursor()

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 5000)
        self.server.bind(self.server_address)

        self.clients = []
        self.pending_requests = {}
        self.banned_users = {}
        self.authenticated_users = set()
        self.is_authenticated = False

    def inscription_handler(self, username, alias, password):
        """
        Gère le processus d'inscription pour un nouvel utilisateur.

        Args:
            username (str): Le nom d'utilisateur choisi par l'utilisateur.
            alias (str): L'alias choisi par l'utilisateur.
            password (str): Le mot de passe choisi par l'utilisateur.

        Returns:
            str: Message indiquant le résultat de l'inscription.
        """
        try:
            if not self.is_username_unique(username):
                return "Nom d'utilisateur déjà utilisé. Choisissez un autre."
            if not self.is_alias_unique(alias):
                return "Alias déjà utilisé. Choisissez un autre."
            
            if self.authenticate_user(username, password):
                return "Nom d'utilisateur déjà utilisé. Choisissez un autre."

            password_hash = hashlib.sha256(password.encode()).hexdigest()

            query = "INSERT INTO clients (username, alias, password_hash) VALUES (%s, %s, %s)"
            values = (username, alias, password_hash)
            self.cursor.execute(query, values)
            self.db_connection.commit()

            salons_a_integrer = ['Général']
            for salon in salons_a_integrer:
                query = f"INSERT INTO salons_adheres (username, salon_id) VALUES (%s, %s)"
                salon_id = self.get_salon_id(salon)
                values = (username, salon_id)
                self.cursor.execute(query, values)
                self.db_connection.commit()

            return "Inscription réussie!"
        except Exception as e:
            return f"Erreur lors de l'inscription : {e}"

    def is_alias_unique(self, alias):
        """
        Vérifie si l'alias est unique dans la base de données.

        Args:
            alias (str): L'alias à vérifier.

        Returns:
            bool: True si l'alias est unique, False sinon.
        """
        query_check = f"SELECT * FROM clients WHERE alias = '{alias}'"
        self.cursor.execute(query_check)
        result_check = self.cursor.fetchone()
        return result_check is None
    
    def is_username_unique(self, username):
        """
        Vérifie si le nom d'utilisateur est unique dans la base de données.

        Args:
            username (str): Le nom d'utilisateur à vérifier.

        Returns:
            bool: True si le nom d'utilisateur est unique, False sinon.
        """
        query_check = f"SELECT * FROM clients WHERE username = '{username}'"
        self.cursor.execute(query_check)
        result_check = self.cursor.fetchone()
        return result_check is None


    def insert_message(self, client_id, salon_id, contenu):
        """
        Insère un message dans la base de données.

        Args:
            client_id (int): L'ID du client qui envoie le message.
            salon_id (int): L'ID du salon dans lequel le message est envoyé.
            contenu (str): Le contenu du message.

        Returns:
            None
        """
        try:
            query = "INSERT INTO messages (client_id, salon_id, contenu) VALUES (%s, %s, %s)"
            values = (client_id, salon_id, contenu)
            self.cursor.execute(query, values)
            self.db_connection.commit()
        except Exception as e:
            print(f"Erreur lors de l'insertion du message dans la base de données : {e}")

    def get_salons(self):
        """
        Récupère la liste de tous les salons depuis la base de données.

        Returns:
            list: Liste des salons disponibles.
        """
        query = "SELECT * FROM salons"
        self.cursor.execute(query)
        salons = self.cursor.fetchall()
        return salons

    def get_user_salons(self, username):
        """
        Récupère la liste des salons auxquels un utilisateur est inscrit.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur.

        Returns:
            list: Liste des salons auxquels l'utilisateur est inscrit.
        """
        try:
            query = f"SELECT salon_id FROM salons_adheres WHERE username = '{username}'"
            self.cursor.execute(query)
            salons_adheres = self.cursor.fetchall()

            subscribed_salons = []
            for salon_id in salons_adheres:
                salon_name = self.get_salon_name(salon_id[0])
                subscribed_salons.append({"salon_id": salon_id[0], "salon_name": salon_name})

            return subscribed_salons

        except Exception as e:
            print(f"Error retrieving subscribed salons for {username}: {e}")
            return []


    def get_salon_name(self, salon_id):
        """
        Récupère le nom d'un salon à partir de son ID.

        Args:
            salon_id (int): L'ID du salon.

        Returns:
            str: Le nom du salon.
        """
        query = f"SELECT nom_salon FROM salons WHERE salon_id = {salon_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else None
    
    def get_client_id(self, username):
        """
        Récupère l'ID du client à partir du nom d'utilisateur.

        Args:
            username (str): Le nom d'utilisateur du client.

        Returns:
            int or None: L'ID du client s'il existe, None sinon.
        """
        query = f"SELECT client_id FROM clients WHERE username = '{username}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_salon_id(self, salon):
        """
        Récupère l'ID d'un salon à partir de son nom.

        Args:
            salon (str): Le nom du salon.

        Returns:
            int or None: L'ID du salon s'il existe, None sinon.
        """
        query = f"SELECT salon_id FROM salons WHERE nom_salon = '{salon}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else None

    def handle_client(self, client_socket, username, password):
        """
        Gère les interactions avec un client connecté au serveur.

        Args:
            client_socket (socket.socket): Le socket du client.
            username (str): Le nom d'utilisateur du client.
            password (str): Le mot de passe du client.

        Returns:
            None
        """
        try:            
            if self.is_user_banned(username):
                client_socket.send("Vous êtes banni. Réessayez dans quelques minutes.".encode('utf-8'))
                return

            salons = self.get_salons()
            salons_data = json.dumps(salons)
            client_socket.send(salons_data.encode('utf-8'))

            self.update_client_status(username, 'connected')

            salons_adheres = self.get_user_salons(username)
            client_socket.send(json.dumps(salons_adheres).encode('utf-8'))

            if 'Général' in salons:
                self.pending_requests.pop('Général', None)

            while True:
                data = client_socket.recv(1024).decode('utf-8')

                if not data:
                    break

                elif data.startswith('AUTH:'):
                    _, auth_username, auth_password = data.split(':')
                    if self.authenticate_user(auth_username, auth_password):
                        client_socket.send("CONNECTED".encode('utf-8'))
                    else:
                        client_socket.send("AUTH_FAILED".encode('utf-8'))
                        client_socket.close()
                
                elif data.startswith('BAN:'):
                    _, target_username = data.split(':')
                    if self.is_user_permanently_banned(target_username):
                        client_socket.send("User is permanently banned.".encode('utf-8'))
                        client_socket.close()
                    else:
                        self.ban_user(target_username)

                elif data.startswith('JOIN:'):
                    salon_name = data.split(':')[1]

                    # Si l'utilisateur est déjà adhéré au salon, ignorer la demande
                    if self.is_user_adhered(username, salon_name):
                        print(f"L'utilisateur {username} est déjà adhéré au salon {salon_name}.")
                        continue

                    # Sinon, traiter la demande d'adhésion
                    self.handle_join_request(username, salon_name)

                elif data.startswith('REGISTER:'):
                    _, username, alias, password = data.split(':')
                    response = self.inscription_handler(username, alias, password)
                    client_socket.send(response.encode('utf-8'))
                    break

                elif data.startswith('MSG ('):
                    _, rest = data.split('(', 1)
                    salon, message = rest.split('):', 1)

                    insert_query = "INSERT INTO messages (client_id, salon_id, contenu) VALUES (%s, %s, %s)"
                    insert_values = (self.get_client_id(username), self.get_salon_id(salon), message)
                    self.cursor.execute(insert_query, insert_values)
                    self.db_connection.commit()

                    self.broadcast(f"{username} dans le salon {salon}: {message}")
                
                elif data.startswith('PRIVATE:'):
                    _, rest = data.split(':', 1)
                    self.handle_private_message(username, rest)
        except Exception as e:
            print(f"Erreur avec {username}: {e}")
        finally:
            self.update_client_status(username, 'disconnected')
            self.remove_client(client_socket, username)

    def handle_join_request(self, username, salon_to_join):
        """
        Traite la demande d'adhésion d'un utilisateur à un salon.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur faisant la demande.
            salon_to_join (str): Le nom du salon auquel l'utilisateur veut adhérer.

        Returns:
            None
        """
        if salon_to_join.lower() == "blabla":
            self.add_user_to_salon(username, salon_to_join)
        else:
            if salon_to_join not in self.pending_requests:
                self.pending_requests[salon_to_join] = []

            self.pending_requests[salon_to_join].append(username)
            print(f"Join request from {username} for salon {salon_to_join}.")

    def is_user_adhered(self, username, salon_name):
        """
        Vérifie si un utilisateur est adhérent à un salon spécifié.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur à vérifier.
            salon_name (str): Le nom du salon auquel vérifier l'adhésion.

        Returns:
            bool: True si l'utilisateur est adhérent, False sinon.
        """
        try:
            salon_id = self.get_salon_id(salon_name)

            query_check = f"SELECT * FROM salons_adheres WHERE username = '{username}' AND salon_id = {salon_id}"
            self.cursor.execute(query_check)
            result_check = self.cursor.fetchone()

            return result_check is not None
        except Exception as e:
            print(f"Erreur lors de la vérification de l'adhésion de {username} au salon {salon_name}: {e}")
            return False


    def accept_join_request(self, username, salon_to_join):
        """
        Accepte la demande d'adhésion d'un utilisateur à un salon spécifié.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur dont la demande est acceptée.
            salon_to_join (str): Le nom du salon auquel l'utilisateur est ajouté.

        Returns:
            None
        """
        if salon_to_join in self.pending_requests and username in self.pending_requests[salon_to_join]:
            self.pending_requests[salon_to_join].remove(username)
            if salon_to_join.lower() == "blabla":
                self.add_user_to_salon_direct(username, salon_to_join)
            else:
                self.add_user_to_salon(username, salon_to_join)

            message = f"{username} a rejoint le salon {salon_to_join}."
            self.broadcast(message)


    def reject_join_request(self, username, salon_to_join):
        """
        Rejette la demande d'adhésion d'un utilisateur à un salon spécifié.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur dont la demande est rejetée.
            salon_to_join (str): Le nom du salon dont la demande est rejetée.

        Returns:
            None
        """
        if salon_to_join in self.pending_requests and username in self.pending_requests[salon_to_join]:
            self.pending_requests[salon_to_join].remove(username)

            message = f"Votre demande d'adhésion au salon {salon_to_join} a été refusée. Accès restreint"
            self.broadcast(message)
            self.remove_user_from_salon(username, salon_to_join)
            

    def remove_user_from_salon(self, username, salon_name):
        """
        Retire un utilisateur d'un salon spécifié.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur à retirer.
            salon_name (str): Le nom du salon duquel retirer l'utilisateur.

        Returns:
            None
        """
        try:
            salon_id = self.get_salon_id(salon_name)

            query = f"DELETE FROM salons_adheres WHERE username = '{username}' AND salon_id = {salon_id}"
            self.cursor.execute(query)
            self.db_connection.commit()

            print(f"Utilisateur {username} retiré du salon {salon_id}.")
        except Exception as e:
            print(f"Erreur lors de la suppression de {username} du salon {salon_name}: {e}")

    def add_user_to_salon(self, username, salon):
        """
        Ajoute un utilisateur à un salon spécifié.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur à ajouter.
            salon (str): Le nom du salon auquel ajouter l'utilisateur.

        Returns:
            None
        """
        try:
            salon_id = self.get_salon_id(salon)

            if not salon_id:
                print(f"Le salon {salon} n'existe pas.")
                return

            query_check = f"SELECT * FROM salons_adheres WHERE username = '{username}' AND salon_id = {salon_id}"
            self.cursor.execute(query_check)
            result_check = self.cursor.fetchone()

            if not result_check:
                query = f"INSERT INTO salons_adheres (username, salon_id) VALUES (%s, %s)"
                values = (username, salon_id)
                self.cursor.execute(query, values)
                self.db_connection.commit()

                print(f"Utilisateur {username} ajouté au salon {salon_id}.")

        except Exception as e:
            print(f"Erreur lors de l'ajout de {username} au salon {salon}: {e}")


    def handle_client_disconnect(self, username):
        """
        Gère la déconnexion d'un client en retirant ses demandes d'adhésion.

        Args:
            username (str): Le nom d'utilisateur du client qui se déconnecte.

        Returns:
            None
        """
        try:
            for salon, demandeurs in self.pending_requests.items():
                if username in demandeurs:
                    demandeurs.remove(username)
                    break
        except Exception as e:
            print(f"Erreur lors de la gestion de la déconnexion de {username}: {e}")

    def remove_client(self, client_socket, username):
        """
        Retire un client de la liste des clients connectés.

        Args:
            client_socket (socket): Le socket du client à retirer.
            username (str): Le nom d'utilisateur du client à retirer.

        Returns:
            None
        """
        try:
            for client, client_username in self.clients:
                if client == client_socket and client_username == username:
                    client_socket.close()
                    self.clients.remove((client_socket, client_username))
                    self.handle_client_disconnect(username)
                    break
        except Exception as e:
            print(f"Erreur lors de la déconnexion de {username}: {e}")
    
    def update_client_status(self, username, new_status):
        """
        Met à jour le statut d'un client dans la base de données.

        Args:
            username (str): Le nom d'utilisateur du client à mettre à jour.
            new_status (str): Le nouveau statut du client.

        Returns:
            None
        """
        query = f"UPDATE clients SET status = '{new_status}' WHERE username = '{username}'"
        self.cursor.execute(query)
        self.db_connection.commit()



    def authenticate_user(self, username, password):
        """
        Authentifie un utilisateur en vérifiant le nom d'utilisateur et le mot de passe.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur à authentifier.
            password (str): Le mot de passe de l'utilisateur.

        Returns:
            bool: True si l'authentification réussit, False sinon.
        """
        query = f"SELECT password_hash FROM clients WHERE username = '{username}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result:
            stored_password_hash = result[0]
            input_password_hash = hashlib.sha256(password.encode()).hexdigest()
            return stored_password_hash == input_password_hash
        return False

    def kick_user(self, target_username):
        """
        Expulse un utilisateur du serveur.

        Args:
            target_username (str): Le nom d'utilisateur de l'utilisateur à expulser.

        Returns:
            None
        """
        for client, username in self.clients:
            if username == target_username:
                try:
                    client.send("Vous avez été expulsé du serveur. Vous êtes banni pendant 5 minutes.".encode('utf-8'))
                except Exception as e:
                    print(f"Erreur lors de l'envoi du message à {username}: {e}")
                finally:
                    self.banned_users[target_username] = time.time()
                    self.clients.remove((client, username))
                    client.close()
                break

    def ban_user(self, target_username):
        """
        Banni définitivement un utilisateur du serveur.

        Args:
            target_username (str): Le nom d'utilisateur de l'utilisateur à bannir.

        Returns:
            None
        """
        for client, username in self.clients:
            if username == target_username:
                try:
                    client.send("Vous avez été banni définitivement du serveur !".encode('utf-8'))
                except Exception as e:
                    print(f"Erreur lors de l'envoi du message à {username}: {e}")
                finally:
                    self.remove_user_from_database(target_username)
                    self.clients.remove((client, username))
                    client.close()
                break

    def remove_user_from_database(self, username):
        """
        Supprime un utilisateur de la base de données, y compris ses adhésions et messages.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur à supprimer.

        Returns:
            None
        """
        try:
            client_id = self.get_client_id(username)
            query_delete_salon = f"DELETE FROM salons_adheres WHERE username = '{username}'"
            self.cursor.execute(query_delete_salon)
            query_delete_messages = f"DELETE FROM messages WHERE client_id = {client_id}"
            self.cursor.execute(query_delete_messages)
            query_delete_client = f"DELETE FROM clients WHERE username = '{username}'"
            self.cursor.execute(query_delete_client)
            self.db_connection.commit()

            print(f"Utilisateur {username} supprimé de la base de données.")
        except Exception as e:
            print(f"Erreur lors de la suppression de {username} de la base de données: {e}")

    def is_user_banned(self, username):
        """
        Vérifie si un utilisateur est banni du serveur.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur à vérifier.

        Returns:
            bool: True si l'utilisateur est banni, False sinon.
        """
        if username in self.banned_users:
            return time.time() - self.banned_users[username] < 300
        return False

    def kill_server(self):
        """
        Arrête le serveur de manière contrôlée.

        Envoie des messages d'arrêt aux clients, attend 10 secondes, puis ferme les connexions et arrête le serveur.

        Args:
            None

        Returns:
            None
        """
        print("Arrêt du serveur par commande KILL.")
        self.broadcast("Le serveur va s'arrêter dans 10 secondes. Merci de vous déconnecter.")
        time.sleep(10)

        for client, _ in self.clients:
            try:
                client.send("Le serveur va s'arrêter. Merci de vous déconnecter.".encode('utf-8'))
                client.close()
            except Exception as e:
                print(f"Erreur lors de la fermeture de la connexion du client : {e}")

        os._exit(0)

    def handle_commands(self):
        """
        Gère les commandes entrées par l'utilisateur (utilisé dans le thread séparé).

        Les commandes possibles sont KICK, BAN, KILL, ACCEPT, et REJECT.

        Args:
            None

        Returns:
            None
        """
        while True:
            command = input("Tapez une commande (KICK/BAN/KILL/ACCEPT/REJECT): ").strip()
            if command.startswith('KICK:'):
                _, target_username = command.split(':')
                self.kick_user(target_username)
            elif command.startswith('BAN:'):
                _, target_username = command.split(':')
                self.ban_user(target_username)
            elif command.startswith('ACCEPT:'):
                _, username, salon_to_join = command.split(':')
                self.accept_join_request(username, salon_to_join)
            elif command.startswith('REJECT:'):
                _, username, salon_to_join = command.split(':')
                self.reject_join_request(username, salon_to_join)
            elif command == 'KILL':
                self.kill_server()

    def broadcast(self, message):
        """
        Diffuse un message à tous les clients connectés.

        Args:
            message (str): Le message à diffuser.

        Returns:
            None
        """
        for client, username in self.clients:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Erreur lors de l'envoi du message à {username}: {e}")
                self.remove_client(client, username)  

    def update_password(self, username, new_password):
        """
        Met à jour le mot de passe d'un utilisateur dans la base de données.

        Args:
            username (str): Le nom d'utilisateur de l'utilisateur.
            new_password (str): Le nouveau mot de passe.

        Returns:
            str: Un message indiquant le succès ou l'échec de la mise à jour.
        """
        try:
            password_hash = hashlib.sha256(new_password.encode()).hexdigest()
            query = f"UPDATE clients SET password_hash = '{password_hash}' WHERE username = '{username}'"
            self.cursor.execute(query)
            self.db_connection.commit()
            return "Mot de passe mis à jour avec succès!"
        except Exception as e:
            return f"Erreur lors de la mise à jour du mot de passe : {e}"

    def start_server(self):
        """
        Démarre le serveur, gère l'authentification initiale et écoute les connexions entrantes.

        Args:
            None

        Returns:
            None
        """
        while True:
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")

            if self.authenticate_user(username, password) and username in ['admin', 'server']:
                print(f"Authentification réussie pour l'utilisateur {username}.")
                self.authenticated_users.add(username)
                break
            else:
                print("Authentification échouée. Veuillez réessayer.")

        self.server.listen(5)
        print("Serveur en attente de connexions...")

        command_handler = threading.Thread(target=self.handle_commands)
        command_handler.start()

        while True:
            client_socket, client_address = self.server.accept()
            credentials = client_socket.recv(1024).decode('utf-8').split(':')
            
            if len(credentials) >= 2:
                if credentials[0] == "INSCRIPTION":
                    _, username, alias, password = credentials
                    response = self.inscription_handler(username, alias, password)
                    client_socket.send(response.encode('utf-8'))
                    client_socket.close()
                else:
                    username, password = credentials[:2]

                    if self.authenticate_user(username, password):
                        self.clients.append((client_socket, username))
                        client_handler = threading.Thread(target=self.handle_client, args=(client_socket, username, password))
                        client_handler.start()
                        client_socket.send("CONNECTED".encode('utf-8'))
                    else:
                        client_socket.send("AUTH_FAILED".encode('utf-8'))
                        client_socket.close()
            else:
                print("Erreur : Liste credentials invalide.")

if __name__ == "__main__":
    server = Server()
    server.start_server()