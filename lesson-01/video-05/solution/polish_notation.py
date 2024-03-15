def polish_notation_without_stack(expression):
    expression = expression.split()
    operators = ['+', '-', '*', '/']
    while len(expression) > 1:
        for i in range(len(expression)):
            if expression[i] in operators:
                operator = expression[i]
                operand1 = int(expression[i - 2])
                operand2 = int(expression[i - 1])
                if operator == '+':
                    result = operand1 + operand2
                elif operator == '-':
                    result = operand1 - operand2
                elif operator == '*':
                    result = operand1 * operand2
                elif operator == '/':
                    result = operand1 / operand2
                expression = expression[:i - 2] + [str(result)] + expression[i + 1:]
                break
    return int(expression[0])
