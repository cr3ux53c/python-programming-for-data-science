from functools import reduce
x = 10
reduce(lambda x, y: x * y, list(range(x, 0, -1)))
