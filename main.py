import sys

def calculate(operator, operand1, operand2):
    try:
        operand1 = float(operand1)
        operand2 = float(operand2)
    except ValueError:
        print("Error: Invalid operands. Please enter numbers.")
        sys.exit(1)

    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            print("Error: Division by zero.")
            sys.exit(1)
        return operand1 / operand2
    else:
        print("Error: Invalid operator. Please use +, -, *, or /.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python pycalc.py <operator> <operand1> <operand2>")
        sys.exit(1)

    operator = sys.argv[1]
    operand1 = sys.argv[2]
    operand2 = sys.argv[3]

    result = calculate(operator, operand1, operand2)
    print(f"Result: {result}")