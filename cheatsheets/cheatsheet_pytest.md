# Cheat-Sheet — pytest

Nachschlagewerk für die pytest-Bedienung in den Übungen.

## Tests ausführen

Aus dem jeweiligen Übungsordner heraus:

```bash
python -m pytest
```

Pytest sucht automatisch alle Dateien `test_*.py` und in ihnen alle Funktionen `test_*`.

> **Nicht** `pytest` direkt aufrufen. `python -m pytest` umgeht zwei häufige Stolperfallen: pytest-Installation außerhalb des aktiven `venv` und fehlender PATH-Eintrag.

Für ausführlichere Ausgabe:

```bash
python -m pytest -v
```

## Aufbau einer Test-Funktion

```python
from <thema> import function_under_test


def test_input_two_returns_four() -> None:
    """Returns 4 when called with input 2."""
    result = function_under_test(2)
    assert result == 4
```

Konventionen:

- Datei beginnt mit `test_`.
- Funktion beginnt mit `test_`.
- Sprechender Funktionsname: was wird geprüft?
- **Eine Funktion = ein Testfall.**

## Häufige Assertions

```python
assert value == expected        # Gleichheit
assert value != forbidden       # Ungleichheit
assert value is True            # exakt True
assert value is False           # exakt False
assert part in whole            # Mitgliedschaft (z. B. Element in Liste)
assert value > threshold        # Vergleich
```

## Ausgabe lesen

```
============================ test session starts =============================
collected 4 items

test_square.py ..F.                                                     [ 75%]

================================== FAILURES ==================================
__________ test_negative_input_returns_positive_result _______________________
    def test_negative_input_returns_positive_result() -> None:
        result = square(-2)
>       assert result == 4
E       assert -4 == 4
```

| Zeichen | Bedeutung |
|---|---|
| `.` | Test bestanden |
| `F` | Test fehlgeschlagen (`assert` falsch) |
| `E` | Fehler beim Aufruf (z. B. `ImportError`, `TypeError`) |

## Häufige Fehlerbilder

| Meldung | Ursache | Lösung |
|---|---|---|
| `ModuleNotFoundError: No module named '<thema>'` | Aus falschem Ordner aufgerufen | In den Übungsordner wechseln, dann `python -m pytest` |
| `collected 0 items` | Datei- oder Funktionsname beginnt nicht mit `test_` | Namen anpassen |
| `AssertionError` ohne Detail | Vergleich liefert `False` | Mit `-v` ausführen, dann zeigt pytest beide Werte |
| `IndentationError` / `SyntaxError` | Fehler in der Test- oder Library-Datei | Datei prüfen — pytest kann nicht laden, was nicht parsiert |
