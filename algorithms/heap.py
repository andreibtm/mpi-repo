"""Heap Sort - O(n log n) heap-based sorting algorithm."""

import heapq


def heap_sort(arr):
    """
    Sort array using heap sort.
    Time: O(n log n) worst/avg/best
    Space: O(n)
    
    Uses Python's heapq for efficient heap operations.
    """
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
