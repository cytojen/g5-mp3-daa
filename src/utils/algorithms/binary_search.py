def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    """
    # Initialize a list to track the passes (comparisons)
    passes = []
    # Set the initial search boundaries of the entire array
    low, high = 0, len(arr) - 1

    # Repeat the search while there is a valid portion of the array to check
    while low <= high:
        mid = (low + high) // 2
        passes.append((low, mid, high, arr[mid]))

        if arr[mid] == target:
            return passes, mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return passes, -1
