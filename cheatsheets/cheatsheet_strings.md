# Cheat-Sheet — Strings

Nachschlagewerk für Grundoperationen mit Strings (Zeichenketten). Operiert auf denselben Bausteinen wie das Listen-Cheat-Sheet — mit einer wichtigen Asymmetrie (siehe Vergleich am Ende).

## String erzeugen

```python
word = "Hello"
sentence = 'A short text'
empty = ""
```

Doppelte und einfache Anführungszeichen sind gleichwertig.

## Länge

```python
length = len(word)          # 5
```

## Indexzugriff (lesen)

```python
first = word[0]                     # "H"
last = word[len(word) - 1]          # "o"
```

> Indizes beginnen bei `0`. Ein Zugriff auf einen ungültigen Index löst einen `IndexError` aus.

## Strings sind unveränderlich

Anders als bei Listen lassen sich einzelne Zeichen **nicht** ersetzen:

```python
word[0] = "X"               # TypeError: 'str' object does not support item assignment
```

Zum Ändern muss ein neuer String gebaut werden.

## Mitgliedschaft

```python
"l" in word                 # True
"x" in word                 # False
"ell" in "Hello"            # True — substrings match too
```

## Iteration

Über die Zeichen:

```python
for char in word:
    print(char)
```

Über die Indizes (wenn Position oder Nachbar gebraucht wird):

```python
for i in range(len(word)):
    print(i, word[i])
```

## Verkettung

```python
greeting = "Hello" + " " + "World"      # "Hello World"
```

`+` mit `str` und `int` schlägt fehl — vorher mit `str(...)` umwandeln:

```python
n = 3
text = "attempt " + str(n)              # "attempt 3"
```

## f-Strings

Bequemer als Verkettung: ein String mit dem Präfix `f` darf in geschweiften Klammern **Ausdrücke** einbetten. Das Ergebnis jedes Ausdrucks wird automatisch in seine String-Darstellung umgewandelt — `str(...)` ist nicht nötig.

```python
name = "Anna"
age = 17

greeting = f"Hallo, {name}!"            # "Hallo, Anna!"
info = f"{name} ist {age} Jahre alt"    # "Anna ist 17 Jahre alt"
```

In den Klammern sind nicht nur Variablen erlaubt, sondern beliebige Ausdrücke:

```python
a = 2
b = 3
text = f"Summe: {a + b}"                # "Summe: 5"
text = f"Erstes Zeichen: {name[0]}"     # "Erstes Zeichen: A"
```

Geschweifte Klammern selbst stehen verdoppelt — `{{` und `}}`:

```python
print(f"{{Hinweis}}: {name}")           # "{Hinweis}: Anna"
```

> **Tellerrand — Python vs. C#/Java:** C# kennt eine fast identische Syntax mit `$"Hallo, {name}!"`. In Java gibt es bis einschließlich Java 21 keine direkte Variableninterpolation in Strings — dort wird `String.format("Hallo, %s!", name)` oder die Verkettung mit `+` genutzt.

## Vergleich

```python
"Hello" == "Hello"          # True
"a" == "A"                  # False — case-sensitive
```

---

## Listen vs. Strings

| Operation | Liste | String |
|---|---|---|
| Länge | `len(lst)` | `len(s)` |
| Index lesen | `lst[i]` | `s[i]` |
| Index **schreiben** | `lst[i] = x` ✓ | `s[i] = x` → `TypeError` |
| Mitgliedschaft | `x in lst` | `c in s` (auch Teilstrings) |
| Iteration | `for x in lst:` | `for c in s:` |
| Verkettung | `lst1 + lst2` | `s1 + s2` |
| Anhängen | `lst.append(x)` | nur `s = s + x` (neuer String) |

---

## Außerhalb der Baseline

Folgende Konstrukte sind **nicht** Teil der Baseline. Wenn eine Übung sie braucht, führt der Aufgabentext sie ein:

- Slicing (`s[1:4]`, `s[::-1]`)
- Methoden wie `.upper()`, `.lower()`, `.strip()`, `.split()`, `.replace()`, `.startswith()`, `.endswith()`
- Format-Spezifizierer in f-Strings (`f"{x:.2f}"`, `f"{n:04d}"`, `f"{text:>10}"`)
- Escape-Sequenzen über `\n` / `\t` hinaus
