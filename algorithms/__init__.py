"""
Sorting algorithm registry.
Each entry: "Name": (function, complexity_tag)

Complexity tags used for skip logic in the benchmark runner:
  "n2"         — O(n²): skipped for sizes > 10,000
  "nlogn"      — O(n log n): runs at all sizes
  "nk"         — O(nk) non-comparative (Radix): integer-only, runs at all sizes
  "linked"     — Linked list variants
  "parallel"   — Parallel variants: skipped for sizes < 10,000
"""

import sys
import heapq
import random

sys.setrecursionlimit(500000)

# ── Bubble Sort ────────────────────────────────────────────────────────────────

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# ── Selection Sort ─────────────────────────────────────────────────────────────

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# ── Insertion Sort ─────────────────────────────────────────────────────────────

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# ── Shell Sort ─────────────────────────────────────────────────────────────────

def shell_sort(arr):
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

# ── Heap Sort ──────────────────────────────────────────────────────────────────

def heap_sort(arr):
    heapq.heapify(arr)
    arr[:] = [heapq.heappop(arr) for _ in range(len(arr))]

# ── Merge Sort ─────────────────────────────────────────────────────────────────

def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# ── Quick Sort ─────────────────────────────────────────────────────────────────

def quick_sort(arr):
    def _qs(items, low, high):
        if low >= high:
            return
        # 3-way partition: handles duplicates without deep recursion
        pivot = items[random.randint(low, high)]
        lt, gt = low, high
        i = low
        while i <= gt:
            if items[i] < pivot:
                items[lt], items[i] = items[i], items[lt]
                lt += 1
                i += 1
            elif items[i] > pivot:
                items[gt], items[i] = items[i], items[gt]
                gt -= 1
            else:
                i += 1
        _qs(items, low, lt - 1)
        _qs(items, gt + 1, high)
    _qs(arr, 0, len(arr) - 1)

# ── Python Timsort (built-in) ──────────────────────────────────────────────────

def timsort(arr):
    arr.sort()

# ── Radix Sort (integers only) ─────────────────────────────────────────────────

def radix_sort(arr):
    if not arr:
        return

    # Handle negatives: sort separately and combine
    negatives = [-x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]

    def _radix(a):
        if not a:
            return a
        max_val = max(a)
        exp = 1
        while max_val // exp > 0:
            counting = [[] for _ in range(10)]
            for num in a:
                counting[(num // exp) % 10].append(num)
            a = [num for bucket in counting for num in bucket]
            exp *= 10
        return a

    positives = _radix(positives)
    negatives = _radix(negatives)
    arr[:] = [-x for x in reversed(negatives)] + positives

# ── Linked List implementations ────────────────────────────────────────────────

class _Node:
    __slots__ = ('val', 'next')
    def __init__(self, val):
        self.val = val
        self.next = None

def _to_ll(arr):
    if not arr:
        return None
    head = _Node(arr[0])
    cur = head
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
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

def _ll_merge_sort(head):
    if not head or not head.next:
        return head
    mid = _ll_get_mid(head)
    right = mid.next
    mid.next = None
    return _ll_merge(_ll_merge_sort(head), _ll_merge_sort(right))

def _ll_insertion_sort(head):
    dummy = _Node(0)
    cur = head
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
    """Linked list merge sort — O(n log n), O(1) extra space."""
    head = _to_ll(arr)
    arr[:] = _to_arr(_ll_merge_sort(head))

def ll_insertion_sort(arr):
    """Linked list insertion sort — O(n²), O(1) extra space."""
    head = _to_ll(arr)
    arr[:] = _to_arr(_ll_insertion_sort(head))

# ── Parallel Sort ──────────────────────────────────────────────────────────────

def parallel_merge_sort(arr):
    """
    Parallel merge sort using multiprocessing.
    Splits into CPU-count chunks, sorts each in a worker process, then merges.
    Only meaningful for large inputs (>= 10,000 elements).
    """
    import multiprocessing

    def _worker(chunk):
        chunk.sort()
        return chunk

    def _merge_sorted(lists):
        import heapq
        result = []
        heap = []
        iters = [iter(lst) for lst in lists]
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
        return result

    n_workers = min(multiprocessing.cpu_count(), 4)
    chunk_size = max(1, len(arr) // n_workers)
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with multiprocessing.Pool(n_workers) as pool:
        sorted_chunks = pool.map(_worker, chunks)

    arr[:] = _merge_sorted(sorted_chunks)


# ── Algorithm Registry ─────────────────────────────────────────────────────────

ALGORITHMS = {
    # Classic O(n²)
    "Bubble Sort":          (bubble_sort,          "n2"),
    "Selection Sort":       (selection_sort,        "n2"),
    "Insertion Sort":       (insertion_sort,        "n2"),
    # Intermediate
    "Shell Sort":           (shell_sort,            "nlogn"),
    # O(n log n)
    "Heap Sort":            (heap_sort,             "nlogn"),
    "Merge Sort":           (merge_sort,            "nlogn"),
    "Quick Sort":           (quick_sort,            "nlogn"),
    "Python Timsort":       (timsort,               "nlogn"),
    # Non-comparative (integers only)
    "Radix Sort":           (radix_sort,            "nk"),
    # Linked list variants
    "LL Merge Sort":        (ll_merge_sort,         "linked"),
    "LL Insertion Sort":    (ll_insertion_sort,     "linked"),
    # Parallel
    "Parallel Merge Sort":  (parallel_merge_sort,   "parallel"),
}
