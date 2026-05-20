def run_length_encode(text: str) -> list[tuple[str, int]]:
    """Encode the text as a list of (character, run-length) pairs.

    A run is a maximal sequence of the same character. Each run is encoded as
    a tuple (character, count). See cheatsheet_tupel.md for tuple syntax.

    text: the text to encode.
    Return: list of (character, count) tuples in left-to-right order. An
        empty text returns an empty list.
    """
    # TODO
