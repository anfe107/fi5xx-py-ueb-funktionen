# Testfallkatalog B7 — reverse_number
#
# | Nr. | Eingabe | Erwartete Ausgabe | Begründung                                    |
# |-----|---------|-------------------|-----------------------------------------------|
# | 1   | 123     | 321               | Normalfall: dreistellig                       |
# | 2   | 0       | 0                 | Randfall: Null                                |
# | 3   | 5       | 5                 | Randfall: einstellig                          |
# | 4   | 1000    | 1                 | Sonderfall: nachgestellte Nullen verschwinden |
# | 5   | 9876    | 6789              | Normalfall: vierstellig                       |

from reverse_number import reverse_number


def test_three_digits_reversed() -> None:
    """123 reversed is 321."""
    result = reverse_number(123)
    assert result == 321


def test_zero_reversed_is_zero() -> None:
    """0 reversed is 0."""
    result = reverse_number(0)
    assert result == 0


def test_single_digit_reversed_is_itself() -> None:
    """A single-digit number reversed is itself."""
    result = reverse_number(5)
    assert result == 5


def test_trailing_zeros_disappear() -> None:
    """1000 reversed becomes 1 — trailing zeros are lost."""
    result = reverse_number(1000)
    assert result == 1


def test_four_digits_reversed() -> None:
    """9876 reversed is 6789."""
    result = reverse_number(9876)
    assert result == 6789
