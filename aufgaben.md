# Aufgaben

Gegliedert nach Niveau und laufender Nummer. Setup, Test-Workflow und Niveau-Schema stehen in der [README](README.md); Cheat-Sheets liegen in [`cheatsheets/`](cheatsheets/).

**Tests ausführen** (in jedem Übungsordner): `python -m pytest`. An den Test-Dateien für **Niveau 1** nichts ändern; in **Niveau 2** und **3** ergänzen Sie eigene Testfälle gemäß Aufgabentext.

---

## A1 — Vokale zählen ✦

[`count_vowels.py`](uebungen/a1_count_vowels/count_vowels.py) · [Lösung](uebungen/a1_count_vowels/loesung/)

**Kontext.** Erste Berührung mit dem Muster „Schleife über Zeichen + Bedingung + Zähler". Ein Vokal-Zähler ist eines der einfachsten Werkzeuge der Textverarbeitung — etwa als Hilfsfunktion für einfache Lesbarkeits-Heuristiken oder als Baustein in größeren Anwendungen.

**Aufgabe.** Implementieren Sie die Funktion `count_vowels(word: str) -> int`. Die Funktion zählt die Vokale (a, e, i, o, u) im übergebenen Wort. Groß- und Kleinschreibung **nicht** unterscheiden — `"A"` zählt genauso wie `"a"`. Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.**

| Nr. | Eingabe           | Erwartete Ausgabe | Begründung                                              |
| --- | ----------------- | ----------------- | ------------------------------------------------------- |
| 1   | `"Hallo"`         | `2`               | Normalfall: gemischtes Wort mit zwei Vokalen            |
| 2   | `""`              | `0`               | Randfall: leerer String                                 |
| 3   | `"xyz"`           | `0`               | Normalfall: Wort ohne Vokal                             |
| 4   | `"AEIOU"`         | `5`               | Sonderfall: alle Zeichen sind Großbuchstaben-Vokale     |
| 5   | `"Programmieren"` | `5`               | Normalfall: längeres Wort mit Groß- und Kleinbuchstaben |

---

## A2 — Liste summieren ✦

[`sum_list.py`](uebungen/a2_sum_list/sum_list.py) · [Lösung](uebungen/a2_sum_list/loesung/)

**Kontext.** Klassische Akkumulator-Schleife: einen Zählwert über eine Liste hochsummieren. Grundbaustein für Statistik, Zwischensummen oder Bewertungs-Aggregationen — und das einfachste Beispiel dafür, dass eine Funktion mit „leerer Eingabe" einen sinnvollen Defaultwert zurückgeben muss.

**Aufgabe.** Implementieren Sie die Funktion `sum_list(numbers: list[int]) -> int`. Die Funktion summiert alle ganzen Zahlen der übergebenen Liste. Bei einer leeren Liste ist das Ergebnis `0`. Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.**

| Nr. | Eingabe          | Erwartete Ausgabe | Begründung                                                    |
| --- | ---------------- | ----------------- | ------------------------------------------------------------- |
| 1   | `[1, 2, 3]`      | `6`               | Normalfall: kleine Liste mit positiven Zahlen                 |
| 2   | `[]`             | `0`               | Randfall: leere Liste                                         |
| 3   | `[42]`           | `42`              | Randfall: einelementige Liste                                 |
| 4   | `[-1, 1, -2, 2]` | `0`               | Sonderfall: Summe aus negativen und positiven Zahlen ergibt 0 |
| 5   | `[-5, -10, -3]`  | `-18`             | Normalfall: alle Zahlen negativ                               |

---

## A3 — Gerade Zahl ✦

[`is_even.py`](uebungen/a3_is_even/is_even.py) · [Lösung](uebungen/a3_is_even/loesung/)

**Kontext.** Die Prüfung „ist die Zahl gerade?" ist die einfachste praktische Anwendung des Modulo-Operators. Sie taucht überall dort auf, wo etwas in zwei Hälften aufgeteilt wird — abwechselnde Sortierung, Hashing, Paritätsbits oder einfache Spielzüge.

**Aufgabe.** Implementieren Sie die Funktion `is_even(n: int) -> bool`. Die Funktion liefert `True`, wenn `n` durch 2 teilbar ist; sonst `False`. Negative Zahlen und Null sind zulässige Eingaben — `0` gilt als gerade. Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.** Vervollständigen Sie die Spalte _Begründung_.

| Nr. | Eingabe | Erwartete Ausgabe | Begründung |
| --- | ------- | ----------------- | ---------- |
| 1   | `4`     | `True`            |            |
| 2   | `7`     | `False`           |            |
| 3   | `0`     | `True`            |            |
| 4   | `-2`    | `True`            |            |
| 5   | `-3`    | `False`           |            |

