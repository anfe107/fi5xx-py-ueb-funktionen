# Testfallkatalog B2 — contains_duplicates
#
# | Nr. | Eingabe        | Erwartete Ausgabe | Begründung                                  |
# |-----|----------------|-------------------|---------------------------------------------|
# | 1   | [1, 2, 3]      | False             | Normalfall: keine Duplikate                 |
# | 2   | [1, 2, 1]      | True              | Normalfall: ein Duplikat                    |
# | 3   | []             | False             | Randfall: leere Liste                       |
# | 4   | [42]           | False             | Randfall: einelementige Liste               |
# | 5   | [1, 1, 1]      | True              | Sonderfall: alle Elemente identisch         |
# | 6   | [5, 1, 2, 3, 5]| True              | Sonderfall: Duplikat am Ende der Liste      |

from contains_duplicates import contains_duplicates


def test_unique_elements_returns_false() -> None:
    """[1, 2, 3] contains no duplicates."""
    result = contains_duplicates([1, 2, 3])
    assert result is False


def test_one_duplicate_returns_true() -> None:
    """[1, 2, 1] has a duplicate."""
    result = contains_duplicates([1, 2, 1])
    assert result is True


def test_empty_list_returns_false() -> None:
    """An empty list has no duplicates."""
    result = contains_duplicates([])
    assert result is False


def test_single_element_list_returns_false() -> None:
    """A one-element list has no duplicates."""
    result = contains_duplicates([42])
    assert result is False


def test_all_elements_identical() -> None:
    """[1, 1, 1] is full of duplicates."""
    result = contains_duplicates([1, 1, 1])
    assert result is True


def test_duplicate_at_end_of_list() -> None:
    """[5, 1, 2, 3, 5] has a duplicate at the end."""
    result = contains_duplicates([5, 1, 2, 3, 5])
    assert result is True
