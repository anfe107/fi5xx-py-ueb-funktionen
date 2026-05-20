# Cheat-Sheet — try / except

Nachschlagewerk für die Fehlerbehandlung bei Eingaben. Deckt nur den Umfang ab, der für die Eingabe-Validierung gebraucht wird.

## Wozu `try` / `except`?

Manche Operationen schlagen zur Laufzeit fehl und lösen einen **Fehler** (eine *Exception*) aus. Klassisches Beispiel: `int()` auf eine Eingabe, die keine Zahl ist.

```python
int("42")       # 42
int("abc")      # ValueError — das Programm bricht ab
```

Ohne Behandlung beendet ein solcher Fehler das Programm sofort. Mit `try`/`except` fangen Sie ihn ab und reagieren kontrolliert.

## Grundform

```python
try:
    zahl = int(eingabe)
except ValueError:
    print("Das war keine ganze Zahl.")
```

- `try:` — Block mit der Operation, die fehlschlagen **kann**.
- `except ValueError:` — läuft nur, wenn im `try`-Block ein `ValueError` auftritt.
- Tritt **kein** Fehler auf, wird der `except`-Block übersprungen.

`ValueError` ist der Fehlertyp, den `int()` bei ungültigem Text auslöst. Man fängt gezielt diesen Typ ab — nicht „alle Fehler".

## Typisches Muster: Eingabe wiederholen, bis sie gültig ist

`try`/`except` kombiniert sich mit `while True … break` (siehe [cheatsheet_schleifen.md](cheatsheet_schleifen.md)) zur robusten Eingabe:

```python
while True:
    eingabe = input("Verschiebung (ganze Zahl): ")
    try:
        zahl = int(eingabe)
        break                       # wird nur bei Erfolg erreicht
    except ValueError:
        print("Bitte eine ganze Zahl eingeben.")

print(zahl)
```

Ablauf: Schlägt `int()` fehl, springt die Ausführung sofort in den `except`-Block — `break` wird übersprungen, die Schleife läuft erneut. Gelingt die Umwandlung, folgt `break` und die Schleife endet.

> Das `break` steht **innerhalb** des `try`-Blocks, direkt nach der Operation, die gelingen muss. So wird es nur bei Erfolg erreicht.

## Was gehört in den `try`-Block?

Nur die Zeile(n), die wirklich fehlschlagen können — hier `int(eingabe)`. Code, der ohnehin nicht scheitert, gehört nicht hinein; sonst verbirgt `except` womöglich einen ganz anderen Fehler.

> **Tellerrand — Python vs. C#/Java:** Das Prinzip ist dasselbe, nur die Schlüsselwörter unterscheiden sich: Python `try`/`except`, C# und Java `try`/`catch`. Der Fehlertyp heißt in Python `ValueError`, in C#/Java z. B. `FormatException` bzw. `NumberFormatException`.

---

## Außerhalb der Baseline

Folgende Konstrukte sind **nicht** Teil der Baseline. Wenn eine Übung sie braucht, führt der Aufgabentext sie ein:

- `except` ohne Typ oder `except Exception` — fängt *alle* Fehler (zu grob)
- mehrere `except`-Zweige für verschiedene Fehlertypen
- `else`- und `finally`-Zweige am `try`
- `raise` — einen Fehler selbst auslösen
- `as fehler` — das Fehlerobjekt an einen Namen binden (`except ValueError as fehler`)
