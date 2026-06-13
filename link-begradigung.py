import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def main():
    # Sucht nach Mustern, die auf die alte Ordnerstruktur verweisen
    # Beispiel: ../../www.phil-splitter.com/philosophie/index.html
    muster = re.compile(r'(?:../../|../)?www\.phil-splitter\.com/', re.IGNORECASE)
    
    print("Begradige die Link-Pfade im Archiv...")
    
    anzahl_dateien = 0
    anzahl_links = 0

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm')):
                datei_pfad = os.path.join(root, file)
                try:
                    with open(datei_pfad, 'r', encoding='iso-8859-1') as f:
                        inhalt = f.read()
                except Exception:
                    continue

                if muster.search(inhalt):
                    # Ersetzt den gesamten Pfad-Müll durch ein einfaches /
                    neuer_inhalt = muster.sub(r'/', inhalt)
                    
                    with open(datei_pfad, 'w', encoding='iso-8859-1') as f:
                        f.write(neuer_inhalt)
                    
                    anzahl_dateien += 1
                    # Zähle, wie oft ersetzt wurde (vereinfacht)
                    anzahl_links += inhalt.count('www.phil-splitter.com/')

    print("=" * 50)
    print(f"Begradigung abgeschlossen!")
    print(f"-> {anzahl_dateien} Dateien wurden angepasst.")
    print(f"-> {anzahl_links} defekte Links wurden repariert.")
    print("=" * 50)

if __name__ == "__main__":
    main()
