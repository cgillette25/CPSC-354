Calculator Implementation Specifications
Introduction
This calculator evaluates mathematical expressions provided as command-line arguments. It supports addition, subtraction, multiplication, division, exponentiation, unary negation, and logarithms with specified bases. The program uses the Lark parsing library to parse expressions defined in a context-free grammar and evaluates them by traversing an abstract syntax tree (AST).

Program Flow
Parsing the Grammar: The program reads the grammar from grammar.lark and initializes a Lark parser.

Parsing the Input: It takes the input expression from the command line and parses it into a parse tree using the Lark parser.

Transforming to AST: The parse tree is transformed into an AST using the CalcTransformer class.

Evaluating the AST: The AST is recursively evaluated using the evaluate function to compute the result.

Output: The result is printed to the console.

Methods and Their Purpose

Class CalcTransformer(Transformer)
Purpose: Transforms the parse tree into an AST suitable for evaluation.
Methods:
plus(self, items): Handles addition; returns ('plus', left, right).
minus(self, items): Handles subtraction; returns ('minus', left, right).
times(self, items): Handles multiplication; returns ('times', left, right).
divide(self, items): Handles division; returns ('divide', left, right).
neg(self, items): Handles unary negation; returns ('neg', operand).
power(self, items): Handles exponentiation; returns ('power', base, exponent).
logbase(self, items): Handles logarithms with a specified base; returns ('logbase', value, base).
paren(self, items): Handles expressions in parentheses; returns the inner expression.
num(self, items): Converts number strings to floats; returns ('num', float_value).

Function evaluate(ast)
Purpose: Recursively evaluates the AST to compute the final result.
Logic:

Binary Operations: For plus, minus, times, divide, and power, it recursively evaluates left and right operands and applies the operation.
Unary Operation: For neg, it evaluates the operand and negates it.
Logarithm: For logbase, it evaluates the value and base, then computes the logarithm using math.log.
Number: For num, it returns the numeric value.
Error Handling: Raises a ValueError if an unknown operation is encountered.
Internal Logic of Methods
Transformation Methods: Each method in CalcTransformer corresponds to a grammar rule and constructs an AST node as a tuple representing the operation and its operands.

Evaluation Function: The evaluate function uses conditional statements to determine the type of operation and performs the computation by recursively evaluating the operands.

General Logic
Expression Parsing: The input expression is parsed according to the grammar rules, ensuring correct operator precedence and associativity.

AST Construction: The parse tree is transformed into an AST that mirrors the hierarchical structure of the expression.

Recursive Evaluation: The AST is evaluated from the bottom up, computing the result of sub-expressions before combining them at higher levels.

Result Output: The final computed result is displayed to the user.