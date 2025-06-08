import time
import random
from src.utils.algorithms.binary_search import binary_search
from src.utils.algorithms.insertion_sort import insertion_sort
from src.utils.algorithms.rmm import russian_multiplication

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

# BINARY SEARCH HELPER
def is_sorted(arr):
    """Check if the array is sorted in ascending order."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def measure_binary_search_runtime(arr, target):
    """
    Runs binary_search and measures runtime.
    """
    sorted_flag = is_sorted(arr)
    start = time.perf_counter()
    passes, index = binary_search(arr, target) if sorted_flag else ([], -1)
    end = time.perf_counter()
    runtime = end - start
    return runtime, passes, index, sorted_flag

def generate_sorted_array(n, min_val, max_val, value_type="Numbers", allow_floats=False):
    """
    Generate a sorted array of numbers or letters.
    """
    if value_type == "Numbers":
        if allow_floats:
            arr = [random.uniform(min_val, max_val) for _ in range(n)]
        else:
            arr = [random.randint(min_val, max_val) for _ in range(n)]
    elif value_type == "Letters":
        arr = [chr(random.randint(min_val, max_val)) for _ in range(n)]
    else:
        raise ValueError("Invalid value_type. Must be 'Numbers' or 'Letters'.")
    return sorted(arr)

# RMM HELPER
def gen_two_random_values(min_val=1, max_val=100):
    """Generate two non-negative random integers."""
    a = random.randint(min_val, max_val)
    b = random.randint(min_val, max_val)
    return a, b

def format_rmm_steps(a, b):
    """Run RMM and format steps for display."""

    if not (float(a).is_integer() and float(b).is_integer()):
        raise ValueError("Decimal values are not supported by Russian Multiplication Method. Please enter whole numbers.")

    if a < 0 or b < 0:
        raise ValueError("Negative values are not supported by Russian Multiplication Method.")
    
    result, steps = russian_multiplication(a, b)
    formatted = []
    for x, y, keep in steps:
        line = f"{x:5} | {y:5} | {'✓' if keep else '✗'}"
        formatted.append(line)
    return result, steps, formatted

