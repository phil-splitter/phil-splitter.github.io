import os

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def fixe_such_ordner():
    print("Starte Sanierung des Such-Unterordners...")
    
    # Der Inhalt für die Weiterleitung
    weiterleitung = """
    <!DOCTYPE HTML>
    <html>
    <head>
        <meta http-equiv="refresh" content="0; url=https://www.google.com/search?q=site:phil-splitter.github.io">
    </head>
    <body>
        <p>Sie werden zur Suche weitergeleitet...</p>
    </body>
    </html>
    """
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Wir prüfen, ob der Ordner 'Suche' (oder 'suche') im Pfad vorkommt
        if "suche" in root.lower():
            for file in files:
                if file.endswith(('.html', '.htm')):
                    datei_pfad = os.path.join(root, file)
                    with open(datei_pfad, 'w', encoding='utf-8') as f:
                        f.write(weiterleitung)
                    print(f"Suchseite {file} auf Google umgeleitet.")

    print("Alle Seiten im Ordner 'Suche' leiten nun auf Google um.")

if __name__ == "__main__":
    fixe_such_ordner()
