"""Parallel Merge Sort - Multi-core sorting with process-based parallelism."""

from parallel_sort import parallel_merge_sort


def parallel_merge(arr):
    """Sort array using parallel merge sort across multiple CPU cores."""
    parallel_merge_sort(arr)
