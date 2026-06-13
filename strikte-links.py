import os

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def pruefe_links():
    print("Starte strikte Prüfung: Existiert die Zieldatei physisch?")
    
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm')):
                datei_pfad = os.path.join(root, file)
                
                # Wir lesen die Datei Zeile für Zeile, um Links zu finden
                with open(datei_pfad, 'r', encoding='iso-8859-1') as f:
                    for line in f:
                        if 'href=' in line:
                            # Extrahiere Pfade aus href="..."
                            teile = line.split('href="')[1:]
                            for teil in teile:
                                ziel = teil.split('"')[0]
                                
                                # Ignoriere externe oder Anker-Links
                                if ziel.startswith(('http', 'mailto', '#')):
                                    continue
                                
                                # Wandle relativen Pfad in absoluten Festplattenpfad um
                                target_abs = os.path.normpath(os.path.join(root, ziel))
                                
                                if not os.path.exists(target_abs):
                                    print(f"TOTER LINK gefunden in {file}: {ziel}")

if __name__ == "__main__":
    pruefe_links()
