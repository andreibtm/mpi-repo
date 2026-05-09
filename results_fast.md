# Sorting Algorithm Benchmark Results

> Timing: `time.perf_counter_ns()` — nanosecond resolution

## Size: 20  x  100,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Shell Sort** | Random Ints | 4.90 us | 423.7 ns | 3.62 us | 21.62 us | OK |
| **Heap Sort** | Random Ints | 1.77 us | 236.7 ns | 1.58 us | 40.58 us | OK |
| **Merge Sort** | Random Ints | 12.29 us | 339.3 ns | 11.54 us | 38.92 us | OK |
| **Quick Sort** | Random Ints | 12.14 us | 1.07 us | 8.67 us | 41.33 us | OK |
| **Timsort (built-in)** | Random Ints | 464.5 ns | 74.3 ns | 333.0 ns | 11.33 us | OK |
| **Timsort (custom)** | Random Ints | 5.96 us | 738.6 ns | 3.08 us | 25.83 us | OK |
| **Radix Sort** | Random Ints | 6.59 us | 274.2 ns | 6.25 us | 23.50 us | OK |
| **Counting Sort** | Random Ints | 11.16 us | 702.9 ns | 7.54 us | 37.92 us | OK |
| **Shell Sort** | Sorted Ints | 2.39 us | 144.5 ns | 2.21 us | 19.67 us | OK |
| **Heap Sort** | Sorted Ints | 1.66 us | 154.0 ns | 1.58 us | 24.04 us | OK |
| **Merge Sort** | Sorted Ints | 10.68 us | 323.8 ns | 10.25 us | 31.00 us | OK |
| **Quick Sort** | Sorted Ints | 12.55 us | 2.01 us | 9.42 us | 66.33 us | OK |
| **Timsort (built-in)** | Sorted Ints | 111.9 ns | 41.2 ns | 41.0 ns | 6.00 us | OK |
| **Timsort (custom)** | Sorted Ints | 1.39 us | 117.7 ns | 1.25 us | 11.88 us | OK |
| **Radix Sort** | Sorted Ints | 4.48 us | 274.4 ns | 4.25 us | 29.96 us | OK |
| **Counting Sort** | Sorted Ints | 2.96 us | 187.6 ns | 2.75 us | 17.92 us | OK |
| **Shell Sort** | Reverse Sorted | 3.97 us | 199.1 ns | 3.75 us | 22.00 us | OK |
| **Heap Sort** | Reverse Sorted | 1.63 us | 150.7 ns | 1.54 us | 14.71 us | OK |
| **Merge Sort** | Reverse Sorted | 11.21 us | 342.5 ns | 10.71 us | 40.50 us | OK |
| **Quick Sort** | Reverse Sorted | 12.52 us | 2.06 us | 9.42 us | 60.42 us | OK |
| **Timsort (built-in)** | Reverse Sorted | 115.7 ns | 46.5 ns | 41.0 ns | 6.29 us | OK |
| **Timsort (custom)** | Reverse Sorted | 10.05 us | 310.8 ns | 9.58 us | 27.00 us | OK |
| **Radix Sort** | Reverse Sorted | 4.50 us | 260.5 ns | 4.29 us | 31.29 us | OK |
| **Counting Sort** | Reverse Sorted | 2.91 us | 176.3 ns | 2.75 us | 21.58 us | OK |
| **Shell Sort** | Almost Sorted | 3.04 us | 568.4 ns | 2.29 us | 20.50 us | OK |
| **Heap Sort** | Almost Sorted | 1.73 us | 157.3 ns | 1.58 us | 19.38 us | OK |
| **Merge Sort** | Almost Sorted | 11.25 us | 420.4 ns | 10.42 us | 32.17 us | OK |
| **Quick Sort** | Almost Sorted | 12.53 us | 2.14 us | 9.33 us | 73.92 us | OK |
| **Timsort (built-in)** | Almost Sorted | 261.1 ns | 95.0 ns | 83.0 ns | 10.25 us | OK |
| **Timsort (custom)** | Almost Sorted | 2.13 us | 482.6 ns | 1.33 us | 15.25 us | OK |
| **Radix Sort** | Almost Sorted | 4.55 us | 267.3 ns | 4.33 us | 26.46 us | OK |
| **Counting Sort** | Almost Sorted | 3.03 us | 158.5 ns | 2.83 us | 18.50 us | OK |
| **Shell Sort** | Half Sorted | 4.22 us | 400.1 ns | 2.83 us | 19.46 us | OK |
| **Heap Sort** | Half Sorted | 1.86 us | 145.0 ns | 1.71 us | 22.75 us | OK |
| **Merge Sort** | Half Sorted | 11.83 us | 323.9 ns | 11.04 us | 29.04 us | OK |
| **Quick Sort** | Half Sorted | 10.21 us | 1.13 us | 6.46 us | 31.92 us | OK |
| **Timsort (built-in)** | Half Sorted | 324.3 ns | 43.2 ns | 250.0 ns | 8.83 us | OK |
| **Timsort (custom)** | Half Sorted | 3.70 us | 557.3 ns | 1.83 us | 35.21 us | OK |
| **Radix Sort** | Half Sorted | 4.77 us | 406.5 ns | 3.04 us | 42.00 us | OK |
| **Counting Sort** | Half Sorted | 3.19 us | 199.8 ns | 2.50 us | 18.38 us | OK |
| **Shell Sort** | Flat (Few Unique) | 4.17 us | 384.5 ns | 3.04 us | 23.21 us | OK |
| **Heap Sort** | Flat (Few Unique) | 1.92 us | 153.5 ns | 1.75 us | 17.96 us | OK |
| **Merge Sort** | Flat (Few Unique) | 12.24 us | 317.0 ns | 11.38 us | 28.21 us | OK |
| **Quick Sort** | Flat (Few Unique) | 5.57 us | 1.94 us | 2.67 us | 49.71 us | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 444.1 ns | 107.9 ns | 291.0 ns | 17.92 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 5.16 us | 716.2 ns | 2.29 us | 20.79 us | OK |
| **Radix Sort** | Flat (Few Unique) | 3.12 us | 227.3 ns | 2.92 us | 30.25 us | OK |
| **Counting Sort** | Flat (Few Unique) | 2.32 us | 164.3 ns | 2.08 us | 21.42 us | OK |
| **Shell Sort** | Floats | 4.90 us | 429.5 ns | 3.42 us | 23.50 us | OK |
| **Heap Sort** | Floats | 1.71 us | 126.4 ns | 1.54 us | 20.00 us | OK |
| **Merge Sort** | Floats | 12.20 us | 332.0 ns | 11.50 us | 31.62 us | OK |
| **Quick Sort** | Floats | 12.73 us | 2.21 us | 9.50 us | 75.54 us | OK |
| **Timsort (built-in)** | Floats | 517.5 ns | 90.5 ns | 416.0 ns | 17.96 us | OK |
| **Timsort (custom)** | Floats | 5.91 us | 724.5 ns | 3.42 us | 30.42 us | OK |
| Radix Sort | Floats | — | — | — | — | Skipped (integers only) |
| Counting Sort | Floats | — | — | — | — | Skipped (integers only) |
| **Shell Sort** | Strings | 5.19 us | 446.1 ns | 3.71 us | 21.88 us | OK |
| **Heap Sort** | Strings | 2.21 us | 122.2 ns | 2.00 us | 15.38 us | OK |
| **Merge Sort** | Strings | 12.42 us | 324.4 ns | 11.79 us | 34.62 us | OK |
| **Quick Sort** | Strings | 12.97 us | 1.05 us | 10.00 us | 41.83 us | OK |
| **Timsort (built-in)** | Strings | 674.6 ns | 73.2 ns | 542.0 ns | 14.50 us | OK |
| **Timsort (custom)** | Strings | 6.35 us | 895.1 ns | 3.50 us | 22.83 us | OK |
| Radix Sort | Strings | — | — | — | — | Skipped (integers only) |
| Counting Sort | Strings | — | — | — | — | Skipped (integers only) |

