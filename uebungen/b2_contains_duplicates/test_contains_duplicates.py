from contains_duplicates import contains_duplicates


def test_unique_elements_returns_false() -> None:
    """[1, 2, 3] contains no duplicates."""
    result = contains_duplicates([1, 2, 3])
    assert result is False


def test_one_duplicate_returns_true() -> None:
    """[1, 9, 9] contains one duplicate."""
    result = contains_duplicates([1, 9, 9])
    assert result is True


def test_three_unique_elements_return_false() -> None:
    """[5, 5, 5] contains no duplicates."""
    result = contains_duplicates([5, 5, 5])
    assert result is True


def test_empty_list_returns_false() -> None:
    """[] contains no duplicates."""
    result = contains_duplicates([])
    assert result is False


def test_similar_elements_returns_false() -> None:
    """[1, 11, 111] contains no duplicates."""
    result = contains_duplicates([1, 11, 111])
    assert result is False
# Ergänzen Sie weitere Tests: mindestens ein Normalfall (mit Duplikat), ein
# Randfall (leere oder einelementige Liste) und ein Sonderfall.
