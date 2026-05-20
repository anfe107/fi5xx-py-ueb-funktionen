from run_length_encode import run_length_encode


def test_three_runs_in_aaabbc() -> None:
    """'aaabbc' encodes to three runs."""
    result = run_length_encode("aaabbc")
    assert result == [("a", 3), ("b", 2), ("c", 1)]


# Entwerfen Sie eigene Testfälle: mindestens ein Normalfall, ein Randfall
# (z. B. leerer Text) und ein Sonderfall (z. B. ein Zeichen kommt nach einer
# anderen Lauflänge erneut vor — `"aabbaa"`).