---

## Size: 30  x  100,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Shell Sort** | Random Ints | 8.28 us | 630.4 ns | 6.21 us | 33.04 us | OK |
| **Heap Sort** | Random Ints | 2.70 us | 168.2 ns | 2.46 us | 19.04 us | OK |
| **Merge Sort** | Random Ints | 19.64 us | 651.3 ns | 18.54 us | 93.83 us | OK |
| **Quick Sort** | Random Ints | 19.60 us | 1.45 us | 14.75 us | 42.58 us | OK |
| **Timsort (built-in)** | Random Ints | 748.6 ns | 71.9 ns | 625.0 ns | 9.21 us | OK |
| **Timsort (custom)** | Random Ints | 11.93 us | 1.29 us | 6.54 us | 43.62 us | OK |
| **Radix Sort** | Random Ints | 8.56 us | 267.6 ns | 8.17 us | 27.00 us | OK |
| **Counting Sort** | Random Ints | 17.74 us | 898.5 ns | 12.79 us | 44.33 us | OK |
| **Shell Sort** | Sorted Ints | 3.72 us | 176.0 ns | 3.50 us | 19.67 us | OK |
| **Heap Sort** | Sorted Ints | 2.59 us | 154.9 ns | 2.46 us | 19.08 us | OK |
| **Merge Sort** | Sorted Ints | 17.15 us | 418.0 ns | 16.58 us | 48.71 us | OK |
| **Quick Sort** | Sorted Ints | 20.07 us | 2.49 us | 15.67 us | 89.75 us | OK |
| **Timsort (built-in)** | Sorted Ints | 139.3 ns | 50.4 ns | 83.0 ns | 10.38 us | OK |
| **Timsort (custom)** | Sorted Ints | 1.89 us | 132.8 ns | 1.75 us | 18.67 us | OK |
| **Radix Sort** | Sorted Ints | 5.80 us | 249.9 ns | 5.58 us | 25.67 us | OK |
| **Counting Sort** | Sorted Ints | 4.22 us | 217.3 ns | 3.96 us | 20.17 us | OK |
| **Shell Sort** | Reverse Sorted | 7.20 us | 267.4 ns | 6.88 us | 33.00 us | OK |
| **Heap Sort** | Reverse Sorted | 2.48 us | 182.7 ns | 2.33 us | 25.38 us | OK |
| **Merge Sort** | Reverse Sorted | 17.71 us | 418.5 ns | 17.12 us | 42.88 us | OK |
| **Quick Sort** | Reverse Sorted | 20.03 us | 2.54 us | 15.50 us | 72.75 us | OK |
| **Timsort (built-in)** | Reverse Sorted | 136.9 ns | 57.1 ns | 83.0 ns | 9.38 us | OK |
| **Timsort (custom)** | Reverse Sorted | 21.20 us | 458.4 ns | 20.54 us | 51.75 us | OK |
| **Radix Sort** | Reverse Sorted | 5.83 us | 235.0 ns | 5.58 us | 25.25 us | OK |
| **Counting Sort** | Reverse Sorted | 4.14 us | 224.1 ns | 3.96 us | 20.58 us | OK |
| **Shell Sort** | Almost Sorted | 4.70 us | 823.2 ns | 3.62 us | 20.50 us | OK |
| **Heap Sort** | Almost Sorted | 2.63 us | 175.1 ns | 2.46 us | 17.54 us | OK |
| **Merge Sort** | Almost Sorted | 17.97 us | 649.1 ns | 16.92 us | 89.25 us | OK |
| **Quick Sort** | Almost Sorted | 20.08 us | 2.61 us | 15.75 us | 72.12 us | OK |
| **Timsort (built-in)** | Almost Sorted | 349.1 ns | 109.2 ns | 83.0 ns | 10.38 us | OK |
| **Timsort (custom)** | Almost Sorted | 2.97 us | 688.5 ns | 1.83 us | 16.29 us | OK |
| **Radix Sort** | Almost Sorted | 5.86 us | 242.7 ns | 5.62 us | 25.38 us | OK |
| **Counting Sort** | Almost Sorted | 4.32 us | 189.4 ns | 4.08 us | 22.88 us | OK |
| **Shell Sort** | Half Sorted | 7.10 us | 562.2 ns | 5.04 us | 36.33 us | OK |
| **Heap Sort** | Half Sorted | 2.79 us | 150.2 ns | 2.58 us | 15.33 us | OK |
| **Merge Sort** | Half Sorted | 18.84 us | 450.2 ns | 17.96 us | 48.75 us | OK |
| **Quick Sort** | Half Sorted | 16.44 us | 1.55 us | 11.04 us | 43.50 us | OK |
| **Timsort (built-in)** | Half Sorted | 495.7 ns | 68.4 ns | 375.0 ns | 15.46 us | OK |
| **Timsort (custom)** | Half Sorted | 6.88 us | 963.5 ns | 3.29 us | 23.12 us | OK |
| **Radix Sort** | Half Sorted | 6.25 us | 221.7 ns | 5.92 us | 21.46 us | OK |
| **Counting Sort** | Half Sorted | 4.51 us | 219.7 ns | 3.67 us | 20.88 us | OK |
| **Shell Sort** | Flat (Few Unique) | 6.68 us | 562.6 ns | 4.58 us | 33.42 us | OK |
| **Heap Sort** | Flat (Few Unique) | 2.93 us | 149.1 ns | 2.67 us | 19.71 us | OK |
| **Merge Sort** | Flat (Few Unique) | 19.70 us | 458.9 ns | 18.62 us | 45.04 us | OK |
| **Quick Sort** | Flat (Few Unique) | 7.13 us | 2.17 us | 4.62 us | 74.00 us | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 710.7 ns | 78.4 ns | 583.0 ns | 10.04 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 9.94 us | 1.33 us | 5.04 us | 29.54 us | OK |
| **Radix Sort** | Flat (Few Unique) | 4.05 us | 195.0 ns | 3.83 us | 22.29 us | OK |
| **Counting Sort** | Flat (Few Unique) | 3.05 us | 192.0 ns | 2.75 us | 25.67 us | OK |
| **Shell Sort** | Floats | 8.35 us | 639.3 ns | 6.33 us | 34.79 us | OK |
| **Heap Sort** | Floats | 2.59 us | 159.2 ns | 2.38 us | 23.96 us | OK |
| **Merge Sort** | Floats | 19.61 us | 433.6 ns | 18.62 us | 48.12 us | OK |
| **Quick Sort** | Floats | 20.37 us | 2.52 us | 15.92 us | 96.38 us | OK |
| **Timsort (built-in)** | Floats | 847.4 ns | 89.6 ns | 708.0 ns | 14.58 us | OK |
| **Timsort (custom)** | Floats | 11.80 us | 1.25 us | 6.75 us | 29.12 us | OK |
| Radix Sort | Floats | — | — | — | — | Skipped (integers only) |
| Counting Sort | Floats | — | — | — | — | Skipped (integers only) |
| **Shell Sort** | Strings | 8.82 us | 658.2 ns | 6.67 us | 27.67 us | OK |
| **Heap Sort** | Strings | 3.39 us | 132.6 ns | 3.17 us | 17.79 us | OK |
| **Merge Sort** | Strings | 19.98 us | 513.4 ns | 19.04 us | 42.58 us | OK |
| **Quick Sort** | Strings | 20.83 us | 1.46 us | 16.42 us | 51.08 us | OK |
| **Timsort (built-in)** | Strings | 1.12 us | 118.4 ns | 1.00 us | 26.21 us | OK |
| **Timsort (custom)** | Strings | 12.62 us | 1.36 us | 7.04 us | 41.79 us | OK |
| Radix Sort | Strings | — | — | — | — | Skipped (integers only) |
| Counting Sort | Strings | — | — | — | — | Skipped (integers only) |

---

