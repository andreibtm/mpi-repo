# Sorting Algorithms Benchmark Suite — v2

A modular benchmarking framework comparing sorting algorithms across input size,
data shape, element type, data structure, and hardware platform.

## What's new in v2

- **Nanosecond timing** — uses `time.perf_counter_ns()` so no result ever shows 0
- **Custom Timsort** — hand-written Python implementation alongside the built-in
- **Counting Sort** added (non-comparative, integer arrays with bounded range)
- **Shell Sort** now uses the Knuth gap sequence (much better than n//2)
- **Standard deviation, min, max** recorded for every measurement
- **Timsort comparison category** — `--category timsort` isolates the comparison

## Project structure

```
├── algorithms/
│   └── __init__.py    # All implementations + ALGORITHMS registry
├── generators.py      # All data generators + GENERATORS registry
├── cli.py             # Benchmark runner
├── graph.py           # Charting
└── README.md
```

## Algorithms

| Algorithm | Complexity | Notes |
| :--- | :--- | :--- |
| Bubble Sort | O(n²) | Early-exit optimisation |
| Selection Sort | O(n²) | No adaptivity |
| Insertion Sort | O(n²) | Highly adaptive |
| Shell Sort | O(n^1.5) | Knuth gap sequence |
| Heap Sort | O(n log n) | In-place |
| Merge Sort | O(n log n) | Stable |
| Quick Sort | O(n log n) avg | Randomised pivot, 3-way partition |
| Timsort (built-in) | O(n log n) | Python's C-level list.sort() |
| Timsort (custom) | O(n log n) | Hand-written Python implementation |
| Radix Sort | O(nk) | Integers only |
| Counting Sort | O(n+k) | Integers only, bounded range |
| LL Merge Sort | O(n log n) | Linked list, O(1) extra space |
| LL Insertion Sort | O(n²) | Linked list |
| Parallel Merge Sort | O(n log n) | multiprocessing, large inputs only |

## Usage

```bash
# Full benchmark
python cli.py

# Timsort built-in vs custom vs competitors
python cli.py --category timsort --sizes 20 30 50 100 1000 10000 100000 1000000

# Fast algorithms only
python cli.py --category fast --sizes 100000 1000000

# O(n^2) algorithms, small sizes
python cli.py --category slow --sizes 20 30 50 100 1000

# Linked list comparison
python cli.py --category linked --sizes 1000 10000 100000

# Save to specific file
python cli.py --output results_mac.md
```

## Charting

```bash
# Plot Random Ints
python graph.py

# Timsort comparison panel
python graph.py --category timsort --save timsort_comparison.png

# Compare two machines
python graph.py --compare results_mac.csv results_windows.csv \
                --labels "Apple M4" "Windows x86" --shape "Random Ints"
```

## Timing methodology

All measurements use `time.perf_counter_ns()` (nanosecond resolution).
A fresh random array is generated for every iteration.
Iteration counts scale inversely with input size:

| Size | Default iterations |
| ---: | ---: |
| 20 – 100 | 100,000 |
| 1,000 | 1,000 |
| 10,000 | 100 |
| 100,000 | 10 |
| 1,000,000 | 3 |

The CSV output includes average, standard deviation, min, and max for every
(algorithm, shape, size) triple.
