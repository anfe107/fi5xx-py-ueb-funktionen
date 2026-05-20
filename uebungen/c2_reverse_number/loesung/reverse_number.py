def reverse_number(n: int) -> int:
    """Reverse the decimal digits of a non-negative integer.

    n: a non-negative integer.
    Return: the integer formed by reversing the digits of n. Trailing zeros
        are lost — reverse_number(1000) returns 1, not 0001.
        reverse_number(0) returns 0; single-digit numbers return themselves.
    """
    reversed_value = 0
    while n > 0:
        reversed_value = reversed_value * 10 + n % 10
        n = n // 10
    return reversed_value
