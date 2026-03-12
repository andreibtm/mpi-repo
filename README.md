## Sorting Algorithms Benchmark Suite

A modular benchmarking system for comparing sorting algorithm performance across different input sizes and data patterns.

### Structure

```
├── algorithms/              # Individual sorting algorithm modules
│   ├── __init__.py         # Algorithm registry (ALGORITHMS dict)
│   ├── bubble.py           # Bubble Sort
│   ├── selection.py        # Selection Sort
│   ├── insertion.py        # Insertion Sort
│   ├── shell.py            # Shell Sort
│   ├── heap.py             # Heap Sort
│   ├── merge.py            # Merge Sort
│   ├── quick.py            # Quick Sort
│   ├── builtin.py          # Python's Timsort
│   └── radix.py            # Radix Sort (NEW!)
├── generators.py           # Data generators (GENERATORS dict)
├── cli.py                  # Command-line interface for benchmarking
├── graph.py                # Visualization (parses markdown output)
├── benchmark.py            # (legacy - use cli.py instead)
└── README.md               # This file
```

### Algorithms Included

- **Bubble Sort** — O(n²) comparison-based
- **Selection Sort** — O(n²) comparison-based
- **Insertion Sort** — O(n²) but fast for small/nearly-sorted data
- **Shell Sort** — O(n log n) with gap sequences
- **Heap Sort** — O(n log n) using heap structure
- **Merge Sort** — O(n log n) stable divide-and-conquer
- **Quick Sort** — O(n log n) average with random pivots
- **Python Timsort** — O(n log n) hybrid (built-in sort)
- **Radix Sort** — O(nk) non-comparative integer sorting (NEW!)

### Data Patterns Tested

- **Random Ints** — Uniformly random integers
- **Almost Sorted** — 98% sorted with small perturbations
- **Reverse Sorted** — Data in descending order
- **Flat (Few Unique)** — Only 5 unique values repeated

### Usage

#### Basic Usage

```bash
# Benchmark all algorithms with default sizes
python3 cli.py

# Benchmark specific algorithms
python3 cli.py --algorithms "Radix Sort" "Quick Sort" "Merge Sort"

# Benchmark with custom sizes
python3 cli.py --sizes 100 1000 10000 100000

# Benchmark with custom output filename
python3 cli.py --output my_results.md
```

#### Advanced Examples

```bash
# Test only fast algorithms with large sizes
python3 cli.py --algorithms "Radix Sort" "Quick Sort" "Python Timsort" \
               --sizes 100000 1000000

# Test sorting algorithms with multiple iterations for averaging
python3 cli.py --algorithms all --iterations 3 --output averaged_results.md

# Benchmark just the quadratic algorithms with small sizes
python3 cli.py --algorithms "Bubble Sort" "Selection Sort" "Insertion Sort" \
               --sizes 50 100 500
```

#### Command-Line Options

```
--algorithms     Algorithm names to test (default: all)
                 Use 'all' for all algorithms or specify names
--sizes          Input sizes to test (default: 50 1000 10000 100000 1000000)
--iterations     Number of iterations per test (default: 1)
--output         Output markdown filename (default: benchmark_results.md)
```

### Generating Graphs

After running a benchmark, generate a graph of the results:

```bash
python3 graph.py
```

This reads `benchmark_results.md` and creates `sorting_graph.png` with a log-scale comparison.

To use a custom markdown file:

Edit `graph.py` and change:

```python
parse_benchmark_markdown("benchmark_results.md", data_shape="Random Ints")
```

### Example Output

```markdown
## Data Size: 1000 elements

| Algorithm       | Data Shape  | Avg Time (s) | Status  |
| :-------------- | :---------- | :----------- | :------ |
| **Radix Sort**  | Random Ints | 0.000428     | Success |
| **Quick Sort**  | Random Ints | 0.000546     | Success |
| **Merge Sort**  | Random Ints | 0.001843     | Success |
| **Bubble Sort** | Random Ints | 0.018220     | Success |
```

### Adding New Algorithms

1. Create a new file in `algorithms/` (e.g., `algorithms/counting.py`)
2. Implement the sorting function that modifies the array in-place
3. Add it to `algorithms/__init__.py`:

```python
from algorithms.counting import counting_sort

ALGORITHMS = {
    # ... existing algorithms ...
    "Counting Sort": (counting_sort, "nk"),  # Add this line
}
```

4. Import it in the `__all__` list

### Adding New Data Generators

1. Add a function to `generators.py`:

```python
def generate_geometric(n):
    """Generate values following a geometric distribution."""
    return [int(1.5 ** i % n) for i in range(n)]
```

2. Register it in the `GENERATORS` dict:

```python
GENERATORS = {
    # ... existing generators ...
    "Geometric": generate_geometric,
}
```

### Notes

- Quadratic algorithms (Bubble, Selection) are automatically skipped for sizes > 10,000
- Recursion limit is set to 20,000 to handle deep recursion in Merge/Quick sort
- Radix Sort is optimized for non-negative integers and handles negatives by separating them
- All timing is averaged across iterations using `time.perf_counter()`
