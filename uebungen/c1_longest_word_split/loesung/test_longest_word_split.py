# Testfallkatalog B5 — longest_word_split
#
# | Nr. | Eingabe                    | Erwartete Ausgabe | Begründung                                  |
# |-----|----------------------------|-------------------|---------------------------------------------|
# | 1   | "hi world"              | "world"           | Normalfall: längstes Wort am Ende           |
# | 2   | "alles"                    | "alles"           | Randfall: ein einzelnes Wort                |
# | 3   | ""                         | ""                | Randfall: leerer Satz                       |
# | 4   | "a bb ccc dd"              | "ccc"             | Normalfall: längstes Wort in der Mitte      |
# | 5   | "aa bb cc"                 | "aa"              | Sonderfall: alle gleich lang, erstes gewinnt |
# | 6   | "Programmieren ist toll"   | "Programmieren"   | Normalfall: längstes Wort am Anfang         |

from longest_word_split import longest_word_split


def test_two_words_returns_longer() -> None:
    """In 'hi world' the longer word is 'world'."""
    result = longest_word_split("hi world")
    assert result == "world"


def test_single_word_sentence() -> None:
    """A sentence with one word returns that word."""
    result = longest_word_split("alles")
    assert result == "alles"


def test_empty_sentence_returns_empty_string() -> None:
    """An empty sentence returns the empty string."""
    result = longest_word_split("")
    assert result == ""


def test_longest_word_in_the_middle() -> None:
    """The longest word may sit in the middle."""
    result = longest_word_split("a bb ccc dd")
    assert result == "ccc"


def test_tie_returns_first() -> None:
    """When several words share the maximum length, the first wins."""
    result = longest_word_split("aa bb cc")
    assert result == "aa"


def test_longest_word_at_the_start() -> None:
    """The longest word may sit at the start."""
    result = longest_word_split("Programmieren ist toll")
    assert result == "Programmieren"
