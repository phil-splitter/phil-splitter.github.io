import os
import re

BASE_DIR = "/home/henning/Phil Splitter neu/GitHub"

def harmonisiere_suche():
    print("Harmonisiere alle Suchfelder auf das funktionierende Google-Formular...")
    
    # 1. Das funktionierende Suchformular (exakt aus Ihrem funktionierenden Code)
    gutes_formular = """
    <form action="https://www.google.com/search" method="get" target="_blank" style="margin:0; padding:0;">
        <input type="hidden" name="q" value="site:phil-splitter.github.io">
        <input type="text" name="q" placeholder="Suche..." style="width:120px; font-size:11px;">
        <input type="submit" value="Suchen" style="font-size:11px;">
    </form>
    """
    
    # Reguläre Ausdrücke, um die verschiedenen kaputten Varianten aufzuspüren:
    # a) Alte Google-Skript-Blöcke (cse)
    pattern_script = re.compile(r'<script[^>]*src="[^"]*cse\.google\.com[^"]*"[^>]*>.*?</script>', re.DOTALL | re.IGNORECASE)
    # b) Alte Google-Such-Container (gsc-control...)
    pattern_div = re.compile(r'<div[^>]*class="[^"]*gsc-[^"]*"[^>]*>.*?</div>', re.DOTALL | re.IGNORECASE)
    # c) Spezifische fehlerhafte NetObjects-Suchformulare, die auf lokale Pfade oder cse verweisen
    pattern_old_form = re.compile(r'<form[^>]*action="[^"]*cse\.google[^"]*"[^>]*>.*?</form>', re.DOTALL | re.IGNORECASE)

    dateien_geaendert = 0

    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.html', '.htm')):
                datei_pfad = os.path.join(root, file)
                
                try:
                    with open(datei_pfad, 'r', encoding='utf-8', errors='ignore') as f:
                        inhalt = f.read()
                    
                    alter_inhalt = inhalt
                    
                    # Kaputte Elemente durch das funktionierende Formular ersetzen
                    inhalt = pattern_script.sub('', inhalt)  # Skripte restlos löschen
                    inhalt = pattern_div.sub(gutes_formular, inhalt)  # Container ersetzen
                    inhalt = pattern_old_form.sub(gutes_formular, inhalt)  # Alte Formulare ersetzen
                    
                    # Nur speichern, wenn sich wirklich etwas geändert hat
                    if inhalt != alter_inhalt:
                        with open(datei_pfad, 'w', encoding='utf-8') as f:
                            f.write(inhalt)
                        dateien_geaendert += 1
                        print(f"Suche erfolgreich harmonisiert: {file}")
                        
                except Exception as e:
                    print(f"Fehler bei Datei {file}: {e}")

    print("=" * 50)
    print(f"Fertig! Die funktionierende Suche wurde in {dateien_geaendert} Dateien integriert.")
    print("=" * 50)

if __name__ == "__main__":
    harmonisiere_suche()
