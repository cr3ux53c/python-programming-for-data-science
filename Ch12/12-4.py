def sum_data(list_data_a, list_data_b):
    for i in list_data_a:
        for j in list_data_b:
            result = i+j
    return result

a = [1, 2]
b = [3, 4]

print(sum_data(a, b))
