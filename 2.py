def factorials(n):
    cur = 1
    for i in range(1, n+1):
        cur *= i
        yield cur


print(factorials(10))
