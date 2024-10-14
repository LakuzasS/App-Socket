# 2 Une converison entre degrés Celsius et Kelvin
#   La conversion entre degré Celsius et Kelvin est relativement simple puisqu’il faut 
#   ajouter (K à °C) ou supprimer (°C à K) 273,15 (température du zéro absolu).
#       • -273.15 °C = 0 K = température du zéro absolu
#   Il faudra gérer les événements suivants :
#       • Changement d’unités lorsque la combobox change
#       • Erreur de saisie dans la zone d’entrée si peux que l’utilisation saisisse une chaîne de caractère de
#         type « aaa ». Vous pourrez déclencher un message d’alerte dans une boite de dialogue.
#       • Si une température est inférieure au 0 absolu soit -273,15 °C ou 0 K
"""
Le programme utilise PyQt6 pour créer une interface graphique permettant la conversion de 
température entre Celsius (°C) et Kelvin (K). La classe principale, TemperatureConverter, 
hérite de QWidget et représente la fenêtre principale de l'application.

La méthode initUI est utilisée pour initialiser l'interface utilisateur en utilisant un 
layout en grille (QGridLayout). Les composants comprennent des étiquettes (QLabel) pour 
afficher les textes statiques tels que "Température" et "Conversion", des zones de texte 
(QLineEdit) pour l'entrée de la température et l'affichage du résultat, un bouton "Convertir"
(QPushButton) pour déclencher la conversion, une combobox (QComboBox) pour sélectionner la 
direction de la conversion, et un bouton "?" (QPushButton) pour afficher de l'aide.

Les méthodes convert_temperature et show_help sont connectées aux boutons "Convertir" et "?", 
respectivement. La première effectue la conversion de la température en fonction de la sélection 
de la combobox et affiche le résultat, tandis que la seconde affiche une boîte de dialogue d'aide.

La méthode update_unit_labels est connectée au signal currentIndexChanged de la combobox et met à
jour les libellés des unités en fonction de la sélection (°C ou K).

Le programme se termine en instanciant une application (QApplication) et la fenêtre principale 
(TemperatureConverter), puis en affichant la fenêtre à l'écran.
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QPushButton, QComboBox, QMessageBox

class TemperatureConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Conversion de Température")
        self.resize(350, 150)
        self.layout = QGridLayout()

        self.label_temp = QLabel("Température")
        self.input_temp = QLineEdit()
        self.label_unit = QLabel("°C")
        self.layout.addWidget(self.label_temp, 0, 0)
        self.layout.addWidget(self.input_temp, 0, 1)
        self.layout.addWidget(self.label_unit, 0, 2)

        self.convert_button = QPushButton("Convertir")
        self.layout.addWidget(self.convert_button, 1, 0, 1, 1)  

        self.label_result = QLabel("Conversion")
        self.result_temp = QLineEdit()
        self.label_result_unit = QLabel("K")
        self.layout.addWidget(self.label_result, 2, 0)
        self.layout.addWidget(self.result_temp, 2, 1)
        self.layout.addWidget(self.label_result_unit, 2, 2)

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["°C -> K", "K -> °C"])
        self.layout.addWidget(self.unit_combo, 1, 1, 1, 1)  

        self.help_button = QPushButton("?")
        self.layout.addWidget(self.help_button, 4, 2)

        self.convert_button.clicked.connect(self.convert_temperature)
        self.help_button.clicked.connect(self.show_help)
        self.unit_combo.currentIndexChanged.connect(self.update_unit_labels)
        self.help_button.setFixedSize(30, 30)

        self.setLayout(self.layout)

    def convert_temperature(self):
        try:
            temperature = float(self.input_temp.text())
            unit_index = self.unit_combo.currentIndex()

            if unit_index == 0 and temperature < -273.15:
                raise ValueError("La température ne peut pas être inférieure au zéro absolu.")
            
            if unit_index == 0:
                converted_temp = temperature + 273.15
                self.label_result_unit.setText("K")
            else:
                converted_temp = temperature - 273.15
                self.label_result_unit.setText("°C")

            self.result_temp.setText(str(round(converted_temp, 2)))
        except ValueError as e:
            QMessageBox.critical(self, "Erreur de saisie", str(e))

    

    def update_unit_labels(self):
        unit_index = self.unit_combo.currentIndex()
        if unit_index == 0:
            self.label_unit.setText("°C")
            self.label_result_unit.setText("K")
        else:
            self.label_unit.setText("K")
            self.label_result_unit.setText("°C")

    def show_help(self):
        QMessageBox.information(self, "Aide", "Permet de convertir un nombre soit de Kelvin vers Celsius, soit de Celsius vers Kelvin.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = TemperatureConverter()
    converter.show()
    sys.exit(app.exec())
