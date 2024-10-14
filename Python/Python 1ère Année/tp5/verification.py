import os.path
import datetime
fichier1 = str(input("nom du fichier n°1 :"))
fichier2 = str(input("nom du fichier n°2 :"))
if os.path.isfile(fichier1):
    print(True,",le fichier n°1 existe.")
if os.path.isfile(fichier2):
    print(True,",le fichier n°2 existe.")
print(datetime.datetime.fromtimestamp(os.path.getmtime(fichier1)))
print(datetime.datetime.fromtimestamp(os.path.getmtime(fichier2)))
time1 = os.path.getmtime(fichier1)
time2 = os.path.getmtime(fichier2)
if time1 > time2:
    time1 = datetime.datetime.fromtimestamp(time1)
    print(f"\nLe fichier le plus récent est {fichier1}, sa date de modification est le {time1}")

else:
    time2 = datetime.datetime.fromtimestamp(time2)
    print(f"\nLe fichier le plus récent est {fichier2}, sa date de modification est le {time2}")