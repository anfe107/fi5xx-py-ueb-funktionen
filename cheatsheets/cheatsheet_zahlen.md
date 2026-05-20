# Cheat-Sheet — Zahlen

Nachschlagewerk für Grundoperationen mit ganzen und Gleitkommazahlen.

## Erzeugen

```python
n = 42                      # int
x = 3.14                    # float
zero = 0
```

## Konvertieren

```python
int("42")                   # 42
float("3.14")               # 3.14
str(42)                     # "42"
int(3.7)                    # 3 — fractional part is dropped
float(2)                    # 2.0
```

## Arithmetische Operatoren

```python
a + b                       # addition
a - b                       # subtraction
a * b                       # multiplication
a ** b                      # exponent: 2 ** 3 == 8
```

## Division — drei Varianten

```python
7 / 2                       # 3.5  — always float division
7 // 2                      # 3    — floor division (toward -infinity)
7 % 2                       # 1    — remainder
```

> `/` liefert **immer** ein Float — auch wenn beide Operanden ganzzahlig sind und das Ergebnis ganzzahlig wäre. `8 / 2` ist `4.0`, nicht `4`.

## Mischen von int und float

```python
2 + 0.5                     # 2.5      — int + float yields float
2 ** 0.5                    # 1.4142...  — square root via exponent
```

## `range()` — ganzzahlige Folge

```python
for i in range(5):
    print(i)                # 0, 1, 2, 3, 4

for i in range(2, 6):
    print(i)                # 2, 3, 4, 5

for i in range(0, 10, 3):
    print(i)                # 0, 3, 6, 9
```

`range(stop)` startet bei `0` und stoppt **vor** `stop`. `range(start, stop)` und `range(start, stop, step)` analog.

## Vergleichsoperatoren

```python
a == b                      # equality
a != b                      # inequality
a < b, a <= b, a > b, a >= b
```

## Float-Gleichheit

```python
0.1 + 0.2 == 0.3                  # False — floats use binary representation
abs((0.1 + 0.2) - 0.3) < 1e-9     # True  — compare with tolerance
```

> **Tellerrand — Python vs. C#/Java:**
> - In Python ist `int` **beliebig groß**; `2 ** 1000` ergibt eine Zahl mit über 300 Stellen.
>   In C# / Java sind `int` 32 Bit, `long` 64 Bit; für beliebig große Zahlen `BigInteger`.
> - Beim Modulo mit negativen Werten unterscheidet sich das Verhalten:
>   Python `-7 % 3 == 2` (Vorzeichen des Divisors); C# / Java `-7 % 3 == -1` (Vorzeichen des Dividenden).

---

## Außerhalb der Baseline

Folgende Konstrukte sind **nicht** Teil der Baseline. Wenn eine Übung sie braucht, führt der Aufgabentext sie ein:

- Builtins wie `abs(x)`, `min(a, b)`, `max(a, b)`, `sum(iterable)`, `round(x, n)`
- `math`-Modul (`math.sqrt`, `math.pi`, `math.floor`, `math.ceil`)
- `divmod(a, b)` — liefert `(a // b, a % b)` als Tupel
- Komplexe Zahlen (`complex`)
- `Decimal`, `Fraction` für exakte Arithmetik
- Format-Spezifizierer in f-Strings für Zahlen-Formatierung (`f"{x:.2f}"`, `f"{n:04d}"`) — siehe `cheatsheet_strings.md`
