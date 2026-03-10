import time
import random
import copy
import sys
import string
import heapq


sys.setrecursionlimit(20000)

# ==========================================
# 1. SORTING ALGORITHMS
# ==========================================
# Increase recursion depth for deep Quick/Merge sort trees


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def heap_sort(arr):
    # Using Python's heapq for an efficient O(n log n) in-place-like heap sort
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

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

def built_in_sort(arr):
    """Python's highly optimized Timsort."""
    arr.sort()

def insertion_sort(arr):
    """O(n^2) but extremely fast for small or almost-sorted lists."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    """O(n log n) stable sort. Implemented to modify the array in-place for our benchmark."""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def quick_sort(arr):
    """O(n log n) average case. Uses a random pivot to avoid worst-case on sorted data."""
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


# ==========================================
# 2. DATA GENERATORS
# ==========================================

def generate_random_ints(n): return [random.randint(0, 1000000) for _ in range(n)]
def generate_sorted_ints(n): return list(range(n))
def generate_reverse_ints(n): return list(range(n, 0, -1))
def generate_flat_ints(n): return [random.choice([1, 2, 3]) for _ in range(n)]
def generate_floats(n): return [random.uniform(0.0, 1000.0) for _ in range(n)]
def generate_strings(n): 
    return [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(n)]

def generate_almost_sorted(n, randomness=0.02):
    arr = list(range(n))
    num_swaps = int(n * randomness)
    for _ in range(num_swaps):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


# ==========================================
# 3. BENCHMARKING LOGIC
# ==========================================

def run_benchmark(sort_function, data, iterations=1):
    total_time = 0
    for _ in range(iterations):
        data_copy = copy.deepcopy(data) 
        start_time = time.perf_counter()
        sort_function(data_copy)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    return total_time / iterations

# ==========================================
# 3. UPDATED MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    # Define test sizes: From tiny to large
    # Note: 1,000,000 is pushing Python's limits for Merge/Quick sort.
    test_cases = {
        50: 1000,       # Small
        1000: 100,      # Medium-Small
        10000: 10,      # Medium
        100000: 2,      # Large
        1000000: 1      # Very Large (Only for O(n log n) algos)
    }

    generators = {
        "Random Ints": lambda n: [random.randint(0, n*10) for _ in range(n)],
        "Almost Sorted": lambda n: sorted([random.randint(0, n*10) for _ in range(n)])[:int(n*0.98)] + [random.randint(0, n*10) for _ in range(int(n*0.02))],
        "Reverse Sorted": lambda n: list(range(n, 0, -1)),
        "Flat (Few Unique)": lambda n: [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]
    }

    # Map algorithms to their Big-O category
    algorithms = {
        "Python Timsort": (built_in_sort, "nlogn"),
        "Quick Sort": (quick_sort, "nlogn"),
        "Merge Sort": (merge_sort, "nlogn"),
        "Heap Sort": (heap_sort, "nlogn"),
        "Shell Sort": (shell_sort, "n_intermediate"),
        "Insertion Sort": (insertion_sort, "n2"),
        "Selection Sort": (selection_sort, "n2"),
        "Bubble Sort": (bubble_sort, "n2")
    }

    output_filename = "comprehensive_benchmark.md"
    
    with open(output_filename, "w") as md_file:
        md_file.write("# Comprehensive Sorting Analysis\n\n")
        
        for size, iterations in test_cases.items():
            print(f"Testing Size: {size}...")
            md_file.write(f"## Data Size: {size} elements\n")
            md_file.write("| Algorithm | Data Shape | Avg Time (s) | Status |\n")
            md_file.write("| :--- | :--- | :--- | :--- |\n")
            
            for gen_name, generator in generators.items():
                base_data = generator(size)
                
                for alg_name, (func, complexity) in algorithms.items():
                    # SAFETY CHECK: Skip O(n^2) if size is too large
                    if complexity == "n2" and size > 10000:
                        md_file.write(f"| {alg_name} | {gen_name} | N/A | Skipped (Too Slow) |\n")
                        continue
                    
                    try:
                        avg_time = run_benchmark(func, base_data, iterations)
                        md_file.write(f"| **{alg_name}** | {gen_name} | {avg_time:.6f} | Success |\n")
                    except Exception as e:
                        md_file.write(f"| {alg_name} | {gen_name} | Error | {str(e)[:20]} |\n")
            
            md_file.write("\n---\n\n")

    print(f"Done! Data exported to {output_filename}")