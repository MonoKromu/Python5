import sys
from functools import reduce

print(reduce(lambda a, b: a if a < b else b, sys.stdin.read().strip().split()))
