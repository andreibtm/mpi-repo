"""
Parallel sorting algorithms using multiprocessing.

Bypasses Python's GIL (Global Interpreter Lock) by spawning separate processes,
allowing true multi-core parallelization.

Key insight: For small arrays (< 10,000 elements), the overhead of spawning
processes outweighs the benefit. Parallel sorting shines at massive scales.

Note: On macOS and Windows, multiprocessing uses 'spawn' mode which has overhead.
On Linux, 'fork' mode is faster but less safe.
"""

import multiprocessing
import math


def _worker_sort(chunk):
    """Sort a chunk using Python's built-in sort (runs on separate CPU core)."""
    chunk.sort()
    return chunk


def _merge_two_arrays(left, right):
    """Merge two sorted arrays."""
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def parallel_merge_sort(arr):
    """
    Sort array using parallel merge sort with multiprocessing.
    
    Time: O(n log n) + overhead
    Space: O(n) for sorted chunks
    
    Strategy:
    1. Split array into chunks (one per CPU core)
    2. Sort chunks in parallel on separate CPU cores
    3. Merge sorted chunks back together
    
    Performance:
    - < 10K elements: Standard sort is faster (overhead dominates)
    - > 100K elements: Parallel sort shows real speedup
    - > 1M elements: Parallel sort can be 2-4x faster on multi-core systems
    
    Note: On macOS, multiprocessing spawning has overhead (~0.05-0.1s).
    """
    # Don't use parallel for small arrays; overhead is too high
    if len(arr) < 10000:
        arr.sort()
        return
    
    try:
        cores = multiprocessing.cpu_count()
        chunk_size = math.ceil(len(arr) / cores)
        
        # 1. Split array into chunks
        chunks = [arr[i : i + chunk_size] for i in range(0, len(arr), chunk_size)]
        
        # 2. Sort chunks in parallel using a Process Pool
        # Use context managers and explicit process spawning for better control
        with multiprocessing.Pool(processes=cores) as pool:
            sorted_chunks = pool.map(_worker_sort, chunks)
        
        # 3. Merge sorted chunks sequentially
        while len(sorted_chunks) > 1:
            merged_level = []
            for i in range(0, len(sorted_chunks), 2):
                if i + 1 < len(sorted_chunks):
                    merged = _merge_two_arrays(sorted_chunks[i], sorted_chunks[i + 1])
                    merged_level.append(merged)
                else:
                    merged_level.append(sorted_chunks[i])
            sorted_chunks = merged_level
        
        # Copy the sorted data back to the original array
        arr[:] = sorted_chunks[0]
    except Exception as e:
        # Fallback to single-threaded sort if multiprocessing fails
        print(f"Warning: Parallel sort failed ({type(e).__name__}), falling back to regular sort")
        arr.sort()