---

## B1 — Quersumme ✦✦

[`digit_sum.py`](uebungen/b1_digit_sum/digit_sum.py) · [Lösung](uebungen/b1_digit_sum/loesung/)

**Kontext.** Die Quersumme einer Zahl ist die Summe ihrer Dezimalziffern: aus `123` wird `1 + 2 + 3 = 6`. Sie ist Baustein in Teilbarkeitsregeln (eine Zahl ist durch 3 teilbar, genau wenn ihre Quersumme es ist) und in einfachen Prüfziffer-Verfahren.

**Aufgabe.** Implementieren Sie die Funktion `digit_sum(n: int) -> int`. Die Funktion liefert die Summe der Dezimalziffern von `n`. Vorbedingung: `n ≥ 0` (im Docstring festgehalten). Einstellige Zahlen liefern sich selbst, `digit_sum(0)` liefert `0`. Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

> Hinweis: Mit `n % 10` erhalten Sie die letzte Dezimalstelle von `n` — `123 % 10` ergibt `3`. Mit `n // 10` entfernen Sie diese letzte Stelle — `123 // 10` ergibt `12`. Wiederholen Sie dieses Muster in einer Schleife, bis keine Stellen mehr übrig sind.

**Schreibtischtest.** Verfolgen Sie die Ausführung von `digit_sum(123)` Schritt für Schritt — bevor Sie mit der Implementierung beginnen.

| Durchlauf | `n` | `n > 0` | `n % 10` | `total` | neues `n` |
| --------- | --- | ------- | -------- | ------- | --------- |
| —         | 123 | —       | —        | 0       | —         |
| 1         | 123 | wahr    | 3        | 3       | 12        |
| 2         | 12  | wahr    |          |         |           |
| 3         |     |         |          |         |           |
| Ende      | 0   | falsch  | —        |         | —         |

**Testfallkatalog.** Vervollständigen Sie die Spalte _Begründung_.

| Nr. | Eingabe | Erwartete Ausgabe | Begründung |
| --- | ------- | ----------------- | ---------- |
| 1   | `123`   | `6`               |            |
| 2   | `0`     | `0`               |            |
| 3   | `5`     | `5`               |            |
| 4   | `9999`  | `36`              |            |
| 5   | `1000`  | `1`               |            |

---

## B2 — Duplikate prüfen ✦✦

[`contains_duplicates.py`](uebungen/b2_contains_duplicates/contains_duplicates.py) · [Lösung](uebungen/b2_contains_duplicates/loesung/)

**Kontext.** Eine Eingabeliste auf Doppelvorkommen prüfen ist ein wiederkehrendes Muster — etwa bei der Validierung von eindeutigen Schlüsseln, Sitzplatznummern oder Benutzer-IDs. Zwei klassische Lösungswege stehen zur Auswahl: eine Doppelschleife (jedes Paar vergleichen) oder eine Hilfsliste „schon gesehen", die in einer einfachen Schleife wächst.

**Aufgabe.** Implementieren Sie die Funktion `contains_duplicates(elements: list[int]) -> bool`. Die Funktion liefert `True`, wenn mindestens ein Element mehrfach in der Liste vorkommt; sonst `False`. Eine leere Liste liefert `False`. Beide oben skizzierten Lösungswege sind zulässig. Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.** Füllen Sie die Tabelle vor dem Implementieren aus (mindestens je ein Normalfall, Randfall und Sonderfall) und übertragen Sie sie nach `test_contains_duplicates.py`.

| Nr. | Eingabe        | Erwartete Ausgabe | Begründung                  |
| --- | -------------- | ----------------- | --------------------------- |
| 1   | `[1, 2, 3]`    | `False`           | Normalfall: keine Duplikate |
| 2   | `[1, 9, 9]`    | `True`            | Normalfall: ein Duplikat    |
| 3   | `[5, 5, 5]`    | `True`            | Normalfall: zwei Duplikate  |
| 4   | `[]`           | `False`           | Sonderfall: leere Liste     |
| 5   | `[1, 11, 111]` | `False`           | Normalfall: keine Duplikate |
|     |                |                   |                             |

---

## B3 — Gemeinsame Elemente ✦✦

[`common_elements.py`](uebungen/b3_common_elements/common_elements.py) · [Lösung](uebungen/b3_common_elements/loesung/)

**Kontext.** Die Schnittmenge zweier Listen zu bilden ist ein wiederkehrendes Muster — etwa „welche Tags haben zwei Beiträge gemeinsam?" oder „welche Module sind sowohl im Standard- als auch im Wahlpflichtbereich vorgesehen?". Ohne Mengen-Datentyp aus der Baseline löst man die Aufgabe mit `in` und einer Ergebnisliste, die schrittweise wächst.

