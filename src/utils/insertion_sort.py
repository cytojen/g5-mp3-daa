import time

def insertion_sort(arr, ascending=True):
    """Performs insertion sort"""

    # Track the array after each sorting step
    passes = []

    # Make a copy of the input array so we don't modify the original
    a = []

    # Copy each element from the original array to a new one so we don’t modify the input directly
    for item in arr:
        a.append(item)

    # Go through each item starting from the second one and insert it into the correct position
    # in the sorted part of the array (which is on the left side)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and ((a[j] > key) if ascending else (a[j] < key)):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

        current_pass = []
        for item in a:
            current_pass.append(item)
        passes.append(current_pass)
    
    return passes, a

def print_passes(passes):
    """Prints the number of passes for each state of the array"""
    for i in range(len(passes)):
        print("Pass", i + 1, ":", passes[i])

def measure_runtime(arr, ascending=True):
    """Measures the run time of the algorithm 
    (just to show lang here yung difference ng run time based on the number of inputs)
    """
    start = time.perf_counter()
    passes, sorted_arr = insertion_sort(arr, ascending)
    end = time.perf_counter()

    duration = end - start
    return duration, passes, sorted_arr