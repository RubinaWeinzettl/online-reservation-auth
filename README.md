📘 Auth Service – Online Reservierung

Identity & Authentication für ein Microservice-basiertes Reservierungssystem

🌿 Über dieses Repository

Dieses Repository enthält den Auth Service für mein Portfolio-Projekt Online Reservierung.
Der Service ist als eigener Microservice umgesetzt und dient als Einstiegspunkt in die Themen:

Authentifizierung

Autorisierung

Rollenmodelle (RBAC)

Token-basierte Identität

Service-übergreifende Sicherheit

Das Projekt begleitet mich in meiner Lernreise in Richtung Microservices, FastAPI und moderner Webarchitektur.

🎯 Aufgaben des Auth Services

Der Auth-Service übernimmt alle Funktionen rund um Benutzeridentität und Zugangskontrolle. Dazu gehören:

✔ Registrierung

Erstellen eines neuen Accounts

Speicherung des Passwort-Hashes

Initiale Zuweisung einer Benutzerrolle (z. B. customer)

✔ Login

Validierung von E-Mail + Passwort

Ausgabe eines JWT Access Tokens

Ausgabe eines optionalen Refresh Tokens (später)

✔ Rollen & Claims

Speicherung der Rolle des Users

Übergabe der Rolle im JWT (z. B. role=customer, role=business)

Grundlage für Weiterleitung in das passende Frontend

✔ Token-Verifizierung

Endpunkt zum Validieren bestehender Tokens

Wird von den beiden BFFs (Business & Customer) verwendet

✔ Weiterleitung / Frontend-Erkennung

Nach dem Login wird entschieden, welches UI der Benutzer sieht

Customer-Frontend

Business-Frontend

(Der eigentliche Redirect passiert auf Clientseite – der Auth-Service liefert nur die Rollen dafür.)

🧱 Teil der Gesamtarchitektur

Der Auth-Service bildet die Basis für alle weiteren Komponenten des Systems.

graph LR
  CFE[Customer Frontend] --> CBFF[Customer BFF]
  BFE[Business Frontend] --> BBFF[Business BFF]

  CBFF -->|Verify Token| AUTH[Auth Service]
  BBFF -->|Verify Token| AUTH

  AUTH --> DBAUTH[(Auth DB)]


Er dient den BFFs als Identity Provider und sorgt dafür, dass Benutzer korrekt authentifiziert und autorisiert werden.

🛠 Technologien

Python

FastAPI

JWT (JSON Web Tokens)

Passlib / bcrypt (Passwort-Hashing)

Pydantic (Validierung)

SQLAlchemy / SQLite oder PostgreSQL

Docker (für lokale Entwicklung)

📄 API Endpunkte (MVP)
Methode	Endpoint	Beschreibung
POST	/register	Erstellt einen neuen Benutzer
POST	/login	Gibt ein JWT Access Token zurück
GET	/me	Gibt Infos über den eingeloggten Benutzer zurück
POST	/verify	Validiert ein Token
GET	/roles/{id}	(optional) Gibt Rolleninfo zurück

Diese Endpunkte können sich im Laufe des Projekts erweitern – beispielsweise um password-reset, token-refresh, oder invite-based registration.

🗂 Datenmodell (Basis)
User
––––––––––––––––
id (UUID)
email
password_hash
role (customer | business | staff | owner | admin)
created_at
updated_at


Später möglich:

Tenant-Beziehungen

Teams / Unternehmen

Multi-Rollen pro User

🚀 Lokale Entwicklung
1. Repository klonen
git clone <REPO_URL>
cd online-reservierung-auth

2. Virtual Environment erstellen
python3 -m venv venv
source venv/bin/activate

3. Dependencies installieren
pip install -r requirements.txt

4. Server starten
uvicorn app.main:app --reload


Der Service läuft anschließend unter:

http://localhost:8000

📚 Was ich mit diesem Service lerne

Grundlagen von Authentifizierung & Autorisierung

Best Practices im Umgang mit JWT

Identity Provider Pattern

Trennung zwischen Auth-Service und Anwendungslogik

Zusammenspiel zwischen BFF und Auth-Service

Sicherer Umgang mit Passwörtern (Hashing, Validation)

Architekturentscheidungen im Microservice-Kontext

🧭 Status

Der Auth-Service befindet sich im aktiven Aufbau.
Neue Funktionen und Sicherheitsmechanismen werden laufend ergänzt.

🤝 Feedback & Austausch

Ich freue mich über Impulse, Verbesserungsvorschläge oder Code-Reviews – besonders rund um Best Practices für Authentifizierung, Token-Sicherheit und FastAPI.
