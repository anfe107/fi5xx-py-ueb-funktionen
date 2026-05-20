# Szenario: Ein Sachbearbeiter gibt Daten für einen neuen Auftrag
# in das System ein. Bestellmenge, Lieferfrist und Stückpreis werden
# nacheinander abgefragt und auf Plausibilität geprüft.
#
# Code-Smell: Die Prüfung "value <= 0" ist dreimal mit identischer
# Logik vorhanden. Alle drei Felder sind verschieden — aber die Regel
# ist identisch. Eine Änderung (z. B. Mindestmenge auf 5 Stück
# anheben) müsste an drei Stellen gleichzeitig vorgenommen werden.

print("=== Auftragserfassung ===")

quantity = int(input("Bestellmenge (Stück): "))
if quantity <= 0:
    print(f"Fehler: Bestellmenge {quantity} ist ungültig")
else:
    print(f"Bestellmenge: {quantity} Stück")

delivery_days = int(input("Lieferfrist (Tage): "))
if delivery_days <= 0:
    print(f"Fehler: Lieferfrist {delivery_days} ist ungültig")
else:
    print(f"Lieferfrist: {delivery_days} Tage")

price = int(input("Stückpreis (Cent): "))
if price <= 0:
    print(f"Fehler: Stückpreis {price} ist ungültig")
else:
    print(f"Stückpreis: {price} Cent")
