# 🛡️ My AdGuard Blocklist

🇮🇹 [Italiano]
Benvenuto nel mio repository! Sono un Cyber Security Engineer (Analyst) operante nel CERT di un importante ente italiano e questa è la mia blocklist DNS personalizzata, progettata per l'utilizzo con AdGuard Home (o Pi-hole). L'obiettivo di questa lista è erigere un muro digitale a livello di rete per respingere minacce informatiche, spam e tentativi di aggiramento del DNS locale.

🤖 Automazione & Threat Intelligence (OSINT)
A differenza delle liste statiche, questo repository integra un workflow DevSecOps automatizzato tramite GitHub Actions. Ogni 3 ore, un motore Python interroga database globali di Threat Intelligence per mantenere la protezione aggiornata contro le minacce "zero-day".

Le fonti integrate includono:

Abuse.ch (URLhaus): Identificazione in tempo reale di domini che distribuiscono malware.

Abuse.ch (ThreatFox): Tracciamento delle infrastrutture di Comando e Controllo (C2).

OpenPhish: Rilevamento di campagne di phishing attive nelle ultime ore.

Tutti i domini estratti vengono automaticamente validati e formattati con la nostra sintassi restrittiva.

⚙️ Metodologia di Blocco (Sintassi Wildcard Estesa)
Per garantire la massima efficacia, le regole seguono una logica di blocco estremamente restrittiva: ||*.sitodabloccare.net^$important

🌐 L'aggiunta del *. (Wildcard Totale): Assicura che il motore DNS abbatta non solo il dominio principale, ma qualsiasi sottodominio (es. api.sito.net, c2.server.sito.net). Essenziale contro i malware che cambiano rapidamente host.

🛑 Il modificatore $important (Deny Assoluto): Applica una policy Zero Trust. Impone ad AdGuard di dare priorità massima a questa regola, sovrascrivendo qualsiasi whitelist o eccezione presente in altre liste meno restrittive.

🎯 Cosa blocca questa lista?
🌍 Geoblocking (TLD): Oscuramento totale delle estensioni di dominio dei paesi statisticamente più usati per attacchi statali e botnet (es. .ru, .cn, .ir, .kp, .by).

🗑️ Spam & Truffe: Blocco dei domini "economici" usati per phishing (.top, .gdn, .xyz).

🔒 Anti-Bypass DNS (DoH / Private Relay): Blocco dei Canary Domains per impedire ai client di evadere il controllo locale.

🦠 Dynamic OSINT Feed: Blocchi dinamici basati su segnalazioni CERT internazionali e database Abuse.ch (aggiornati ogni 3 ore).

🚀 Come usarla
Apri il pannello di AdGuard Home.

Vai su Filtri -> DNS Blocklists -> Aggiungi blocco -> Aggiungi una lista personalizzata.

Incolla il link RAW: https://raw.githubusercontent.com/baliano1/my-adguard-blocklist/main/filtri-personali.txt

⚠️ Attenzione: L'aggressività della lista potrebbe causare falsi positivi su alcuni dispositivi IoT. Controlla il Query Log in caso di problemi.

🇬🇧 [English]
Welcome! I am a Cyber Security Engineer (Analyst) working at the CERT of a major Italian entity. This is my custom DNS blocklist for AdGuard Home (or Pi-hole), designed to deploy a network-wide shield against cyber threats and DNS bypass attempts.

🤖 Automation & Threat Intelligence (OSINT)
This repository features a DevSecOps workflow powered by GitHub Actions. Every 3 hours, a Python engine fetches and processes Indicators of Compromise (IoC) from global Threat Intel databases:

Abuse.ch (URLhaus): Real-time malware distribution domains.

Abuse.ch (ThreatFox): Command and Control (C2) infrastructure tracking.

OpenPhish: Zero-day phishing campaign detection.

All extracted domains are automatically validated and formatted according to our restrictive syntax.

⚙️ Blocking Methodology (Extended Wildcard Syntax)
Rules use a highly restrictive logic: ||*.malicious-site.net^$important

🌐 The *. (Total Wildcard): Ensures the DNS engine drops the root domain and all subdomains (e.g., api.site.net, c2.server.site.net). Critical against malware domain rotation.

🛑 The $important modifier (Absolute Deny): Enforces a Zero Trust policy, overriding any whitelist or exception from less restrictive lists active on the network.

🎯 What does this list block?
🌍 Geoblocking (TLD): Complete blackout of Top-Level Domains associated with state-sponsored attacks (e.g., .ru, .cn, .ir, .kp, .by).

🗑️ Spam & Scams: Root-level blocking of "cheap" domains abused for phishing (.top, .gdn, .xyz).

🔒 Anti-DNS Bypass (DoH / Private Relay): Canary Domain blocking to force clients to obey local DNS filters.

🦠 Dynamic OSINT Feed: Real-time blocks based on international CERT reports and Abuse.ch databases (updated every 3 hours).

🚀 How to use it
Open your AdGuard Home dashboard.

Go to Filters -> DNS blocklists -> Add blocklist -> Add a custom list.

Paste the RAW link: https://raw.githubusercontent.com/baliano1/my-adguard-blocklist/main/filtri-personali.txt

⚠️ Warning: The aggressive nature of this list may break some IoT devices. Monitor your Query Log to troubleshoot potential false positives.
