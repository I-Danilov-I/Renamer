# Modul zum Operieren mit dem Operation System
import os
import time

# Pfad zum Ordner der Dateien die Umbenannt werden müssen
pfad = "C:\\Users\\ARHITEKTOR\\Desktop\\Berichtsheft 2022"

# Dateien in im angegeben Ordner durchlaufen und in der Liste Speichern
file_liste = os.listdir(pfad)


def umbenennen():
    for file_name in file_liste:
        # Extrahiere die KW-Woche aus dem Dateinamen
        kw = file_name[40:44]

        # Extrahiere den Dateityp (Dateiendung) aus dem ursprünglichen Dateinamen
        dateityp = os.path.splitext(file_name)[1]

        # Neuer Dateiname
        new_file_name = f"Berichtsheft_2022 {kw}_Anatoliy_Danilov{dateityp}"
        # Überprüfe, ob die Datei bereits existiert
        if not os.path.exists(os.path.join(pfad, new_file_name)):
            # Umbenennung der Dateien
            os.rename(os.path.join(pfad, file_name), os.path.join(pfad, new_file_name))
        else:
            print(f"Die Datei {new_file_name} existiert bereits.")
    print("Dateien wurden erfolgreich umbenannt!")


def ausgabe():
    # Durchlaufe der Liste durch
    for file_name in file_liste:
        print("Dateiname: | ", file_name)


umbenennen()
time.sleep(5)
ausgabe()
