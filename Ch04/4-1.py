def calculator(N):
    if n % 2 == 0:
        result = 1
        for i in range(1, N + 1):
            result = result * i
    else:
        result = 0
        for i in range(1, N + 1):
            result = result + i
    return result
