## Sorting Algorithms Benchmark Suite

A comprehensive modular benchmarking system for comparing sorting algorithm performance across different data structures (arrays vs. linked lists), execution models (single-core vs. multi-core), input sizes, and data patterns.

### Project Structure

```
├── algorithms/                  # Individual sorting algorithm modules
│   ├── __init__.py             # Algorithm registry (ALGORITHMS dict)
│   ├── bubble.py               # Bubble Sort
│   ├── selection.py            # Selection Sort
│   ├── insertion.py            # Insertion Sort
│   ├── shell.py                # Shell Sort
│   ├── heap.py                 # Heap Sort
│   ├── merge.py                # Merge Sort
│   ├── quick.py                # Quick Sort
│   ├── builtin.py              # Python's Timsort
│   ├── radix.py                # Radix Sort
│   ├── ll_merge.py             # Linked List Merge Sort
│   └── ll_insertion.py         # Linked List Insertion Sort
│
├── data_structures.py           # Linked list implementation & conversions
├── parallel_sort.py             # Multi-core parallel sorting (multiprocessing)
├── generators.py                # Data generators (GENERATORS dict)
├── cli.py                       # Command-line interface
├── graph.py                     # Visualization (parses markdown output)
├── benchmark.py                 # (legacy - use cli.py instead)
└── ALGORITHMS_README.md         # This file
```

### Algorithms Included

#### Classic Array-Based (8 algorithms)

- **Bubble Sort** — O(n²) comparison-based
- **Selection Sort** — O(n²) comparison-based
- **Insertion Sort** — O(n²) but fast for small/nearly-sorted data
- **Shell Sort** — O(n log n) with gap sequences
- **Heap Sort** — O(n log n) using heap structure
- **Merge Sort** — O(n log n) stable divide-and-conquer
- **Quick Sort** — O(n log n) average with random pivots
- **Python Timsort** — O(n log n) hybrid (built-in sort)

#### Integer-Specific

- **Radix Sort** — O(nk) non-comparative, handles negatives

#### Linked List Variants

- **LL Merge Sort** — O(n log n), O(1) extra space (pointer rewiring)
- **LL Insertion Sort** — O(n²), O(1) extra space

#### Parallel / Multi-Core

- **Parallel Merge Sort** — Multi-core version using multiprocessing (spawns processes to bypass GIL)

### Data Patterns Tested

- **Random Ints** — Uniformly random integers
- **Almost Sorted** — 98% sorted with small perturbations
- **Reverse Sorted** — Data in descending order
- **Flat (Few Unique)** — Only 5 unique values repeated

### Quick Start

#### Test Categories

```bash
# Basic: All classic array-based algorithms
python3 cli.py --category basic --sizes 100 1000 10000

# Linked List: Compare array vs linked list implementations
python3 cli.py --category linked-list --sizes 1000 10000

# Parallel: Multi-core sorting (shows benefit at large sizes)
python3 cli.py --category parallel --sizes 100000 1000000

# Comparison: Array vs Linked List vs Parallel (same algorithm)
python3 cli.py --category comparison --sizes 10000 100000

# Integer sorting: Radix Sort vs comparison-based
python3 cli.py --category integer --sizes 100000 1000000
```

#### Individual Algorithms

```bash
# Specific algorithms
python3 cli.py --algorithms "Radix Sort" "Quick Sort" "Merge Sort"

# All algorithms (default)
python3 cli.py --algorithms all --sizes 50 1000 10000 100000
```

#### Custom Parameters

```bash
# Custom sizes and output file
python3 cli.py --category basic --sizes 500 5000 50000 --output my_results.md

# Multiple iterations for averaging
python3 cli.py --category comparison --sizes 100000 1000000 --iterations 3

# Combine everything
python3 cli.py --algorithms "Radix Sort" "Merge Sort" "Parallel Merge Sort" \
               --sizes 50000 500000 --iterations 2 --output perf_test.md
```

### Expected Performance Insights

#### Array vs. Linked List

**Key Finding:** Despite Linked List Merge Sort being theoretically superior (O(1) extra space via pointer rewiring), **Array Merge Sort is faster in practice**.

**Why?**

- Arrays are contiguous in memory (cache-friendly)
- Linked lists create scattered `ListNode` objects throughout RAM
- Python's memory allocator adds overhead for each object

