# Übungsaufgaben zum Thema Funktionen und UNIT-Testing

Ziel: Wiederholung vor/ Klausurvorbereitung für SuD-Klausur-2: kurze, voneinander unabhängige Übungen zu Funktionen, Tests und Listen.

Alle Aufgabentexte und Testfallkataloge stehen gesammelt in [aufgaben.md](aufgaben.md).

## Übungen

| Nr. | Niveau | Funktion               | Thema                                       | Code                                                          | Lösung                                         |
| --- | ------ | ---------------------- | ------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------- |
| A1  | ✦      | `count_vowels`         | Vokale in einem Wort zählen                 | [→](uebungen/a1_count_vowels/count_vowels.py)                 | [→](uebungen/a1_count_vowels/loesung/)         |
| A2  | ✦      | `sum_list`             | Summe einer Zahlenliste                     | [→](uebungen/a2_sum_list/sum_list.py)                         | [→](uebungen/a2_sum_list/loesung/)             |
| A3  | ✦      | `is_even`              | Prüfung auf gerade Zahl                     | [→](uebungen/a3_is_even/is_even.py)                           | [→](uebungen/a3_is_even/loesung/)              |
| B1  | ✦✦     | `digit_sum`            | Quersumme einer Zahl                        | [→](uebungen/b1_digit_sum/digit_sum.py)                       | [→](uebungen/b1_digit_sum/loesung/)            |
| B2  | ✦✦     | `contains_duplicates`  | Duplikate in einer Liste                    | [→](uebungen/b2_contains_duplicates/contains_duplicates.py)   | [→](uebungen/b2_contains_duplicates/loesung/)  |
| B3  | ✦✦     | `common_elements`      | Schnittmenge zweier Listen                  | [→](uebungen/b3_common_elements/common_elements.py)           | [→](uebungen/b3_common_elements/loesung/)      |
| B4  | ✦✦     | `is_prime`             | Primzahltest                                | [→](uebungen/b4_is_prime/is_prime.py)                         | [→](uebungen/b4_is_prime/loesung/)             |
| B5  | ✦✦     | `clamp`                | Wert auf Intervall einschränken             | [→](uebungen/b5_clamp/clamp.py)                               | [→](uebungen/b5_clamp/loesung/)                |
| B6  | ✦✦     | `median`               | Median einer Zahlenliste                    | [→](uebungen/b6_median/median.py)                             | [→](uebungen/b6_median/loesung/)               |
| C1  | ✦✦✦    | `longest_word_split`   | Längstes Wort eines Satzes                  | [→](uebungen/c1_longest_word_split/longest_word_split.py)     | [→](uebungen/c1_longest_word_split/loesung/)   |
| C2  | ✦✦✦    | `reverse_number`       | Ziffern einer Zahl umkehren                 | [→](uebungen/c2_reverse_number/reverse_number.py)             | [→](uebungen/c2_reverse_number/loesung/)       |
| C3  | ✦✦✦    | `most_frequent_letter` | Häufigster Buchstabe in einem Wort          | [→](uebungen/c3_most_frequent_letter/most_frequent_letter.py) | [→](uebungen/c3_most_frequent_letter/loesung/) |
| C4  | ✦✦✦    | `run_length_encode`    | Lauflängen-Kodierung eines Texts            | [→](uebungen/c4_run_length_encode/run_length_encode.py)       | [→](uebungen/c4_run_length_encode/loesung/)    |
| R1b | ✦✦     | `is_positive`          | Auftragserfassung (Refactoring, geführt)    | [→](uebungen/r1b_order_input/order_input.py)                 | [→](uebungen/r1b_order_input/loesung/)         |
| R2c | ✦✦✦    | `sum_positive`, `report_category` | Tagesabschluss (Refactoring, offen) | [→](uebungen/r2c_sales_report/sales_report.py)               | [→](uebungen/r2c_sales_report/loesung/)        |
| Z1b | ✦✦     | —                      | Cäsar-Verschlüsselung (Zerlegung, geführt)  | [→](uebungen/z1b_caesar/caesar.py)                           | [→](uebungen/z1b_caesar/loesung/)              |
| Z1c | ✦✦✦    | —                      | Cäsar-Verschlüsselung (Zerlegung, offen)    | [→](uebungen/z1c_caesar/caesar.py)                           | [→](uebungen/z1c_caesar/loesung/)              |

## Struktur

- `uebungen/<niveau><nr>_<thema>/` — eine Übung pro Ordner (Codegerüst, Tests, Lösung)
- `aufgaben.md` — zentrale Sammlung aller Aufgabentexte und Testfallkataloge
- `cheatsheets/` — Nachschlagewerk (Funktionen, Listen, Schleifen, Strings, Tupel, Zahlen, pytest, try/except)
- `klausur/` — Aufgaben für Klausur-Sammlungen (Schüler bearbeiten diese nicht als reguläre Übung)
- `reste/` — Archivierte Aufgaben für Reserve / Nachschlag

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pytest
```

## Tests ausführen

Im jeweiligen Übungsordner:

```bash
python -m pytest
```

## Lösungen

Jede Übung enthält einen `loesung/`-Ordner mit Musterimplementierung und vollständigen Tests — bewusst sichtbar zur Selbstkontrolle.

## Niveaus

| Niveau | Schwerpunkt                                     |
| ------ | ----------------------------------------------- |
| ✦      | Funktion gegen vorgegebene Tests implementieren |
| ✦✦     | Funktion implementieren und selbst testen       |
| ✦✦✦    | Komposition, algorithmisches Denken, Reflexion  |
