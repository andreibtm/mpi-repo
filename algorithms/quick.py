"""Quick Sort - O(n log n) average case divide-and-conquer sorting algorithm."""

import random


def quick_sort(arr):
    """
    Sort array using quick sort.
    Time: O(n log n) average, O(n²) worst case
    Space: O(log n) recursion depth
    
    Uses random pivot selection to avoid worst-case on sorted data.
    """
    def _quick_sort(items, low, high):
        if low < high:
            # Random pivot selection
            pivot_idx = random.randint(low, high)
            items[high], items[pivot_idx] = items[pivot_idx], items[high]
            
            pivot = items[high]
            i = low - 1
            for j in range(low, high):
                if items[j] <= pivot:
                    i = i + 1
                    items[i], items[j] = items[j], items[i]
            items[i + 1], items[high] = items[high], items[i + 1]
            pi = i + 1

            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)
