import paho.mqtt.client as mqtt
from django.utils import timezone
import random
import string
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from collecte.models import Capteur, Donnee

MQTT_BROKER = "test.mosquitto.org"
MQTT_TOPICS = ["IUT/Colmar2023/SAE2.04/Maison1", "IUT/Colmar2023/SAE2.04/Maison2"]

def create_capteur(identifiant, piece, emplacement):
    if identifiant == "A72E3F6B79BB":
        nom = "Maison 1"
    elif identifiant == "B8A5F3569EFF":
        nom = "Maison 2"
    else:
        raise ValueError("Identifiant de capteur non pris en charge")
    emplacements = ["Rez de chaussée", "Étage", "Cave", "Grenier", "Jardin"]
    emplacement = random.choice(emplacements)
    capteur = Capteur.objects.create(id=identifiant, nom=nom, piece=piece, emplacement=emplacement)
    print("Capteur créé:", capteur)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        for topic in MQTT_TOPICS:
            client.subscribe(topic)
            print("Subscribed to", topic)
    else:
        print("Bad connection:", rc)

def on_message(client, userdata, msg):
    message = msg.topic + " " + str(msg.payload.decode("utf-8"))
    print(message)

    topic_parts = msg.topic.split('/')
    identifiant = message.split("Id=")[1].split(",")[0]
    piece = message.split("piece=")[1].split(",")[0]
    timestamp = timezone.now()
    temperature = float(message.split("temp=")[1])

    nombre_individus = random.randint(0, 6)

    if nombre_individus > 0:
        presence = True
    else:
        presence = False

    try:
        capteur = Capteur.objects.get(id=identifiant)
    except Capteur.DoesNotExist:
        create_capteur(identifiant, piece, topic_parts[3])
        capteur = Capteur.objects.get(id=identifiant)

    donnee = Donnee(capteur=capteur, timestamp=timestamp, temperature=temperature, presence=presence, nombre_individus=nombre_individus)
    donnee.save()
    print("Donnée enregistrée:", donnee)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER)
client.loop_forever()
