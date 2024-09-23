def check_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return "no"
    return "yes" if not stack else "no"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        expression = input("Enter an expression with parentheses: ")
    else:
        expression = sys.argv[1]
    print(check_parentheses(expression))
