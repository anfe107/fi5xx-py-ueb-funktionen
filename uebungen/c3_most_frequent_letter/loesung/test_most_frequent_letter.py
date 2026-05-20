# Testfallkatalog C1 — most_frequent_letter
#
# | Nr. | Eingabe          | Erwartete Ausgabe | Begründung                                  |
# |-----|------------------|-------------------|---------------------------------------------|
# | 1   | "abracadabra"    | "a"               | Normalfall: ein klares Maximum              |
# | 2   | ""               | ""                | Randfall: leeres Wort                       |
# | 3   | "x"              | "x"               | Randfall: einzelnes Zeichen                 |
# | 4   | "abc"            | "a"               | Sonderfall: alle Zeichen einmal — erstes gewinnt |
# | 5   | "aabbcc"         | "a"               | Sonderfall: gleich häufig — Tie-Break       |
# | 6   | "mississippi"    | "i"               | Normalfall: 'i' und 's' je 4× — 'i' kommt früher |

from most_frequent_letter import most_frequent_letter


def test_a_is_most_frequent_in_abracadabra() -> None:
    """'abracadabra' contains 'a' five times — the most of any letter."""
    result = most_frequent_letter("abracadabra")
    assert result == "a"


def test_empty_word_returns_empty_string() -> None:
    """An empty word returns the empty string."""
    result = most_frequent_letter("")
    assert result == ""


def test_single_character_word() -> None:
    """A one-character word returns that character."""
    result = most_frequent_letter("x")
    assert result == "x"


def test_all_unique_characters_first_wins() -> None:
    """When all characters appear once, the first wins by tie-break."""
    result = most_frequent_letter("abc")
    assert result == "a"


def test_tie_break_returns_earliest() -> None:
    """'aabbcc' has three letters tied at 2 — 'a' wins as the earliest."""
    result = most_frequent_letter("aabbcc")
    assert result == "a"


def test_mississippi_returns_i() -> None:
    """'mississippi' has 'i' and 's' tied at 4 — 'i' appears first."""
    result = most_frequent_letter("mississippi")
    assert result == "i"
