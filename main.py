# Modul zum Operieren mit dem Operation System
import os

# Pfad zum Ordner, wo sich dateien zum unebenen Befinden
pfad = "C:\\Users\\ARHITEKTOR\\Desktop\\BERICHTSHEFT"

# Dateien in im angegeben Ordner durchlaufen und in der Liste Speichern
file_liste = os.listdir(pfad)


def ausgabe():
    # Durchlaufe und nummeriere die Dateien in der Liste durch
    for name in file_liste:
        # Durchnummerierte Ausgabe der Dateien
        print("Dateiname: | ", name)


def umbenennen():
    new_name = "Berichtsheft_2023_KW XY_Anatoliy_Danilov"

    # Durchlaufe und nummeriere die Dateien in der Liste durch
    for index, name in enumerate(file_liste):
        # Die Nummerierung soll mit einer 1 beginnen, anstatt mit 0.
        index = index + 1

        # Führende Null hinzufügen, wenn der Index nur eine Ziffer hat
        if len(str(index)) == 1:
            index = f"0{index}"

        kw = index

        # Umbenennung der Dateien
        os.rename(os.path.join(pfad, name), os.path.join(pfad, f"Berichtsheft_2023_KW {kw}_Anatoliy_Danilov"))

        # Durchnummerierte Ausgabe der Dateien
        print("New_Dateiname:", name)


umbenennen()
