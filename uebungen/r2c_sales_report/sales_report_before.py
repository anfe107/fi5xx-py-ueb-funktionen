# Szenario: Tagesabschluss einer Filiale. Für drei Produktkategorien
# liegen Buchungsbeträge vor. Negative Einträge sind Stornierungen und
# fließen nicht in die Summe ein. Am Ende wird zusätzlich die
# Gesamtsumme über alle Kategorien ausgegeben.
#
# Code-Smell: Hier steckt mehr als eine Redundanz.
#  (a) Die Filter-Summen-Logik (nur positive Beträge aufsummieren) steht
#      gleich viermal da — für jede Kategorie und noch einmal für die
#      Gesamtsumme.
#  (b) Das Muster "Summe berechnen und Zeile ausgeben" wiederholt sich
#      für jede Kategorie.

print("=== Tagesabschluss ===")

food_bookings = [45, -12, 30, 8, -5]
food_total = 0
for amount in food_bookings:
    if amount > 0:
        food_total = food_total + amount
print(f"Lebensmittel: {food_total} EUR")

drinks_bookings = [20, 15, -8, 12]
drinks_total = 0
for amount in drinks_bookings:
    if amount > 0:
        drinks_total = drinks_total + amount
print(f"Getränke: {drinks_total} EUR")

nonfood_bookings = [60, -20, 35, -10, 25, 10]
nonfood_total = 0
for amount in nonfood_bookings:
    if amount > 0:
        nonfood_total = nonfood_total + amount
print(f"Non-Food: {nonfood_total} EUR")

# Gesamtsumme über alle Kategorien
grand_total = 0
for amount in food_bookings:
    if amount > 0:
        grand_total = grand_total + amount
for amount in drinks_bookings:
    if amount > 0:
        grand_total = grand_total + amount
for amount in nonfood_bookings:
    if amount > 0:
        grand_total = grand_total + amount
print(f"Gesamt: {grand_total} EUR")
