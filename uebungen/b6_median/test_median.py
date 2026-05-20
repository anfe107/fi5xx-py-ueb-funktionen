import pytest
from median import median


def test_example_odd_length():
    """Beispieltest: Median bei ungerader Listenlänge."""
    assert median([3, 1, 4, 1, 5]) == 3.0


# Ergänzen Sie weitere Testfälle entsprechend der Aufgabe und des Testfallkatalogs.
