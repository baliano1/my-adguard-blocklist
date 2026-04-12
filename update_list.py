import requests
from urllib.parse import urlparse
from datetime import datetime
import os

# Configurazione
FILE_NAME = "filtri-personali.txt"
MARKER = "! --- START OF AUTOMATED FEED ---"
domini_malevoli = set()

print("Inizio raccolta IoC...")

# --- FEED 1: URLhaus (Malware) ---
try:
    r = requests.get("https://urlhaus.abuse.ch/downloads/hostfile/", timeout=15)
    for line in r.text.splitlines():
        if line.startswith("127.0.0.1") and "localhost" not in line:
            domini_malevoli.add(line.split()[1].strip())
except: print("Errore URLhaus")

# --- FEED 2: ThreatFox (C2) ---
try:
    r = requests.get("https://threatfox.abuse.ch/export/csv/domains/recent/", timeout=15)
    for line in r.text.splitlines():
        if not line.startswith("#") and '","' in line:
            parti = line.split('","')
            if len(parti) > 2:
                domini_malevoli.add(parti[2].replace('"', '').strip())
except: print("Errore ThreatFox")

# --- FEED 3: OpenPhish (Phishing) ---
try:
    r = requests.get("https://openphish.com/feed.txt", timeout=15)
    for line in r.text.splitlines():
        if line.startswith("http"):
            dominio = urlparse(line).netloc.split(':')[0]
            domini_malevoli.add(dominio)
except: print("Errore OpenPhish")

# --- ELABORAZIONE FILE ---
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        linee = f.readlines()
    
    # Cerchiamo dove finisce la tua parte manuale
    nuovo_contenuto = []
    for l in linee:
        nuovo_contenuto.append(l)
        if MARKER in l:
            break
    else:
        # Se il marker non esiste, lo aggiungiamo in fondo
        if nuovo_contenuto and not nuovo_contenuto[-1].endswith("\n"):
            nuovo_contenuto.append("\n")
        nuovo_contenuto.append(MARKER + "\n")

    # Scrittura finale
    with open(FILE_NAME, "w") as f:
        f.writelines(nuovo_contenuto)
        f.write(f"! Ultimo aggiornamento automatico: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Inserimento domini con sintassi richiesta
        for dom in sorted(domini_malevoli):
            if dom and "." in dom: # Verifica minima che sia un dominio
                f.write(f"||*.{dom}^$important\n")

    print(f"File {FILE_NAME} aggiornato con {len(domini_malevoli)} nuovi domini.")
else:
    print(f"Errore: il file {FILE_NAME} non esiste!")
