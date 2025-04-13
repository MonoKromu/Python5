def arithmetic_operation(operation):
    if operation == '+':
        return lambda a, b: a + b
    elif operation == '-':
        return lambda a, b: a - b
    elif operation == '*':
        return lambda a, b: a * b
    elif operation == '/':
        return lambda a, b: a / b
    else:
        return None


task = input().split()
print(arithmetic_operation(task[1])(int(task[0]), int(task[2])))
