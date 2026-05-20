# Testfallkatalog B4 — common_elements
#
# | Nr. | Eingabe                   | Erwartete Ausgabe | Begründung                                        |
# |-----|---------------------------|-------------------|---------------------------------------------------|
# | 1   | ([1, 2, 3], [2, 3, 4])    | [2, 3]            | Normalfall: einfache Überschneidung               |
# | 2   | ([], [1, 2])              | []                | Randfall: erste Liste leer                        |
# | 3   | ([1, 2], [])              | []                | Randfall: zweite Liste leer                       |
# | 4   | ([1, 2, 3], [4, 5, 6])    | []                | Sonderfall: keine Überschneidung                  |
# | 5   | ([1, 1, 2, 2], [1, 2, 3]) | [1, 2]            | Sonderfall: Duplikate in `a`, im Ergebnis nur einmal |
# | 6   | ([1, 2, 3], [3, 2, 1])    | [1, 2, 3]         | Normalfall: Reihenfolge folgt `a`, nicht `b`      |

from common_elements import common_elements


def test_two_overlapping_lists() -> None:
    """[1, 2, 3] and [2, 3, 4] share 2 and 3."""
    result = common_elements([1, 2, 3], [2, 3, 4])
    assert result == [2, 3]


def test_first_list_empty() -> None:
    """An empty first list yields an empty result."""
    result = common_elements([], [1, 2])
    assert result == []


def test_second_list_empty() -> None:
    """An empty second list yields an empty result."""
    result = common_elements([1, 2], [])
    assert result == []


def test_no_overlap() -> None:
    """[1, 2, 3] and [4, 5, 6] share nothing."""
    result = common_elements([1, 2, 3], [4, 5, 6])
    assert result == []


def test_duplicates_in_first_list_appear_once() -> None:
    """Duplicates in `a` appear only once in the result."""
    result = common_elements([1, 1, 2, 2], [1, 2, 3])
    assert result == [1, 2]


def test_order_follows_first_list() -> None:
    """Order in the result follows `a`, not `b`."""
    result = common_elements([1, 2, 3], [3, 2, 1])
    assert result == [1, 2, 3]
