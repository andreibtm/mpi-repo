"""Linked List Insertion Sort - O(n²) but suited for linked structures."""

from data_structures import linked_list_insertion_sort_wrapper


def ll_insertion_sort(arr):
    """Sort array by converting to linked list, sorting, and converting back."""
    linked_list_insertion_sort_wrapper(arr)
