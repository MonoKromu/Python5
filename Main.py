import math
import sys
from functools import reduce


# №1
# numbers = [1, 2, 3, 4, 5, 8, 10, 13, 17, 25, 30, 60, 140]
# print(list(filter(lambda x: x < 5, numbers)))
# print(list(map(lambda x: x / 2, numbers)))
# print(list(map(lambda x: x / 2, filter(lambda x: x > 17, numbers))))
# print(sum(map(lambda x: x ** 2, filter(lambda x: x % 9 == 0, [i for i in range(10, 100)]))))

# №2
# def factorials(n):
#     cur = 1
#     for i in range(1, n+1):
#         cur *= i
#         yield cur
#
#
# print(factorials(10))

# №3
# def square_fibonacci(n):
#     fi = [0, 1]
#     for _ in range(n):
#         yield fi[1]
#         next_fi = fi[0] + fi[1]
#         fi[0], fi[1] = fi[1], next_fi
#
#
# print(list(square_fibonacci(10)))

# №4
# def russian_alfabet():
#     for i in range(ord('а'), ord('я')+1):
#         yield chr(i)
#
#
# print(list(russian_alfabet()))

# №5
# expr = (chr(i) for i in range(ord('а'), ord('я')+1))
# for i in expr:
#     print(i, end=' ')

# №6
# def arithmetic_operation(operation):
#     if operation == '+':
#         return lambda a, b: a + b
#     elif operation == '-':
#         return lambda a, b: a - b
#     elif operation == '*':
#         return lambda a, b: a * b
#     elif operation == '/':
#         return lambda a, b: a / b
#     else:
#         return None
#
#
# task = input().split()
# print(arithmetic_operation(task[1])(int(task[0]), int(task[2])))

# №7
# def same_by(characteristic, objects):
#     result = [characteristic(i) for i in objects]
#     return all(result) or not any(result)
#
#
# nums = [10, 25, 40, 50]
# print(same_by(lambda x: x / 10 > 5, nums))
# print(same_by(lambda x: x % 2, nums))

# №8
# def print_operation_table(operation, rows=9, columns=9):
#     print(*[i for i in range(1, columns+1)], sep='\t')
#     for i in range(2, rows+1):
#         print(*[i] + [operation(j, i) for j in range(2, columns+1)], sep='\t')
#
#
# print_operation_table(lambda x, y: x - y, 5)

# №9
# def ask_password(login: str, password: str, successful, failure):
#     login = login.lower()
#     password = password.lower()
#     vowels = 'aeiouy'
#     consonants = 'bcdfghjklmnpqrstvwxz'
#     correct_vowels = len(list(filter(lambda x: x in vowels, password))) == 3
#     correct_consonants = [i for i in password if i in consonants] == [i for i in login if i in consonants]
#     if not correct_vowels and not correct_consonants:
#         failure(login, 'Everything is wrong')
#     elif not correct_vowels:
#         failure(login, 'Wrong number of vowels')
#     elif not correct_consonants:
#         failure(login, 'Wrong consonants')
#     else:
#         successful(login)
#
#
# def main(login, password):
#     successful = lambda log: print(f"Привет, {log}!")
#     failure = lambda log, err: print(f"Кто-то попытался притвориться пользователем {log}, "
#                                      f"но допустил ошибку: {str.upper(err)}")
#     ask_password(login, password, successful, failure)
#
#
# main('anastasia', 'nsyatos')
# main('eugen', 'aaanig')

# №10
# text = 'cats dog CAT DOGGY monkey'
# print(sorted(text.split()))
# print(sorted(text.split(), key=lambda x: x.lower()))

# №11
# numbers = [-100, 5, 38, -1, -72, 72, 41, -49]
# print(sorted(numbers, key=lambda x: abs(x), reverse=True))

# №12
# points = [(1, 2), (-10, 10), (-5, 5), (2, 30), (0, 0), (8, -15), (2, 1), (0, 5), (5, 0), (0, 3), (0, -3)]
# print(sorted(points, key=lambda a: ((a[0] ** 2 + a[1] ** 2) ** 0.5, a[0], a[1])))

# №13
# table = [[1, 5, 9], [0, 6, 10], [6, 2, 945]]
# print(any([not all(i) for i in table]))

# №14
# words = {}
# for n, word in enumerate(sys.stdin.read().split()):
#     word = word.replace('.', '')
#     if word.istitle() and words.get(word) is None:
#         words[word] = n
# print(*[f"{words.get(word)} - {word}" for word in sorted(words.keys())], sep='\n')

# №15
# print(reduce(lambda a, b: a if a < b else b, sys.stdin.read().strip().split()))

# №16
# print(reduce(math.gcd, map(int, sys.stdin.read().strip().split())))

# №17
# def check_password(func):
#
#     def new_func(*args, **kwargs):
#         if input('Введите пароль:') != 'qwe123!@#':
#             print('В доступе отказано.')
#             return None
#         else:
#             return func(*args, **kwargs)
#
#     return new_func
#
#
# calculator = check_password(lambda x, y: x + y)
# print(calculator(1, 5))

# №18
# def check_password(password):
#     def decorator(func):
#
#         def new_func(*args, **kwargs):
#             if input('Введите пароль:') != password:
#                 print('В доступе отказано.')
#                 return None
#             else:
#                 return func(*args, **kwargs)
#
#         return new_func
#
#     return decorator
#
#
# @check_password('superstrongpassword')
# def summa(a, b):
#     return a + b
#
#
# print(summa(1, 2))

# №19
# def cached(func):
#     cache = {}
#
#     def new_func(*args, **kwargs):
#         key = (args, frozenset(kwargs.items()))
#         if key in cache:
#             return cache[key]
#         result = func(*args, **kwargs)
#         cache[key] = result
#         return result
#
#     return new_func
#
#
# @cached
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
#
#
# print(fibonacci(100))
# print(fibonacci(100))
