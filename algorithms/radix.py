"""Radix Sort - O(nk) non-comparative sorting algorithm for integers."""


def radix_sort(arr):
    """
    Sort array using radix sort.
    Time: O(nk) where k is number of digits
    Space: O(n + k)
    
    Works best for non-negative integers.
    Converts negatives to non-negative for processing.
    """
    if not arr or len(arr) == 0:
        return
    
    # Handle negatives by separating and processing
    has_negative = any(x < 0 for x in arr)
    
    if has_negative:
        negatives = [abs(x) for x in arr if x < 0]
        positives = [x for x in arr if x >= 0]
        
        _radix_sort_positive(negatives)
        _radix_sort_positive(positives)
        
        # Combine: negatives in reverse, then positives
        negatives.sort(reverse=True)
        arr.clear()
        arr.extend([-x for x in negatives])
        arr.extend(positives)
    else:
        _radix_sort_positive(arr)


def _radix_sort_positive(arr):
    """Helper function to sort non-negative integers."""
    if not arr:
        return
    
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        _counting_sort(arr, exp)
        exp *= 10


def _counting_sort(arr, exp):
    """Counting sort for a specific digit position."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = output[i]
