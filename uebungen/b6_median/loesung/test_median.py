import pytest
from median import median


# Testfallkatalog (aus aufgaben.md)
# | Nr. | Eingabe        | Erwartete Ausgabe | Begründung |
# | --- | -------------- | ----------------- | ---------- |
# | 1   | `[3, 1, 4, 1, 5]` | `3.0`          | Normalfall: ungerade Länge, unsortiert |
# | 2   | `[1, 2, 3, 4]` | `2.5`             | Normalfall: gerade Länge |
# | 3   | `[42]`         | `42.0`            | Randfall: einzelnes Element |
# | 4   | `[]`           | `0.0`             | Sonderfall: leere Liste |
# | 5   | `[5, 5, 5]`    | `5.0`             | Sonderfall: alle Elemente identisch |


def test_odd_length_unsorted():
    """Normalfall: ungerade Länge, unsortierte Eingabe."""
    assert median([3, 1, 4, 1, 5]) == 3.0


def test_even_length():
    """Normalfall: gerade Länge."""
    assert median([1, 2, 3, 4]) == 2.5


def test_single_element():
    """Randfall: Liste mit einzelnem Element."""
    assert median([42]) == 42.0


def test_empty_list():
    """Sonderfall: leere Liste."""
    assert median([]) == 0.0


def test_all_identical():
    """Sonderfall: alle Elemente gleich."""
    assert median([5, 5, 5]) == 5.0


def test_odd_length_already_sorted():
    """Normalfall: ungerade Länge, bereits sortiert."""
    assert median([1, 2, 3]) == 2.0


def test_even_length_with_negatives():
    """Normalfall: gerade Länge mit negativen Zahlen."""
    assert median([-2, -1, 1, 2]) == 0.0


def test_two_elements():
    """Randfall: zwei Elemente (kleinste gerade Länge)."""
    assert median([10, 20]) == 15.0
