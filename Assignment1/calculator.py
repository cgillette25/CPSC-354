import re

# Function to check if the initial input is valid
def is_valid_initial_equation(equation):
    pattern = r'^[0-9\(\)\+\*/\-\s\^\.]+$'
    if not re.match(pattern, equation):
        return False
    if not (equation[0].isdigit() or equation[0] == '('):
        return False
    if not (equation[-1].isdigit() or equation[-1] == ')'):
        return False
    return True

# Function to handle exponentiation
def solve_exponentiation(equation):
    while True:
        exp_pattern = r'(\d+(?:\.\d+)?|\([\d\+\-\*/^\s]+\))(\s*\^\s*)(\d+(?:\.\d+)?|\([\d\+\-\*/^\s]+\))'
        match = re.search(exp_pattern, equation)
        if not match:
            break

        left, operator, right = match.groups()

        left = eval(solve_parentheses(left))
        right = eval(solve_parentheses(right))

        result = float(left) ** float(right)

        equation = equation[:match.start()] + str(result) + equation[match.end():]

    return equation

# Function to handle multiplication and division
def solve_multiplication_division(equation):
    while True:
        md_pattern = r'(\d+(?:\.\d+)?)(\s*[\*/]\s*)(\d+(?:\.\d+)?)'
        match = re.search(md_pattern, equation)
        if not match:
            break

        left, operator, right = match.groups()
        if operator.strip() == '*':
            result = float(left) * float(right)
        elif operator.strip() == '/':
            if float(right) == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = float(left) / float(right)

        equation = equation[:match.start()] + str(result) + equation[match.end():]

    return equation

# Function to handle addition and subtraction
def solve_addition_subtraction(equation):
    equation = re.sub(r'(?<=\d)-', ' + -', equation)
    terms = re.split(r'\s*\+\s*', equation)
    total = 0
    for term in terms:
        total += float(term.strip())
    return total

# Function to handle parentheses
def solve_parentheses(equation):
    while '(' in equation:
        parentheses_pattern = r'\(([^\(\)]+)\)'
        match = re.search(parentheses_pattern, equation)
        if match:
            inside = match.group(1)
            solved_inside = solve_exponentiation(inside)  # Evaluate exponentiation first
            solved_inside = solve_multiplication_division(solved_inside)
            solved_inside = solve_addition_subtraction(solved_inside)
            equation = equation[:match.start()] + str(solved_inside) + equation[match.end():]

    return equation

# Main function to evaluate a single input expression
def evaluate_expression(equation):
    if not is_valid_initial_equation(equation):
        raise ValueError("Invalid input. Please enter a valid equation.")

    equation = solve_parentheses(equation)
    equation = solve_exponentiation(equation)
    equation = solve_multiplication_division(equation)
    result = solve_addition_subtraction(equation)

    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        equation = input("Enter an equation: ").strip()
    else:
        equation = sys.argv[1].strip()
    
    try:
        result = evaluate_expression(equation)
        print(result)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
