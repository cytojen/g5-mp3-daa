def russian_multiplication(a, b):
    """Perform Russian multiplication and track steps.
    """
    #List to store each step
    steps = []
    #Initialize the total
    total = 0

    # Repeat the process while a is greater than 0
    while a > 0:
        # Check if a is odd. If it is, we add the current b to the total
        keep = a % 2 != 0
        if keep:
            total += b
        steps.append((a, b, keep))
        a //= 2
        b *= 2

    return total, steps