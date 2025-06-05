def insertion_sort(arr, ascending=True):
    """Perform insertion sort and record passes after each step."""
    # Track the array after each sorting step
    passes = []
    # copy input to avoid modifying original
    a = arr[:]  

    # Go through each item starting from the second one and insert it into the correct position
    # in the sorted part of the array (which is on the left side)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and ((a[j] > key) if ascending else (a[j] < key)):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

        passes.append(a[:]) 

    return passes, a
