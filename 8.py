def print_operation_table(operation, rows=9, columns=9):
    print(*[i for i in range(1, columns+1)], sep='\t')
    for i in range(2, rows+1):
        print(*[i] + [operation(j, i) for j in range(2, columns+1)], sep='\t')


print_operation_table(lambda x, y: x - y, 5)
