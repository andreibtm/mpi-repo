"""Python's Built-in Sort - Timsort (hybrid stable sorting algorithm)."""


def builtin_sort(arr):
    """
    Sort array using Python's built-in sort (Timsort).
    Time: O(n log n) worst/avg, O(n) best (nearly sorted)
    Space: O(n)
    
    Highly optimized hybrid algorithm combining merge sort and insertion sort.
    """
    arr.sort()