**Aufgabe.** Implementieren Sie die Funktion `common_elements(a: list[int], b: list[int]) -> list[int]`. Die Funktion liefert eine neue Liste mit allen Elementen, die in **beiden** Eingabelisten vorkommen.

Spezifikationen:

- Reihenfolge: wie das Element zuerst in `a` auftritt.
- Duplikate: jedes Element steht im Ergebnis **höchstens einmal**, auch wenn es in `a` oder `b` mehrfach vorkommt.
- Ist eine der beiden Listen leer, ist das Ergebnis die leere Liste.

Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.** Füllen Sie die Tabelle vor dem Implementieren aus (mindestens je ein Normalfall, Randfall und Sonderfall) und übertragen Sie sie nach `test_common_elements.py`.

| Nr. | Eingabe                  | Erwartete Ausgabe | Begründung                          |
| --- | ------------------------ | ----------------- | ----------------------------------- |
| 1   | `([1, 2, 3], [2, 3, 4])` | `[2, 3]`          | Normalfall: einfache Überschneidung |
|     |                          |                   |                                     |

---

## B4 — Primzahltest ✦✦

[`is_prime.py`](uebungen/b4_is_prime/is_prime.py) · [Lösung](uebungen/b4_is_prime/loesung/)

**Kontext.** Eine Primzahl ist eine ganze Zahl ≥ 2, die nur durch 1 und sich selbst teilbar ist. Primzahltests sind Bausteine in der Kryptografie, in Hashing-Verfahren und in der Zahlentheorie. Algorithmisch sind sie ein Standardbeispiel für eine Schleife mit **Frühausstieg** — sobald ein Teiler gefunden ist, kann die Funktion sofort `False` zurückgeben.

**Aufgabe.** Implementieren Sie die Funktion `is_prime(n: int) -> bool`. Die Funktion liefert `True`, wenn `n` eine Primzahl ist; sonst `False`. Vorbedingung: `n ≥ 2` (im Docstring festgehalten). Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.** Füllen Sie die Tabelle vor dem Implementieren aus (mindestens je ein Normalfall, Randfall und Sonderfall) und übertragen Sie sie nach `test_is_prime.py`.

| Nr. | Eingabe | Erwartete Ausgabe | Begründung                  |
| --- | ------- | ----------------- | --------------------------- |
| 1   | `7`     | `True`            | Normalfall: kleine Primzahl |
|     |         |                   |                             |

---

## B5 — Wert einschränken ✦✦

[`clamp.py`](uebungen/b5_clamp/clamp.py) · [Lösung](uebungen/b5_clamp/loesung/)

**Kontext.** „Clamping" — einen Zahlwert auf ein erlaubtes Intervall einzuschränken — ist ein klassischer Baustein in der Grafikprogrammierung (Farbwerte zwischen 0 und 255), in Spielen (Lebensanzeige zwischen 0 und 100) und in der Behandlung von Benutzereingaben (Lautstärke, Prozentwerte). Methodisch führt diese Aufgabe ein neues Sprachfeature ein: **Default-Werte für Parameter**.

**Neu in dieser Übung — Default-Werte für Parameter.** Funktionsparameter dürfen einen Default-Wert tragen, der greift, wenn beim Aufruf kein Argument für diesen Parameter angegeben wird:

```python
def clamp(value: int, lower: int = 0, upper: int = 100) -> int:
    ...

clamp(50)                   # nutzt die Defaults: lower=0, upper=100   → 50
clamp(150)                  # nutzt die Defaults                       → 100
clamp(15, 10, 20)           # alle drei Argumente explizit             → 15
```

Parameter mit Default-Werten stehen in der Signatur **nach** allen Parametern ohne Default. Details und Tellerrand siehe [`cheatsheet_funktionen.md`](cheatsheets/cheatsheet_funktionen.md).

**Aufgabe.** Implementieren Sie die Funktion `clamp(value: int, lower: int = 0, upper: int = 100) -> int`. Die Funktion liefert `value` zurück, wenn dieser zwischen `lower` und `upper` einschließlich liegt; ist `value` darunter, wird `lower` geliefert, darüber `upper`. Vorbedingung: `lower ≤ upper`. Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.** Füllen Sie die Tabelle vor dem Implementieren aus (mindestens je ein Normalfall, Randfall und Sonderfall) und übertragen Sie sie nach `test_clamp.py`. Decken Sie **beide** Aufrufformen ab — solche, die die Default-Werte nutzen (`clamp(50)`), und solche, die alle drei Argumente explizit setzen (`clamp(15, 10, 20)`).

