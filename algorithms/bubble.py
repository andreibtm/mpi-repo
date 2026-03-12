"""Bubble Sort - O(n²) comparison-based sorting algorithm."""


def bubble_sort(arr):
    """
    Sort array using bubble sort.
    Time: O(n²) worst/avg, O(n) best
    Space: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
