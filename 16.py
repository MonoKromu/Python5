import math
import sys
from functools import reduce

print(reduce(math.gcd, map(int, sys.stdin.read().strip().split())))
