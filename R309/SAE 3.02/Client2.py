import sys
from PyQt5.QtGui import QPalette, QColor, QBrush, QLinearGradient, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QDialog, QMessageBox, QGridLayout, QSizePolicy
from PyQt5.QtCore import pyqtSignal, QThread
import socket
import json

class InscriptionDialog(QDialog):
    def __init__(self, server_address):
        """
        Initialise la boîte de dialogue d'inscription.

        Args:
            server_address (tuple): L'adresse du serveur auquel l'utilisateur souhaite s'inscrire.

        Returns:
            None
        """
        super().__init__()
        self.setWindowTitle("Page d'inscription")
        self.setMinimumWidth(300)

        self.username_label = QLabel("Nom d'utilisateur:")
        self.username_input = QLineEdit()

        self.alias_label = QLabel("Alias:")
        self.alias_input = QLineEdit()

        self.password_label = QLabel("Mot de passe:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.inscription_button = QPushButton("S'inscrire")
        self.inscription_button.clicked.connect(self.inscrire)

        self.server_address = server_address

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.alias_label)
        layout.addWidget(self.alias_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.inscription_button)

        self.setLayout(layout)

    def inscrire(self):
        """
        Méthode appelée lors du clic sur le bouton d'inscription.

        Args:
            None

        Returns:
            None
        """
        username = self.username_input.text().strip()
        alias = self.alias_input.text().strip()
        password = self.password_input.text().strip()

        inscription_request = f"INSCRIPTION:{username}:{alias}:{password}"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect(self.server_address)
                client_socket.send(inscription_request.encode('utf-8'))

                inscription_response = client_socket.recv(1024).decode('utf-8')
                print(inscription_response)
                QMessageBox.information(self, "Résultat de l'inscription", inscription_response)

                if inscription_response == "Inscription réussie!":
                    adhesion_request = f'JOIN:Général'
                    client_socket.send(adhesion_request.encode('utf-8'))
                    self.accept()
            except Exception as e:
                print(f"Erreur lors de l'envoi de la demande d'inscription : {e}")

class AdhesionDialog(QDialog):
    def __init__(self, salon_name, client):
        """
        Initialise la boîte de dialogue d'adhésion.

        Args:
            salon_name (str): Le nom du salon auquel l'utilisateur souhaite adhérer.
            client (Client): L'instance du client associée à cette boîte de dialogue.

        Returns:
            None
        """
        super().__init__()
        self.setWindowTitle("Adhésion au Salon")

        self.salon_name = salon_name
        self.server_response = None
        self.client = client

        label = QLabel(f"Voulez-vous adhérer au salon {salon_name}?")

        join_button = QPushButton("Oui")
        join_button.clicked.connect(self.adherer_au_salon)

        cancel_button = QPushButton("Non")
        cancel_button.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(join_button)
        layout.addWidget(cancel_button)

        self.setLayout(layout)


    def adherer_au_salon(self):
        """
        Méthode appelée lors du clic sur le bouton "Oui" pour adhérer au salon.

        Args:
            None

        Returns:
            None
        """
        formatted_request = f'JOIN:{self.salon_name}'
        self.server_response = formatted_request
        self.accept()

    def send_automatic_adhesion_request(self):
        """
        Méthode pour envoyer une demande d'adhésion automatique à Blabla (ou un autre salon).

        Args:
            None

        Returns:
            None
        """
        blabla_request = f'JOIN:Blabla'
        self.client.socket.send(blabla_request.encode('utf-8'))

class Client(QThread):
    message_received = pyqtSignal(str)
    subscribed_salons_received = pyqtSignal(list)

    def __init__(self, username, host, port, password):
        """
        Initialise le client.

        Args:
            username (str): Le nom d'utilisateur du client.
            host (str): L'adresse IP du serveur.
            port (int): Le numéro de port du serveur.
            password (str): Le mot de passe du client.

        Returns:
            None
        """
        super().__init__()
        self.username = username
        self.host = host
        self.port = port
        self.password = password
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        """
        Méthode principale pour exécuter le thread client.

        Args:
            None

        Returns:
            None
        """
        try:
            self.socket.connect((self.host, self.port))
            credentials = f"{self.username}:{self.password}"
            self.socket.send(credentials.encode('utf-8'))

            initial_response = self.socket.recv(1024).decode('utf-8')

            if initial_response == "CONNECTED":
                print(f"Connexion établie avec {self.username}.")

                salons_data = self.socket.recv(1024).decode('utf-8')
                self.message_received.emit(salons_data)

                subscribed_salons_data = self.socket.recv(1024).decode('utf-8')
                subscribed_salons = json.loads(subscribed_salons_data)
                self.subscribed_salons_received.emit(subscribed_salons)

                while not self.isInterruptionRequested():
                    data = self.socket.recv(1024).decode('utf-8')

                    if not data:
                        break

                    if data == "AUTH_FAILED":
                        print("L'authentification a échoué. Veuillez vérifier votre nom d'utilisateur et mot de passe.")
                        break

                    if data.startswith('{') and data.endswith('}'):
                        try:
                            json_data = json.loads(data)
                            self.message_received.emit(json_data)
                        except json.decoder.JSONDecodeError as e:
                            print(f"Erreur lors du décodage JSON : {e}")
                    else:
                        self.message_received.emit(data)

        except Exception as e:
            print(f"Erreur dans le client : {e}")
        finally:
            self.socket.close()    

