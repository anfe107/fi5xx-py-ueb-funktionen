# ============================================================
# Z1 — Cäsar-Verschlüsselung (Variante B: geführt)
# Aufgabentext: aufgaben.md, Abschnitt Z1
#
# Unten steht der vollständige ALGORITHMUS DES HAUPTPROGRAMMS
# als Pseudocode. Ihre Aufgabe:
#   1. Erkennen Sie zusammengehörige Blöcke (die beiden
#      Einlese-Schleifen, das Verschlüsseln) und lagern Sie
#      sie in eigene Funktionen/Prozeduren aus.
#   2. Entwerfen Sie für jede Funktion SELBST Namen, Parameter
#      und Rückgabewert — mit Type Hints und Docstring.
#   3. Rufen Sie Ihre Funktionen im Hauptprogramm auf.
#
# Cheat-Sheet zu try/except: cheatsheets/cheatsheet_try_except.md
# ============================================================

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


# --- Ihre Funktionen / Prozeduren -------------------------
# TODO: Funktionen hier oberhalb des Hauptprogramms definieren.


# --- Hauptprogramm ----------------------------------------
if __name__ == "__main__":
    # ALGORITHMUS (Pseudocode — durch Aufrufe Ihrer Funktionen ersetzen):
    #
    #   1) Klartext einlesen — Schleife, bis nur a–z enthalten
    #   while True:
    #       klartext ← Eingabe "Klartext (nur a–z): "
    #       gueltig  ← WAHR
    #       WENN klartext leer: gueltig ← FALSCH
    #       FÜR jedes zeichen in klartext:
    #           WENN zeichen NICHT in ALPHABET: gueltig ← FALSCH
    #       WENN gueltig: break
    #
    #   2) Verschiebung einlesen — Schleife, bis eine ganze Zahl kommt
    #   while True:
    #       eingabe ← Eingabe "Verschiebung (ganze Zahl): "
    #       try:    verschiebung ← int(eingabe); break
    #       except ValueError:  Hinweis ausgeben
    #
    #   3) Verschlüsseln
    #   geheimtext ← ""
    #   FÜR jedes zeichen in klartext:
    #       pos        ← Position von zeichen in ALPHABET
    #       neue_pos   ← (pos + verschiebung) MODULO 26
    #       geheimtext ← geheimtext + ALPHABET[neue_pos]
    #
    #   4) geheimtext ausgeben
    #
    # TODO: Hauptprogramm umsetzen.
    pass
