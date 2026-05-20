def count_vowels(word: str) -> int:
    """Count the vowels in the word.

    word: the word to inspect.
    Return: number of vowels (a, e, i, o, u, case-insensitive).
    """
    count = 0
    for char in word:
        if char in "aeiouAEIOU":
            count = count + 1
    return count
