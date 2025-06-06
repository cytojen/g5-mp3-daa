def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    """
    # Initialize a list to track the passes (comparisons)
    passes = []
    low, high = 0, len(arr) - 1

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
