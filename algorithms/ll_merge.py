"""Linked List Merge Sort - O(n log n) with O(1) extra space (pointer rewiring)."""

from data_structures import linked_list_merge_sort_wrapper


def ll_merge_sort(arr):
    """Sort array by converting to linked list, sorting, and converting back."""
    linked_list_merge_sort_wrapper(arr)
