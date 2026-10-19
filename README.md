# Interpreter Zaawansowanego Kalkulatora (Ewaluator Wyrażeń)

## Autor
* **Bartłomiej Cichy**

## Opis projektu
Projekt realizuje autorski parser oraz interpreter zaawansowanych wyrażeń matematycznych. Program przekształca kod wejściowy na AST (Abstract Syntax Tree), uwzględniając prawidłowy priorytet operatorów oraz ich łączność (lewostronną dla podstawowych działań, prawostronną dla potęgowania). 

Narzędzie posiada wbudowaną pamięć, co pozwala na definiowanie zmiennych i ponowne ich wykorzystywanie w kolejnych wyrażeniach. Program został zabezpieczony przed krytycznymi błędami – zamiast rzucać surowe wyjątki z poziomu interpretera Pythona (np. `IndexError`, `ZeroDivisionError`), przechwytuje błędy składniowe, semantyczne oraz matematyczne, wyświetlając użytkownikowi czytelne komunikaty.

## Formalna Gramatyka i Tokeny
Język został zdefiniowany za pomocą gramatyki bezkontekstowej (**Typ 2 w hierarchii Chomsky'ego**). Do wygenerowania parsera zastosowano analizator składniowy typu LALR.

### Tokeny (Elementy Leksykalne)
* `NUMBER`: Ciąg cyfr, opcjonalnie zawierający kropkę dziesiętną.
* `CNAME`: Identyfikator zmiennej rozpoczynający się od litery, zawierający litery, cyfry lub znaki podkreślenia.
* Operatory i znaki specjalne: `=`, `+`, `-`, `*`, `/`, `^`, `(`, `)`.
* Białe znaki (`WS`): Ignorowane przez lekser.

### Definicja Gramatyki
* **Symbol startowy**: `program`
* **Nieterminale**: `program`, `statement`, `assignment`, `expr`, `term`, `pow`, `factor`

```text
?start:program

program: statement*

?statement: assignment
            | expr

assignment: CNAME "=" expr

?expr: term
    | expr "+" term -> add
    | expr "-" term -> sub

?term: pow
    | term "*" pow -> mul
    | term "/" pow -> div

?pow: factor
    | factor "^" pow -> pow

?factor: NUMBER -> number
        | CNAME -> var
        | "(" expr ")"
```

## Instrukcja uruchomienia i przykłady użycia

1. Upewnij się, że posiadasz zainstalowanego Pythona (wersja 3).
2. Zainstaluj bibliotekę 'lark'.
```bash
pip install lark
```
3. Uruchom główny skrypt demonstracyjny:
```bash
python main.py
```

### Przykład 1: Poprawne budowanie AST i priorytet operatorów

**Wejście:**
```text
x = 5 + 3 * 2
```
**Wynik interpretacji:** `11.0`

**Opis działania:** Program poprawnie interpretuje priorytet operatorów. Drzewo AST buduje węzeł `Assignment` dla zmiennej `x`, gdzie prawym dzieckiem jest operacja `BinOp(+)`. Dziećmi dodawania są `Number(5)` oraz `BinOp(*)`, które z kolei zawiera wartości `Number(3)` i `Number(2)`.

### Przykład 2: Wykorzystanie zmiennych w pamięci

**Wejście:**
```text
y = x ^ 2
```
**Wynik interpretacji:** `121.0`

**Opis działania:** Program odwołuje się do środowiska (`env`), pobiera wartość przypisaną wcześniej do zmiennej `x` (11.0) i wykonuje operację potęgowania z zachowaniem łączności prawostronnej.

### Przykład 3: Odporność na błędy (Error Handling)

Zgodnie z wymaganiami program nie kończy się rzuceniem surowego wyjątku, lecz poprawnie go przechwytuje.

**Wejście 1 (błąd składniowy):**
```text
z = 10 + * 5
```
**Wynik programu:**
```text
Syntax error: nieoczekiwany token w linii 1, kolumnie 10.
```

**Wejście 2 (błąd matematyczny):**
```text
10 / 0
```
**Wynik programu:**
```text
Błąd. Dzielenie przez zero!
```