Assignment 1: Calculator Implementation
1. parentheses.py
Function: check_parentheses(expression)
Purpose: This function checks if the parentheses in the input string expression are balanced. It returns "yes" if they are balanced and "no" if they are not.

Internal Logic:

A stack is used to keep track of the opening parentheses (.
When a closing parenthesis ) is encountered, the function checks if there's a matching opening parenthesis in the stack.
If the stack is empty at the end, the parentheses are balanced.
Flow:

Loop through each character of the input string.
If ( is found, push it onto the stack.
If ) is found, check if the stack is non-empty and pop the top of the stack.
If the stack is empty after processing the string, return "yes", otherwise return "no".


2. calculator.py

Function: is_valid_initial_equation(equation)
Purpose: This function checks whether the input equation is valid. It verifies that the string contains only valid characters (numbers, +, *, ^, -, /, (, ), and whitespace) and checks that it starts and ends correctly.
Internal Logic:
Uses a regular expression to ensure valid characters are used.
Checks that the equation begins with either a number or an opening parenthesis ( and ends with either a number or closing parenthesis ).

Function: solve_exponentiation(equation)
Purpose: This function evaluates and solves all exponentiation (^) operations in the equation.
Internal Logic:
Finds all instances of exponentiation using a regular expression.
If parentheses are involved, it evaluates them first.
Performs the exponentiation operation and replaces the part of the equation with the result.
Flow:
While exponentiation is found in the equation, solve it and replace it with the result.
Continue until all exponentiation operations are handled.

Function: solve_multiplication_division(equation)
Purpose: This function evaluates and solves all multiplication (*) and division (/) operations in the equation.
Internal Logic:
Uses a regular expression to identify all multiplication and division operations.
Handles multiplication and division one at a time, ensuring operations are executed left to right (standard order of operations).
Flow:
While multiplication or division is found in the equation, solve it and replace it with the result.
Continue until all multiplication and division operations are handled.

Function: solve_addition_subtraction(equation)
Purpose: This function evaluates and solves all addition (+) and subtraction (-) operations in the equation.
Internal Logic:
Splits the equation by addition signs (+) and handles negative numbers by substituting - with + -.
Adds all terms together, respecting the negative numbers.

Function: solve_parentheses(equation)
Purpose: This function handles and solves any sub-expressions inside parentheses () in the equation.
Internal Logic:
Uses a regular expression to find the innermost parentheses.
Solves the sub-expression inside the parentheses using the exponentiation, multiplication, division, and addition/subtraction functions.
Replaces the parentheses with the solved result.

Function: evaluate_expression(equation)
Purpose: The main function that handles the overall evaluation of the arithmetic expression, combining the functionality of the other methods.
Internal Logic:
First, it checks if the input equation is valid using is_valid_initial_equation.
Then, it solves any parentheses using solve_parentheses.
After parentheses, it solves exponentiation using solve_exponentiation.
Then it evaluates multiplication and division using solve_multiplication_division.
Finally, it handles addition and subtraction using solve_addition_subtraction.
Returns the final result of the expression.
Flow:

Validate the input equation.
Process parentheses.
Process exponentiation.
Process multiplication and division.
Process addition and subtraction.
Return the result.