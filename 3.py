def square_fibonacci(n):
    fi = [0, 1]
    for _ in range(n):
        yield fi[1]
        next_fi = fi[0] + fi[1]
        fi[0], fi[1] = fi[1], next_fi


print(list(square_fibonacci(10)))
