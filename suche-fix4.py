import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub" # Prüfen Sie ggf. das doppelte /home/ im Pfad, falls Tippfehler

def finaler_javascript_bieger():
    print("Werfe das Netz an der JavaScript-Stelle aus...")
    
    neues_ziel = "https://www.google.com/search?q=site:phil-splitter.github.io"
    
    # Wir suchen nach dem Pfad zur alten Suche, egal in welchen Anführungszeichen 
    # und unabhängig davon, wie viele '../' oder 'www...' davorstehen.
    js_such_muster = re.compile(r'[\'"][^\'"]*suche\.(html|htm)[\'"]', re.IGNORECASE)
    
    dateien_korrigiert = 0

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm', '.js')): # Wir nehmen .js Dateien sicherheitshalber mit!
                datei_pfad = os.path.join(root, file)
                
                try:
                    with open(datei_pfad, 'r', encoding='utf-8', errors='ignore') as f:
                        inhalt = f.read()
                    
                    if js_such_muster.search(inhalt):
                        # Wir ersetzen den kompletten String (inklusive der Anführungszeichen)
                        # und setzen das neue Ziel in dieselben Anführungszeichen
                        neuer_inhalt = js_such_muster.sub(f"'{neues_ziel}'", inhalt)
                        
                        with open(datei_pfad, 'w', encoding='utf-8') as f:
                            f.write(neuer_inhalt)
                        
                        dateien_korrigiert += 1
                        print(f"JavaScript-Logik geheilt in: {file}")
                        
                except Exception as e:
                    print(f"Fehler bei Datei {file}: {e}")

    print("=" * 50)
    print(f"Fang abgeschlossen! {dateien_korrigiert} Dateien wurden auf JavaScript-Ebene korrigiert.")
    print("=" * 50)

if __name__ == "__main__":
    finaler_javascript_bieger()
