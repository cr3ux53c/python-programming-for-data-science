def get_half_value(number):
    assert isinstance(number, int), 'input value must be integer.'
    result = number / 2
    assert isinstance(result, int), 'output value must be transformed integer.'
    return result

print(get_half_value(50))
