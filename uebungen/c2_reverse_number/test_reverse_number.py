from reverse_number import reverse_number


def test_three_digits_reversed() -> None:
    """123 reversed is 321."""
    result = reverse_number(123)
    assert result == 321


# Ergänzen Sie weitere Tests: mindestens ein Normalfall (z. B. größere Zahl),
# ein Randfall (z. B. Null oder einstellige Zahl) und ein Sonderfall (z. B.
# Zahl mit nachgestellten Nullen — was passiert mit denen?).