## Size: 50  x  100,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Shell Sort** | Random Ints | 16.16 us | 965.1 ns | 12.96 us | 38.50 us | OK |
| **Heap Sort** | Random Ints | 4.46 us | 202.0 ns | 4.12 us | 21.04 us | OK |
| **Merge Sort** | Random Ints | 35.83 us | 789.6 ns | 34.29 us | 110.71 us | OK |
| **Quick Sort** | Random Ints | 35.51 us | 2.21 us | 27.83 us | 69.00 us | OK |
| **Timsort (built-in)** | Random Ints | 1.40 us | 89.7 ns | 1.25 us | 13.62 us | OK |
| **Timsort (custom)** | Random Ints | 22.27 us | 1.43 us | 16.21 us | 43.75 us | OK |
| **Radix Sort** | Random Ints | 12.61 us | 372.9 ns | 12.17 us | 45.29 us | OK |
| **Counting Sort** | Random Ints | 30.00 us | 1.07 us | 24.42 us | 60.83 us | OK |
| **Shell Sort** | Sorted Ints | 6.93 us | 543.1 ns | 6.62 us | 32.12 us | OK |
| **Heap Sort** | Sorted Ints | 4.34 us | 238.4 ns | 4.12 us | 23.75 us | OK |
| **Merge Sort** | Sorted Ints | 30.92 us | 635.9 ns | 29.96 us | 60.92 us | OK |
| **Quick Sort** | Sorted Ints | 36.37 us | 2.73 us | 29.79 us | 78.29 us | OK |
| **Timsort (built-in)** | Sorted Ints | 178.6 ns | 40.8 ns | 125.0 ns | 10.04 us | OK |
| **Timsort (custom)** | Sorted Ints | 7.15 us | 266.1 ns | 6.83 us | 25.21 us | OK |
| **Radix Sort** | Sorted Ints | 8.40 us | 298.6 ns | 8.12 us | 29.46 us | OK |
| **Counting Sort** | Sorted Ints | 6.71 us | 510.7 ns | 6.38 us | 49.12 us | OK |
| **Shell Sort** | Reverse Sorted | 12.40 us | 306.8 ns | 11.92 us | 28.79 us | OK |
| **Heap Sort** | Reverse Sorted | 4.17 us | 212.9 ns | 3.92 us | 22.46 us | OK |
| **Merge Sort** | Reverse Sorted | 32.00 us | 611.6 ns | 31.17 us | 56.83 us | OK |
| **Quick Sort** | Reverse Sorted | 36.22 us | 2.77 us | 29.50 us | 97.04 us | OK |
| **Timsort (built-in)** | Reverse Sorted | 187.0 ns | 55.7 ns | 125.0 ns | 9.50 us | OK |
| **Timsort (custom)** | Reverse Sorted | 34.35 us | 614.3 ns | 33.50 us | 64.46 us | OK |
| **Radix Sort** | Reverse Sorted | 8.37 us | 287.2 ns | 8.04 us | 30.83 us | OK |
| **Counting Sort** | Reverse Sorted | 6.61 us | 268.6 ns | 6.33 us | 24.29 us | OK |
| **Shell Sort** | Almost Sorted | 8.47 us | 1.30 us | 6.79 us | 26.42 us | OK |
| **Heap Sort** | Almost Sorted | 4.43 us | 220.8 ns | 4.17 us | 18.29 us | OK |
| **Merge Sort** | Almost Sorted | 31.97 us | 784.8 ns | 30.38 us | 61.62 us | OK |
| **Quick Sort** | Almost Sorted | 36.26 us | 2.80 us | 29.92 us | 86.12 us | OK |
| **Timsort (built-in)** | Almost Sorted | 533.6 ns | 162.4 ns | 166.0 ns | 11.12 us | OK |
| **Timsort (custom)** | Almost Sorted | 8.61 us | 867.3 ns | 7.00 us | 30.46 us | OK |
| **Radix Sort** | Almost Sorted | 8.46 us | 272.1 ns | 8.12 us | 29.33 us | OK |
| **Counting Sort** | Almost Sorted | 6.76 us | 240.0 ns | 6.50 us | 32.12 us | OK |
| **Shell Sort** | Half Sorted | 14.13 us | 925.6 ns | 9.83 us | 34.42 us | OK |
| **Heap Sort** | Half Sorted | 4.61 us | 239.4 ns | 4.29 us | 24.17 us | OK |
| **Merge Sort** | Half Sorted | 33.79 us | 761.8 ns | 32.42 us | 76.83 us | OK |
| **Quick Sort** | Half Sorted | 30.16 us | 2.30 us | 22.62 us | 59.96 us | OK |
| **Timsort (built-in)** | Half Sorted | 871.3 ns | 84.7 ns | 709.0 ns | 11.58 us | OK |
| **Timsort (custom)** | Half Sorted | 15.35 us | 1.11 us | 11.04 us | 40.83 us | OK |
| **Radix Sort** | Half Sorted | 8.93 us | 270.6 ns | 8.54 us | 29.42 us | OK |
| **Counting Sort** | Half Sorted | 7.04 us | 235.0 ns | 5.88 us | 26.00 us | OK |
| **Shell Sort** | Flat (Few Unique) | 12.10 us | 751.9 ns | 9.50 us | 30.17 us | OK |
| **Heap Sort** | Flat (Few Unique) | 5.03 us | 202.9 ns | 4.62 us | 22.17 us | OK |
| **Merge Sort** | Flat (Few Unique) | 35.74 us | 865.1 ns | 33.83 us | 65.62 us | OK |
| **Quick Sort** | Flat (Few Unique) | 10.02 us | 1.97 us | 7.33 us | 69.71 us | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 1.33 us | 112.6 ns | 1.12 us | 13.04 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 19.81 us | 1.44 us | 13.92 us | 46.46 us | OK |
| **Radix Sort** | Flat (Few Unique) | 5.84 us | 250.7 ns | 5.50 us | 28.83 us | OK |
| **Counting Sort** | Flat (Few Unique) | 4.45 us | 335.2 ns | 4.08 us | 43.58 us | OK |
| **Shell Sort** | Floats | 16.31 us | 977.7 ns | 12.88 us | 42.25 us | OK |
| **Heap Sort** | Floats | 4.31 us | 205.2 ns | 4.00 us | 23.62 us | OK |
| **Merge Sort** | Floats | 35.73 us | 634.9 ns | 34.46 us | 64.67 us | OK |
| **Quick Sort** | Floats | 36.81 us | 2.79 us | 30.71 us | 84.33 us | OK |
| **Timsort (built-in)** | Floats | 1.60 us | 116.5 ns | 1.42 us | 12.75 us | OK |
| **Timsort (custom)** | Floats | 22.55 us | 1.46 us | 16.96 us | 44.21 us | OK |
| Radix Sort | Floats | — | — | — | — | Skipped (integers only) |
| Counting Sort | Floats | — | — | — | — | Skipped (integers only) |
| **Shell Sort** | Strings | 17.11 us | 1.02 us | 13.71 us | 43.25 us | OK |
| **Heap Sort** | Strings | 5.90 us | 232.0 ns | 5.58 us | 22.71 us | OK |
| **Merge Sort** | Strings | 36.26 us | 756.6 ns | 34.92 us | 111.00 us | OK |
| **Quick Sort** | Strings | 37.85 us | 2.28 us | 31.00 us | 71.79 us | OK |
| **Timsort (built-in)** | Strings | 2.13 us | 103.6 ns | 1.96 us | 15.08 us | OK |
| **Timsort (custom)** | Strings | 23.33 us | 1.55 us | 17.33 us | 50.96 us | OK |
| Radix Sort | Strings | — | — | — | — | Skipped (integers only) |
| Counting Sort | Strings | — | — | — | — | Skipped (integers only) |

---