| Nr. | Eingabe     | Erwartete Ausgabe | Begründung                                      |
| --- | ----------- | ----------------- | ----------------------------------------------- |
| 1   | `clamp(50)` | `50`              | Normalfall: Wert innerhalb des Default-Bereichs |
|     |             |                   |                                                 |

---

## B6 — Median ✦✦

[`median.py`](uebungen/b6_median/median.py) · [Lösung](uebungen/b6_median/loesung/)

**Kontext.** Der Median (Zentralwert) ist eine klassische Lagemaß-Statistik: nach Sortierung der Werte ist der Median das mittlere Element (bei ungerader Länge) oder der Durchschnitt der beiden mittleren Elemente (bei gerader Länge). Im Gegensatz zum arithmetischen Mittelwert (B-Niveau in klausur) ist der Median robust gegen Ausreißer — eine wichtige Eigenschaft in der Datenanalyse.

**Neue Funktion für diese Übung — `sorted()`** erzeugt eine neue, sortierte Liste aus einer bestehenden:

```python
sorted([3, 1, 4, 1, 5])    # [1, 1, 3, 4, 5]
sorted([5, 2, 8, 1])       # [1, 2, 5, 8]
sorted([])                 # []
```

Die ursprüngliche Liste bleibt unverändert. Wenn die Liste nur ein oder zwei Elemente hat, ist `sorted()` sehr einfach zu handhaben.

> **Tellerrand — Python vs. C#/Java:** In Python ist `sorted()` eine eingebaute Funktion für beliebige Sequenzen. In C# heißt das Pendant `LINQ .OrderBy()` oder `Array.Sort()`; in Java `Arrays.sort()` oder Stream-API.

**Aufgabe.** Implementieren Sie die Funktion `median(numbers: list[int]) -> float`. Die Funktion liefert den Median der Zahlenliste.

Spezifikationen:

- Ungerade Listenlänge: Rückgabe ist die mittlere Zahl **als `float`** (z. B. `[1, 3, 5]` → `3.0`).
- Gerade Listenlänge: Rückgabe ist der Durchschnitt der beiden mittleren Zahlen (z. B. `[1, 2, 3, 4]` → `2.5`).
- Leere Liste: Rückgabe ist per Konvention `0.0`.

Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Schreibtischtest.** Verfolgen Sie die Ausführung von `median([3, 1, 4, 1, 5])` Schritt für Schritt — bevor Sie mit der Implementierung beginnen.

| Schritt | original | nach `sorted()` | Länge | Mitte-Index(e) | Median-Berechnung | Ergebnis |
| ------- | -------- | --------------- | ----- | -------------- | ----------------- | -------- |
| —       | [3,1,4,1,5] | —            | —     | —              | —                 | —        |
| 1       |          | [1,1,3,4,5]     | 5     | 2              | `sorted[2]`       | 3.0      |

**Testfallkatalog.** Vervollständigen Sie die Spalte _Begründung_.

| Nr. | Eingabe        | Erwartete Ausgabe | Begründung |
| --- | -------------- | ----------------- | ---------- |
| 1   | `[3, 1, 4, 1, 5]` | `3.0`          |            |
| 2   | `[1, 2, 3, 4]` | `2.5`             |            |
| 3   | `[42]`         | `42.0`            |            |
| 4   | `[]`           | `0.0`             |            |
| 5   | `[5, 5, 5]`    | `5.0`             |            |

---

## C1 — Längstes Wort ✦✦✦

[`longest_word_split.py`](uebungen/c1_longest_word_split/longest_word_split.py) · [Lösung](uebungen/c1_longest_word_split/loesung/)

**Kontext.** Aus einem Satz das längste Wort herauszufinden ist Standard-Repertoire jeder Textverarbeitung — etwa für einfache Lesbarkeits-Heuristiken oder zur Auswahl markanter Begriffe. Diese Übung verwendet die String-Methode `.split()`, um den Satz an Leerzeichen in eine Liste von Wörtern zu zerlegen, und führt anschließend die bekannte „Maximum mitführen"-Schleife durch.

**Neue Methode für diese Übung — `.split()`.** Wird mit einem Aufruf an einem String verwendet und liefert eine **Liste** der durch Leerzeichen getrennten Wörter:

```python
"hello world".split()           # ["hello", "world"]
"alles".split()                 # ["alles"]
"".split()                      # []
```

> **Tellerrand — Python vs. C#/Java:** In Python ist `.split()` eine Methode am String-Objekt und liefert direkt eine Liste. In C# heißt das Pendant `string.Split(...)` und liefert ein Array (`string[]`); in Java `String.split(...)` ebenfalls ein Array.

