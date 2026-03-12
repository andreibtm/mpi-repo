"""Sorting algorithms module."""

from algorithms.bubble import bubble_sort
from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort
from algorithms.heap import heap_sort
from algorithms.merge import merge_sort
from algorithms.quick import quick_sort
from algorithms.shell import shell_sort
from algorithms.builtin import builtin_sort
from algorithms.radix import radix_sort
from algorithms.ll_merge import ll_merge_sort
from algorithms.ll_insertion import ll_insertion_sort
from algorithms.parallel_merge import parallel_merge

# Registry of all algorithms with their complexity class
ALGORITHMS = {
    "Bubble Sort": (bubble_sort, "n2"),
    "Selection Sort": (selection_sort, "n2"),
    "Insertion Sort": (insertion_sort, "n2"),
    "Shell Sort": (shell_sort, "n_intermediate"),
    "Heap Sort": (heap_sort, "nlogn"),
    "Merge Sort": (merge_sort, "nlogn"),
    "Quick Sort": (quick_sort, "nlogn"),
    "Python Timsort": (builtin_sort, "nlogn"),
    "Radix Sort": (radix_sort, "nk"),
    # Data structure variants
    "LL Merge Sort": (ll_merge_sort, "nlogn_linked"),
    "LL Insertion Sort": (ll_insertion_sort, "n2_linked"),
    # Parallel variants (multiprocessing)
    "Parallel Merge Sort": (parallel_merge, "nlogn_parallel"),
}

__all__ = [
    "bubble_sort",
    "selection_sort",
    "insertion_sort",
    "heap_sort",
    "merge_sort",
    "quick_sort",
    "shell_sort",
    "builtin_sort",
    "radix_sort",
    "ll_merge_sort",
    "ll_insertion_sort",
    "parallel_merge",
    "ALGORITHMS",
]
