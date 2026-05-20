from most_frequent_letter import most_frequent_letter


def test_a_is_most_frequent_in_abracadabra() -> None:
    """'abracadabra' contains 'a' five times — the most of any letter."""
    result = most_frequent_letter("abracadabra")
    assert result == "a"


# Entwerfen Sie eigene Testfälle: mindestens ein Normalfall, ein Randfall
# und ein Sonderfall. Reflektieren Sie insbesondere Tie-Break-Situationen
# und das leere Wort.
