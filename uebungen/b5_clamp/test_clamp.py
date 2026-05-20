from clamp import clamp


def test_value_within_default_range() -> None:
    """50 lies within the default range [0, 100] and passes through unchanged."""
    result = clamp(50)
    assert result == 50


# Entwerfen Sie eigene Testfälle: mindestens ein Normalfall, ein Randfall
# und ein Sonderfall. Decken Sie sowohl Aufrufe mit Default-Werten (z. B.
# clamp(150)) als auch Aufrufe mit explizit angegebenen Grenzen (z. B.
# clamp(50, 10, 20)) ab.
