# Testfallkatalog A1 — count_vowels
#
# | Nr. | Eingabe         | Erwartete Ausgabe | Begründung                                |
# |-----|-----------------|-------------------|-------------------------------------------|
# | 1   | "Hallo"         | 2                 | Normalfall: gemischte Schreibweise        |
# | 2   | ""              | 0                 | Randfall: leerer String                   |
# | 3   | "xyz"           | 0                 | Sonderfall: keine Vokale enthalten        |
# | 4   | "AEIOU"         | 5                 | Sonderfall: nur Vokale, alle groß         |
# | 5   | "Programmieren" | 5                 | Normalfall: längeres Wort, mehrere Vokale |

from count_vowels import count_vowels


def test_hallo_has_two_vowels() -> None:
    """'Hallo' contains two vowels: a, o."""
    result = count_vowels("Hallo")
    assert result == 2


def test_empty_word_has_zero_vowels() -> None:
    """An empty word has zero vowels."""
    result = count_vowels("")
    assert result == 0


def test_word_without_vowels_returns_zero() -> None:
    """A word without vowels returns 0."""
    result = count_vowels("xyz")
    assert result == 0


def test_uppercase_vowels_are_counted() -> None:
    """Uppercase vowels are counted as well."""
    result = count_vowels("AEIOU")
    assert result == 5


def test_programmieren_has_five_vowels() -> None:
    """'Programmieren' contains five vowels: o, a, i, e, e."""
    result = count_vowels("Programmieren")
    assert result == 5
