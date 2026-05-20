def run_length_encode(text: str) -> list[tuple[str, int]]:
    """Encode the text as a list of (character, run-length) pairs.

    A run is a maximal sequence of the same character. Each run is encoded as
    a tuple (character, count). See cheatsheet_tupel.md for tuple syntax.

    text: the text to encode.
    Return: list of (character, count) tuples in left-to-right order. An
        empty text returns an empty list.
    """
    if text == "":
        return []
    result = []
    current_char = text[0]
    current_count = 1
    for i in range(1, len(text)):
        if text[i] == current_char:
            current_count = current_count + 1
        else:
            result.append((current_char, current_count))
            current_char = text[i]
            current_count = 1
    # last run — without this append, the final run would be missed
    result.append((current_char, current_count))
    return result
