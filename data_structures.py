"""
Linked List data structure and Linked List sorting algorithms.

Demonstrates key differences from array-based sorting:
- Sequential access (O(n) to reach an element)
- No extra memory for merge operations (pointers can be rewired in-place)
- Different performance characteristics for each algorithm
"""


class ListNode:
    """Node for a singly-linked list."""
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --- Conversion helpers ---

def array_to_linked_list(arr):
    """Convert array to linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    """Convert linked list back to array."""
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


# --- Linked List Merge Sort (O(n log n) time, O(1) extra space) ---

def get_middle(head):
    """Find middle of linked list using slow/fast pointers."""
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge_lists(l1, l2):
    """Merge two sorted linked lists in-place."""
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


def linked_list_merge_sort(head):
    """
    Sort linked list using merge sort.
    Time: O(n log n)
    Space: O(1) extra (pointers rewired in-place)
    """
    if not head or not head.next:
        return head
    
    # 1. Split the list into two halves using slow/fast pointers
    mid = get_middle(head)
    right_head = mid.next
    mid.next = None  # Break the link
    
    # 2. Recursively sort each half
    left = linked_list_merge_sort(head)
    right = linked_list_merge_sort(right_head)
    
    # 3. Merge the sorted halves
    return merge_lists(left, right)


def linked_list_insertion_sort(head):
    """
    Sort linked list using insertion sort.
    Time: O(n²) worst case
    Space: O(1) extra
    
    Despite O(n²) complexity, insertion sort is good for linked lists
    because we don't need random access—we just follow the chain.
    """
    if not head or not head.next:
        return head
    
    dummy = ListNode()
    current = head
    
    while current:
        next_current = current.next
        
        # Find the correct position to insert
        pos = dummy
        while pos.next and pos.next.val <= current.val:
            pos = pos.next
        
        # Insert current after pos
        current.next = pos.next
        pos.next = current
        current = next_current
    
    return dummy.next


# --- Wrapper functions for benchmarking ---

def linked_list_merge_sort_wrapper(arr):
    """
    Wrapper to make linked list merge sort compatible with benchmarks.
    Converts array → linked list → sort → convert back to array.
    """
    ll_head = array_to_linked_list(arr)
    sorted_head = linked_list_merge_sort(ll_head)
    arr[:] = linked_list_to_array(sorted_head)


def linked_list_insertion_sort_wrapper(arr):
    """
    Wrapper to make linked list insertion sort compatible with benchmarks.
    """
    ll_head = array_to_linked_list(arr)
    sorted_head = linked_list_insertion_sort(ll_head)
    arr[:] = linked_list_to_array(sorted_head)
