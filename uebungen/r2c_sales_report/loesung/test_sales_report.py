# Testfallkatalog R2c — Tagesabschluss:
#
# sum_positive(amounts) -> int
# Nr. | Eingabe               | Erwartet | Begründung
#  1  | [45, -12, 30, 8, -5]  |   83     | Normalfall: gemischte Buchungen
#  2  | []                    |    0     | Randfall: keine Buchungen
#  3  | [-12, -8, -20]        |    0     | Sonderfall: nur Stornierungen
#  4  | [20, 15, 12]          |   47     | Normalfall: alle Beträge positiv
#  5  | [10]                  |   10     | Randfall: ein positiver Eintrag
#  6  | [-5]                  |    0     | Randfall: ein negativer Eintrag
#
# report_category(label, amounts) -> int
# Gibt zusätzlich eine Zeile aus; geprüft wird hier der Rückgabewert
# (die reine Ausgabe lässt sich mit assert nicht direkt prüfen).

from sales_report import sum_positive, report_category


def test_mixed_bookings():
    """Normalfall: Buchungen mit Stornierungen gemischt."""
    assert sum_positive([45, -12, 30, 8, -5]) == 83


def test_empty_list():
    """Randfall: leere Buchungsliste ergibt 0."""
    assert sum_positive([]) == 0


def test_only_cancellations():
    """Sonderfall: ausschließlich Stornierungen."""
    assert sum_positive([-12, -8, -20]) == 0


def test_all_positive():
    """Normalfall: alle Beträge sind positiv."""
    assert sum_positive([20, 15, 12]) == 47


def test_single_positive():
    """Randfall: einelementige Liste mit positivem Betrag."""
    assert sum_positive([10]) == 10


def test_single_cancellation():
    """Randfall: einelementige Liste mit Stornierung."""
    assert sum_positive([-5]) == 0


def test_report_category_returns_total():
    """report_category liefert die Summe der positiven Beträge."""
    assert report_category("Lebensmittel", [45, -12, 30, 8, -5]) == 83


def test_report_category_empty():
    """Randfall: leere Kategorie liefert 0."""
    assert report_category("Leer", []) == 0
