from sum_list import sum_list


def test_sum_of_one_two_three_is_six() -> None:
    """Sum of [1, 2, 3] is 6."""
    result = sum_list([1, 2, 3])
    assert result == 6


def test_empty_list_sums_to_zero() -> None:
    """An empty list sums to 0."""
    result = sum_list([])
    assert result == 0


def test_single_element_list_returns_element() -> None:
    """A one-element list returns that element."""
    result = sum_list([42])
    assert result == 42


def test_negatives_and_positives_cancel() -> None:
    """[-1, 1, -2, 2] sums to 0."""
    result = sum_list([-1, 1, -2, 2])
    assert result == 0


def test_only_negatives_sum_correctly() -> None:
    """Sum of [-5, -10, -3] is -18."""
    result = sum_list([-5, -10, -3])
    assert result == -18