**Use case:** Linked List Merge Sort shines in languages with different memory models (C++, Java with better memory locality), or when in-place sorting with zero extra memory is absolutely critical.

#### Single-Core vs. Parallel

**Key Finding:** Parallel sorting has **overhead that dominates at small sizes**.

**Threshold:**

- **< 10,000 elements:** Standard single-core sort is faster (process spawning overhead)
- **≥ 10,000 elements:** Parallel shows benefit on multi-core systems
- **≥ 100,000+ elements:** Parallel can be 2-4x faster on 4+ core CPUs

**Example Output:**

```
Size 1,000:    Parallel skipped (overhead too high)
               Merge Sort: 0.000675s
               LL Merge Sort: 0.000631s

Size 10,000:   Parallel tested
               Merge Sort: 0.008707s
               LL Merge Sort: 0.008046s
               Parallel Merge Sort: 0.118057s  ← Still slower due to overhead

Size 100,000+: Parallel wins
               Merge Sort: ~0.100s
               Parallel Merge Sort: ~0.030s  (on 4-core system)
```

### Command-Line Options

```
--category {basic, integer, linked-list, parallel, comparison}
            Use preset algorithm groups

--algorithms ALGORITHM_NAMES
            Specific algorithms or 'all'

--sizes SIZE1 SIZE2 SIZE3 ...
            Input sizes to test (default: 50 1000 10000 100000 1000000)

--iterations N
            Repetitions per test for averaging (default: 1)

--output FILENAME
            Markdown output file (default: benchmark_results.md)
```

### Generating Graphs

After running a benchmark:

```bash
.venv/bin/python graph.py
```

This reads the markdown output and creates `sorting_graph.png` with:

- Logarithmic scale on X-axis (handles sizes 50 to 1,000,000)
- Linear scale on Y-axis (time in seconds)
- One curve per algorithm

### Adding New Algorithms

1. Create `algorithms/myalgo.py`:

```python
def my_sort(arr):
    """Your implementation here."""
    pass
```

2. Update `algorithms/__init__.py`:

```python
from algorithms.myalgo import my_sort

ALGORITHMS = {
    # ... existing ...
    "My Algorithm": (my_sort, "complexity_class"),
}
```

3. Add to `__all__` list

4. (Optional) Add to a category in `cli.py`:

```python
ALGORITHM_CATEGORIES = {
    "custom": ["My Algorithm", "Other Algorithm"],
}
```

### Adding New Data Generators

1. Add to `generators.py`:

```python
def generate_zigzag(n):
    """Alternating high/low values."""
    return [i if i % 2 == 0 else n - i for i in range(n)]
```

2. Register in `GENERATORS`:

```python
GENERATORS = {
    # ... existing ...
    "Zigzag": generate_zigzag,
}
```

### Understanding the Code

- **`data_structures.py`**: `ListNode` class + conversion helpers (`array_to_linked_list`, `linked_list_to_array`)
- **`parallel_sort.py`**: Uses `multiprocessing.Pool` to spawn worker processes that sort chunks in parallel, bypassing Python's GIL
- **`cli.py`**: Orchestrates the benchmark, handles CLI args, coordinates with generators and algorithms
- **`graph.py`**: Parses markdown tables, extracts timing data, plots with matplotlib

### Performance Notes

- **Recursion Limit:** Set to 20,000 to handle deep sort trees (Merge/Quick Sort)
- **O(n²) Safety:** Automatically skipped for arrays > 10,000 to avoid timeouts
- **Parallel Overhead:** Multiprocessing spawning takes ~0.05-0.1 seconds; doesn't pay off until n >> 10K
- **GIL Bypass:** `multiprocessing` creates separate Python processes (not threads) to enable true multi-core execution

### Example Workflow

```bash
# 1. Run a focused benchmark on linked lists
.venv/bin/python cli.py --category linked-list --sizes 5000 50000 100000

# 2. Compare with array version
.venv/bin/python cli.py --category comparison --sizes 10000 100000 1000000

# 3. Visualize
.venv/bin/python graph.py   # Generates sorting_graph.png

# 4. Analyze the markdown output
cat benchmark_results.md
```

### References & Credits

- **Linked List concepts:** Classic CS algorithms (Sedgewick, Cormen et al.)
- **Parallel sorting:** Python multiprocessing module
- **Benchmark design:** Based on comprehensive algorithm analysis principles
- **Original implementation:** Google Gemini API suggestions, implemented with modular architecture
