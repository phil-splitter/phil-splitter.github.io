import os

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def repariere_verzeichnis():
    print(f"Durchsuche das gesamte Verzeichnis nach kaputten Umlauten...\nPfad: {BASE_DIR}")
    
    # Das Wörterbuch der typischen Doppel-Kodierungs-Fehler
    ersetzungen = {
        'Ã¤': 'ä', 'Ã¶': 'ö', 'Ã¼': 'ü',
        'Ã„': 'Ä', 'Ã–': 'Ö', 'Ãœ': 'Ü',
        'ÃŸ': 'ß'
    }
    
    dateien_repariert = 0

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            # Wir prüfen nur HTML-Dateien
            if file.endswith(('.html', '.htm')):
                datei_pfad = os.path.join(root, file)
                
                try:
                    with open(datei_pfad, 'r', encoding='utf-8') as f:
                        inhalt = f.read()
                        
                    # Wir prüfen, ob überhaupt einer der kryptischen Strings vorkommt
                    muss_repariert_werden = any(falsch in inhalt for falsch in ersetzungen.keys())
                    
                    if muss_repariert_werden:
                        # Ersetzen aller bekannten Fehler
                        for falsch, richtig in ersetzungen.items():
                            inhalt = inhalt.replace(falsch, richtig)
                            
                        # Überschreiben der Datei mit den reparierten Umlauten
                        with open(datei_pfad, 'w', encoding='utf-8') as f:
                            f.write(inhalt)
                            
                        dateien_repariert += 1
                        print(f"Geheilt: {datei_pfad.replace(BASE_DIR, '')}")
                        
                except Exception as e:
                    print(f"Konnte {file} nicht verarbeiten: {e}")

    print("=" * 50)
    print(f"Großreinemachen abgeschlossen! {dateien_repariert} Dateien wurden repariert.")
    print("=" * 50)

if __name__ == "__main__":
    repariere_verzeichnis()
