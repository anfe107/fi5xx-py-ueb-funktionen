# Testfallkatalog A5 — digit_sum
#
# | Nr. | Eingabe | Erwartete Ausgabe | Begründung                              |
# |-----|---------|-------------------|-----------------------------------------|
# | 1   | 123     | 6                 | Normalfall: dreistellige Zahl           |
# | 2   | 0       | 0                 | Randfall: Null (Schleife läuft 0×)      |
# | 3   | 5       | 5                 | Randfall: einstellige Zahl              |
# | 4   | 9999    | 36                | Sonderfall: alle Ziffern gleich         |
# | 5   | 1000    | 1                 | Sonderfall: Ziffern enthalten Null      |

from digit_sum import digit_sum


def test_three_digits_sum_to_six() -> None:
    """123 has digits 1, 2, 3 — digit sum is 6."""
    result = digit_sum(123)
    assert result == 6


def test_zero_returns_zero() -> None:
    """0 has digit sum 0 by convention."""
    result = digit_sum(0)
    assert result == 0


def test_single_digit_returns_itself() -> None:
    """A single-digit number returns itself."""
    result = digit_sum(5)
    assert result == 5


def test_all_nines_four_digits() -> None:
    """9999 has digit sum 36."""
    result = digit_sum(9999)
    assert result == 36


def test_number_with_inner_zeros() -> None:
    """1000 has digits 1, 0, 0, 0 — digit sum is 1."""
    result = digit_sum(1000)
    assert result == 1