## Size: 100  x  100,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Shell Sort** | Random Ints | 39.23 us | 1.75 us | 32.75 us | 72.96 us | OK |
| **Heap Sort** | Random Ints | 9.35 us | 295.9 ns | 8.71 us | 35.46 us | OK |
| **Merge Sort** | Random Ints | 80.24 us | 1.07 us | 77.88 us | 146.88 us | OK |
| **Quick Sort** | Random Ints | 79.06 us | 4.16 us | 66.58 us | 127.17 us | OK |
| **Timsort (built-in)** | Random Ints | 3.24 us | 169.6 ns | 2.96 us | 26.12 us | OK |
| **Timsort (custom)** | Random Ints | 52.28 us | 2.26 us | 43.88 us | 94.50 us | OK |
| **Radix Sort** | Random Ints | 22.60 us | 1.71 us | 21.33 us | 54.62 us | OK |
| **Counting Sort** | Random Ints | 62.28 us | 1.85 us | 56.17 us | 94.83 us | OK |
| **Shell Sort** | Sorted Ints | 15.64 us | 343.3 ns | 15.04 us | 36.83 us | OK |
| **Heap Sort** | Sorted Ints | 9.14 us | 266.5 ns | 8.79 us | 30.17 us | OK |
| **Merge Sort** | Sorted Ints | 68.50 us | 920.7 ns | 66.96 us | 99.71 us | OK |
| **Quick Sort** | Sorted Ints | 80.66 us | 4.68 us | 68.92 us | 187.50 us | OK |
| **Timsort (built-in)** | Sorted Ints | 263.2 ns | 57.0 ns | 208.0 ns | 10.08 us | OK |
| **Timsort (custom)** | Sorted Ints | 20.69 us | 431.4 ns | 20.12 us | 46.04 us | OK |
| **Radix Sort** | Sorted Ints | 14.91 us | 320.2 ns | 14.46 us | 37.21 us | OK |
| **Counting Sort** | Sorted Ints | 12.99 us | 323.3 ns | 12.50 us | 35.46 us | OK |
| **Shell Sort** | Reverse Sorted | 27.58 us | 504.9 ns | 26.88 us | 55.12 us | OK |
| **Heap Sort** | Reverse Sorted | 8.82 us | 252.4 ns | 8.42 us | 27.08 us | OK |
| **Merge Sort** | Reverse Sorted | 70.50 us | 937.6 ns | 69.00 us | 103.38 us | OK |
| **Quick Sort** | Reverse Sorted | 80.44 us | 4.63 us | 67.83 us | 130.88 us | OK |
| **Timsort (built-in)** | Reverse Sorted | 274.6 ns | 58.3 ns | 208.0 ns | 12.25 us | OK |
| **Timsort (custom)** | Reverse Sorted | 74.38 us | 935.2 ns | 73.04 us | 106.17 us | OK |
| **Radix Sort** | Reverse Sorted | 20.63 us | 378.0 ns | 19.92 us | 42.83 us | OK |
| **Counting Sort** | Reverse Sorted | 12.84 us | 353.5 ns | 12.33 us | 38.25 us | OK |
| **Shell Sort** | Almost Sorted | 21.19 us | 2.91 us | 15.71 us | 42.71 us | OK |
| **Heap Sort** | Almost Sorted | 9.21 us | 270.0 ns | 8.79 us | 27.75 us | OK |
| **Merge Sort** | Almost Sorted | 71.66 us | 1.60 us | 67.92 us | 147.79 us | OK |
| **Quick Sort** | Almost Sorted | 80.75 us | 4.71 us | 68.88 us | 183.67 us | OK |
| **Timsort (built-in)** | Almost Sorted | 1.04 us | 285.0 ns | 250.0 ns | 16.58 us | OK |
| **Timsort (custom)** | Almost Sorted | 24.74 us | 1.61 us | 20.58 us | 45.50 us | OK |
| **Radix Sort** | Almost Sorted | 15.15 us | 381.8 ns | 14.67 us | 38.96 us | OK |
| **Counting Sort** | Almost Sorted | 13.04 us | 335.3 ns | 12.50 us | 43.50 us | OK |
| **Shell Sort** | Half Sorted | 34.84 us | 1.67 us | 28.42 us | 61.62 us | OK |
| **Heap Sort** | Half Sorted | 9.71 us | 297.7 ns | 9.25 us | 34.33 us | OK |
| **Merge Sort** | Half Sorted | 74.99 us | 1.12 us | 72.67 us | 182.62 us | OK |
| **Quick Sort** | Half Sorted | 67.96 us | 4.21 us | 54.83 us | 110.62 us | OK |
| **Timsort (built-in)** | Half Sorted | 1.84 us | 130.5 ns | 1.62 us | 17.17 us | OK |
| **Timsort (custom)** | Half Sorted | 36.79 us | 1.49 us | 31.08 us | 63.00 us | OK |
| **Radix Sort** | Half Sorted | 18.17 us | 2.80 us | 15.38 us | 44.71 us | OK |
| **Counting Sort** | Half Sorted | 13.54 us | 485.0 ns | 12.12 us | 42.79 us | OK |
| **Shell Sort** | Flat (Few Unique) | 26.62 us | 1.17 us | 23.04 us | 59.00 us | OK |
| **Heap Sort** | Flat (Few Unique) | 10.99 us | 371.8 ns | 10.17 us | 47.62 us | OK |
| **Merge Sort** | Flat (Few Unique) | 79.90 us | 1.12 us | 76.83 us | 114.17 us | OK |
| **Quick Sort** | Flat (Few Unique) | 17.29 us | 2.50 us | 13.21 us | 59.71 us | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 2.79 us | 153.3 ns | 2.46 us | 18.83 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 47.13 us | 2.04 us | 38.54 us | 78.38 us | OK |
| **Radix Sort** | Flat (Few Unique) | 10.56 us | 267.0 ns | 10.12 us | 29.38 us | OK |
| **Counting Sort** | Flat (Few Unique) | 7.85 us | 267.2 ns | 7.38 us | 32.88 us | OK |
| **Shell Sort** | Floats | 39.73 us | 1.85 us | 33.79 us | 117.83 us | OK |
| **Heap Sort** | Floats | 9.27 us | 236.8 ns | 8.71 us | 30.75 us | OK |
| **Merge Sort** | Floats | 79.96 us | 1.09 us | 77.29 us | 111.79 us | OK |
| **Quick Sort** | Floats | 82.24 us | 4.55 us | 70.71 us | 136.33 us | OK |
| **Timsort (built-in)** | Floats | 3.67 us | 142.8 ns | 3.33 us | 18.54 us | OK |
| **Timsort (custom)** | Floats | 52.94 us | 2.09 us | 43.42 us | 87.17 us | OK |
| Radix Sort | Floats | — | — | — | — | Skipped (integers only) |
| Counting Sort | Floats | — | — | — | — | Skipped (integers only) |
| **Shell Sort** | Strings | 41.55 us | 1.86 us | 35.21 us | 74.25 us | OK |
| **Heap Sort** | Strings | 12.90 us | 331.7 ns | 12.38 us | 44.38 us | OK |
| **Merge Sort** | Strings | 80.94 us | 1.12 us | 78.38 us | 154.71 us | OK |
| **Quick Sort** | Strings | 84.56 us | 4.37 us | 72.21 us | 116.50 us | OK |
| **Timsort (built-in)** | Strings | 4.95 us | 216.0 ns | 4.58 us | 26.67 us | OK |
| **Timsort (custom)** | Strings | 54.84 us | 2.19 us | 45.12 us | 91.29 us | OK |
| Radix Sort | Strings | — | — | — | — | Skipped (integers only) |
| Counting Sort | Strings | — | — | — | — | Skipped (integers only) |

---

