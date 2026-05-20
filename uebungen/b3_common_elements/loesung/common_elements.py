def common_elements(a: list[int], b: list[int]) -> list[int]:
    """Return the elements that appear in both lists.

    a, b: two lists of integers (either may be empty).
    Return: a new list containing each element that appears in both `a` and
        `b`. The order follows the order of first appearance in `a`. Each
        element appears at most once in the result, even if it occurs
        multiple times in `a` or `b`.
    """
    result = []
    for element in a:
        if element in b and element not in result:
            result.append(element)
    return result
