# Cheat-Sheet — Listen

Nachschlagewerk für Grundoperationen mit Listen. Deckt nur ab, was in der Vorkenntnis-Baseline (CLAUDE.md §3) zugelassen ist.

## Liste erzeugen

```python
numbers = [1, 2, 3, 4]
names = ["Anna", "Ben", "Clara"]
empty = []
```

## Länge

```python
length = len(numbers)       # 4
```

## Indexzugriff

```python
first = numbers[0]                    # 1
last = numbers[len(numbers) - 1]      # 4
numbers[2] = 99                       # replace element
```

> Indizes beginnen bei `0`. Ein Zugriff auf einen ungültigen Index löst einen `IndexError` aus.

## Mitgliedschaft prüfen

```python
present = 2 in numbers      # True
missing = 100 in numbers    # False
```

## Iteration

Über die Elemente:

```python
for number in numbers:
    print(number)
```

Über die Indizes (wenn Position oder Nachbar gebraucht wird):

```python
for i in range(len(numbers)):
    print(i, numbers[i])
```

## Anhängen

```python
numbers.append(5)           # numbers is now [1, 2, 99, 4, 5]
```

`.append()` verändert die Liste an Ort und Stelle und gibt `None` zurück:

```python
result = numbers.append(6)  # result is None
```

## Liste aufbauen

Typisches Muster: leer starten, in einer Schleife füllen.

```python
squares = []
for number in numbers:
    squares.append(number * number)
```

---

## Außerhalb der Baseline

Folgende Konstrukte sind **nicht** Teil der Baseline. Wenn eine Übung sie braucht, führt der Aufgabentext sie ein — ansonsten nicht verwenden:

- Slicing über `lst[i]` hinaus (z. B. `lst[1:3]`, `lst[::-1]`)
- List Comprehensions (`[x*x for x in lst]`)
- `enumerate(lst)`, `zip(a, b)`
- Methoden wie `.pop()`, `.insert()`, `.remove()`, `.sort()`, `.reverse()`
- Tupel, Dicts, Mengen
