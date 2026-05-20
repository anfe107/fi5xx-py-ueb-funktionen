def digit_sum(n: int) -> int:
    """Compute the sum of the decimal digits of a non-negative integer.

    Approach: take the rightmost digit, add it to a running total, then
    remove that digit from the number, and repeat until no digits remain.

    n: a non-negative integer. Behavior is undefined for negative input.
    Return: sum of the decimal digits. digit_sum(0) returns 0; single-digit
        numbers return themselves.
    """
    # TODO
