import os
import urllib.parse

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def main():
    print("Starte tiefe Dateinamen-Dekodierung auf der Festplatte...")
    
    umbenannt_gesamt = 0

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            # Wir jagen JEDEN Dateinamen durch den URL-Decoder
            # Das verwandelt %5f, %20 etc. in echte Zeichen
            neuer_dateiname = urllib.parse.unquote(file)
            
            # Falls sich der Name durch das Dekodieren verändert hat (z.B. %5f zu _)
            if neuer_dateiname != file:
                alter_pfad = os.path.join(root, file)
                neuer_pfad = os.path.join(root, neuer_dateiname)
                
                try:
                    os.rename(alter_pfad, neuer_pfad)
                    print(f"Erfolgreich dekodiert: {file} -> {neuer_dateiname}")
                    umbenannt_gesamt += 1
                except Exception as e:
                    print(f"Fehler bei {file}: {e}")

    print("=" * 50)
    print("Dekodierungs-Bereinigung abgeschlossen!")
    print(f"-> {umbenannt_gesamt} Dateien wurden physisch korrigiert.")
    print("=" * 50)

if __name__ == "__main__":
    main()
