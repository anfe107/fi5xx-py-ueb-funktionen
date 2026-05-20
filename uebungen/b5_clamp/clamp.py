def clamp(value: int, lower: int = 0, upper: int = 100) -> int:
    """Restrict `value` to the closed interval [lower, upper].

    value: the integer to restrict.
    lower: lower bound (default 0).
    upper: upper bound (default 100). Must satisfy lower <= upper.
    Return: `value` if it lies within [lower, upper]; otherwise the nearer
        bound — `lower` if value is too small, `upper` if value is too large.
    """
    # TODO
