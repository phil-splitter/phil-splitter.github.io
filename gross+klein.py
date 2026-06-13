import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def main():
    print("Analysiere physische Dateien auf der Festplatte...")
    # Wir erstellen ein Wörterbuch aller existierenden Dateien in Kleinbuchstaben -> echte Schreibweise
    echte_dateien = {}
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            # Merke dir den relativen Pfad in Kleinbuchstaben als Schlüssel
            rel_pfad = os.path.relpath(os.path.join(root, file), BASE_DIR).replace("\\", "/")
            echte_dateien[rel_pfad.lower()] = rel_pfad

    print(f"-> {len(echte_dateien)} physische Dateien registriert.")
    print("Gleiche HTML-Code mit Linux-Dateisystem ab...")

    # Regulärer Ausdruck, um src="..." und href="..." zu finden
    pfad_muster = re.compile(r'(src|href)=["\']([^"\']+)["\']', re.IGNORECASE)
    
    dateien_geaendert = 0
    korrekturen_gesamt = 0

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm', '.js', '.css')):
                datei_pfad = os.path.join(root, file)
                aktuelle_rel_dir = os.path.relpath(root, BASE_DIR).replace("\\", "/")
                
                try:
                    with open(datei_pfad, 'r', encoding='iso-8859-1') as f:
                        inhalt = f.read()
                except Exception:
                    continue

                def ersetzungs_funktion(match):
                    nonlocal korrekturen_gesamt
                    attribut = match.group(1)
                    pfad = match.group(2)
                    
                    # Ignoriere externe Links
                    if pfad.startswith(('http', 'https', 'mailto', 'ftp', 'whatsapp')):
                        return match.group(0)
                    
                    # Berechne den mutmaßlichen Pfad ab dem Hauptverzeichnis (Root)
                    sauberer_pfad = pfad.lstrip('/')
                    
                    # Falls der Pfad relativ ist (z.B. html/fusion.css oder ../assets/...)
                    if pfad.startswith('.'):
                        # Einfache Pfad-Auflösung
                        kombiniert = os.path.normpath(os.path.join(aktuelle_rel_dir, pfad)).replace("\\", "/")
                        sauberer_pfad = kombiniert.lstrip('/')
                    elif not aktuelle_rel_dir == '.' and not pfad.startswith('assets') and not pfad.startswith('html'):
                        # Falls in einem Unterordner und direkt aufgerufen
                        kombiniert = os.path.normpath(os.path.join(aktuelle_rel_dir, pfad)).replace("\\", "/")
                        sauberer_pfad = kombiniert.lstrip('/')
                    else:
                        sauberer_pfad = sauberer_pfad
                    
                    schluessel = sauberer_pfad.lower()
                    
                    if schluessel in echte_dateien:
                        exakter_physischer_pfad = echte_dateien[schluessel]
                        
                        # Wenn der Pfad im Code anders geschrieben ist als auf der Festplatte:
                        if sauberer_pfad != exakter_physischer_pfad:
                            korrekturen_gesamt += 1
                            # Behalte die ursprüngliche Struktur bei (absolut / oder relativ)
                            if pfad.startswith('/'):
                                return f'{attribut}="/{exakter_physischer_pfad}"'
                            elif pfad.startswith('.'):
                                # Relativen Bezug wiederherstellen ist komplex, wir biegen es auf absolut um, da das serverfest ist!
                                return f'{attribut}="/{exakter_physischer_pfad}"'
                            else:
                                return f'{attribut}="/{exakter_physischer_pfad}"'
                    
                    return match.group(0)

                neuer_inhalt = pfad_muster.sub(ersetzungs_funktion, inhalt)
                
                if neuer_inhalt != inhalt:
                    with open(datei_pfad, 'w', encoding='iso-8859-1') as f:
                        f.write(neuer_inhalt)
                    dateien_geaendert += 1

    print("=" * 50)
    print("Case-Sensitivity-Korrektur abgeschlossen!")
    print(f"-> {dateien_geaendert} HTML/JS-Dateien wurden an das Linux-Dateisystem angepasst.")
    print(f"-> {korrekturen_gesamt} falsche Groß-/Kleinschreibungen korrigiert.")
    print("=" * 50)

if __name__ == "__main__":
    main()
