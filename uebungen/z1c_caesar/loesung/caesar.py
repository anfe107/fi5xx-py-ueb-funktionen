# Z1 — Cäsar-Verschlüsselung — Musterlösung
#
# Eine mögliche Zerlegung: je eine Funktion für die beiden
# Einlese-Schleifen, eine zum Verschlüsseln und eine Hilfs-
# funktion für die Position eines Buchstabens im Alphabet.
# Andere sinnvolle Zerlegungen sind ebenso richtig.
#
# Kontrollfrage (siehe aufgaben.md): Warum funktioniert die
# Verschiebung auch bei negativen Werten und bei Werten >= 26?
# Antwort: Der Modulo-Operator % bildet jedes Ergebnis wieder
# auf 0..25 ab. In Python liefert % bei positivem Divisor stets
# ein nicht-negatives Ergebnis, z. B. (-3) % 26 == 23. Damit
# sind der Umbruch nach hinten (große Verschiebung) und nach
# vorn (negative Verschiebung) automatisch abgedeckt.

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def read_plaintext() -> str:
    """Read a plaintext from the console and return it.

    Repeats the prompt until the input is non-empty and contains
    only lowercase letters a-z.
    Return: the validated plaintext.
    """
    while True:
        text = input("Klartext (nur a-z): ")
        valid = True
        if text == "":
            valid = False
        for char in text:
            if char not in ALPHABET:
                valid = False
        if valid:
            return text
        print("Bitte nur Kleinbuchstaben a-z eingeben.")


def read_shift() -> int:
    """Read a shift value from the console and return it as int.

    Repeats the prompt until the input can be converted to an
    integer. Negative values are allowed.
    Return: the validated shift.
    """
    while True:
        entry = input("Verschiebung (ganze Zahl): ")
        try:
            return int(entry)
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")


def letter_position(letter: str) -> int:
    """Return the index of a lowercase letter within ALPHABET.

    letter: a single character from a-z.
    Return: its position (0 for 'a', 25 for 'z').
    """
    for i in range(len(ALPHABET)):
        if ALPHABET[i] == letter:
            return i
    return -1


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text with a Caesar shift and return the ciphertext.

    text: the plaintext (lowercase letters a-z).
    shift: the number of positions to move each letter.
    Return: the encrypted text.
    """
    result = ""
    for char in text:
        pos = letter_position(char)
        new_pos = (pos + shift) % len(ALPHABET)
        result = result + ALPHABET[new_pos]
    return result


if __name__ == "__main__":
    plaintext = read_plaintext()
    shift = read_shift()
    ciphertext = caesar_encrypt(plaintext, shift)
    print(f"Geheimtext: {ciphertext}")
