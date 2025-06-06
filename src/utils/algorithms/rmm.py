def russian_peasant_multiplication(a, b):
    """
    Perform Russian Peasant Multiplication.
    """
    #Initialize a list of dictionaries showing each halving and doubling
    steps = []
    result = 0

    while a > 0:
        steps.append({'a': a, 'b': b, 'included': a % 2 != 0})
        if a % 2 != 0:
            result += b
        a //= 2
        b *= 2

    return steps, result
