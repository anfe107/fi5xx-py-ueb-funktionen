def longest_word_split(sentence: str) -> str:
    """Return the longest word in the sentence.

    sentence: words separated by single spaces.
    Return: the longest word. If multiple words share the maximum length, the
        first one is returned. An empty sentence returns the empty string.
    """
    words = sentence.split()
    if len(words) == 0:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
