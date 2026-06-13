import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def umkodieren():
    print("Starte Umkodierung nach UTF-8...")
    
    # Meta-Tag für UTF-8
    meta_utf8 = '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
    meta_muster = re.compile(r'<meta[^>]+charset=[^>]+>', re.IGNORECASE)

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm')):
                datei_pfad = os.path.join(root, file)
                
                try:
                    # 1. Datei im alten Format lesen
                    with open(datei_pfad, 'r', encoding='iso-8859-1') as f:
                        inhalt = f.read()
                    
                    # 2. Meta-Tag anpassen
                    neuer_inhalt = meta_muster.sub(meta_utf8, inhalt)
                    
                    # 3. Datei im neuen Format speichern
                    with open(datei_pfad, 'w', encoding='utf-8') as f:
                        f.write(neuer_inhalt)
                        
                except Exception as e:
                    print(f"Fehler bei {file}: {e}")

    print("Alle Dateien wurden nach UTF-8 konvertiert.")

if __name__ == "__main__":
    umkodieren()
