import os

# Bitte hier wieder den exakten Pfad zu Ihrer Religions-HTML-Datei eintragen
DATEI_PFAD = "/home/henning/Phil Splitter neu/GitHub/hegel.religion.phil-splitter.com/index.html"

def rette_scharfes_s():
    print(f"Ersetze einsame 'Ã' durch 'ß' in: {DATEI_PFAD}")
    
    if not os.path.exists(DATEI_PFAD):
        print("Fehler: Datei nicht gefunden! Bitte Pfad prüfen.")
        return

    try:
        # Wir öffnen die Datei sicher im UTF-8-Modus und ignorieren defekte Bytes
        with open(DATEI_PFAD, 'r', encoding='utf-8', errors='ignore') as f:
            inhalt = f.read()
        
        # Das einsame 'Ã' wird durch das korrekte 'ß' ersetzt
        if "Ã" in inhalt:
            neuer_inhalt = inhalt.replace("Ã", "ß")
            
            with open(DATEI_PFAD, 'w', encoding='utf-8') as f:
                f.write(neuer_inhalt)
            print("Erfolg! Das einsame 'Ã' wurde erfolgreich zum 'ß' bekehrt.")
        else:
            print("Kein freistehendes 'Ã' mehr in der Datei gefunden.")
            
    except Exception as e:
        print(f"Fehler bei der Verarbeitung: {e}")

if __name__ == "__main__":
    rette_scharfes_s()
