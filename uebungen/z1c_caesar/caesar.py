# ============================================================
# Z1 — Cäsar-Verschlüsselung (Variante C: offen)
# Aufgabentext: aufgaben.md, Abschnitt Z1
#
# Unten steht der ALGORITHMUS DES HAUPTPROGRAMMS in Worten.
# Er beschreibt, WAS zu tun ist — nicht, mit welchen Python-
# Konstrukten. Ihre Aufgabe:
#   1. Übersetzen Sie jeden Schritt in Python (Schleifenform,
#      Abbruch, Fehlerbehandlung und Umbruch wählen Sie selbst).
#   2. Lagern Sie zusammengehörige Blöcke in eigene Funktionen/
#      Prozeduren aus — Namen, Parameter und Rückgabewert
#      entwerfen Sie selbst (mit Type Hints und Docstring).
#   3. Rufen Sie Ihre Funktionen im Hauptprogramm auf.
#
# Cheat-Sheet zu try/except: cheatsheets/cheatsheet_try_except.md
# ============================================================

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


# --- Ihre Funktionen / Prozeduren -------------------------
# TODO: Funktionen hier oberhalb des Hauptprogramms definieren.


# --- Hauptprogramm ----------------------------------------
if __name__ == "__main__":
    # ALGORITHMUS (in Worten — selbst in Python umsetzen):
    #
    #   1. Klartext beschaffen
    #      Fordern Sie einen Klartext an. Akzeptieren Sie ihn erst,
    #      wenn er nicht leer ist und ausschließlich aus Klein-
    #      buchstaben (a–z) besteht — sonst erneut fragen.
    #
    #   2. Verschiebung beschaffen
    #      Fordern Sie eine Verschiebung an. Akzeptieren Sie sie
    #      erst, wenn es sich um eine ganze Zahl handelt — sonst
    #      erneut fragen.
    #
    #   3. Verschlüsseln
    #      Bilden Sie aus dem Klartext den Geheimtext, indem Sie
    #      jeden Buchstaben um die Verschiebung im Alphabet weiter-
    #      rücken. Hinter 'z' geht es bei 'a' weiter.
    #
    #   4. Ausgeben
    #      Geben Sie den Geheimtext aus.
    #
    # TODO: Hauptprogramm umsetzen.
    pass
