def most_frequent_letter(word: str) -> str:
    """Return the most frequent character in the word.

    word: the word to inspect.
    Return: the character that appears most often. If multiple characters
        share the highest count, returns the one that appears first in the
        word. An empty word returns the empty string.
    """
    if word == "":
        return ""
    best_char = word[0]
    best_count = 0
    for candidate in word:
        count = 0
        for char in word:
            if char == candidate:
                count = count + 1
        if count > best_count:
            best_count = count
            best_char = candidate
    return best_char
