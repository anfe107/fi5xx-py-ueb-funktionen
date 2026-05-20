# Testfallkatalog R1b — Auftragserfassung:
# Nr. | Eingabe | Erwartet | Begründung
#  1  |    5    |  True    | Normalfall: positive Bestellmenge
#  2  |    1    |  True    | Randfall: kleinstmöglicher gültiger Wert
#  3  |    0    |  False   | Randfall: Null ist nicht positiv
#  4  |   -1    |  False   | Randfall: knapp unterhalb von 0
#  5  | -100    |  False   | Sonderfall: stark negativer Wert
#  6  | 1000    |  True    | Normalfall: große Bestellmenge

from order_input import is_positive


def test_positive_value():
    """Normalfall: Wert größer null ist gültig."""
    assert is_positive(5) == True


def test_minimum_valid_value():
    """Randfall: 1 ist der kleinste gültige Wert."""
    assert is_positive(1) == True


def test_zero_is_invalid():
    """Randfall: 0 ist nicht positiv."""
    assert is_positive(0) == False


def test_minus_one_is_invalid():
    """Randfall: -1 liegt knapp unterhalb der Grenze."""
    assert is_positive(-1) == False


def test_large_negative_value():
    """Sonderfall: stark negativer Wert ist ungültig."""
    assert is_positive(-100) == False


def test_large_positive_value():
    """Normalfall: große Bestellmenge ist gültig."""
    assert is_positive(1000) == True
