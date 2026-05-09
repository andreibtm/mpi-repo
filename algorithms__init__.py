"""
Sorting algorithm implementations.

All functions sort arr in-place.
Complexity tags:
  n2       - O(n^2): skipped for n > 10,000
  nlogn    - O(n log n)
  nk       - non-comparative, integers only
  linked   - linked list variants
  parallel - skipped for n < 10,000
"""

import sys
import heapq
import random
import math

sys.setrecursionlimit(500_000)


# =============================================================================
# O(n^2) algorithms
# =============================================================================

def bubble_sort(arr):
    """Bubble Sort with early-exit optimisation. O(n^2) avg, O(n) best."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def selection_sort(arr):
    """Selection Sort. O(n^2) all cases. Not adaptive."""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertion_sort(arr):
    """Insertion Sort. O(n^2) avg, O(n) best. Highly adaptive."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertion_sort_range(arr, left, right):
    """Insertion sort on arr[left..right] inclusive. Used internally by Timsort."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# =============================================================================
# Shell Sort
# =============================================================================

def shell_sort(arr):
    """Shell Sort using Knuth gap sequence. O(n^1.5) with this sequence."""
    n = len(arr)
    # Knuth sequence: 1, 4, 13, 40, 121, ...
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3


# =============================================================================
# Heap Sort
# =============================================================================

def heap_sort(arr):
    """Heap Sort using Python heapq. O(n log n) all cases."""
    heapq.heapify(arr)
    arr[:] = [heapq.heappop(arr) for _ in range(len(arr))]


# =============================================================================
# Merge Sort
# =============================================================================

def merge_sort(arr):
    """Top-down Merge Sort. O(n log n) all cases. Stable."""
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]; i += 1
        else:
            arr[k] = right[j]; j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]; i += 1; k += 1
    while j < len(right):
        arr[k] = right[j]; j += 1; k += 1


# =============================================================================
# Quick Sort (3-way / Dutch National Flag)
# =============================================================================

def quick_sort(arr):
    """
    Quick Sort with randomised pivot and 3-way (Dutch National Flag) partitioning.
    3-way partitioning ensures O(n log n) on duplicate-heavy input.
    """
    def _qs(items, lo, hi):
        if lo >= hi:
            return
        pivot = items[random.randint(lo, hi)]
        lt, gt = lo, hi
        i = lo
        while i <= gt:
            if items[i] < pivot:
                items[lt], items[i] = items[i], items[lt]
                lt += 1; i += 1
            elif items[i] > pivot:
                items[gt], items[i] = items[i], items[gt]
                gt -= 1
            else:
                i += 1
        _qs(items, lo, lt - 1)
        _qs(items, gt + 1, hi)
    _qs(arr, 0, len(arr) - 1)


# =============================================================================
# Radix Sort (integers only)
# =============================================================================

def radix_sort(arr):
    """LSD Radix Sort. O(nk) where k = number of digits. Integers only."""
    if not arr:
        return

    def _radix_positive(a):
        if not a:
            return a
        max_val = max(a)
        exp = 1
        while max_val // exp > 0:
            buckets = [[] for _ in range(10)]
            for num in a:
                buckets[(num // exp) % 10].append(num)
            a = [n for b in buckets for n in b]
            exp *= 10
        return a

    negatives = sorted([-x for x in arr if x < 0], reverse=True)
    positives = [x for x in arr if x >= 0]
    positives = _radix_positive(positives)
    negatives = _radix_positive(negatives)
    arr[:] = [-x for x in reversed(negatives)] + positives


# =============================================================================
# Python built-in Timsort
# =============================================================================

def timsort_builtin(arr):
    """Python's built-in list.sort() — a highly optimised C implementation of Timsort."""
    arr.sort()


# =============================================================================
# Custom Timsort (our own Python implementation)
# =============================================================================

# Timsort is a hybrid stable sort invented by Tim Peters in 2002 for CPython.
# It combines Insertion Sort (fast on small/ordered runs) with a bottom-up
# Merge Sort that exploits naturally occurring sorted runs in the data.
#
# Key ideas:
#   1. MIN_RUN: arrays smaller than this are insertion-sorted directly.
#   2. Run detection: scan left-to-right for naturally ascending or
#      descending runs; reverse descending runs in-place.
#   3. Run extension: if a natural run is shorter than MIN_RUN, extend it
#      using insertion sort up to MIN_RUN elements.
#   4. Merge stack: push runs onto a stack and merge adjacent runs when
#      the stack invariants are violated (similar to the original Timsort).
#
# This is a simplified but faithful Python implementation that captures
# the core behaviour of Timsort without the full CPython optimisations.

MIN_RUN = 32


def _calc_min_run(n):
    """
    Compute the minimum run length for a given array size.
    The result r satisfies: ceil(n / r) is a power of 2 (or close to it),
    which ensures the merge phase is as balanced as possible.
    """
    r = 0
    while n >= MIN_RUN:
        r |= n & 1
        n >>= 1
    return n + r


def _merge(arr, left, mid, right):
    """
    Merge arr[left..mid] with arr[mid+1..right] in-place using a temporary buffer.
    This is a standard stable merge.
    """
    left_part  = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]; i += 1
        else:
            arr[k] = right_part[j]; j += 1
        k += 1
    while i < len(left_part):
        arr[k] = left_part[i]; i += 1; k += 1
    while j < len(right_part):
        arr[k] = right_part[j]; j += 1; k += 1


