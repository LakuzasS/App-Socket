# 1 Un affichage simple
#   Pour cela, repartez du code proposé dans le cours (avec l’héritage).
#   Faites attention à bien positionner
#       • A partir d’une classe
#       • Les attributs de classe pertinents
#       • Et de compléter les éléments manquants dans le code du cours
#         https://e-formation.uha.fr/pluginfile.php/597406/mod_resource/content/14/Programmation%20Evenementielle%20-%20v5.2.pdf
#       • Arrangez pour redimensionner la fenêtre pour que le titre soit visible
"""
Le programme utilise PyQt6 pour créer une interface graphique simple. Il démarre en important 
les modules nécessaires, tels que sys pour l'accès aux fonctionnalités système et les éléments 
PyQt6 pour la création de l'interface utilisateur. 

La classe principale, MainWindow, hérite de QWidget et représente la fenêtre principale de 
l'application. Son initialisation (initUI) se concentre sur la création des composants de 
l'interface graphique.

Une disposition verticale (QVBoxLayout) est utilisée pour organiser les éléments de manière 
linéaire. Une étiquette ("Saisir votre nom") est ajoutée en haut de la fenêtre, suivie d'un 
champ de saisie pour le nom. Deux boutons, "Ok" et "Quitter", sont ajoutés respectivement 
pour valider la saisie et quitter l'application.

La méthode actionOk est connectée au bouton "Ok" et est appelée lorsque ce dernier est cliqué. 
Elle récupère le texte saisi dans le champ de saisie, crée un message de salutation avec ce nom, 
puis affiche le message dans une étiquette située en dessous.

La méthode actionQuitter est connectée au bouton "Quitter" et permet de fermer l'application 
lorsque le bouton est pressé.

Le programme principal commence en instanciant une application (QApplication) et la fenêtre 
principale (MainWindow). La fenêtre est ensuite affichée à l'écran, permettant à l'utilisateur 
d'interagir avec les composants créés.
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        label = QLabel("Saisir votre nom", self)
        layout.addWidget(label)

        self.saisie_nom = QLineEdit(self)
        layout.addWidget(self.saisie_nom)

        bouton_ok = QPushButton("Ok", self)
        bouton_ok.clicked.connect(self.actionOk)
        layout.addWidget(bouton_ok)

        self.message_label = QLabel("", self)
        layout.addWidget(self.message_label)

        bouton_quitter = QPushButton("Quitter", self)
        bouton_quitter.clicked.connect(self.actionQuitter)
        layout.addWidget(bouton_quitter)

        self.setWindowTitle("Une première fenêtre")
        self.resize(350, 150)

    def actionOk(self):
        prenom = self.saisie_nom.text()
        message = f'Bonjour {prenom} !'
        self.message_label.setText(message)

    def actionQuitter(self):
        QApplication.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
