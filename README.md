# 🛡️ My AdGuard Blocklist

🇮🇹 **[Italiano]**

Benvenuto nel mio repository! Sono un **Cyber Security Engineer (Analyst)** operante nel CERT di un importante ente italiano e questa è la mia blocklist DNS personalizzata, progettata per l'utilizzo con **AdGuard Home** (o Pi-hole). L'obiettivo di questa lista è erigere un muro digitale a livello di rete per respingere minacce informatiche, spam e tentativi di aggiramento del DNS locale.

### ⚙️ Metodologia di Blocco (Sintassi Wildcard Estesa)
Per garantire la massima efficacia e non lasciare alcun "punto cieco" agli attaccanti, le regole all'interno di questa lista sono strutturate seguendo una logica di blocco estremamente restrittiva, formattata nel seguente modo: `||*.sitodabloccare.net^$important`

* 🌐 **L'aggiunta del `*.` (Wildcard Totale):** Oltre alla sintassi base Adblock (`||`), l'inserimento esplicito dell'asterisco assicura che il motore DNS abbatta chirurgicamente non solo il dominio principale, ma **qualsiasi sottodominio** generato dinamicamente (es. `api.sito.net`, `c2.server.sito.net`, `mail.sito.net`). È una misura essenziale contro le infrastrutture malware che cambiano rapidamente i sottodomini.
* 🛑 **Il carattere finale `$important` (Deny Assoluto):** Questa è l'applicazione di una policy "Zero Trust". Il modificatore `$important` impone ad AdGuard di dare priorità massima e assoluta a questa regola, **sovrascrivendo e annullando qualsiasi regola di whitelist** o eccezione presente in altre liste meno restrittive attive sulla rete. Se un dominio (o un TLD) è in questa lista, il suo traffico viene droppato senza eccezioni.

### 🎯 Cosa blocca questa lista?
* 🌍 **Geoblocking (TLD):** Oscuramento totale delle estensioni di dominio dei paesi statisticamente più usati per attacchi statali, botnet e malware (es. `||*.ru^$important`, `||*.cn^$important`, `.ir`, `.kp`, `.by`).
* 🗑️ **Spam & Truffe:** Blocco alla radice dei domini "economici" utilizzati massicciamente per campagne di phishing ed email truffa (`.top`, `.gdn`, `.xyz`).
* 🔒 **Anti-Bypass DNS (DoH / Private Relay):** Blocco dei *Canary Domains* di Firefox, Chrome e Apple iCloud, costringendo i client a non evadere il controllo locale.

### 🚀 Come usarla
1. Apri il tuo pannello di **AdGuard Home**.
2. Vai su **Filtri** -> **DNS Blocklists** -> **Aggiungi blocco** -> **Aggiungi una lista personalizzata**.
3. Inserisci un nome a tua scelta e incolla il link RAW di questa repository:
   `https://raw.githubusercontent.com/baliano1/my-adguard-blocklist/main/filtri-personali.txt`

⚠️ **Attenzione:** L'aggressività di questa lista (in particolare il blocco totale di alcuni TLD) potrebbe impedire il corretto funzionamento di dispositivi IoT o acquisti su siti specifici. Controlla il tuo Query Log in AdGuard per individuare eventuali falsi positivi.

---

🇬🇧 **[English]**

Welcome to my repository! I am a **Cyber Security Engineer (Analyst)** working at the CERT of a major Italian entity, and this is my custom DNS blocklist, built for **AdGuard Home** (or Pi-hole). The goal of this list is to deploy a network-wide digital shield to block cyber threats, spam, and local DNS bypass attempts.

### ⚙️ Blocking Methodology (Extended Wildcard Syntax)
To ensure maximum efficacy and leave no blind spots for threat actors, the rules in this list are structured using a highly restrictive blocking logic, formatted as follows: `||*.malicious-site.net^$important`

* 🌐 **The addition of `*.` (Total Wildcard):** In addition to the basic Adblock syntax (`||`), the explicit insertion of the asterisk ensures that the DNS engine surgically drops not only the root domain but **any dynamically generated subdomain** (e.g., `api.site.net`, `c2.server.site.net`, `mail.site.net`). This is a critical countermeasure against malware infrastructures that rapidly rotate subdomains.
* 🛑 **The final `$important` modifier (Absolute Deny):** This enforces a "Zero Trust" policy. The `$important` modifier instructs AdGuard to give absolute, top priority to this rule, **overriding and nullifying any whitelist rule** or exception from other, less restrictive lists active on the network. If a domain (or TLD) is on this list, its traffic is dropped without exception.

### 🎯 What does this list block?
* 🌍 **Geoblocking (TLD):** Complete blackout of Top-Level Domains from countries heavily associated with state-sponsored attacks, botnets, and malware (e.g., `||*.ru^$important`, `||*.cn^$important`, `.ir`, `.kp`, `.by`).
* 🗑️ **Spam & Scams:** Root-level blocking of "cheap" domains massively abused for phishing campaigns and scam emails (`.top`, `.gdn`, `.xyz`).
* 🔒 **Anti-DNS Bypass (DoH / Private Relay):** Blocking of *Canary Domains* for browsers and Apple iCloud, forcing clients to obey the local DNS filter.

### 🚀 How to use it
1. Open your **AdGuard Home** dashboard.
2. Go to **Filters** -> **DNS blocklists** -> **Add blocklist** -> **Add a custom list**.
3. Choose a name and paste the RAW link of this repository:
   `https://raw.githubusercontent.com/baliano1/my-adguard-blocklist/main/filtri-personali.txt`

⚠️ **Warning:** The aggressive nature of this list (especially the total blackout of entire TLDs) might break some IoT smart devices or specific online stores. Monitor your AdGuard Query Log to troubleshoot any potential false positives.
