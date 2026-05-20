# Leitfragen — Antworten:
#
# 1. Wer ruft die Funktion(en) auf — und mit welchen Werten?
#    Das Hauptskript ruft report_category mit einem Kategorienamen (str)
#    und einer Liste von Buchungsbeträgen (list[int]) auf. report_category
#    selbst ruft sum_positive mit der Betragsliste auf.
#
# 2. Welche Information braucht jede Funktion?
#    sum_positive: nur die Liste der Beträge. report_category: zusätzlich
#    den Anzeigenamen der Kategorie. Die Filterregel (> 0) ist eine feste
#    Geschäftsregel — kein Parameter, sondern Bedingung im Body.
#
# 3. Was ist im Ausgangscode redundant?
#    Zwei Dinge: (a) die Filter-Summen-Schleife steht für jede Kategorie
#    UND für die Gesamtsumme da; (b) "Summe berechnen und Zeile ausgeben"
#    wiederholt sich pro Kategorie.
#
# 4. Wie könnten die Funktionen benannt werden?
#    sum_positive (Summe der positiven Beträge) und report_category (gibt
#    die Zeile einer Kategorie aus und liefert deren Summe zurück).
#    report_category hängt von sum_positive ab; die Gesamtsumme entsteht,
#    indem die Rückgabewerte aufaddiert werden — so wird jede Summe nur
#    einmal berechnet.

def sum_positive(amounts: list[int]) -> int:
    """Sum all positive elements in a list of integers.

    Parameter amounts: list of integers to process.
    Returns the sum of all elements greater than zero.
    Returns 0 for an empty list or a list with no positive elements.
    """
    total = 0
    for amount in amounts:
        if amount > 0:
            total = total + amount
    return total


def report_category(label: str, amounts: list[int]) -> int:
    """Print the report line for one category and return its total.

    Parameter label: the display name of the category.
    Parameter amounts: the booking amounts of the category.
    Returns the category total (sum of the positive amounts).
    """
    total = sum_positive(amounts)
    print(f"{label}: {total} EUR")
    return total


# Refaktorierter Ausgangscode: Tagesabschluss mit den neuen Funktionen
print("=== Tagesabschluss ===")

food_bookings = [45, -12, 30, 8, -5]
drinks_bookings = [20, 15, -8, 12]
nonfood_bookings = [60, -20, 35, -10, 25, 10]

grand_total = 0
grand_total = grand_total + report_category("Lebensmittel", food_bookings)
grand_total = grand_total + report_category("Getränke", drinks_bookings)
grand_total = grand_total + report_category("Non-Food", nonfood_bookings)
print(f"Gesamt: {grand_total} EUR")
