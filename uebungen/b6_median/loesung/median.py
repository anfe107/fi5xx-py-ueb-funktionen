def median(numbers: list[int]) -> float:
    """
    Berechnet den Median (Zentralwert) einer Liste von Zahlen.

    Der Median ist der mittlere Wert bei ungerader Listenlänge,
    oder der Durchschnitt der beiden mittleren Werte bei gerader Länge.

    Vorbedingung: keine (eine leere Liste liefert 0.0 per Konvention).

    Args:
        numbers: Liste von ganzen Zahlen

    Returns:
        float: Der Median als Gleitkommawert

    Examples:
        median([1, 3, 5]) → 3.0 (ungerade Länge, mittleres Element)
        median([1, 2, 3, 4]) → 2.5 (gerade Länge, Durchschnitt der beiden mittleren)
        median([]) → 0.0 (leere Liste)
    """
    if len(numbers) == 0:
        return 0.0

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        # Ungerade Länge: mittleres Element
        middle_index = n // 2
        return float(sorted_numbers[middle_index])
    else:
        # Gerade Länge: Durchschnitt der beiden mittleren Elemente
        middle_left = n // 2 - 1
        middle_right = n // 2
        return (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2.0
