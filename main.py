# Modul zum Operieren mit dem Operation System
import os


def umbenennen():
    # Dateien in im angegeben Ordner durchlaufen und in der Liste Speichern
    file_liste = os.listdir(pfad)

    for file_name in file_liste:
        # Extrahiere die KW-Woche aus dem Dateinamen
        kw = file_name[40:44]

        # Extrahiere den Dateityp (Dateiendung) aus dem ursprünglichen Dateinamen
        dateityp = os.path.splitext(file_name)[1]

        # Neuer Dateiname
        new_file_name = f"Berichtsheft_2023 {kw}_Anatoliy_Danilov{dateityp}"
        # Überprüfe, ob die Datei bereits existiert
        if not os.path.exists(os.path.join(pfad, new_file_name)):
            # Umbenennung der Dateien
            os.rename(os.path.join(pfad, file_name), os.path.join(pfad, new_file_name))
        else:
            print(f"Datei: {new_file_name} existiert bereits!")
    print("Dateien wurden erfolgreich umbenannt!")


def ausgabe():
    # Dateien in im angegeben Ordner durchlaufen und in der Liste Speichern
    file_liste = os.listdir(pfad)

    # Durchlaufe der Liste durch
    for file_name in file_liste:
        print("Dateiname: | ", file_name)


# Pfad zum Ordner der Dateien die Umbenannt werden müssen
pfad = "C:\\Users\\ARHITEKTOR\\Desktop\\Berichtsheft"


try:
    umbenennen()
    ausgabe()
except FileNotFoundError:
    print(f"Das System kann den angegebenen Pfad nicht finden:", pfad)
