def binary_search(arr, search_value):
    """
    Performs binary search on a sorted array.
    """
    # Initialize a list to track the passes (comparisons)
    passes = []
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        passes.append((left, mid, right, arr[mid]))

        if arr[mid] == search_value:
            return passes, mid
        elif arr[mid] < search_value:
            left = mid + 1
        else:
            right = mid - 1

    return passes, -1
