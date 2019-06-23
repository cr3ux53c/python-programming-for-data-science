tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)

def quiz_1(data_1, data_2):
    result = [ ]

    for i in (tuple_1 + tuple_2):
        result.append(i)
    return (result)

print(quiz_1(tuple_1, tuple_2))
