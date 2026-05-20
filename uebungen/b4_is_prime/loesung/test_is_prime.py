# Testfallkatalog B6 — is_prime
#
# | Nr. | Eingabe | Erwartete Ausgabe | Begründung                                  |
# |-----|---------|-------------------|---------------------------------------------|
# | 1   | 7       | True              | Normalfall: kleine Primzahl                 |
# | 2   | 4       | False             | Normalfall: kleinste zusammengesetzte Zahl  |
# | 3   | 2       | True              | Randfall: kleinste Primzahl                 |
# | 4   | 9       | False             | Sonderfall: ungerade zusammengesetzte Zahl  |
# | 5   | 13      | True              | Normalfall: größere Primzahl                |
# | 6   | 15      | False             | Sonderfall: Produkt zweier Primzahlen       |

from is_prime import is_prime


def test_seven_is_prime() -> None:
    """7 is a prime number."""
    result = is_prime(7)
    assert result is True


def test_four_is_not_prime() -> None:
    """4 is composite (2 * 2)."""
    result = is_prime(4)
    assert result is False


def test_two_is_smallest_prime() -> None:
    """2 is the smallest prime number."""
    result = is_prime(2)
    assert result is True


def test_nine_is_not_prime() -> None:
    """9 is composite (3 * 3)."""
    result = is_prime(9)
    assert result is False


def test_thirteen_is_prime() -> None:
    """13 is a prime number."""
    result = is_prime(13)
    assert result is True


def test_fifteen_is_not_prime() -> None:
    """15 is composite (3 * 5)."""
    result = is_prime(15)
    assert result is False