**Aufgabe.** Implementieren Sie die Funktion `longest_word_split(sentence: str) -> str`. Die Funktion liefert das längste Wort des Satzes. Sind mehrere Wörter gleich lang, wird das **erste** zurückgegeben. Bei einem leeren Satz ist das Ergebnis der leere String `""`. Verwenden Sie `.split()` zum Zerlegen des Satzes. Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.** Füllen Sie die Tabelle vor dem Implementieren aus (mindestens je ein Normalfall, Randfall und Sonderfall) und übertragen Sie sie nach `test_longest_word_split.py`.

| Nr. | Eingabe      | Erwartete Ausgabe | Begründung                               |
| --- | ------------ | ----------------- | ---------------------------------------- |
| 1   | `"hi world"` | `"world"`         | Normalfall: zwei Wörter, längstes hinten |
|     |              |                   |                                          |

---

## C2 — Zahl umkehren ✦✦✦

[`reverse_number.py`](uebungen/c2_reverse_number/reverse_number.py) · [Lösung](uebungen/c2_reverse_number/loesung/)

**Kontext.** Die Ziffern einer Zahl umzukehren — aus `123` wird `321` — taucht in einfachen Spielereien (Zahlenrätsel) ebenso auf wie als Vorstufe zu Palindrom-Tests oder einfachen Verschlüsselungen. Methodisch ist es eine Variation des Quersummen-Patterns aus B1: eine Ziffer extrahieren, sie an das richtige Ende des Ergebnisses anbauen, und die Ausgangszahl um eine Stelle verkürzen.

**Aufgabe.** Implementieren Sie die Funktion `reverse_number(n: int) -> int`. Vorbedingung: `n ≥ 0`. Beachten Sie: **Nachgestellte Nullen gehen verloren** — `reverse_number(1000)` liefert `1`, weil `0001` als Zahl ebenfalls `1` ist. Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.** Füllen Sie die Tabelle vor dem Implementieren aus (mindestens je ein Normalfall, Randfall und Sonderfall) und übertragen Sie sie nach `test_reverse_number.py`.

| Nr. | Eingabe | Erwartete Ausgabe | Begründung              |
| --- | ------- | ----------------- | ----------------------- |
| 1   | `123`   | `321`             | Normalfall: dreistellig |
|     |         |                   |                         |

---

## C3 — Häufigster Buchstabe ✦✦✦

[`most_frequent_letter.py`](uebungen/c3_most_frequent_letter/most_frequent_letter.py) · [Lösung](uebungen/c3_most_frequent_letter/loesung/)

**Kontext.** Den häufigsten Buchstaben eines Wortes zu bestimmen ist ein Klassiker der Statistik — etwa für Textanalyse, einfache Häufigkeitsverteilungen oder als Vorstufe zu Frequenzanalyse-Verfahren. Ohne Dictionaries (außerhalb der Baseline) entsteht die Lösung aus einer **äußeren** Schleife über Kandidaten-Zeichen und einer **inneren** Schleife zum Zählen — eine zweifach-geschachtelte Struktur, die in N3 typisch ist.

**Aufgabe.** Implementieren Sie die Funktion `most_frequent_letter(word: str) -> str`. Die Funktion liefert das Zeichen, das im Wort am häufigsten vorkommt.

Spezifikationen:

- Tie-Break: Bei mehreren Zeichen mit gleicher Maximalhäufigkeit gewinnt das **zuerst** auftretende.
- Leeres Wort: Rückgabe ist der leere String `""`.
- Groß- und Kleinschreibung wird unterschieden (`"a"` ≠ `"A"`).

Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.** Füllen Sie die Tabelle vor dem Implementieren aus (mindestens je ein Normalfall, Randfall und Sonderfall) und übertragen Sie sie nach `test_most_frequent_letter.py`.

| Nr. | Eingabe         | Erwartete Ausgabe | Begründung                     |
| --- | --------------- | ----------------- | ------------------------------ |
| 1   | `"abracadabra"` | `"a"`             | Normalfall: ein klares Maximum |
|     |                 |                   |                                |

> _Welche Äquivalenzklassen haben Sie unterschieden? Welcher Randfall war am leichtesten zu übersehen?_

---

## C4 — Lauflängen-Kodierung ✦✦✦

[`run_length_encode.py`](uebungen/c4_run_length_encode/run_length_encode.py) · [Lösung](uebungen/c4_run_length_encode/loesung/)

**Kontext.** Die Lauflängen-Kodierung (run-length encoding) ist eines der einfachsten verlustfreien Kompressionsverfahren: aufeinanderfolgende gleiche Zeichen werden zu einem Paar `(Zeichen, Anzahl)` zusammengefasst. Aus `"aaabbc"` wird `[("a", 3), ("b", 2), ("c", 1)]`. Anwendung findet das Verfahren in einfachen Bildformaten und beim Aufzeichnen wiederholter Zustände.