## Size: 1,000  x  1,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Shell Sort** | Random Ints | 872.18 us | 34.13 us | 790.46 us | 998.58 us | OK |
| **Heap Sort** | Random Ints | 108.79 us | 2.38 us | 104.83 us | 125.92 us | OK |
| **Merge Sort** | Random Ints | 1.106 ms | 7.30 us | 1.088 ms | 1.151 ms | OK |
| **Quick Sort** | Random Ints | 1.154 ms | 42.32 us | 1.058 ms | 1.342 ms | OK |
| **Timsort (built-in)** | Random Ints | 48.40 us | 967.2 ns | 47.12 us | 60.42 us | OK |
| **Timsort (custom)** | Random Ints | 926.79 us | 20.14 us | 879.04 us | 984.12 us | OK |
| **Radix Sort** | Random Ints | 241.13 us | 13.33 us | 232.79 us | 290.33 us | OK |
| **Counting Sort** | Random Ints | 633.09 us | 8.67 us | 612.67 us | 677.33 us | OK |
| **Shell Sort** | Sorted Ints | 263.90 us | 3.86 us | 260.38 us | 298.54 us | OK |
| **Heap Sort** | Sorted Ints | 107.86 us | 1.95 us | 105.17 us | 127.33 us | OK |
| **Merge Sort** | Sorted Ints | 929.20 us | 8.03 us | 910.54 us | 960.54 us | OK |
| **Quick Sort** | Sorted Ints | 1.145 ms | 42.98 us | 1.060 ms | 1.364 ms | OK |
| **Timsort (built-in)** | Sorted Ints | 1.91 us | 77.1 ns | 1.79 us | 2.62 us | OK |
| **Timsort (custom)** | Sorted Ints | 419.82 us | 5.19 us | 414.54 us | 456.17 us | OK |
| **Radix Sort** | Sorted Ints | 178.61 us | 2.07 us | 175.46 us | 199.58 us | OK |
| **Counting Sort** | Sorted Ints | 138.46 us | 2.47 us | 135.71 us | 158.38 us | OK |
| **Shell Sort** | Reverse Sorted | 499.59 us | 6.61 us | 491.17 us | 541.33 us | OK |
| **Heap Sort** | Reverse Sorted | 106.16 us | 2.42 us | 102.79 us | 123.25 us | OK |
| **Merge Sort** | Reverse Sorted | 936.31 us | 7.38 us | 922.79 us | 983.62 us | OK |
| **Quick Sort** | Reverse Sorted | 1.148 ms | 45.79 us | 1.048 ms | 1.404 ms | OK |
| **Timsort (built-in)** | Reverse Sorted | 2.03 us | 87.3 ns | 1.92 us | 2.92 us | OK |
| **Timsort (custom)** | Reverse Sorted | 1.183 ms | 19.16 us | 1.162 ms | 1.274 ms | OK |
| **Radix Sort** | Reverse Sorted | 225.21 us | 2.54 us | 220.54 us | 249.54 us | OK |
| **Counting Sort** | Reverse Sorted | 134.65 us | 2.21 us | 132.25 us | 152.00 us | OK |
| **Shell Sort** | Almost Sorted | 516.43 us | 24.30 us | 443.62 us | 626.42 us | OK |
| **Heap Sort** | Almost Sorted | 108.19 us | 2.16 us | 104.58 us | 125.17 us | OK |
| **Merge Sort** | Almost Sorted | 1.004 ms | 8.71 us | 976.08 us | 1.052 ms | OK |
| **Quick Sort** | Almost Sorted | 1.143 ms | 44.17 us | 1.048 ms | 1.328 ms | OK |
| **Timsort (built-in)** | Almost Sorted | 12.45 us | 898.5 ns | 9.75 us | 21.50 us | OK |
| **Timsort (custom)** | Almost Sorted | 514.56 us | 8.42 us | 492.12 us | 551.54 us | OK |
| **Radix Sort** | Almost Sorted | 180.19 us | 1.82 us | 177.04 us | 196.54 us | OK |
| **Counting Sort** | Almost Sorted | 139.83 us | 2.07 us | 135.67 us | 154.08 us | OK |
| **Shell Sort** | Half Sorted | 758.19 us | 27.60 us | 698.92 us | 928.21 us | OK |
| **Heap Sort** | Half Sorted | 111.60 us | 1.84 us | 108.33 us | 122.04 us | OK |
| **Merge Sort** | Half Sorted | 1.021 ms | 7.41 us | 1.004 ms | 1.083 ms | OK |
| **Quick Sort** | Half Sorted | 1.022 ms | 43.65 us | 927.38 us | 1.222 ms | OK |
| **Timsort (built-in)** | Half Sorted | 25.67 us | 613.5 ns | 24.71 us | 36.25 us | OK |
| **Timsort (custom)** | Half Sorted | 686.98 us | 13.22 us | 660.54 us | 740.42 us | OK |
| **Radix Sort** | Half Sorted | 203.83 us | 22.51 us | 183.29 us | 249.00 us | OK |
| **Counting Sort** | Half Sorted | 144.39 us | 2.14 us | 140.71 us | 166.67 us | OK |
| **Shell Sort** | Flat (Few Unique) | 413.23 us | 9.74 us | 387.75 us | 457.25 us | OK |
| **Heap Sort** | Flat (Few Unique) | 132.47 us | 1.77 us | 127.17 us | 149.79 us | OK |
| **Merge Sort** | Flat (Few Unique) | 1.099 ms | 8.83 us | 1.080 ms | 1.201 ms | OK |
| **Quick Sort** | Flat (Few Unique) | 155.87 us | 19.19 us | 128.96 us | 200.29 us | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 31.02 us | 787.0 ns | 30.25 us | 41.17 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 823.62 us | 11.95 us | 794.46 us | 884.42 us | OK |
| **Radix Sort** | Flat (Few Unique) | 90.57 us | 1.37 us | 87.88 us | 101.33 us | OK |
| **Counting Sort** | Flat (Few Unique) | 70.50 us | 1.47 us | 68.62 us | 95.29 us | OK |
| **Shell Sort** | Floats | 845.19 us | 26.66 us | 775.79 us | 978.67 us | OK |
| **Heap Sort** | Floats | 114.70 us | 2.41 us | 110.46 us | 130.17 us | OK |
| **Merge Sort** | Floats | 1.112 ms | 6.65 us | 1.095 ms | 1.148 ms | OK |
| **Quick Sort** | Floats | 1.179 ms | 42.88 us | 1.091 ms | 1.388 ms | OK |
| **Timsort (built-in)** | Floats | 53.78 us | 1.19 us | 52.33 us | 69.00 us | OK |
| **Timsort (custom)** | Floats | 913.15 us | 14.13 us | 877.96 us | 984.17 us | OK |
| Radix Sort | Floats | — | — | — | — | Skipped (integers only) |
| Counting Sort | Floats | — | — | — | — | Skipped (integers only) |
| **Shell Sort** | Strings | 892.38 us | 30.01 us | 827.46 us | 1.006 ms | OK |
| **Heap Sort** | Strings | 174.19 us | 2.11 us | 168.12 us | 184.38 us | OK |
| **Merge Sort** | Strings | 1.139 ms | 5.13 us | 1.126 ms | 1.171 ms | OK |
| **Quick Sort** | Strings | 1.238 ms | 43.87 us | 1.127 ms | 1.413 ms | OK |
| **Timsort (built-in)** | Strings | 75.49 us | 1.05 us | 73.96 us | 88.46 us | OK |
| **Timsort (custom)** | Strings | 963.85 us | 15.14 us | 920.25 us | 1.025 ms | OK |
| Radix Sort | Strings | — | — | — | — | Skipped (integers only) |
| Counting Sort | Strings | — | — | — | — | Skipped (integers only) |

---

