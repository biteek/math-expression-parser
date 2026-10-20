# Advanced Calculator Interpreter (Expression Evaluator)

## Author
- **Bartłomiej Cichy**

## Project Description
This project implements a custom parser and interpreter for advanced mathematical expressions. The program transforms the input code into an AST (Abstract Syntax Tree), taking into account correct operator precedence and associativity (left-associative for basic operations, right-associative for exponentiation). 

The tool features built-in memory, allowing users to define variables and reuse them in subsequent expressions. The program is secured against critical errors – instead of throwing raw exceptions from the Python interpreter level (e.g., `IndexError`, `ZeroDivisionError`), it catches syntax, semantic, and mathematical errors, displaying readable messages to the user.

## Formal Grammar and Tokens
The language is defined using a context-free grammar (**Type 2 in the Chomsky hierarchy**). An LALR parser was used for syntax analysis.

### Tokens (Lexical Elements)
- `NUMBER`: A sequence of digits, optionally containing a decimal point.
- `CNAME`: A variable identifier starting with a letter, containing letters, digits, or underscores.
- Operators and special characters: `=`, `+`, `-`, `*`, `/`, `^`, `(`, `)`.
- Whitespace (`WS`): Ignored by the lexer.

### Grammar Definition
- **Start symbol**: `program`
- **Non-terminals**: `program`, `statement`, `assignment`, `expr`, `term`, `pow`, `factor`

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

## Setup and Usage Examples

1. Make sure you have Python installed (version 3).
2. Install the 'lark' library.
```bash
pip install lark
```
3. Run the main demo script:
```bash
python main.py
```

### Example 1: Correct AST construction and operator precedence

**Input:**
```text
x = 5 + 3 * 2
```
**Result:** `11.0`

**Description:** The program correctly interprets operator precedence. The AST builds an `Assignment` node for the variable `x`, where the right child is a `BinOp(+)` operation. The children of the addition are `Number(5)` and `BinOp(*)`, which in turn contains the values `Number(3)` and `Number(2)`.

### Example 2: Using variables in memory

**Input:**
```text
y = x ^ 2
```
**Result:** `121.0`

**Description:** The program queries the environment (`env`), retrieves the value previously assigned to the variable `x` (11.0), and performs the exponentiation operation while maintaining right-associativity.

### Example 3: Error Handling

As required, the program does not crash by throwing a raw exception, but correctly catches it (error messages in polish language).

**Input 1 (syntax error):**
```text
z = 10 + * 5
```
**Program output:**
```text
Syntax error: nieoczekiwany token w linii 1, kolumnie 10.
```

**Input 2 (math error):**
```text
10 / 0
```
**Program output:**
```text
Błąd. Dzielenie przez zero!
```