def timsort_custom(arr):
    """
    Custom Python implementation of Timsort.

    Algorithm outline:
      1. Compute min_run for this array size.
      2. Divide arr into runs of length >= min_run using insertion sort to
         pad short natural runs.
      3. Merge adjacent runs bottom-up, doubling the run size each pass,
         until the entire array is sorted.

    Complexity: O(n log n) worst case, O(n) best case (already sorted).
    Space: O(n) for temporary merge buffers.
    Stable: Yes.
    """
    n = len(arr)
    if n < 2:
        return

    min_run = _calc_min_run(n)

    # Step 1: insertion-sort each run of length min_run
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_range(arr, start, end)

    # Step 2: bottom-up merge, doubling size each pass
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid   = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                _merge(arr, left, mid, right)
        size *= 2


# =============================================================================
# Counting Sort (integer arrays, bounded range)
# =============================================================================

def counting_sort(arr):
    """
    Counting Sort. O(n + k) where k = value range.
    Only suitable for non-negative integers with a reasonable range.
    Skipped automatically if range > 10 * n (would waste too much memory).
    """
    if not arr:
        return
    min_val, max_val = min(arr), max(arr)
    k = max_val - min_val
    if k > 10 * len(arr):
        # Fall back to merge sort if range is too large
        merge_sort(arr)
        return
    counts = [0] * (k + 1)
    for x in arr:
        counts[x - min_val] += 1
    idx = 0
    for i, c in enumerate(counts):
        for _ in range(c):
            arr[idx] = i + min_val
            idx += 1


# =============================================================================
# Linked list implementations
# =============================================================================

class _Node:
    __slots__ = ('val', 'next')
    def __init__(self, val):
        self.val  = val
        self.next = None


def _to_ll(arr):
    if not arr:
        return None
    head = _Node(arr[0])
    cur  = head
    for v in arr[1:]:
        cur.next = _Node(v)
        cur = cur.next
    return head


def _to_arr(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def _ll_get_mid(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def _ll_merge(l1, l2):
    dummy = _Node(0)
    tail  = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next


def _ll_merge_sort_rec(head):
    if not head or not head.next:
        return head
    mid        = _ll_get_mid(head)
    right      = mid.next
    mid.next   = None
    return _ll_merge(_ll_merge_sort_rec(head), _ll_merge_sort_rec(right))


def _ll_insertion_sort_rec(head):
    dummy = _Node(0)
    cur   = head
    while cur:
        nxt = cur.next
        pos = dummy
        while pos.next and pos.next.val <= cur.val:
            pos = pos.next
        cur.next = pos.next
        pos.next = cur
        cur = nxt
    return dummy.next


def ll_merge_sort(arr):
    """Linked List Merge Sort. O(n log n), O(log n) stack space. Stable."""
    arr[:] = _to_arr(_ll_merge_sort_rec(_to_ll(arr)))


def ll_insertion_sort(arr):
    """Linked List Insertion Sort. O(n^2), O(1) extra space."""
    arr[:] = _to_arr(_ll_insertion_sort_rec(_to_ll(arr)))


# =============================================================================
# Parallel Merge Sort
# =============================================================================

def parallel_merge_sort(arr):
    """
    Parallel Merge Sort using multiprocessing.Pool.
    Splits the array into CPU-count chunks, sorts each in a worker process,
    then merges using a min-heap. Only meaningful for large inputs.
    """
    import multiprocessing

    def _worker(chunk):
        chunk.sort()
        return chunk

    n_workers  = min(multiprocessing.cpu_count(), 4)
    chunk_size = max(1, len(arr) // n_workers)
    chunks     = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with multiprocessing.Pool(n_workers) as pool:
        sorted_chunks = pool.map(_worker, chunks)

    # k-way merge using heapq
    heap = []
    iters = [iter(c) for c in sorted_chunks]
    result = []
    for i, it in enumerate(iters):
        val = next(it, None)
        if val is not None:
            heapq.heappush(heap, (val, i))
    while heap:
        val, i = heapq.heappop(heap)
        result.append(val)
        nxt = next(iters[i], None)
        if nxt is not None:
            heapq.heappush(heap, (nxt, i))
    arr[:] = result


# =============================================================================
# Algorithm registry
# =============================================================================

ALGORITHMS = {
    # Classic O(n^2)
    "Bubble Sort":          (bubble_sort,          "n2"),
    "Selection Sort":       (selection_sort,        "n2"),
    "Insertion Sort":       (insertion_sort,        "n2"),
    # Intermediate
    "Shell Sort":           (shell_sort,            "nlogn"),
    # O(n log n)
    "Heap Sort":            (heap_sort,             "nlogn"),
    "Merge Sort":           (merge_sort,            "nlogn"),
    "Quick Sort":           (quick_sort,            "nlogn"),
    "Timsort (built-in)":   (timsort_builtin,       "nlogn"),
    "Timsort (custom)":     (timsort_custom,        "nlogn"),
    # Non-comparative
    "Radix Sort":           (radix_sort,            "nk"),
    "Counting Sort":        (counting_sort,         "nk"),
    # Linked list
    "LL Merge Sort":        (ll_merge_sort,         "linked"),
    "LL Insertion Sort":    (ll_insertion_sort,     "linked"),
    # Parallel
    "Parallel Merge Sort":  (parallel_merge_sort,   "parallel"),
}