## Size: 10,000  x  100 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Shell Sort** | Random Ints | 14.918 ms | 779.47 us | 13.552 ms | 17.602 ms | OK |
| **Heap Sort** | Random Ints | 1.639 ms | 58.67 us | 1.555 ms | 1.849 ms | OK |
| **Merge Sort** | Random Ints | 14.735 ms | 204.23 us | 14.371 ms | 15.198 ms | OK |
| **Quick Sort** | Random Ints | 15.161 ms | 528.02 us | 14.374 ms | 17.287 ms | OK |
| **Timsort (built-in)** | Random Ints | 661.54 us | 5.81 us | 651.79 us | 686.79 us | OK |
| **Timsort (custom)** | Random Ints | 12.252 ms | 319.16 us | 11.739 ms | 12.858 ms | OK |
| **Radix Sort** | Random Ints | 2.840 ms | 108.18 us | 2.774 ms | 3.287 ms | OK |
| **Counting Sort** | Random Ints | 6.315 ms | 131.20 us | 6.101 ms | 6.606 ms | OK |
| **Shell Sort** | Sorted Ints | 3.698 ms | 38.94 us | 3.668 ms | 3.896 ms | OK |
| **Heap Sort** | Sorted Ints | 1.422 ms | 13.48 us | 1.391 ms | 1.454 ms | OK |
| **Merge Sort** | Sorted Ints | 11.798 ms | 122.28 us | 11.637 ms | 12.118 ms | OK |
| **Quick Sort** | Sorted Ints | 14.691 ms | 492.44 us | 13.895 ms | 15.972 ms | OK |
| **Timsort (built-in)** | Sorted Ints | 19.20 us | 1.06 us | 18.50 us | 25.04 us | OK |
| **Timsort (custom)** | Sorted Ints | 7.353 ms | 126.30 us | 7.202 ms | 7.765 ms | OK |
| **Radix Sort** | Sorted Ints | 2.241 ms | 14.03 us | 2.216 ms | 2.289 ms | OK |
| **Counting Sort** | Sorted Ints | 1.396 ms | 14.11 us | 1.381 ms | 1.451 ms | OK |
| **Shell Sort** | Reverse Sorted | 7.050 ms | 40.36 us | 6.972 ms | 7.234 ms | OK |
| **Heap Sort** | Reverse Sorted | 1.358 ms | 17.42 us | 1.313 ms | 1.424 ms | OK |
| **Merge Sort** | Reverse Sorted | 12.022 ms | 73.08 us | 11.886 ms | 12.205 ms | OK |
| **Quick Sort** | Reverse Sorted | 14.701 ms | 428.91 us | 13.963 ms | 16.364 ms | OK |
| **Timsort (built-in)** | Reverse Sorted | 20.63 us | 961.4 ns | 19.96 us | 28.17 us | OK |
| **Timsort (custom)** | Reverse Sorted | 12.149 ms | 85.26 us | 12.037 ms | 12.290 ms | OK |
| **Radix Sort** | Reverse Sorted | 2.668 ms | 18.78 us | 2.627 ms | 2.699 ms | OK |
| **Counting Sort** | Reverse Sorted | 1.421 ms | 11.84 us | 1.400 ms | 1.482 ms | OK |
| **Shell Sort** | Almost Sorted | 9.467 ms | 355.89 us | 8.921 ms | 11.401 ms | OK |
| **Heap Sort** | Almost Sorted | 1.419 ms | 16.96 us | 1.391 ms | 1.482 ms | OK |
| **Merge Sort** | Almost Sorted | 13.145 ms | 119.31 us | 12.973 ms | 13.485 ms | OK |
| **Quick Sort** | Almost Sorted | 14.694 ms | 431.20 us | 14.018 ms | 16.226 ms | OK |
| **Timsort (built-in)** | Almost Sorted | 129.29 us | 4.14 us | 123.75 us | 150.58 us | OK |
| **Timsort (custom)** | Almost Sorted | 8.943 ms | 184.85 us | 8.729 ms | 9.638 ms | OK |
| **Radix Sort** | Almost Sorted | 2.235 ms | 10.10 us | 2.218 ms | 2.269 ms | OK |
| **Counting Sort** | Almost Sorted | 1.426 ms | 11.79 us | 1.412 ms | 1.474 ms | OK |
| **Shell Sort** | Half Sorted | 13.283 ms | 653.56 us | 12.254 ms | 15.366 ms | OK |
| **Heap Sort** | Half Sorted | 1.525 ms | 24.54 us | 1.480 ms | 1.596 ms | OK |
| **Merge Sort** | Half Sorted | 13.195 ms | 124.02 us | 13.050 ms | 13.747 ms | OK |
| **Quick Sort** | Half Sorted | 13.673 ms | 443.64 us | 13.012 ms | 15.009 ms | OK |
| **Timsort (built-in)** | Half Sorted | 345.29 us | 3.43 us | 338.21 us | 364.29 us | OK |
| **Timsort (custom)** | Half Sorted | 9.809 ms | 185.52 us | 9.638 ms | 10.549 ms | OK |
| **Radix Sort** | Half Sorted | 2.496 ms | 218.00 us | 2.271 ms | 2.774 ms | OK |
| **Counting Sort** | Half Sorted | 1.470 ms | 11.80 us | 1.445 ms | 1.493 ms | OK |
| **Shell Sort** | Flat (Few Unique) | 5.423 ms | 111.83 us | 5.240 ms | 5.683 ms | OK |
| **Heap Sort** | Flat (Few Unique) | 1.485 ms | 26.84 us | 1.434 ms | 1.524 ms | OK |
| **Merge Sort** | Flat (Few Unique) | 14.012 ms | 52.63 us | 13.921 ms | 14.180 ms | OK |
| **Quick Sort** | Flat (Few Unique) | 1.522 ms | 177.98 us | 1.317 ms | 1.882 ms | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 297.57 us | 5.15 us | 294.62 us | 329.21 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 10.940 ms | 42.69 us | 10.854 ms | 11.089 ms | OK |
| **Radix Sort** | Flat (Few Unique) | 855.07 us | 12.51 us | 835.54 us | 921.88 us | OK |
| **Counting Sort** | Flat (Few Unique) | 763.67 us | 7.47 us | 751.92 us | 808.25 us | OK |
| **Shell Sort** | Floats | 14.701 ms | 558.46 us | 13.698 ms | 16.697 ms | OK |
| **Heap Sort** | Floats | 1.716 ms | 27.05 us | 1.664 ms | 1.778 ms | OK |
| **Merge Sort** | Floats | 14.950 ms | 274.23 us | 14.430 ms | 15.421 ms | OK |
| **Quick Sort** | Floats | 15.433 ms | 418.95 us | 14.690 ms | 16.486 ms | OK |
| **Timsort (built-in)** | Floats | 723.05 us | 6.21 us | 711.29 us | 758.08 us | OK |
| **Timsort (custom)** | Floats | 12.143 ms | 316.06 us | 11.822 ms | 12.829 ms | OK |
| Radix Sort | Floats | — | — | — | — | Skipped (integers only) |
| Counting Sort | Floats | — | — | — | — | Skipped (integers only) |
| **Shell Sort** | Strings | 15.295 ms | 410.13 us | 14.522 ms | 16.512 ms | OK |
| **Heap Sort** | Strings | 2.282 ms | 19.02 us | 2.252 ms | 2.326 ms | OK |
| **Merge Sort** | Strings | 14.865 ms | 100.16 us | 14.742 ms | 15.160 ms | OK |
| **Quick Sort** | Strings | 16.062 ms | 405.45 us | 15.236 ms | 17.233 ms | OK |
| **Timsort (built-in)** | Strings | 1.024 ms | 5.54 us | 1.011 ms | 1.039 ms | OK |
| **Timsort (custom)** | Strings | 12.470 ms | 69.40 us | 12.357 ms | 12.669 ms | OK |
| Radix Sort | Strings | — | — | — | — | Skipped (integers only) |
| Counting Sort | Strings | — | — | — | — | Skipped (integers only) |

---

