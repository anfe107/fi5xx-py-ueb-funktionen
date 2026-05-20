# Cheat-Sheet — Schleifen

Nachschlagewerk für Wiederholungsstrukturen. Deckt nur ab, was in der Vorkenntnis-Baseline (CLAUDE.md §3) zugelassen ist.

## `for` — über eine Sequenz iterieren

```python
for char in "Hallo":
    print(char)             # H, a, l, l, o

for number in [1, 2, 3]:
    print(number)           # 1, 2, 3
```

Die Anzahl der Durchläufe steht beim Schleifenstart **fest** — sie entspricht der Länge der Sequenz.

## `for` mit `range` — gezählte Wiederholung

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):       # 2, 3, 4, 5
    print(i)
```

Geeignet, wenn der Index gebraucht wird (`for i in range(len(s))`) oder eine feste Anzahl Durchläufe (`for _ in range(n)`).

## `while` — abweisende Schleife

```python
n = 1234
total = 0
while n > 0:
    total = total + n % 10
    n = n // 10
print(total)                # 10
```

Die Bedingung wird **vor** jedem Durchlauf geprüft. Ist sie beim ersten Test falsch, läuft der Rumpf **nullmal** — daher der Name *abweisende Schleife*. Geeignet, wenn die Anzahl der Durchläufe vorher unbekannt ist und ein nullter Durchlauf möglich sein soll.

> Im Rumpf muss sich etwas an den Variablen der Bedingung ändern — sonst entsteht eine Endlosschleife.

## `while True` mit `break` — nichtabweisende Schleife

```python
n = 5
result = ""
while True:
    result = str(n % 2) + result
    n = n // 2
    if n == 0:
        break
print(result)               # "101"
```

Der Rumpf läuft mindestens **einmal**, die Abbruchbedingung steht im Inneren. In der Literatur heißt dieses Muster *loop-and-a-half* — der Test sitzt „eineinhalb" Durchläufe weit drinnen. Geeignet, wenn der Algorithmus von sich aus mindestens einen Durchlauf braucht (Bit erzeugen, Wert verarbeiten, Eingabe lesen) und die Abbruchprüfung erst danach Sinn ergibt.

`break` verlässt die Schleife sofort. Code, der im selben Schleifendurchlauf nach `break` stünde, läuft nicht mehr.

## `for` oder `while`?

| Situation                                                  | Wahl                 |
| ---------------------------------------------------------- | -------------------- |
| Über eine bestehende Sequenz iterieren                     | `for`                |
| Feste Anzahl Durchläufe                                    | `for` mit `range`    |
| Anzahl Durchläufe hängt von einer wechselnden Bedingung ab | `while`              |
| Mindestens ein Durchlauf nötig, Abbruch danach             | `while True … break` |

## Abweisend vs. nichtabweisend

| Begriff        | Test prüft   | Mindestdurchläufe | Python-Form                    |
| -------------- | ------------ | ----------------- | ------------------------------ |
| abweisend      | vor dem Rumpf | 0                 | `while bedingung:`             |
| nichtabweisend | nach dem Rumpf | 1                 | `while True: … if cond: break` |

> **Tellerrand — Python vs. C#/Java:** C# und Java haben für die nichtabweisende Schleife eine
> eigene Syntax: `do { ... } while (bedingung);`. Der Rumpf läuft dort garantiert einmal,
> die Bedingung steht hinten. Python kennt diese Form nicht — die nichtabweisende Schleife
> wird mit `while True` und `break` nachgebildet.

---

## Außerhalb der Baseline

Folgende Konstrukte sind **nicht** Teil der Baseline. Wenn eine Übung sie braucht, führt der Aufgabentext sie ein:

- `continue` — überspringt den Rest des aktuellen Durchlaufs
- `else`-Zweig an `for`/`while` (`for ... else:`)
- List Comprehensions als Kurzform einer Schleife (siehe `cheatsheet_listen.md`)
- `enumerate(seq)`, `zip(a, b)` für Iteration mit Index oder über mehrere Sequenzen
