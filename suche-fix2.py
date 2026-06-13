import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def finaler_archivar():
    print("Starte die endgültige Korrektur für Suche und Text...")
    
    # 1. Regulärer Ausdruck für den Grafik-Suchbutton
    # Sucht nach Links, die auf die alte Google-Suche verweisen
    such_link_muster = re.compile(r'href="[^"]*cse\.google\.com[^"]*"', re.IGNORECASE)
    neues_such_ziel = 'href="https://www.google.com/search?q=site:phil-splitter.github.io"'

    # 2. Präzises Umlaut-Wörterbuch (ersetzt nur die exakten Paare, keine Einzelzeichen!)
    umlaut_paare = {
        'Ã¤': 'ä', 'Ã¶': 'ö', 'Ã¼': 'ü',
        'Ã„': 'Ä', 'Ã–': 'Ö', 'Ãœ': 'Ü',
        'ÃŸ': 'ß'
    }

    dateien_geaendert = 0

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm')):
                datei_pfad = os.path.join(root, file)
                
                try:
                    with open(datei_pfad, 'r', encoding='utf-8', errors='ignore') as f:
                        inhalt = f.read()
                    
                    alter_inhalt = inhalt
                    
                    # A) Such-Links korrigieren (aus cse.google wird die direkte Google-Suche)
                    inhalt = such_link_muster.sub(neues_such_ziel, inhalt)
                    
                    # B) Präzise Umlautkorrektur (nur wenn das Paar komplett ist)
                    for falsch, richtig in list(umlaut_paare.items()):
                        inhalt = inhalt.replace(falsch, richtig)
                    
                    # Nur speichern, wenn eine Reparatur stattgefunden hat
                    if inhalt != alter_inhalt:
                        with open(datei_pfad, 'w', encoding='utf-8') as f:
                            f.write(inhalt)
                        dateien_geaendert += 1
                        print(f"Repariert: {file}")
                        
                except Exception as e:
                    print(f"Fehler in {file}: {e}")

    print(f"\nFertig! {dateien_geaendert} Dateien wurden erfolgreich korrigiert.")

if __name__ == "__main__":
    finaler_archivar()
