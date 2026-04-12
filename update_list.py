import requests
from urllib.parse import urlparse
from datetime import datetime

# Usiamo un 'set' per evitare domini duplicati tra le varie fonti
domini_malevoli = set()

print("Inizio il download dei feed OSINT...")

# --- 1. ABUSE.CH: URLhaus (Malware Distribution) ---
try:
    print("Scaricamento URLhaus...")
    urlhaus_url = "https://urlhaus.abuse.ch/downloads/hostfile/"
    r = requests.get(urlhaus_url, timeout=10)
    for line in r.text.splitlines():
        # Il formato è "127.0.0.1 dominio.com"
        if line.startswith("127.0.0.1") and "localhost" not in line:
            dominio = line.split()[1].strip()
            domini_malevoli.add(dominio)
except Exception as e:
    print(f"Errore URLhaus: {e}")

# --- 2. ABUSE.CH: ThreatFox (C2 Infrastructure) ---
try:
    print("Scaricamento ThreatFox...")
    # Feed CSV con i domini recenti
    threatfox_url = "https://threatfox.abuse.ch/export/csv/domains/recent/"
    r = requests.get(threatfox_url, timeout=10)
    for line in r.text.splitlines():
        if not line.startswith("#") and '","' in line:
            # Estrazione rozza ma efficace della colonna dominio dal CSV
            parti = line.split('","')
            if len(parti) > 2:
                dominio = parti[2].replace('"', '').strip()
                domini_malevoli.add(dominio)
except Exception as e:
    print(f"Errore ThreatFox: {e}")

# --- 3. OPENPHISH (Campagne Phishing Zero-Day) ---
try:
    print("Scaricamento OpenPhish...")
    openphish_url = "https://openphish.com/feed.txt"
    r = requests.get(openphish_url, timeout=10)
    for line in r.text.splitlines():
        if line.startswith("http"):
            # OpenPhish fornisce URL completi, a noi serve solo il dominio radice
            dominio = urlparse(line).netloc
            dominio = dominio.split(':')[0] # Rimuove eventuali porte (es. :8080)
            domini_malevoli.add(dominio)
except Exception as e:
    print(f"Errore OpenPhish: {e}")

# --- SCRITTURA DEL FILE PER ADGUARD ---
print(f"Totale domini unici raccolti: {len(domini_malevoli)}")

with open("osint-feed.txt", "w") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"! --- FEED OSINT AUTOMATICO ---\n")
    file.write(f"! Aggiornato il: {timestamp}\n")
    file.write(f"! Fonti: URLhaus, ThreatFox, OpenPhish\n")
    file.write(f"! Totale IoC: {len(domini_malevoli)}\n")
    file.write(f"! --------------------------------------\n\n")
    
    # Applica la formattazione Zero Trust ordinando in ordine alfabetico
    for dominio in sorted(domini_malevoli):
        # Evitiamo di inserire stringhe vuote o IP diretti se vogliamo solo domini
        if dominio:
            file.write(f"||{dominio}^$important\n")

print("File osint-feed.txt generato con successo!")
