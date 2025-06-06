def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    Records the low, mid, and high indices on each pass.
    Returns:
        - passes: list of dictionaries with low, mid, high values
        - index: index of target in arr or -1 if not found
    """
    low = 0
    high = len(arr) - 1
    passes = []

    while low <= high:
        mid = (low + high) // 2
        passes.append({'low': low, 'mid': mid, 'high': high, 'mid_value': arr[mid]})

        if arr[mid] == target:
            return passes, mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return passes, -1