## Size: 100,000  x  10 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Shell Sort** | Random Ints | 248.794 ms | 13.304 ms | 229.788 ms | 269.842 ms | OK |
| **Heap Sort** | Random Ints | 25.506 ms | 358.42 us | 25.054 ms | 26.096 ms | OK |
| **Merge Sort** | Random Ints | 182.278 ms | 3.314 ms | 177.595 ms | 186.995 ms | OK |
| **Quick Sort** | Random Ints | 185.431 ms | 5.808 ms | 178.730 ms | 196.018 ms | OK |
| **Timsort (built-in)** | Random Ints | 8.714 ms | 90.51 us | 8.572 ms | 8.832 ms | OK |
| **Timsort (custom)** | Random Ints | 160.058 ms | 4.194 ms | 155.225 ms | 167.156 ms | OK |
| **Radix Sort** | Random Ints | 33.558 ms | 1.932 ms | 32.355 ms | 37.364 ms | OK |
| **Counting Sort** | Random Ints | 62.926 ms | 1.580 ms | 60.844 ms | 65.143 ms | OK |
| **Shell Sort** | Sorted Ints | 48.029 ms | 307.09 us | 47.475 ms | 48.414 ms | OK |
| **Heap Sort** | Sorted Ints | 16.587 ms | 324.69 us | 16.137 ms | 17.241 ms | OK |
| **Merge Sort** | Sorted Ints | 142.898 ms | 521.86 us | 142.162 ms | 143.695 ms | OK |
| **Quick Sort** | Sorted Ints | 178.797 ms | 5.685 ms | 172.398 ms | 192.521 ms | OK |
| **Timsort (built-in)** | Sorted Ints | 195.50 us | 30.44 us | 178.25 us | 280.25 us | OK |
| **Timsort (custom)** | Sorted Ints | 95.900 ms | 268.08 us | 95.622 ms | 96.285 ms | OK |
| **Radix Sort** | Sorted Ints | 26.302 ms | 143.55 us | 26.102 ms | 26.564 ms | OK |
| **Counting Sort** | Sorted Ints | 14.185 ms | 195.80 us | 13.934 ms | 14.576 ms | OK |
| **Shell Sort** | Reverse Sorted | 87.315 ms | 205.42 us | 87.122 ms | 87.766 ms | OK |
| **Heap Sort** | Reverse Sorted | 15.672 ms | 173.06 us | 15.435 ms | 15.902 ms | OK |
| **Merge Sort** | Reverse Sorted | 144.583 ms | 530.31 us | 143.535 ms | 145.473 ms | OK |
| **Quick Sort** | Reverse Sorted | 179.057 ms | 4.420 ms | 171.293 ms | 186.724 ms | OK |
| **Timsort (built-in)** | Reverse Sorted | 212.78 us | 38.08 us | 192.25 us | 319.42 us | OK |
| **Timsort (custom)** | Reverse Sorted | 156.765 ms | 343.72 us | 156.156 ms | 157.243 ms | OK |
| **Radix Sort** | Reverse Sorted | 30.717 ms | 277.55 us | 30.311 ms | 31.059 ms | OK |
| **Counting Sort** | Reverse Sorted | 14.042 ms | 104.17 us | 13.867 ms | 14.236 ms | OK |
| **Shell Sort** | Almost Sorted | 152.489 ms | 4.468 ms | 147.644 ms | 158.393 ms | OK |
| **Heap Sort** | Almost Sorted | 17.212 ms | 236.67 us | 16.901 ms | 17.632 ms | OK |
| **Merge Sort** | Almost Sorted | 162.326 ms | 818.69 us | 161.515 ms | 163.875 ms | OK |
| **Quick Sort** | Almost Sorted | 179.257 ms | 2.986 ms | 175.029 ms | 182.769 ms | OK |
| **Timsort (built-in)** | Almost Sorted | 1.561 ms | 25.81 us | 1.532 ms | 1.608 ms | OK |
| **Timsort (custom)** | Almost Sorted | 117.136 ms | 661.95 us | 116.479 ms | 118.294 ms | OK |
| **Radix Sort** | Almost Sorted | 26.533 ms | 229.71 us | 26.179 ms | 26.858 ms | OK |
| **Counting Sort** | Almost Sorted | 14.090 ms | 88.25 us | 13.982 ms | 14.277 ms | OK |
| **Shell Sort** | Half Sorted | 224.490 ms | 9.316 ms | 211.474 ms | 237.498 ms | OK |
| **Heap Sort** | Half Sorted | 20.937 ms | 397.86 us | 19.939 ms | 21.400 ms | OK |
| **Merge Sort** | Half Sorted | 160.975 ms | 2.709 ms | 157.516 ms | 166.578 ms | OK |
| **Quick Sort** | Half Sorted | 167.103 ms | 4.938 ms | 163.571 ms | 179.669 ms | OK |
| **Timsort (built-in)** | Half Sorted | 4.431 ms | 23.50 us | 4.393 ms | 4.478 ms | OK |
| **Timsort (custom)** | Half Sorted | 128.219 ms | 3.039 ms | 126.180 ms | 136.447 ms | OK |
| **Radix Sort** | Half Sorted | 28.992 ms | 2.209 ms | 27.063 ms | 31.742 ms | OK |
| **Counting Sort** | Half Sorted | 14.592 ms | 103.90 us | 14.493 ms | 14.783 ms | OK |
| **Shell Sort** | Flat (Few Unique) | 65.420 ms | 1.209 ms | 63.204 ms | 67.270 ms | OK |
| **Heap Sort** | Flat (Few Unique) | 16.770 ms | 132.56 us | 16.567 ms | 17.001 ms | OK |
| **Merge Sort** | Flat (Few Unique) | 169.564 ms | 735.03 us | 168.265 ms | 170.920 ms | OK |
| **Quick Sort** | Flat (Few Unique) | 15.448 ms | 1.736 ms | 13.471 ms | 18.624 ms | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 3.111 ms | 19.50 us | 3.098 ms | 3.163 ms | OK |
| **Timsort (custom)** | Flat (Few Unique) | 141.061 ms | 626.67 us | 140.061 ms | 141.873 ms | OK |
| **Radix Sort** | Flat (Few Unique) | 8.277 ms | 105.40 us | 8.079 ms | 8.431 ms | OK |
| **Counting Sort** | Flat (Few Unique) | 7.664 ms | 66.48 us | 7.612 ms | 7.826 ms | OK |
| **Shell Sort** | Floats | 240.625 ms | 9.184 ms | 228.202 ms | 257.710 ms | OK |
| **Heap Sort** | Floats | 25.652 ms | 865.60 us | 24.817 ms | 27.073 ms | OK |
| **Merge Sort** | Floats | 186.228 ms | 2.771 ms | 179.473 ms | 189.990 ms | OK |
| **Quick Sort** | Floats | 188.268 ms | 3.607 ms | 184.574 ms | 196.927 ms | OK |
| **Timsort (built-in)** | Floats | 9.293 ms | 46.59 us | 9.249 ms | 9.412 ms | OK |
| **Timsort (custom)** | Floats | 163.873 ms | 4.149 ms | 155.722 ms | 166.658 ms | OK |
| Radix Sort | Floats | — | — | — | — | Skipped (integers only) |
| Counting Sort | Floats | — | — | — | — | Skipped (integers only) |
| **Shell Sort** | Strings | 250.947 ms | 11.202 ms | 231.705 ms | 268.283 ms | OK |
| **Heap Sort** | Strings | 29.183 ms | 350.44 us | 28.564 ms | 29.632 ms | OK |
| **Merge Sort** | Strings | 183.741 ms | 476.87 us | 183.142 ms | 184.680 ms | OK |
| **Quick Sort** | Strings | 195.429 ms | 4.116 ms | 189.413 ms | 203.890 ms | OK |
| **Timsort (built-in)** | Strings | 12.597 ms | 391.32 us | 12.155 ms | 13.042 ms | OK |
| **Timsort (custom)** | Strings | 163.376 ms | 528.31 us | 162.664 ms | 164.270 ms | OK |
| Radix Sort | Strings | — | — | — | — | Skipped (integers only) |
| Counting Sort | Strings | — | — | — | — | Skipped (integers only) |

---

