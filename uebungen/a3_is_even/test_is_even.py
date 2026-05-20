from is_even import is_even


def test_positive_even_number_returns_true() -> None:
    """4 is even."""
    result = is_even(4)
    assert result is True


def test_positive_odd_number_returns_false() -> None:
    """7 is odd."""
    result = is_even(7)
    assert result is False


def test_zero_is_even() -> None:
    """0 is considered even."""
    result = is_even(0)
    assert result is True


def test_negative_even_number_returns_true() -> None:
    """-2 is even."""
    result = is_even(-2)
    assert result is True


def test_negative_odd_number_returns_false() -> None:
    """-3 is odd."""
    result = is_even(-3)
    assert result is False
