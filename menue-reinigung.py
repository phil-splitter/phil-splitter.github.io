import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def main():
    # Findet alle Varianten der alten Domain vor assets/ oder html/
    muster = re.compile(r'www\.phil-splitter\.com/(assets|html)/', re.IGNORECASE)
    
    dateien_geaendert = 0
    ersetzungen_gesamt = 0

    print("Starte globale Tiefenreinigung (HTML, JS, CSS)...")

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            # Jetzt nehmen wir auch .js und .css Dateien mit ins Boot!
            if file.endswith(('.html', '.htm', '.js', '.css')):
                datei_pfad = os.path.join(root, file)
                
                try:
                    with open(datei_pfad, 'r', encoding='iso-8859-1') as f:
                        content = f.read()
                except Exception:
                    continue

                if muster.search(content):
                    anzahl = len(muster.findall(content))
                    content = muster.sub(r'/\1/', content)
                    
                    with open(datei_pfad, 'w', encoding='iso-8859-1') as f:
                        f.write(content)
                    
                    dateien_geaendert += 1
                    ersetzungen_gesamt += anzahl

    print("=" * 50)
    print("Globale Sanierung abgeschlossen!")
    print(f"-> {dateien_geaendert} Dateien (inkl. Skripte) wurden bereinigt.")
    print(f"-> {ersetzungen_gesamt} versteckte Pfade korrigiert.")
    print("=" * 50)

if __name__ == "__main__":
    main()
