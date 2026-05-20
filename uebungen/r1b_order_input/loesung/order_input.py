# Leitfragen — Antworten:
#
# 1. Wer ruft die Funktion auf — und mit welchen Werten?
#    Das Hauptskript mit quantity, delivery_days und price — je eine
#    ganze Zahl, direkt aus int(input(...)).
#
# 2. Welche Information braucht die Funktion?
#    Nur den zu prüfenden Wert (eine ganze Zahl). Die Regel "> 0" ist
#    eine feste Geschäftsregel — kein Parameter, sondern Konstante im Body.
#
# 3. Was ist im Ausgangscode redundant?
#    Die Bedingung "value <= 0" taucht dreimal identisch auf — für Menge,
#    Lieferfrist und Preis. Alle drei prüfen dasselbe: ist der Wert positiv?
#
# 4. Wie könnte die Funktion sinnvoll benannt werden?
#    is_positive — formuliert als Ja/Nein-Frage (is_…), englisch,
#    drückt direkt den bool-Rückgabewert und die geprüfte Eigenschaft aus.


def is_positive(value: int) -> bool:
    """Check if value is a positive integer (greater than zero).

    Parameter value: the integer to check.
    Returns True if value is greater than 0, False otherwise.
    """
    if value > 0:
        return True
    return False


# Refaktorierter Ausgangscode: Auftragserfassung mit der neuen Funktion
print("=== Auftragserfassung ===")

quantity = int(input("Bestellmenge (Stück): "))
if is_positive(quantity):
    print(f"Bestellmenge: {quantity} Stück")
else:
    print(f"Fehler: Bestellmenge {quantity} ist ungültig")

delivery_days = int(input("Lieferfrist (Tage): "))
if is_positive(delivery_days):
    print(f"Lieferfrist: {delivery_days} Tage")
else:
    print(f"Fehler: Lieferfrist {delivery_days} ist ungültig")

price = int(input("Stückpreis (Cent): "))
if is_positive(price):
    print(f"Stückpreis: {price} Cent")
else:
    print(f"Fehler: Stückpreis {price} ist ungültig")
