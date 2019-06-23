def factorial_calculator(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial_calculator(n - 1)
print(factorial_calculator(5))
