def sum_list(numbers: list[int]) -> int:
    """Compute the sum of all integers in the list.

    numbers: list of integers (may be empty).
    Return: sum of all elements; 0 if the list is empty.
    """
    total = 0
    for number in numbers:
        total = total + number
    return total
