"""Shell Sort - Generalization of insertion sort with gap sequences."""


def shell_sort(arr):
    """
    Sort array using shell sort.
    Time: O(n log n) to O(n²) depending on gap sequence
    Space: O(1)
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
