# Testfallkatalog C4 — run_length_encode
#
# | Nr. | Eingabe   | Erwartete Ausgabe                          | Begründung                                  |
# |-----|-----------|--------------------------------------------|---------------------------------------------|
# | 1   | "aaabbc"  | [("a", 3), ("b", 2), ("c", 1)]             | Normalfall: drei Läufe absteigender Länge   |
# | 2   | ""        | []                                         | Randfall: leerer Text                       |
# | 3   | "x"       | [("x", 1)]                                 | Randfall: einzelnes Zeichen                 |
# | 4   | "aaaa"    | [("a", 4)]                                 | Sonderfall: nur ein einziger Lauf           |
# | 5   | "abcd"    | [("a", 1), ("b", 1), ("c", 1), ("d", 1)]   | Sonderfall: jeder Lauf hat Länge 1          |
# | 6   | "aabbaa"  | [("a", 2), ("b", 2), ("a", 2)]             | Sonderfall: 'a' kommt nach 'b' als neuer Lauf wieder vor |

from run_length_encode import run_length_encode


def test_three_runs_in_aaabbc() -> None:
    """'aaabbc' encodes to three runs of decreasing length."""
    result = run_length_encode("aaabbc")
    assert result == [("a", 3), ("b", 2), ("c", 1)]


def test_empty_text_returns_empty_list() -> None:
    """An empty text returns the empty list."""
    result = run_length_encode("")
    assert result == []


def test_single_character_text() -> None:
    """A one-character text returns a single one-count tuple."""
    result = run_length_encode("x")
    assert result == [("x", 1)]


def test_text_with_one_run_only() -> None:
    """'aaaa' is a single run of length four."""
    result = run_length_encode("aaaa")
    assert result == [("a", 4)]


def test_each_run_has_length_one() -> None:
    """'abcd' yields four runs of length one each."""
    result = run_length_encode("abcd")
    assert result == [("a", 1), ("b", 1), ("c", 1), ("d", 1)]


def test_repeated_character_after_other_run() -> None:
    """'aabbaa' yields three runs — 'a' appears in two separate runs."""
    result = run_length_encode("aabbaa")
    assert result == [("a", 2), ("b", 2), ("a", 2)]
