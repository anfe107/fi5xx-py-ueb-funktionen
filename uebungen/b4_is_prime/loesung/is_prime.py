def is_prime(n: int) -> bool:
    """Check whether the integer is a prime number.

    n: an integer with n >= 2.
    Return: True if n is prime; False otherwise.
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