class ClientGUI(QWidget):
    def __init__(self):
        """
        Initialise l'interface graphique du client.

        Args:
            None

        Returns:
            None
        """
        super().__init__()
        self.setWindowTitle("Server de Chat")
        self.setMinimumWidth(500)
        self.client = None

        self.username_label = QLabel("Nom d'utilisateur:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Mot de passe:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.connect_button = QPushButton("Se connecter")
        self.connect_button.clicked.connect(self.connect_to_server)

        self.inscription_button = QPushButton("S'inscrire")
        self.inscription_button.clicked.connect(self.afficher_page_inscription)

        self.chat_display = QTextEdit()
        self.message_input = QLineEdit()

        self.salon_label = QLabel("Sélectionnez un salon:")
        self.salon_combobox = QComboBox()

        self.send_button = QPushButton("Envoyer")
        self.send_button.clicked.connect(self.send_message)

        self.disconnect_button = QPushButton("Se déconnecter")
        self.disconnect_button.clicked.connect(self.disconnect_from_server)

        layout = QGridLayout()

        layout.addWidget(self.username_label, 0, 0)
        layout.addWidget(self.password_label, 0, 1)
        layout.addWidget(self.salon_label, 0, 3)

        layout.addWidget(self.username_input, 1, 0)
        layout.addWidget(self.password_input, 1, 1)
        layout.addWidget(self.salon_combobox, 1, 3)

        layout.addWidget(self.connect_button, 2, 0, 1, 2)
        layout.addWidget(self.inscription_button, 2, 2)

        layout.addWidget(self.chat_display, 3, 0, 1, 3)

        layout.addWidget(self.message_input, 4, 0, 1, 2)
        layout.addWidget(self.send_button, 4, 2) 
        layout.addWidget(self.disconnect_button, 4, 3)

        self.setLayout(layout)

        self.client = None
        self.salon_combobox.currentIndexChanged.connect(self.update_salon_display)
        self.salons_adheres = set()
        self.set_gradient_background()
        self.subscribed_salons = []

    def set_gradient_background(self):
        """
        Applique un dégradé en tant que fond pour l'interface graphique.

        Args:
            None

        Returns:
            None
        """
        palette = self.palette()

        gradient_color1 = QColor(173, 216, 230)
        gradient_color2 = QColor(0, 0, 128)   
        

        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, gradient_color1)
        gradient.setColorAt(1, gradient_color2)

        brush = QBrush(gradient)
        palette.setBrush(QPalette.Window, brush)
        self.setPalette(palette)

        self.setStyleSheet("color: black;")

        font = QFont()
        font.setPointSize(15) 
        self.setFont(font)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def connect_to_server(self):
        """
        Méthode pour se connecter au serveur.

        Args:
            None

        Returns:
            None
        """
        if not self.client:
            username = self.username_input.text().strip()
            password = self.password_input.text().strip()
            if username and password:
                self.client = Client(username, 'localhost', 5000, password)
                self.client.message_received.connect(self.populate_salons)
                self.client.subscribed_salons_received.connect(self.update_subscribed_salons) 
                self.client.start()
                self.setWindowTitle(f"Server de Chat - {username}")
            else:
                print("Veuillez entrer un nom d'utilisateur.")


    def populate_salons(self, salons_data):
        """
        Méthode pour peupler la liste des salons.

        Args:
            salons_data (str): Les données sur les salons sous forme de chaîne JSON.

        Returns:
            None
        """
        try:
            if salons_data:
                try:
                    salons = json.loads(salons_data)
                    if isinstance(salons, list) and salons:
                        if all(isinstance(salon, list) and len(salon) >= 2 for salon in salons):
                            self.salon_combobox.clear()
                            self.salon_combobox.addItems([str(salon[1]) for salon in salons])
                except json.decoder.JSONDecodeError as e:
                    self.display_message(salons_data)
        except Exception as ex:
            print(f"Error: {ex}")

    def update_subscribed_salons(self, subscribed_salons):
        """
        Méthode pour mettre à jour la liste des salons auxquels l'utilisateur est abonné.

        Args:
            subscribed_salons (list): La liste des salons auxquels l'utilisateur est abonné.

        Returns:
            None
        """
        print("Salons adhérés:", subscribed_salons)
        self.subscribed_salons = [salon['salon_name'] for salon in subscribed_salons]

    def check_adhesion(self, selected_salon):
        """
        Vérifie si l'utilisateur est déjà abonné au salon sélectionné.

        Args:
            selected_salon (str): Le nom du salon sélectionné.

        Returns:
            None
        """
        if selected_salon.lower() in (salon.lower() for salon in self.subscribed_salons):
            QMessageBox.information(self, "Déjà abonné", f"Vous êtes déjà abonné au salon {selected_salon}.")
        else:
            adhesion_dialog = AdhesionDialog(selected_salon, self.client)
            result = adhesion_dialog.exec_()

            if result == QDialog.Accepted:
                formatted_request = adhesion_dialog.server_response
                print(f"Sending request to join salon: {formatted_request}")
                self.client.socket.send(formatted_request.encode('utf-8'))
                QMessageBox.information(self, "Vérification", f"Votre demande d'adhésion au salon {selected_salon} a été prise en compte !")


    def update_salon_display(self):
        """
        Met à jour l'affichage en fonction du salon sélectionné.

        Args:
            None

        Returns:
            None
        """
        selected_salon = self.salon_combobox.currentText()

        if selected_salon == "Général":
            return

        if selected_salon.lower() == "blabla":
            self.check_adhesion(selected_salon)
        elif selected_salon not in self.subscribed_salons:
            adhesion_dialog = AdhesionDialog(selected_salon, self.client)
            result = adhesion_dialog.exec_()

            if result == QDialog.Accepted:
                adhesion_dialog.send_automatic_adhesion_request()
                self.subscribed_salons.append(selected_salon)
                formatted_request = adhesion_dialog.server_response
                self.client.socket.send(formatted_request.encode('utf-8'))
                QMessageBox.information(self, "Vérification", f"Votre demande d'adhésion au salon {selected_salon} a été prise en compte !")


        print(self.subscribed_salons)
        if selected_salon in self.subscribed_salons:
            self.message_input.setDisabled(False)
            self.send_button.setDisabled(False)
        else:
            QMessageBox.warning(self, "Accès refusé", f"Vous n'êtes pas abonné au salon {selected_salon}. L'accès est refusé.")
            self.message_input.setDisabled(True)
            self.send_button.setDisabled(True)

    def afficher_page_inscription(self):
        """
        Affiche la page d'inscription.

        Args:
            None

        Returns:
            None
        """
        inscription_dialog = InscriptionDialog(('localhost', 5000))
        inscription_dialog.exec_()

    def send_message(self):
        """
        Envoie un message au salon sélectionné.

        Args:
            None

        Returns:
            None
        """
        if self.client:
            username = self.username_input.text().strip()
            if username:
                message = self.message_input.text().strip()
                if message:
                    salon = self.salon_combobox.currentText()
                    formatted_message = f"MSG ({salon}): {message}"
                    self.client.socket.send(formatted_message.encode('utf-8'))
                    self.message_input.clear()
                else:
                    print("Veuillez entrer un message.")
            else:
                print("Veuillez vous connecter d'abord.")

    def display_message(self, message):
        """
        Affiche un message dans la zone de chat si l'utilisateur est abonné au salon.

        Args:
            message (str): Le message à afficher.

        Returns:
            None
        """
        if self.is_user_subscribed_to_current_salon():
            self.chat_display.append(message)
        
    def is_user_subscribed_to_current_salon(self):
        """
        Vérifie si l'utilisateur est abonné au salon actuellement sélectionné.

        Args:
            None

        Returns:
            bool: True si l'utilisateur est abonné, False sinon.
        """
        selected_salon = self.salon_combobox.currentText()
        return any(salon.lower() == selected_salon.lower() for salon in self.subscribed_salons)

    def disconnect_from_server(self):
        """
        Déconnecte le client du serveur.

        Args:
            None

        Returns:
            None
        """
        if self.client:
            self.client.socket.close()
            self.client = None
            self.chat_display.clear()
            self.salon_combobox.clear()
            self.salons_adheres.clear()

    def closeEvent(self, event):
        """
        Méthode appelée lors de la fermeture de l'application.

        Args:
            event (QCloseEvent): L'événement de fermeture.

        Returns:
            None
        """
        if self.client:
            self.client.socket.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientGUI()
    window.show()
    sys.exit(app.exec_())