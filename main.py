# Modul zum Operieren mit dem Operation System
import os

# Pfad zum Ordner, wo sich dateien zum unebenen Befinden
pfad = "C:\\Users\\ARHITEKTOR\\Desktop\\BERICHTSHEFT"

# Dateien in im angegeben Ordner durchlaufen und in der Liste Speichern
file_liste = os.listdir(pfad)

# Durchlaufe und nummeriere die Dateien in der Liste durch
for index, name in enumerate(file_liste):
    # Die Nummerierung soll mit einer 1 beginnen, anstatt mit 0.
    index = index + 1

    # Führende Null hinzufügen, wenn der Index nur eine Ziffer hat
    if len(str(index)) == 1:
        index = f"0{index}"
    # Durchnummerierte Ausgabe der Dateien
    print("Nummer:", index, " | ", "Dateiname:", name)