## Size: 1,000,000  x  3 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Shell Sort** | Random Ints | 4.7628 s | 347.517 ms | 4.5074 s | 5.1585 s | OK |
| **Heap Sort** | Random Ints | 590.633 ms | 7.302 ms | 583.727 ms | 598.276 ms | OK |
| **Merge Sort** | Random Ints | 2.2357 s | 54.765 ms | 2.1726 s | 2.2711 s | OK |
| **Quick Sort** | Random Ints | 2.3548 s | 158.915 ms | 2.2524 s | 2.5379 s | OK |
| **Timsort (built-in)** | Random Ints | 115.831 ms | 1.003 ms | 114.789 ms | 116.789 ms | OK |
| **Timsort (custom)** | Random Ints | 2.0729 s | 52.216 ms | 2.0274 s | 2.1299 s | OK |
| **Radix Sort** | Random Ints | 698.664 ms | 1.981 ms | 697.218 ms | 700.922 ms | OK |
| **Counting Sort** | Random Ints | 693.620 ms | 7.694 ms | 686.921 ms | 702.023 ms | OK |
| **Shell Sort** | Sorted Ints | 582.166 ms | 1.837 ms | 580.411 ms | 584.074 ms | OK |
| **Heap Sort** | Sorted Ints | 205.506 ms | 3.050 ms | 201.986 ms | 207.370 ms | OK |
| **Merge Sort** | Sorted Ints | 1.6961 s | 16.438 ms | 1.6820 s | 1.7141 s | OK |
| **Quick Sort** | Sorted Ints | 2.0825 s | 51.770 ms | 2.0404 s | 2.1403 s | OK |
| **Timsort (built-in)** | Sorted Ints | 1.925 ms | 118.03 us | 1.796 ms | 2.028 ms | OK |
| **Timsort (custom)** | Sorted Ints | 1.2008 s | 30.860 ms | 1.1817 s | 1.2364 s | OK |
| **Radix Sort** | Sorted Ints | 383.865 ms | 4.546 ms | 378.616 ms | 386.524 ms | OK |
| **Counting Sort** | Sorted Ints | 143.696 ms | 201.38 us | 143.476 ms | 143.872 ms | OK |
| **Shell Sort** | Reverse Sorted | 998.103 ms | 5.925 ms | 991.925 ms | 1.0037 s | OK |
| **Heap Sort** | Reverse Sorted | 179.825 ms | 580.78 us | 179.486 ms | 180.496 ms | OK |
| **Merge Sort** | Reverse Sorted | 1.6875 s | 17.731 ms | 1.6741 s | 1.7076 s | OK |
| **Quick Sort** | Reverse Sorted | 2.1148 s | 21.972 ms | 2.0897 s | 2.1305 s | OK |
| **Timsort (built-in)** | Reverse Sorted | 2.104 ms | 112.15 us | 1.983 ms | 2.204 ms | OK |
| **Timsort (custom)** | Reverse Sorted | 1.9393 s | 4.464 ms | 1.9352 s | 1.9441 s | OK |
| **Radix Sort** | Reverse Sorted | 428.174 ms | 1.852 ms | 426.590 ms | 430.210 ms | OK |
| **Counting Sort** | Reverse Sorted | 141.209 ms | 1.106 ms | 140.061 ms | 142.266 ms | OK |
| **Shell Sort** | Almost Sorted | 2.4584 s | 42.193 ms | 2.4192 s | 2.5031 s | OK |
| **Heap Sort** | Almost Sorted | 227.886 ms | 2.128 ms | 225.496 ms | 229.575 ms | OK |
| **Merge Sort** | Almost Sorted | 2.0016 s | 37.148 ms | 1.9633 s | 2.0374 s | OK |
| **Quick Sort** | Almost Sorted | 2.1064 s | 56.157 ms | 2.0631 s | 2.1699 s | OK |
| **Timsort (built-in)** | Almost Sorted | 20.669 ms | 555.85 us | 20.079 ms | 21.182 ms | OK |
| **Timsort (custom)** | Almost Sorted | 1.5045 s | 63.054 ms | 1.4599 s | 1.5766 s | OK |
| **Radix Sort** | Almost Sorted | 388.695 ms | 3.980 ms | 384.851 ms | 392.798 ms | OK |
| **Counting Sort** | Almost Sorted | 146.405 ms | 889.51 us | 145.422 ms | 147.155 ms | OK |
| **Shell Sort** | Half Sorted | 3.8565 s | 180.122 ms | 3.6695 s | 4.0288 s | OK |
| **Heap Sort** | Half Sorted | 357.807 ms | 10.528 ms | 346.275 ms | 366.905 ms | OK |
| **Merge Sort** | Half Sorted | 1.9473 s | 46.697 ms | 1.9194 s | 2.0012 s | OK |
| **Quick Sort** | Half Sorted | 2.0052 s | 40.485 ms | 1.9660 s | 2.0468 s | OK |
| **Timsort (built-in)** | Half Sorted | 58.856 ms | 259.59 us | 58.558 ms | 59.030 ms | OK |
| **Timsort (custom)** | Half Sorted | 1.5866 s | 11.155 ms | 1.5756 s | 1.5979 s | OK |
| **Radix Sort** | Half Sorted | 446.297 ms | 28.552 ms | 415.498 ms | 471.885 ms | OK |
| **Counting Sort** | Half Sorted | 148.684 ms | 624.31 us | 148.244 ms | 149.398 ms | OK |
| **Shell Sort** | Flat (Few Unique) | 754.625 ms | 7.419 ms | 746.348 ms | 760.677 ms | OK |
| **Heap Sort** | Flat (Few Unique) | 188.012 ms | 2.182 ms | 186.380 ms | 190.490 ms | OK |
| **Merge Sort** | Flat (Few Unique) | 1.9998 s | 7.050 ms | 1.9949 s | 2.0079 s | OK |
| **Quick Sort** | Flat (Few Unique) | 169.551 ms | 20.892 ms | 146.966 ms | 188.186 ms | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 34.277 ms | 115.62 us | 34.158 ms | 34.389 ms | OK |
| **Timsort (custom)** | Flat (Few Unique) | 1.7422 s | 2.561 ms | 1.7392 s | 1.7439 s | OK |
| **Radix Sort** | Flat (Few Unique) | 80.906 ms | 369.02 us | 80.554 ms | 81.290 ms | OK |
| **Counting Sort** | Flat (Few Unique) | 77.999 ms | 254.80 us | 77.849 ms | 78.294 ms | OK |
| **Shell Sort** | Floats | 4.3695 s | 281.484 ms | 4.1017 s | 4.6629 s | OK |
| **Heap Sort** | Floats | 614.344 ms | 10.781 ms | 602.319 ms | 623.145 ms | OK |
| **Merge Sort** | Floats | 2.2697 s | 64.244 ms | 2.1960 s | 2.3138 s | OK |
| **Quick Sort** | Floats | 2.2673 s | 18.088 ms | 2.2478 s | 2.2835 s | OK |
| **Timsort (built-in)** | Floats | 121.048 ms | 911.09 us | 120.247 ms | 122.039 ms | OK |
| **Timsort (custom)** | Floats | 2.0834 s | 60.382 ms | 2.0476 s | 2.1531 s | OK |
| Radix Sort | Floats | — | — | — | — | Skipped (integers only) |
| Counting Sort | Floats | — | — | — | — | Skipped (integers only) |
| **Shell Sort** | Strings | 4.9311 s | 243.137 ms | 4.6585 s | 5.1257 s | OK |
| **Heap Sort** | Strings | 661.828 ms | 11.864 ms | 651.979 ms | 674.999 ms | OK |
| **Merge Sort** | Strings | 2.3296 s | 7.423 ms | 2.3218 s | 2.3366 s | OK |
| **Quick Sort** | Strings | 2.4234 s | 17.819 ms | 2.4099 s | 2.4436 s | OK |
| **Timsort (built-in)** | Strings | 182.471 ms | 4.699 ms | 177.221 ms | 186.285 ms | OK |
| **Timsort (custom)** | Strings | 2.2559 s | 4.614 ms | 2.2506 s | 2.2588 s | OK |
| Radix Sort | Strings | — | — | — | — | Skipped (integers only) |
| Counting Sort | Strings | — | — | — | — | Skipped (integers only) |

---

