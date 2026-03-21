# Sorting Algorithms Benchmark Suite

A clean, modular benchmarking framework for comparing sorting algorithm performance across different input sizes, data structures, and data patterns.

---

## Structure

```
├── algorithms/
│   └── __init__.py      # All algorithm implementations + registry
├── generators.py        # All data generators + registry
├── cli.py               # Main benchmark runner
├── graph.py             # Result visualisation
└── README.md
```

---

## Algorithms

| Algorithm | Complexity | Notes |
| :--- | :--- | :--- |
| Bubble Sort | O(n²) | Early-exit optimisation |
| Selection Sort | O(n²) | |
| Insertion Sort | O(n²) | Best on nearly-sorted data |
| Shell Sort | O(n log n) | Gap-sequence variant |
| Heap Sort | O(n log n) | In-place via heapq |
| Merge Sort | O(n log n) | Stable |
| Quick Sort | O(n log n) avg | Randomised pivot |
| Python Timsort | O(n log n) | Built-in `list.sort()` |
| Radix Sort | O(nk) | Integers only |
| LL Merge Sort | O(n log n) | On linked list, O(1) extra space |
| LL Insertion Sort | O(n²) | On linked list |
| Parallel Merge Sort | O(n log n) | multiprocessing, ≥10k elements |

---

## Data Generators

| Name | Description |
| :--- | :--- |
| Random Ints | Uniformly random integers |
| Sorted Ints | Fully ascending |
| Reverse Sorted | Fully descending |
| Almost Sorted | 98% sorted, 2% randomly swapped |
| Half Sorted | First half sorted, second half random |
| Flat (Few Unique) | Only 5 distinct values — high duplicates |
| Floats | Random floats |
| Strings | Random 5-char lowercase strings |

---

## Usage

```bash
# Full benchmark — all algorithms, all data shapes, auto-scaled iterations
python cli.py

# Fast algorithms only, large sizes
python cli.py --category fast --sizes 100000 1000000

# O(n²) algorithms with small sizes and many iterations
python cli.py --category slow --sizes 20 30 50 100 --iterations 100000

# Linked list vs array comparison
python cli.py --category linked --sizes 1000 10000 100000

# Parallel sorting
python cli.py --category parallel --sizes 100000 1000000

# Specific algorithms and sizes
python cli.py --algorithms "Quick Sort" "Merge Sort" "Radix Sort" --sizes 50000

# Custom output file
python cli.py --output my_run.md
```

### Categories

| Category | Algorithms included |
| :--- | :--- |
| `all` | Everything (default) |
| `fast` | Shell, Heap, Merge, Quick, Timsort, Radix |
| `slow` | Bubble, Selection, Insertion |
| `linked` | LL Merge Sort, LL Insertion Sort + array equivalents |
| `parallel` | Parallel Merge Sort vs Timsort vs Merge Sort |
| `integer` | Radix Sort + comparison sorts |

---

## Visualisation

```bash
# Plot Random Ints results (default)
python graph.py

# Plot a specific data shape
python graph.py --shape "Reverse Sorted"

# Save to file
python graph.py --shape "Almost Sorted" --save almost_sorted.png
```

---

## Iteration Scaling

For small lists, a single sort is too fast to measure reliably.
The benchmark auto-scales iterations per size:

| Size | Default iterations |
| ---: | ---: |
| 20 | 100,000 |
| 30 | 100,000 |
| 50 | 100,000 |
| 100 | 100,000 |
| 1,000 | 1,000 |
| 10,000 | 100 |
| 100,000 | 10 |
| 1,000,000 | 1 |

Override with `--iterations N` to use the same count for every size.

---

## Notes

- O(n²) algorithms are automatically skipped for sizes > 10,000
- Radix Sort is skipped for Floats and Strings (integers only)
- Parallel Merge Sort is skipped for sizes < 10,000 (overhead dominates)
- Fresh data is generated for every iteration (critical for small-list accuracy)
- Results are saved as both `.md` (human-readable) and `.csv` (for graphing/analysis)
