# Cheat-Sheet — Tupel

Nachschlagewerk für Tupel — ein **unveränderliches** Bündel mehrerer zusammengehöriger Werte. Wird in einer Übung erst dann eingeführt, wenn jedes Element selbst aus mehreren Bestandteilen besteht (zum Beispiel ein Zeichen und seine Häufigkeit als Paar).

## Tupel erzeugen

```python
pair = ("a", 3)
triple = (1, 2, 3)
empty = ()
```

Runde Klammern, Komma-Trennung. Auch ohne Klammern erlaubt: `pair = "a", 3`.

## Zugriff per Index

```python
character = pair[0]         # "a"
count = pair[1]             # 3
```

Indizes wie bei Listen und Strings, beginnend bei `0`.

## Tupel sind unveränderlich

```python
pair[0] = "b"               # TypeError — a tuple cannot be modified after creation
```

Zum „Ändern" muss ein neues Tupel erzeugt werden.

## Liste von Tupeln

Typisches Muster: leer starten, in einer Schleife Tupel anhängen.

```python
pairs = []
pairs.append(("a", 3))
pairs.append(("b", 2))
# pairs is now [("a", 3), ("b", 2)]
```

## Iteration über eine Liste von Tupeln

```python
for pair in pairs:
    print(pair[0], pair[1])
```

---

## Außerhalb der Baseline

Folgende Konstrukte sind **nicht** Teil der Baseline:

- Tupel-Unpacking (`a, b = pair`)
- Tupel mit benannten Feldern (`namedtuple`, `NamedTuple`)
- Tupel als Schlüssel in Dicts oder Mengen
