number = [5, 6, 7, 8, 9, 1, 2, 3, 4]
result = [ ]
result.append(number.pop(0))
result.append(number.pop())
result.append(number.pop(1))
result.append(number.pop())
result.append(number.pop(0))
print(number[0]+result[-1])
