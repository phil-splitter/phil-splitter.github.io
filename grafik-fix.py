import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def main():
    # Dieses Muster findet die Domain gefolgt von assets/ oder html/, 
    # egal ob in src, href oder nackt im JavaScript-Code.
    muster = re.compile(r'www\.phil-splitter\.com/(assets|html)/', re.IGNORECASE)
    
    dateien_geaendert = 0
    ersetzungen_gesamt = 0

    print("Starte Tiefenreinigung der Menü- und Grafikpfade...")

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm')):
                datei_pfad = os.path.join(root, file)
                
                try:
                    with open(datei_pfad, 'r', encoding='iso-8859-1') as f:
                        content = f.read()
                except Exception:
                    continue

                if muster.search(content):
                    anzahl = len(muster.findall(content))
                    # Ersetzt die Domain durch den absoluten Root-Pfad /assets/ oder /html/
                    content = muster.sub(r'/\1/', content)
                    
                    with open(datei_pfad, 'w', encoding='iso-8859-1') as f:
                        f.write(content)
                    
                    dateien_geaendert += 1
                    ersetzungen_gesamt += anzahl

    print("=" * 50)
    print("Grafik-Sanierung erfolgreich abgeschlossen!")
    print(f"-> {dateien_geaendert} Dateien wurden tiefengereinigt.")
    print(f"-> {ersetzungen_gesamt} versteckte Grafik-Pfade wurden korrigiert.")
    print("=" * 50)

if __name__ == "__main__":
    main()
