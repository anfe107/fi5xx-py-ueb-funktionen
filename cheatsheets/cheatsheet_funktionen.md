# Cheat-Sheet — Funktionen

Nachschlagewerk für die Definition und den Aufruf von Funktionen.

## Funktion definieren

```python
def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b
```

Bestandteile:

- `def add` — Schlüsselwort und Funktionsname (snake_case).
- `(a: int, b: int)` — Parameterliste mit Type Hints.
- `-> int` — Type Hint des Rückgabewerts.
- `:` — leitet den Funktionsblock ein.
- Eingerückter Block — alles Eingerückte gehört zur Funktion.
- `"""..."""` — Docstring.
- `return` — gibt einen Wert zurück und beendet die Funktion.

## Aufruf

```python
result = add(2, 3)          # result is 5
print(add(10, 4))           # prints 14
```

Argumente werden der Reihe nach zugeordnet — `add(2, 3)` setzt `a=2`, `b=3`.

## Rückgabewert

```python
def square(x: int) -> int:
    return x * x
```

`return` beendet die Funktion sofort — Code danach läuft nicht mehr.

```python
def first_negative(numbers: list[int]) -> int:
    for n in numbers:
        if n < 0:
            return n            # early exit
    return 0                    # no negative number found
```

Eine Funktion ohne `return` (oder mit `return` ohne Wert) liefert `None`.

## Docstring

```python
def count_vowels(word: str) -> int:
    """Count the vowels in the word.

    word: the word to inspect.
    Return: number of vowels (a, e, i, o, u, case-insensitive).
    """
    ...
```

Stil: kurze Einleitungszeile, dann Parameter und Rückgabe in Klartext.

## Lokale Variablen

Variablen innerhalb einer Funktion existieren nur dort:

```python
def doubled(x: int) -> int:
    result = x * 2
    return result

print(doubled(5))           # 10
print(result)               # NameError — result is invisible outside
```

## Type Hints

Type Hints **dokumentieren** den erwarteten Typ, **erzwingen ihn aber nicht** zur Laufzeit:

```python
def double(x: int) -> int:
    return x * 2

double("ab")                # returns "abab" — type hint was ignored
```

> **Tellerrand — Python vs. C#/Java:** In Python sind Type Hints optional und
> werden zur Laufzeit nicht erzwungen. In C# und Java ist die Typprüfung Teil
> der Kompilierung — ein Typfehler verhindert dort den Build.

## Default-Werte für Parameter

Parameter dürfen einen Default-Wert tragen — dann darf das Argument beim Aufruf weggelassen werden:

```python
def increment(x: int, by: int = 1) -> int:
    return x + by

increment(5)                # by nutzt den Default 1   → 6
increment(5, 3)             # by explizit 3            → 8
```

Mehrere Default-Werte sind möglich:

```python
def clamp(value: int, lower: int = 0, upper: int = 100) -> int:
    ...

clamp(50)                   # lower=0, upper=100   → 50
clamp(150)                  # lower=0, upper=100   → 100
clamp(15, 10, 20)           # alle drei explizit   → 15
```

Regeln:

- Parameter mit Default-Werten stehen in der Signatur **nach** allen Parametern ohne Default.
- Der Default-Wert wird **einmal** bei der Funktionsdefinition ausgewertet. Für unveränderliche Werte (`int`, `str`, `float`, `bool`) ist das ohne Folgen.

> **Tellerrand — Python vs. C#/Java:** C# kennt Default-Werte als *optional parameters* mit der gleichen Schreibweise. Java erreicht denselben Effekt traditionell über **Methoden-Überladung** — mehrere Methoden mit gleichem Namen und unterschiedlicher Parameterzahl. In Python ist Methoden-Überladung **nicht** verfügbar; Default-Werte sind das Mittel der Wahl.

---

## Außerhalb der Baseline

Folgende Konstrukte sind **nicht** Teil der Baseline. Wenn eine Übung sie braucht, führt der Aufgabentext sie ein:

- Schlüsselwort-Argumente beim Aufruf (`add(a=2, b=3)`)
- Variable Argumentlisten (`*args`, `**kwargs`)
- `lambda`-Ausdrücke
- Geschachtelte Funktionen, Closures, Decorators