**Neuer Datentyp für diese Übung — Tupel.** Ein Tupel bündelt mehrere zusammengehörige Werte in einer unveränderlichen Einheit. Hier wird jedes Lauf-Paar als Tupel `(zeichen, anzahl)` abgelegt. Details: siehe [cheatsheet_tupel.md](cheatsheets/cheatsheet_tupel.md).

```python
pair = ("a", 3)         # erzeugen
pair[0]                 # "a"
pair[1]                 # 3
result = []
result.append(("b", 2)) # an Liste anhängen
```

> **Tellerrand — Python vs. C#/Java:** In Python ist ein Tupel ein eigenständiger Sprachtyp mit kompakter Syntax `(a, b)`. In C# entsprechen Werte-Tupel (`ValueTuple`, ab C# 7) ungefähr; in Java werden zusammengehörige Werte üblicherweise als kleine Klassen oder als `record` (ab Java 14) modelliert.

**Aufgabe.** Implementieren Sie die Funktion `run_length_encode(text: str) -> list[tuple[str, int]]`. Die Funktion liefert eine Liste von `(Zeichen, Anzahl)`-Tupeln in der Reihenfolge ihres Auftretens.

Spezifikationen:

- Ein **Lauf** ist eine maximale Folge gleicher Zeichen.
- Tritt ein Zeichen nach einem anderen Lauf erneut auf, ist das ein **neuer** Lauf — `"aabbaa"` liefert drei Tupel, nicht zwei.
- Ein leerer Text liefert die leere Liste.
- Achten Sie auf den **letzten Lauf**: nach Schleifenende muss er noch angehängt werden.

Signatur und Docstring sind vorgegeben — füllen Sie nur den Funktionskörper aus.

**Testfallkatalog.** Füllen Sie die Tabelle vor dem Implementieren aus (mindestens je ein Normalfall, Randfall und Sonderfall) und übertragen Sie sie nach `test_run_length_encode.py`.

| Nr. | Eingabe    | Erwartete Ausgabe                | Begründung             |
| --- | ---------- | -------------------------------- | ---------------------- |
| 1   | `"aaabbc"` | `[("a", 3), ("b", 2), ("c", 1)]` | Normalfall: drei Läufe |
|     |            |                                  |                        |

> _Welche Äquivalenzklassen haben Sie unterschieden? Welcher Randfall war am leichtesten zu übersehen?_

---

## Refactoring-Übungen (R)

In diesen Übungen ist bereits lauffähiger Code vorhanden. Ihre Aufgabe ist es, diesen Code zu analysieren und eine oder mehrere **Funktionen zu entwerfen**, die den Code verbessern — dabei steht nicht der Algorithmus, sondern die **Schnittstelle** im Vordergrund.

**Leitfragen** — beantworten Sie diese schriftlich, bevor Sie die erste Code-Zeile schreiben:

1. _Wer ruft die Funktion(en) auf — und mit welchen Werten?_
2. _Welche Informationen braucht jede Funktion, um ihre Aufgabe zu erledigen?_
3. _Was ist im Ausgangscode redundant oder könnte ausgelagert werden?_
4. _Wie könnten die Funktionen sinnvoll benannt werden?_

**Arbeitsablauf:** Ausgangscode lesen (`*_before.py`) → Leitfragen in der Skelett-Datei beantworten → Signatur selbst entwerfen → implementieren → testen.

**Niveau.** Alle R-Übungen verlangen das eigenständige Entwerfen der Schnittstelle (mindestens ✦✦). **R1b ✦✦** ist stärker geführt — Tipps und ein Signatur-Gerüst im Skelett, eine einzelne Funktion. **R2c ✦✦✦** ist offen — sie verlangt die Zerlegung in mehrere Funktionen mit Abhängigkeit und schließt mit einer Reflexionsfrage.

---

## R1b — Auftragserfassung ✦✦

[`order_input.py`](uebungen/r1b_order_input/order_input.py) · [Ausgangscode](uebungen/r1b_order_input/order_input_before.py) · [Lösung](uebungen/r1b_order_input/loesung/)

**Kontext.** Im Ausgangscode gibt ein Sachbearbeiter drei verschiedene Auftragsdaten ein — Bestellmenge, Lieferfrist und Stückpreis. Für jedes Feld wird dasselbe geprüft: ist der Wert positiv? Die Prüfbedingung steht dreimal im Code. Alle drei Felder sind semantisch verschieden, aber die Regel ist identisch — das ist der Smell.

**Ausgangscode.** Öffnen Sie `order_input_before.py`. Lesen Sie den Code aufmerksam und formulieren Sie in einem Satz, was die drei `if`-Blöcke gemeinsam haben.

