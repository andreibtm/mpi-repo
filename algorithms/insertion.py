"""Insertion Sort - O(n²) but efficient for small or nearly-sorted arrays."""


def insertion_sort(arr):
    """
    Sort array using insertion sort.
    Time: O(n²) worst/avg, O(n) best
    Space: O(1)
    
    Very fast for small or nearly-sorted lists.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
