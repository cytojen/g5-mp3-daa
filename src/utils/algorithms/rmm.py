def russian_multiplication(a, b):
    """Perform Russian multiplication and track steps.
    """
    #List to store each step
    steps = []
    #Initialize the total
    total = 0

    while a > 0:
        keep = a % 2 != 0
        if keep:
            total += b
        steps.append((a, b, keep))
        a //= 2
        b *= 2

    return total, steps