**Aufgabe.** Entwerfen und implementieren Sie eine Funktion, die die wiederholte Prüfung kapselt. Bearbeiten Sie zuerst die vier Leitfragen im Kommentarblock am Anfang von `order_input.py` — dort finden Sie zu jeder Frage einen **Tipp** und ein **Signatur-Gerüst**, dessen Typen vorgegeben sind. Namen und Parametername wählen Sie selbst.

Spezifikation:

- Die Funktion prüft, ob ein ganzzahliger Wert positiv ist (größer als 0).
- Rückgabe: `True` wenn positiv, `False` sonst.

**Testfallkatalog.** Die Spalten _Eingabe_ und _Erwartete Ausgabe_ sind vorgegeben. Ergänzen Sie die Spalte _Begründung_ und übertragen Sie die Fälle in `test_order_input.py`.

| Nr. | Eingabe | Erwartete Ausgabe | Begründung |
| --- | ------- | ----------------- | ---------- |
| 1   | `5`     | `True`            |            |
| 2   | `1`     | `True`            |            |
| 3   | `0`     | `False`           |            |
| 4   | `-1`    | `False`           |            |
| 5   | `-100`  | `False`           |            |
| 6   | `1000`  | `True`            |            |

---

## R2c — Tagesabschluss ✦✦✦

[`sales_report.py`](uebungen/r2c_sales_report/sales_report.py) · [Ausgangscode](uebungen/r2c_sales_report/sales_report_before.py) · [Lösung](uebungen/r2c_sales_report/loesung/)

**Kontext.** Im Ausgangscode werden Buchungsbeträge für drei Produktkategorien eines Tagesabschlusses ausgewertet; negative Einträge sind Stornierungen und werden nicht gezählt. Am Ende wird zusätzlich die **Gesamtsumme** über alle Kategorien gebildet. Dadurch stecken **zwei** Redundanzen im Code: die Filter-Summen-Logik (viermal — je Kategorie und für die Gesamtsumme) und das Muster „Summe berechnen und Zeile ausgeben" (je Kategorie).

**Ausgangscode.** Öffnen Sie `sales_report_before.py`. Identifizieren Sie **beide** Wiederholungen und überlegen Sie, welche davon sich in welche Funktion auslagern lässt.

**Aufgabe.** Entwerfen und implementieren Sie **mehrere** Funktionen, die die Wiederholungen kapseln — eine darf die andere aufrufen. Bearbeiten Sie zuerst die vier Leitfragen in `sales_report.py`.

Spezifikation:

- Eine Funktion summiert alle positiven Beträge (> 0) einer Liste; eine leere Liste oder eine ohne positive Einträge ergibt `0` (Rückgabe `int`).
- Eine zweite Funktion gibt die Ergebniszeile einer Kategorie aus und nutzt dazu die erste Funktion.
- Das Hauptprogramm bildet damit die drei Kategoriezeilen **und** die Gesamtsumme, ohne die Filter-Summen-Schleife erneut auszuschreiben.

**Testfallkatalog.** Füllen Sie die Tabelle vor der Implementierung aus (mindestens je ein Normalfall, Randfall und Sonderfall) und übertragen Sie die Fälle in `test_sales_report.py`. Testen Sie die Funktion(en) mit Rückgabewert — eine reine Ausgabe-Prozedur lässt sich mit `assert` nicht direkt prüfen.

| Nr. | Eingabe                | Erwartete Ausgabe | Begründung                              |
| --- | ---------------------- | ----------------- | --------------------------------------- |
| 1   | `[45, -12, 30, 8, -5]` | `83`              | Normalfall: Buchungen mit Stornierungen |
|     |                        |                   |                                         |

> _Welche Ihrer Funktionen hängt von welcher ab? Hätten Sie die ausgebende Funktion auch ohne Rückgabewert entwerfen können — mit welchem Nachteil für die Gesamtsumme?_

---

## Zerlegungs-Übungen (Z)

In diesen Übungen ist der **Algorithmus des Hauptprogramms als Pseudocode vorgegeben**. Ihre Aufgabe ist es, das Programm umzusetzen und dabei in sinnvolle **Funktionen/Prozeduren zu zerlegen** — Namen, Parameter und Rückgabewerte entwerfen Sie selbst. Nicht der Algorithmus ist die Herausforderung, sondern die **Struktur**.

Jede Z-Übung gibt es in zwei Führungsvarianten mit **gleicher** Musterlösung:

- **Variante B (✦✦)** — der Pseudocode ist so detailliert, dass er Zeile für Zeile nach Python übersetzt werden kann. Die Zerlegung in Funktionen leisten Sie selbst.
- **Variante C (✦✦✦)** — der Algorithmus ist nur in Worten beschrieben. Zusätzlich wählen Sie selbst die passenden Python-Konstrukte (Schleifenform, Abbruch, Fehlerbehandlung, Umbruch).

