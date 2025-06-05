import time
import random
from src.utils.algorithms.binary_search import binary_search
from src.utils.algorithms.insertion_sort import insertion_sort

# INSERTION SORT HELPER
def measure_insertion_runtime(arr, ascending=True):
    """Measure the runtime of insertion sort."""
    start = time.perf_counter()
    passes, sorted_arr = insertion_sort(arr, ascending)
    end = time.perf_counter()
    return end - start, passes, sorted_arr

def print_passes(passes):
    """Print each pass state."""
    for i, state in enumerate(passes, 1):
        print(f"Pass {i}: {state}")

def generate_random_array(n, min_val, max_val, value_type="Numbers"):
    """
    Generate an unsorted random array of numbers or letters.
    """
    if value_type == "Numbers":
        return [random.randint(min_val, max_val) for _ in range(n)]
    elif value_type == "Letters":
        return [chr(random.randint(min_val, max_val)) for _ in range(n)]
    else:
        raise ValueError("Invalid value_type. Must be 'Numbers' or 'Letters'.")


