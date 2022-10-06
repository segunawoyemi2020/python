def calculate(num1, num2, op):
    try:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 -num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2
        else:
            return ' Give proper operation, +, -, *, / '
    except ValueError:
        return 'invalid value'
