Diese Übungen enthalten **keine** automatisierten Tests. Zur Selbstkontrolle dienen der Schreibtischtest, die Beispieltabelle und der Vergleich mit der Musterlösung.

---

## Z1 — Cäsar-Verschlüsselung ✦✦ / ✦✦✦

Variante B (geführt): [`z1b_caesar/caesar.py`](uebungen/z1b_caesar/caesar.py) · Variante C (offen): [`z1c_caesar/caesar.py`](uebungen/z1c_caesar/caesar.py) · [Lösung](uebungen/z1b_caesar/loesung/)

**Kontext.** Die Cäsar-Verschlüsselung verschiebt jeden Buchstaben um eine feste Anzahl Stellen im Alphabet — aus `a` wird bei Verschiebung 3 ein `d`. Sie ist das klassische Einstiegsbeispiel der Kryptografie. Hier dient sie als vollständiges kleines Programm: Eingaben einlesen und prüfen, etwas berechnen, Ergebnis ausgeben.

**Neu in dieser Übung — `try` / `except`.** Eingaben aus `input()` sind immer Text. Um die Verschiebung als Zahl zu verwenden, wandeln Sie sie mit `int()` um. Bei ungültiger Eingabe (Buchstaben, Sonderzeichen) löst `int()` einen `ValueError` aus, den Sie abfangen:

```python
while True:
    eingabe = input("Verschiebung (ganze Zahl): ")
    try:
        verschiebung = int(eingabe)
        break
    except ValueError:
        print("Bitte eine ganze Zahl eingeben.")
```

Details und Tellerrand siehe [`cheatsheet_try_except.md`](cheatsheets/cheatsheet_try_except.md).

**Aufgabe.** Schreiben Sie ein Programm, das einen Klartext nach dem Cäsar-Verfahren verschlüsselt. Im Skelett ist der Algorithmus des Hauptprogramms als Pseudocode vorgegeben. Zerlegen Sie ihn in Funktionen/Prozeduren und setzen Sie ihn um. Die Konstante `ALPHABET` und das Gerüst `if __name__ == "__main__":` sind vorgegeben.

Spezifikation:

- Klartext einlesen und so lange erneut fragen, bis er **nicht leer** ist und **nur Kleinbuchstaben a–z** enthält (keine Zahlen, keine Sonderzeichen, keine Großbuchstaben).
- Verschiebung als **ganze Zahl** einlesen und so lange erneut fragen, bis eine gültige Zahl eingegeben wurde. Negative Zahlen sind erlaubt.
- Jeden Buchstaben um die Verschiebung weiterrücken; hinter `z` geht es bei `a` weiter (Umbruch über `% 26`).
- Den Geheimtext ausgeben.

Wählen Sie eine der beiden Führungsvarianten (B geführt, C offen) — die Lösung ist für beide dieselbe.

**Schreibtischtest.** Verfolgen Sie die Verschlüsselung von `klartext = "xyz"`, `verschiebung = 3` Schritt für Schritt — bevor Sie mit der Implementierung beginnen. Beachten Sie den Umbruch am Alphabet-Ende.

| Schritt | zeichen | pos | `(pos + 3) % 26` | `ALPHABET[neue_pos]` | geheimtext |
| ------- | ------- | --- | ---------------- | -------------------- | ---------- |
| Start   | —       | —   | —                | —                    | `""`       |
| 1       | x       | 23  | 0                | a                    | `"a"`      |
| 2       | y       | 24  | 1                | b                    | `"ab"`     |
| 3       | z       | 25  | 2                | c                    | `"abc"`    |

**Beispiele zur Selbstkontrolle.** Prüfen Sie Ihr fertiges Programm an diesen Werten (es gibt keine automatisierten Tests):

| Klartext  | Verschiebung | Geheimtext | abgedeckter Fall                          |
| --------- | ------------ | ---------- | ----------------------------------------- |
| `"abc"`   | `1`          | `"bcd"`    | Normalfall                                |
| `"xyz"`   | `3`          | `"abc"`    | Umbruch am Alphabet-Ende                  |
| `"hallo"` | `0`          | `"hallo"`  | Verschiebung 0 lässt den Text unverändert |
| `"abc"`   | `-1`         | `"zab"`    | negative Verschiebung (Umbruch nach vorn) |
| `"abc"`   | `27`         | `"bcd"`    | Verschiebung > 25 (wirkt wie 1)           |

> _Welche Äquivalenzklassen haben Sie unterschieden? Welcher Randfall war am leichtesten zu übersehen?_ (für Variante C)
