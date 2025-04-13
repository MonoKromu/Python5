numbers = [1, 2, 3, 4, 5, 8, 10, 13, 17, 25, 30, 60, 140]
print(list(filter(lambda x: x < 5, numbers)))
print(list(map(lambda x: x / 2, numbers)))
print(list(map(lambda x: x / 2, filter(lambda x: x > 17, numbers))))
print(sum(map(lambda x: x ** 2, filter(lambda x: x % 9 == 0, [i for i in range(10, 100)]))))
