# Testfallkatalog B9 — clamp
#
# | Nr. | Eingabe          | Erwartete Ausgabe | Begründung                                            |
# |-----|------------------|-------------------|-------------------------------------------------------|
# | 1   | clamp(50)        | 50                | Normalfall: Wert innerhalb des Default-Bereichs       |
# | 2   | clamp(150)       | 100               | Normalfall: Wert über oberer Default-Grenze           |
# | 3   | clamp(-5)        | 0                 | Normalfall: Wert unter unterer Default-Grenze         |
# | 4   | clamp(0)         | 0                 | Randfall: genau auf unterer Default-Grenze            |
# | 5   | clamp(100)       | 100               | Randfall: genau auf oberer Default-Grenze             |
# | 6   | clamp(15, 10, 20)| 15                | Sonderfall: explizite Grenzen, Wert innerhalb         |
# | 7   | clamp(5, 10, 20) | 10                | Sonderfall: explizite Grenzen, Wert unterhalb         |
# | 8   | clamp(25, 10, 20)| 20                | Sonderfall: explizite Grenzen, Wert oberhalb          |

from clamp import clamp


def test_value_within_default_range() -> None:
    """50 lies within the default range [0, 100] and passes through unchanged."""
    result = clamp(50)
    assert result == 50


def test_value_above_default_upper() -> None:
    """150 exceeds the default upper bound of 100 and is clamped down."""
    result = clamp(150)
    assert result == 100


def test_value_below_default_lower() -> None:
    """-5 is below the default lower bound of 0 and is clamped up."""
    result = clamp(-5)
    assert result == 0


def test_value_equal_to_default_lower() -> None:
    """A value equal to the lower bound is kept (closed interval)."""
    result = clamp(0)
    assert result == 0


def test_value_equal_to_default_upper() -> None:
    """A value equal to the upper bound is kept (closed interval)."""
    result = clamp(100)
    assert result == 100


def test_explicit_bounds_value_within() -> None:
    """With explicit bounds [10, 20], a value of 15 passes through."""
    result = clamp(15, 10, 20)
    assert result == 15


def test_explicit_bounds_value_below() -> None:
    """With explicit bounds [10, 20], a value of 5 is clamped up to 10."""
    result = clamp(5, 10, 20)
    assert result == 10


def test_explicit_bounds_value_above() -> None:
    """With explicit bounds [10, 20], a value of 25 is clamped down to 20."""
    result = clamp(25, 10, 20)
    assert result == 20
