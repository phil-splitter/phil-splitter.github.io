import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def main():
    # Dieses Muster findet src="www.phil-splitter.com/ und href="www.phil-splitter.com/
    muster = re.compile(r'(src|href)="www\.phil-splitter\.com/', re.IGNORECASE)
    
    dateien_geaendert = 0
    ersetzungen_gesamt = 0

    print("Repariere Java-Boxen und Asset-Pfade...")

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm')):
                datei_pfad = os.path.join(root, file)
                
                try:
                    with open(datei_pfad, 'r', encoding='iso-8859-1') as f:
                        content = f.read()
                except Exception:
                    continue

                if "%www.phil-splitter.com/" in content or "www.phil-splitter.com/" in content:
                    # Zähle die Vorkommen für den Bericht
                    anzahl = len(muster.findall(content))
                    if anzahl > 0:
                        # Ersetze durch den absoluten Root-Pfad /
                        content = muster.sub(r'\1="/', content)
                        
                        with open(datei_pfad, 'w', encoding='iso-8859-1') as f:
                            f.write(content)
                        
                        dateien_geaendert += 1
                        ersetzungen_gesamt += anzahl

    print("=" * 50)
    print("Java-Box-Reparatur abgeschlossen!")
    print(f"-> {dateien_geaendert} Dateien wurden repariert.")
    print(f"-> {ersetzungen_gesamt} Pfade wurden auf den Domain-Root umgestellt.")
    print("=" * 50)

if __name__ == "__main__":
    main()
