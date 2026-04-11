# 🛡️ My AdGuard Blocklist

🇮🇹 [Italiano]

Benvenuto nel mio repository! Sono un Cyber Security Engineer (Analyst) operante nel CERT di un importante ente italiano e questa è la mia blocklist DNS personalizzata, progettata per l'utilizzo con AdGuard Home (o Pi-hole). L'obiettivo di questa lista è erigere un muro digitale a livello di rete per respingere minacce informatiche, spam e tentativi di aggiramento del DNS locale.

⚙️ Metodologia di Blocco (Sintassi)

Per garantire la massima efficacia, questa lista utilizza regole progettate per non lasciare vie di fuga:

🌐 Copertura Totale dei Sottodomini (||dominio^): Tutte le regole utilizzano la sintassi Adblock ||, che equivale a un blocco di tipo wildcard *.. Questo significa che bloccando un dominio (es. ru), verranno automaticamente neutralizzati anche tutti i suoi infiniti sottodomini (es. api.sito.ru, c2.server.ru, mail.sito.ru).

🛑 Deny Assoluto ($important): Ogni regola termina con il modificatore $important. In ambito di sicurezza informatica, questo impone una policy di blocco tassativa. La regola ottiene la priorità massima nel motore DNS, ignorando qualsiasi eccezione (whitelist) o regola permissiva presente in altre liste meno restrittive installate sul server.

🎯 Cosa blocca questa lista?

🌍 Geoblocking (TLD): Oscuramento totale delle estensioni di dominio dei paesi statisticamente più usati per attacchi statali, botnet e malware (.ru, .cn, .ir, .kp, .by).

🗑️ Spam & Truffe: Blocco alla radice dei domini "economici" utilizzati massicciamente per campagne di phishing ed email truffa (.top, .gdn, .xyz).

🔒 Anti-Bypass DNS (DoH / Private Relay): Blocco dei Canary Domains di Firefox, Chrome e Apple iCloud. Questo costringe i browser e i dispositivi a non utilizzare tunnel crittografati privati, obbligandoli a passare sempre per il filtro DNS locale di AdGuard.

🚀 Come usarla

Apri il tuo pannello di AdGuard Home.

Vai su Filtri -> DNS Blocklists -> Aggiungi blocco -> Aggiungi una lista personalizzata.

Inserisci un nome a tua scelta e incolla il link RAW di questa repository:
https://raw.githubusercontent.com/baliano1/my-adguard-blocklist/main/filtri-personali.txt
(Assicurati di sostituire "filtri-personali.txt" con il nome esatto del tuo file).

⚠️ Attenzione: Il blocco totale di alcuni TLD (come .cn o .ru) potrebbe impedire il corretto funzionamento di dispositivi di domotica o acquisti su siti specifici. Controlla il tuo Query Log e sblocca (whitelist) manualmente i domini necessari in caso di problemi.

🇬🇧 [English]

Welcome to my repository! I am a Cyber Security Engineer (Analyst) working at the CERT of a major Italian entity, and this is my custom DNS blocklist, built for AdGuard Home (or Pi-hole). The goal of this list is to deploy a network-wide digital shield to block cyber threats, spam, and local DNS bypass attempts.

⚙️ Blocking Methodology (Syntax)

To ensure maximum efficacy, this list employs strict filtering rules designed to leave no blind spots:

🌐 Wildcard Subdomain Coverage (||domain^): All rules use the Adblock syntax ||, which acts as a *. wildcard block. This ensures that by blocking a root domain (e.g., ru), every single subdomain associated with it (e.g., api.site.ru, c2.server.ru, mail.site.ru) is automatically intercepted and neutralized.

🛑 Strict Deny ($important): Every rule is appended with the $important modifier. In a cybersecurity context, this enforces a strict drop policy. The rule is granted absolute priority within the DNS engine, overriding any local whitelists or conflicting allowed rules from other, less restrictive blocklists running on your server.

🎯 What does this list block?

🌍 Geoblocking (TLD): Complete blackout of Top-Level Domains from countries heavily associated with state-sponsored attacks, botnets, and malware (.ru, .cn, .ir, .kp, .by).

🗑️ Spam & Scams: Root-level blocking of "cheap" domains massively abused for phishing campaigns and scam emails (.top, .gdn, .xyz).

🔒 Anti-DNS Bypass (DoH / Private Relay): Blocking of Canary Domains for Firefox, Chrome, and Apple iCloud. This forces browsers and mobile devices to disable private encrypted tunnels and strictly obey the local AdGuard DNS filter.

🚀 How to use it

Open your AdGuard Home dashboard.

Go to Filters -> DNS blocklists -> Add blocklist -> Add a custom list.

Choose a name and paste the RAW link of this repository:
https://raw.githubusercontent.com/baliano1/my-adguard-blocklist/main/filtri-personali.txt
(Make sure to replace "filtri-personali.txt" with your exact file name).

⚠️ Warning: The aggressive blocking of entire TLDs (like .cn or .ru) might break some smart home IoT devices or specific online stores. Check your Query Log and manually whitelist the necessary domains if you experience any breakage.
