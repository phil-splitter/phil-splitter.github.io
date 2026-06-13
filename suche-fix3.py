import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def biege_such_button_um():
    print("Suche nach alten Such-Links (.../suche.html) und biege sie auf Google um...")
    
    # Das Ziel ist die direkte Google-Suche für Ihr GitHub-Archiv
    neues_ziel = 'href="https://www.google.com/search?q=site:phil-splitter.github.io"'
    
    # Dieser reguläre Ausdruck findet Links auf 'suche.html' oder 'suche.htm',
    # egal ob ein langer Pfad davor steht oder nicht.
    such_link_muster = re.compile(r'href="[^"]*suche\.(html|htm)"', re.IGNORECASE)
    
    dateien_korrigiert = 0

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm')):
                datei_pfad = os.path.join(root, file)
                
                try:
                    with open(datei_pfad, 'r', encoding='utf-8', errors='ignore') as f:
                        inhalt = f.read()
                    
                    if such_link_muster.search(inhalt):
                        # Ersetzen des alten Links durch den direkten Google-Suchlink
                        neuer_inhalt = such_link_muster.sub(neues_ziel, inhalt)
                        
                        with open(datei_pfad, 'w', encoding='utf-8') as f:
                            f.write(neuer_inhalt)
                        
                        dateien_korrigiert += 1
                        print(f"Button repariert in: {file}")
                        
                except Exception as e:
                    print(f"Fehler bei Datei {file}: {e}")

    print("=" * 50)
    print(f"Fertig! Der Such-Button wurde in {dateien_korrigiert} Dateien repariert.")
    print("=" * 50)

if __name__ == "__main__":
    biege_such_button_um()
