sentence = list('You Love Me?')
result = ''
for i in range(len(sentence)):
    if i % 3 == 0:
        result += sentence.pop()
    else:
        result += sentence.pop(0)
print(result)
