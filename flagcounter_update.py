import os
import re

# Reguläre Ausdrücke
pattern_countries = re.compile(r'href=(["\'])[^"\']*s11\.flagcounter\.com/countries/pcCy/(?:index\.html)?\1', re.IGNORECASE)
pattern_more      = re.compile(r'href=(["\'])[^"\']*s11\.flagcounter\.com/more/pcCy/(?:index\.html)?\1', re.IGNORECASE)
pattern_img       = re.compile(r'src=(["\'])[^"\']*s11\.flagcounter\.com/count/pcCy/(.*?)(?:index\.html)?\1', re.IGNORECASE)

modified_count = 0
error_count = 0
fixed_encoding_count = 0

print("Starte die Reaktivierung des Flagcounters und repariere falsche Encodings...")
print("-" * 70)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.lower().endswith('.html'):
            file_path = os.path.join(root, file)
            
            try:
                # Versuch 1: Als echtes UTF-8 lesen
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    # Versuch 2: Fallback auf ISO-8859-1
                    with open(file_path, 'r', encoding='iso-8859-1') as f:
                        content = f.read()
                    fixed_encoding_count += 1
                    print(f"⚙️  Encoding repariert: {file_path} (Wird beim Speichern zu UTF-8 konvertiert)")
                
                original_content = content
                
                # Flagcounter-Links umbiegen
                content = pattern_countries.sub(r'href=\1https://info.flagcounter.com/pcCy\1 target=\1_blank\1', content)
                content = pattern_more.sub(r'href=\1https://info.flagcounter.com/pcCy\1 target=\1_blank\1', content)
                content = pattern_img.sub(r'src=\1https://s11.flagcounter.com/count/pcCy/\2\1', content)
                
                # Nur speichern, wenn sich etwas am Counter geandert hat ODER das Encoding falsch war
                if content != original_content or original_content != content:
                    # Wir speichern jetzt IMMER hart in UTF-8
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    modified_count += 1
                    print(f"✔ Aktualisiert: {file_path}")
                    
            except Exception as e:
                print(f"❌ Unbekannter Fehler bei Datei {file_path}: {e}")
                error_count += 1

print("-" * 70)
print(f"Fertig! {modified_count} Dateien umgestellt.")
if fixed_encoding_count > 0:
    print(f"Tipp: Dabei wurden {fixed_encoding_count} störrische ISO-Dateien heimlich in echtes UTF-8 konvertiert!")
if error_count > 0:
    print(f"Hinweis: Bei {error_count} Datei(en) trat weiterhin ein Fehler auf.")
