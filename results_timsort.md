# Sorting Algorithm Benchmark Results

> Timing: `time.perf_counter_ns()` — nanosecond resolution

## Size: 20  x  100,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Timsort (built-in)** | Random Ints | 466.2 ns | 66.9 ns | 333.0 ns | 8.83 us | OK |
| **Timsort (custom)** | Random Ints | 5.89 us | 774.5 ns | 3.12 us | 25.67 us | OK |
| **Merge Sort** | Random Ints | 12.19 us | 550.2 ns | 10.62 us | 34.04 us | OK |
| **Insertion Sort** | Random Ints | 5.66 us | 792.6 ns | 2.58 us | 21.50 us | OK |
| **Quick Sort** | Random Ints | 12.13 us | 1.13 us | 8.21 us | 32.25 us | OK |
| **Timsort (built-in)** | Sorted Ints | 119.7 ns | 74.9 ns | 41.0 ns | 11.46 us | OK |
| **Timsort (custom)** | Sorted Ints | 1.40 us | 175.4 ns | 1.25 us | 15.08 us | OK |
| **Merge Sort** | Sorted Ints | 10.68 us | 471.7 ns | 9.46 us | 29.96 us | OK |
| **Insertion Sort** | Sorted Ints | 1.12 us | 155.8 ns | 1.00 us | 19.42 us | OK |
| **Quick Sort** | Sorted Ints | 12.48 us | 1.86 us | 9.04 us | 55.25 us | OK |
| **Timsort (built-in)** | Reverse Sorted | 118.6 ns | 44.8 ns | 41.0 ns | 12.21 us | OK |
| **Timsort (custom)** | Reverse Sorted | 9.86 us | 472.4 ns | 8.75 us | 29.21 us | OK |
| **Merge Sort** | Reverse Sorted | 11.22 us | 732.7 ns | 9.88 us | 32.92 us | OK |
| **Insertion Sort** | Reverse Sorted | 9.57 us | 376.7 ns | 8.50 us | 30.54 us | OK |
| **Quick Sort** | Reverse Sorted | 12.46 us | 1.91 us | 9.46 us | 51.83 us | OK |
| **Timsort (built-in)** | Almost Sorted | 267.5 ns | 134.4 ns | 83.0 ns | 12.71 us | OK |
| **Timsort (custom)** | Almost Sorted | 2.13 us | 486.9 ns | 1.33 us | 16.33 us | OK |
| **Merge Sort** | Almost Sorted | 11.21 us | 514.4 ns | 9.62 us | 40.29 us | OK |
| **Insertion Sort** | Almost Sorted | 1.84 us | 494.3 ns | 1.00 us | 20.33 us | OK |
| **Quick Sort** | Almost Sorted | 12.49 us | 1.88 us | 9.46 us | 58.29 us | OK |
| **Timsort (built-in)** | Half Sorted | 322.5 ns | 81.0 ns | 208.0 ns | 12.38 us | OK |
| **Timsort (custom)** | Half Sorted | 3.68 us | 570.3 ns | 1.79 us | 20.75 us | OK |
| **Merge Sort** | Half Sorted | 11.78 us | 519.2 ns | 10.29 us | 29.96 us | OK |
| **Insertion Sort** | Half Sorted | 3.34 us | 558.3 ns | 1.62 us | 25.79 us | OK |
| **Quick Sort** | Half Sorted | 10.21 us | 1.16 us | 6.17 us | 27.62 us | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 446.5 ns | 62.5 ns | 333.0 ns | 11.25 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 5.09 us | 731.6 ns | 2.50 us | 21.25 us | OK |
| **Merge Sort** | Flat (Few Unique) | 12.16 us | 449.3 ns | 10.75 us | 30.25 us | OK |
| **Insertion Sort** | Flat (Few Unique) | 4.80 us | 734.1 ns | 2.17 us | 19.50 us | OK |
| **Quick Sort** | Flat (Few Unique) | 5.56 us | 1.71 us | 2.71 us | 45.04 us | OK |
| **Timsort (built-in)** | Floats | 518.5 ns | 62.2 ns | 416.0 ns | 12.08 us | OK |
| **Timsort (custom)** | Floats | 5.85 us | 818.1 ns | 3.21 us | 22.88 us | OK |
| **Merge Sort** | Floats | 12.23 us | 701.6 ns | 10.62 us | 29.04 us | OK |
| **Insertion Sort** | Floats | 5.54 us | 821.7 ns | 2.62 us | 30.46 us | OK |
| **Quick Sort** | Floats | 12.67 us | 2.08 us | 9.33 us | 58.54 us | OK |
| **Timsort (built-in)** | Strings | 681.9 ns | 170.0 ns | 541.0 ns | 14.00 us | OK |
| **Timsort (custom)** | Strings | 6.26 us | 779.7 ns | 3.50 us | 23.12 us | OK |
| **Merge Sort** | Strings | 12.31 us | 331.0 ns | 10.96 us | 29.12 us | OK |
| **Insertion Sort** | Strings | 5.98 us | 765.0 ns | 3.08 us | 26.58 us | OK |
| **Quick Sort** | Strings | 12.94 us | 1.15 us | 9.92 us | 31.08 us | OK |

---

## Size: 30  x  100,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Timsort (built-in)** | Random Ints | 752.8 ns | 109.2 ns | 625.0 ns | 12.00 us | OK |
| **Timsort (custom)** | Random Ints | 11.78 us | 1.30 us | 6.83 us | 31.46 us | OK |
| **Merge Sort** | Random Ints | 19.69 us | 859.2 ns | 18.62 us | 59.46 us | OK |
| **Insertion Sort** | Random Ints | 11.42 us | 1.30 us | 6.33 us | 39.67 us | OK |
| **Quick Sort** | Random Ints | 19.52 us | 1.47 us | 14.79 us | 42.33 us | OK |
| **Timsort (built-in)** | Sorted Ints | 136.1 ns | 26.2 ns | 83.0 ns | 5.67 us | OK |
| **Timsort (custom)** | Sorted Ints | 1.91 us | 123.7 ns | 1.75 us | 12.50 us | OK |
| **Merge Sort** | Sorted Ints | 17.13 us | 446.9 ns | 16.50 us | 49.25 us | OK |
| **Insertion Sort** | Sorted Ints | 1.61 us | 110.5 ns | 1.46 us | 12.33 us | OK |
| **Quick Sort** | Sorted Ints | 20.02 us | 2.27 us | 15.58 us | 60.92 us | OK |
| **Timsort (built-in)** | Reverse Sorted | 139.9 ns | 66.0 ns | 83.0 ns | 10.50 us | OK |
| **Timsort (custom)** | Reverse Sorted | 20.97 us | 453.5 ns | 20.38 us | 50.58 us | OK |
| **Merge Sort** | Reverse Sorted | 17.58 us | 420.5 ns | 17.00 us | 45.17 us | OK |
| **Insertion Sort** | Reverse Sorted | 20.77 us | 431.0 ns | 20.17 us | 44.54 us | OK |
| **Quick Sort** | Reverse Sorted | 19.96 us | 2.32 us | 15.75 us | 63.38 us | OK |
| **Timsort (built-in)** | Almost Sorted | 354.9 ns | 119.7 ns | 125.0 ns | 11.08 us | OK |
| **Timsort (custom)** | Almost Sorted | 2.94 us | 670.7 ns | 1.83 us | 18.92 us | OK |
| **Merge Sort** | Almost Sorted | 17.80 us | 783.7 ns | 16.75 us | 47.71 us | OK |
| **Insertion Sort** | Almost Sorted | 2.64 us | 672.9 ns | 1.54 us | 17.25 us | OK |
| **Quick Sort** | Almost Sorted | 20.02 us | 2.35 us | 15.71 us | 73.33 us | OK |
| **Timsort (built-in)** | Half Sorted | 498.8 ns | 67.2 ns | 375.0 ns | 12.83 us | OK |
| **Timsort (custom)** | Half Sorted | 6.79 us | 939.1 ns | 3.17 us | 23.92 us | OK |
| **Merge Sort** | Half Sorted | 18.69 us | 480.5 ns | 17.71 us | 55.38 us | OK |
| **Insertion Sort** | Half Sorted | 6.48 us | 956.2 ns | 3.25 us | 41.83 us | OK |
| **Quick Sort** | Half Sorted | 16.40 us | 1.55 us | 11.25 us | 49.25 us | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 717.0 ns | 68.2 ns | 541.0 ns | 14.88 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 9.86 us | 1.23 us | 4.96 us | 28.54 us | OK |
| **Merge Sort** | Flat (Few Unique) | 19.57 us | 467.7 ns | 18.38 us | 51.96 us | OK |
| **Insertion Sort** | Flat (Few Unique) | 9.65 us | 1.24 us | 4.38 us | 29.58 us | OK |
| **Quick Sort** | Flat (Few Unique) | 7.12 us | 1.94 us | 4.17 us | 52.00 us | OK |
| **Timsort (built-in)** | Floats | 850.0 ns | 67.0 ns | 709.0 ns | 10.92 us | OK |
| **Timsort (custom)** | Floats | 11.76 us | 1.27 us | 6.71 us | 41.38 us | OK |
| **Merge Sort** | Floats | 19.61 us | 461.5 ns | 18.67 us | 46.12 us | OK |
| **Insertion Sort** | Floats | 11.41 us | 1.26 us | 6.58 us | 45.58 us | OK |
| **Quick Sort** | Floats | 20.31 us | 2.32 us | 15.62 us | 72.96 us | OK |
| **Timsort (built-in)** | Strings | 1.12 us | 71.4 ns | 1.00 us | 8.96 us | OK |
| **Timsort (custom)** | Strings | 12.61 us | 1.35 us | 7.04 us | 39.79 us | OK |
| **Merge Sort** | Strings | 19.79 us | 435.5 ns | 18.79 us | 44.92 us | OK |
| **Insertion Sort** | Strings | 12.33 us | 1.41 us | 6.75 us | 53.08 us | OK |
| **Quick Sort** | Strings | 20.78 us | 1.48 us | 16.62 us | 52.71 us | OK |

---

## Size: 50  x  100,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Timsort (built-in)** | Random Ints | 1.40 us | 101.1 ns | 1.25 us | 13.25 us | OK |
| **Timsort (custom)** | Random Ints | 21.67 us | 1.40 us | 16.58 us | 47.67 us | OK |
| **Merge Sort** | Random Ints | 35.78 us | 647.5 ns | 34.29 us | 61.00 us | OK |
| **Insertion Sort** | Random Ints | 29.59 us | 2.63 us | 19.17 us | 61.08 us | OK |
| **Quick Sort** | Random Ints | 35.44 us | 2.27 us | 27.83 us | 65.21 us | OK |
| **Timsort (built-in)** | Sorted Ints | 178.1 ns | 60.1 ns | 125.0 ns | 10.38 us | OK |
| **Timsort (custom)** | Sorted Ints | 7.02 us | 253.8 ns | 6.75 us | 32.33 us | OK |
| **Merge Sort** | Sorted Ints | 30.84 us | 605.1 ns | 29.79 us | 61.00 us | OK |
| **Insertion Sort** | Sorted Ints | 2.57 us | 157.1 ns | 2.42 us | 13.42 us | OK |
| **Quick Sort** | Sorted Ints | 36.24 us | 2.69 us | 29.88 us | 77.17 us | OK |
| **Timsort (built-in)** | Reverse Sorted | 186.8 ns | 59.5 ns | 125.0 ns | 8.88 us | OK |
| **Timsort (custom)** | Reverse Sorted | 33.44 us | 606.7 ns | 32.67 us | 62.62 us | OK |
| **Merge Sort** | Reverse Sorted | 32.01 us | 619.7 ns | 31.00 us | 68.33 us | OK |
| **Insertion Sort** | Reverse Sorted | 56.44 us | 881.6 ns | 55.08 us | 87.04 us | OK |
| **Quick Sort** | Reverse Sorted | 35.99 us | 2.66 us | 29.38 us | 93.38 us | OK |
| **Timsort (built-in)** | Almost Sorted | 535.6 ns | 157.3 ns | 125.0 ns | 10.38 us | OK |
| **Timsort (custom)** | Almost Sorted | 8.38 us | 826.7 ns | 6.83 us | 29.79 us | OK |
| **Merge Sort** | Almost Sorted | 31.78 us | 806.2 ns | 30.08 us | 60.92 us | OK |
| **Insertion Sort** | Almost Sorted | 4.22 us | 1.08 us | 2.50 us | 30.21 us | OK |
| **Quick Sort** | Almost Sorted | 36.15 us | 2.65 us | 29.83 us | 75.12 us | OK |
| **Timsort (built-in)** | Half Sorted | 870.6 ns | 63.3 ns | 708.0 ns | 11.04 us | OK |
| **Timsort (custom)** | Half Sorted | 14.52 us | 1.04 us | 10.50 us | 53.71 us | OK |
| **Merge Sort** | Half Sorted | 33.78 us | 725.2 ns | 32.46 us | 71.54 us | OK |
| **Insertion Sort** | Half Sorted | 15.98 us | 1.99 us | 8.42 us | 46.46 us | OK |
| **Quick Sort** | Half Sorted | 30.12 us | 2.29 us | 21.92 us | 58.96 us | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 1.33 us | 105.7 ns | 1.17 us | 17.75 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 19.09 us | 1.37 us | 14.00 us | 44.83 us | OK |
| **Merge Sort** | Flat (Few Unique) | 35.73 us | 913.5 ns | 33.83 us | 61.79 us | OK |
| **Insertion Sort** | Flat (Few Unique) | 24.50 us | 2.60 us | 13.46 us | 47.33 us | OK |
| **Quick Sort** | Flat (Few Unique) | 10.03 us | 1.78 us | 7.42 us | 57.42 us | OK |
| **Timsort (built-in)** | Floats | 1.60 us | 100.6 ns | 1.42 us | 12.25 us | OK |
| **Timsort (custom)** | Floats | 21.87 us | 1.41 us | 15.62 us | 52.88 us | OK |
| **Merge Sort** | Floats | 35.85 us | 851.2 ns | 34.33 us | 111.21 us | OK |
| **Insertion Sort** | Floats | 29.80 us | 2.66 us | 19.62 us | 53.29 us | OK |
| **Quick Sort** | Floats | 36.85 us | 2.65 us | 30.12 us | 80.29 us | OK |
| **Timsort (built-in)** | Strings | 2.13 us | 97.8 ns | 1.92 us | 16.58 us | OK |
| **Timsort (custom)** | Strings | 23.16 us | 1.58 us | 17.38 us | 50.88 us | OK |
| **Merge Sort** | Strings | 36.26 us | 694.4 ns | 34.92 us | 66.79 us | OK |
| **Insertion Sort** | Strings | 32.01 us | 2.88 us | 20.58 us | 109.50 us | OK |
| **Quick Sort** | Strings | 37.70 us | 2.27 us | 30.12 us | 68.50 us | OK |

---

## Size: 100  x  100,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Timsort (built-in)** | Random Ints | 3.23 us | 139.7 ns | 2.92 us | 17.92 us | OK |
| **Timsort (custom)** | Random Ints | 51.55 us | 2.14 us | 43.50 us | 83.29 us | OK |
| **Merge Sort** | Random Ints | 80.22 us | 1.53 us | 77.96 us | 149.17 us | OK |
| **Insertion Sort** | Random Ints | 112.66 us | 7.39 us | 82.75 us | 194.04 us | OK |
| **Quick Sort** | Random Ints | 79.30 us | 4.20 us | 67.17 us | 109.75 us | OK |
| **Timsort (built-in)** | Sorted Ints | 273.7 ns | 64.4 ns | 208.0 ns | 9.58 us | OK |
| **Timsort (custom)** | Sorted Ints | 20.29 us | 435.6 ns | 19.79 us | 49.54 us | OK |
| **Merge Sort** | Sorted Ints | 68.58 us | 1.11 us | 66.75 us | 181.38 us | OK |
| **Insertion Sort** | Sorted Ints | 5.01 us | 221.1 ns | 4.75 us | 28.96 us | OK |
| **Quick Sort** | Sorted Ints | 80.47 us | 4.49 us | 68.08 us | 130.25 us | OK |
| **Timsort (built-in)** | Reverse Sorted | 277.8 ns | 72.8 ns | 208.0 ns | 15.33 us | OK |
| **Timsort (custom)** | Reverse Sorted | 72.74 us | 883.3 ns | 71.58 us | 102.75 us | OK |
| **Merge Sort** | Reverse Sorted | 70.47 us | 1.25 us | 68.67 us | 101.71 us | OK |
| **Insertion Sort** | Reverse Sorted | 223.96 us | 3.27 us | 217.67 us | 335.04 us | OK |
| **Quick Sort** | Reverse Sorted | 80.14 us | 4.51 us | 68.08 us | 139.04 us | OK |
| **Timsort (built-in)** | Almost Sorted | 1.04 us | 244.1 ns | 250.0 ns | 18.75 us | OK |
| **Timsort (custom)** | Almost Sorted | 24.19 us | 1.41 us | 19.96 us | 53.33 us | OK |
| **Merge Sort** | Almost Sorted | 71.35 us | 1.48 us | 67.58 us | 179.33 us | OK |
| **Insertion Sort** | Almost Sorted | 11.16 us | 3.00 us | 5.00 us | 34.54 us | OK |
| **Quick Sort** | Almost Sorted | 80.61 us | 4.58 us | 68.58 us | 147.21 us | OK |
| **Timsort (built-in)** | Half Sorted | 1.84 us | 107.5 ns | 1.62 us | 11.04 us | OK |
| **Timsort (custom)** | Half Sorted | 36.34 us | 1.55 us | 30.25 us | 73.04 us | OK |
| **Merge Sort** | Half Sorted | 74.89 us | 1.09 us | 72.92 us | 141.38 us | OK |
| **Insertion Sort** | Half Sorted | 58.72 us | 5.60 us | 37.33 us | 87.83 us | OK |
| **Quick Sort** | Half Sorted | 68.05 us | 4.25 us | 54.62 us | 108.33 us | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 2.79 us | 153.6 ns | 2.50 us | 18.12 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 45.79 us | 1.97 us | 38.08 us | 79.62 us | OK |
| **Merge Sort** | Flat (Few Unique) | 79.71 us | 1.23 us | 77.00 us | 190.54 us | OK |
| **Insertion Sort** | Flat (Few Unique) | 91.98 us | 7.21 us | 60.92 us | 129.38 us | OK |
| **Quick Sort** | Flat (Few Unique) | 17.17 us | 2.41 us | 13.46 us | 54.42 us | OK |
| **Timsort (built-in)** | Floats | 3.68 us | 158.6 ns | 3.38 us | 18.29 us | OK |
| **Timsort (custom)** | Floats | 51.85 us | 2.03 us | 43.58 us | 79.29 us | OK |
| **Merge Sort** | Floats | 80.25 us | 1.16 us | 78.12 us | 157.96 us | OK |
| **Insertion Sort** | Floats | 113.12 us | 7.39 us | 84.38 us | 151.21 us | OK |
| **Quick Sort** | Floats | 81.99 us | 4.47 us | 70.33 us | 130.08 us | OK |
| **Timsort (built-in)** | Strings | 4.96 us | 193.4 ns | 4.58 us | 29.21 us | OK |
| **Timsort (custom)** | Strings | 54.29 us | 2.14 us | 45.12 us | 90.75 us | OK |
| **Merge Sort** | Strings | 81.03 us | 1.12 us | 79.00 us | 108.67 us | OK |
| **Insertion Sort** | Strings | 121.99 us | 7.93 us | 88.21 us | 196.83 us | OK |
| **Quick Sort** | Strings | 84.47 us | 4.46 us | 72.21 us | 160.04 us | OK |

---

## Size: 1,000  x  1,000 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Timsort (built-in)** | Random Ints | 48.34 us | 1.08 us | 46.88 us | 61.71 us | OK |
| **Timsort (custom)** | Random Ints | 932.14 us | 19.91 us | 888.79 us | 1.005 ms | OK |
| **Merge Sort** | Random Ints | 1.115 ms | 7.13 us | 1.100 ms | 1.162 ms | OK |
| **Insertion Sort** | Random Ints | 12.559 ms | 346.27 us | 11.583 ms | 13.932 ms | OK |
| **Quick Sort** | Random Ints | 1.153 ms | 42.86 us | 1.056 ms | 1.335 ms | OK |
| **Timsort (built-in)** | Sorted Ints | 1.90 us | 214.7 ns | 1.79 us | 8.25 us | OK |
| **Timsort (custom)** | Sorted Ints | 420.10 us | 5.91 us | 415.21 us | 462.62 us | OK |
| **Merge Sort** | Sorted Ints | 929.71 us | 5.97 us | 918.62 us | 965.79 us | OK |
| **Insertion Sort** | Sorted Ints | 57.68 us | 2.08 us | 55.75 us | 78.21 us | OK |
| **Quick Sort** | Sorted Ints | 1.142 ms | 43.96 us | 1.040 ms | 1.379 ms | OK |
| **Timsort (built-in)** | Reverse Sorted | 2.03 us | 101.8 ns | 1.92 us | 3.33 us | OK |
| **Timsort (custom)** | Reverse Sorted | 1.173 ms | 11.66 us | 1.158 ms | 1.243 ms | OK |
| **Merge Sort** | Reverse Sorted | 931.97 us | 6.50 us | 916.92 us | 964.88 us | OK |
| **Insertion Sort** | Reverse Sorted | 24.057 ms | 236.06 us | 23.651 ms | 25.300 ms | OK |
| **Quick Sort** | Reverse Sorted | 1.142 ms | 43.39 us | 1.051 ms | 1.304 ms | OK |
| **Timsort (built-in)** | Almost Sorted | 12.44 us | 1.11 us | 9.62 us | 24.50 us | OK |
| **Timsort (custom)** | Almost Sorted | 517.89 us | 8.83 us | 492.83 us | 560.92 us | OK |
| **Merge Sort** | Almost Sorted | 1.004 ms | 8.88 us | 975.62 us | 1.051 ms | OK |
| **Insertion Sort** | Almost Sorted | 709.06 us | 102.45 us | 397.88 us | 1.075 ms | OK |
| **Quick Sort** | Almost Sorted | 1.144 ms | 44.36 us | 1.058 ms | 1.398 ms | OK |
| **Timsort (built-in)** | Half Sorted | 25.55 us | 636.9 ns | 24.71 us | 34.46 us | OK |
| **Timsort (custom)** | Half Sorted | 686.53 us | 12.56 us | 657.08 us | 749.42 us | OK |
| **Merge Sort** | Half Sorted | 1.020 ms | 8.93 us | 1.003 ms | 1.097 ms | OK |
| **Insertion Sort** | Half Sorted | 6.301 ms | 224.76 us | 5.586 ms | 7.044 ms | OK |
| **Quick Sort** | Half Sorted | 1.026 ms | 46.42 us | 908.33 us | 1.230 ms | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 31.07 us | 669.9 ns | 30.25 us | 38.29 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 823.15 us | 13.18 us | 787.00 us | 886.83 us | OK |
| **Merge Sort** | Flat (Few Unique) | 1.098 ms | 6.98 us | 1.083 ms | 1.140 ms | OK |
| **Insertion Sort** | Flat (Few Unique) | 10.232 ms | 288.79 us | 9.315 ms | 11.720 ms | OK |
| **Quick Sort** | Flat (Few Unique) | 157.12 us | 18.35 us | 130.88 us | 208.71 us | OK |
| **Timsort (built-in)** | Floats | 53.77 us | 961.6 ns | 52.42 us | 63.88 us | OK |
| **Timsort (custom)** | Floats | 911.20 us | 14.76 us | 877.92 us | 999.12 us | OK |
| **Merge Sort** | Floats | 1.112 ms | 10.82 us | 1.085 ms | 1.201 ms | OK |
| **Insertion Sort** | Floats | 12.486 ms | 336.82 us | 11.575 ms | 13.441 ms | OK |
| **Quick Sort** | Floats | 1.181 ms | 42.99 us | 1.084 ms | 1.366 ms | OK |
| **Timsort (built-in)** | Strings | 75.48 us | 1.26 us | 73.29 us | 95.46 us | OK |
| **Timsort (custom)** | Strings | 963.50 us | 13.74 us | 933.92 us | 1.049 ms | OK |
| **Merge Sort** | Strings | 1.142 ms | 10.12 us | 1.116 ms | 1.179 ms | OK |
| **Insertion Sort** | Strings | 13.582 ms | 310.11 us | 12.332 ms | 14.539 ms | OK |
| **Quick Sort** | Strings | 1.242 ms | 49.34 us | 1.140 ms | 1.476 ms | OK |

---

## Size: 10,000  x  100 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Timsort (built-in)** | Random Ints | 662.65 us | 6.49 us | 652.46 us | 699.71 us | OK |
| **Timsort (custom)** | Random Ints | 12.222 ms | 303.08 us | 11.722 ms | 12.752 ms | OK |
| **Merge Sort** | Random Ints | 14.719 ms | 183.41 us | 14.436 ms | 15.076 ms | OK |
| **Insertion Sort** | Random Ints | 1.3180 s | 32.032 ms | 1.2633 s | 1.3750 s | OK |
| **Quick Sort** | Random Ints | 15.208 ms | 469.64 us | 14.389 ms | 16.596 ms | OK |
| **Timsort (built-in)** | Sorted Ints | 19.13 us | 689.3 ns | 18.46 us | 23.96 us | OK |
| **Timsort (custom)** | Sorted Ints | 7.364 ms | 126.19 us | 7.223 ms | 7.778 ms | OK |
| **Merge Sort** | Sorted Ints | 11.725 ms | 120.75 us | 11.529 ms | 12.072 ms | OK |
| **Insertion Sort** | Sorted Ints | 598.87 us | 14.62 us | 589.33 us | 689.54 us | OK |
| **Quick Sort** | Sorted Ints | 14.695 ms | 450.25 us | 13.786 ms | 16.140 ms | OK |
| **Timsort (built-in)** | Reverse Sorted | 21.03 us | 829.4 ns | 20.21 us | 26.58 us | OK |
| **Timsort (custom)** | Reverse Sorted | 12.074 ms | 62.82 us | 11.988 ms | 12.282 ms | OK |
| **Merge Sort** | Reverse Sorted | 11.950 ms | 158.69 us | 11.794 ms | 13.067 ms | OK |
| **Insertion Sort** | Reverse Sorted | 2.5450 s | 14.175 ms | 2.5279 s | 2.5743 s | OK |
| **Quick Sort** | Reverse Sorted | 14.865 ms | 517.08 us | 13.910 ms | 16.305 ms | OK |
| **Timsort (built-in)** | Almost Sorted | 130.63 us | 3.76 us | 123.96 us | 145.62 us | OK |
| **Timsort (custom)** | Almost Sorted | 8.997 ms | 138.62 us | 8.712 ms | 9.423 ms | OK |
| **Merge Sort** | Almost Sorted | 13.156 ms | 121.01 us | 12.927 ms | 13.548 ms | OK |
| **Insertion Sort** | Almost Sorted | 66.634 ms | 3.277 ms | 54.700 ms | 75.230 ms | OK |
| **Quick Sort** | Almost Sorted | 14.660 ms | 430.72 us | 14.009 ms | 16.379 ms | OK |
| **Timsort (built-in)** | Half Sorted | 346.60 us | 3.64 us | 340.75 us | 359.54 us | OK |
| **Timsort (custom)** | Half Sorted | 9.703 ms | 152.77 us | 9.503 ms | 10.280 ms | OK |
| **Merge Sort** | Half Sorted | 13.067 ms | 123.90 us | 12.915 ms | 13.508 ms | OK |
| **Insertion Sort** | Half Sorted | 645.058 ms | 10.481 ms | 627.853 ms | 682.338 ms | OK |
| **Quick Sort** | Half Sorted | 13.613 ms | 487.36 us | 12.751 ms | 15.536 ms | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 297.00 us | 3.54 us | 293.71 us | 323.79 us | OK |
| **Timsort (custom)** | Flat (Few Unique) | 10.827 ms | 41.08 us | 10.748 ms | 10.921 ms | OK |
| **Merge Sort** | Flat (Few Unique) | 13.842 ms | 90.28 us | 13.682 ms | 14.054 ms | OK |
| **Insertion Sort** | Flat (Few Unique) | 1.0105 s | 8.256 ms | 989.744 ms | 1.0346 s | OK |
| **Quick Sort** | Flat (Few Unique) | 1.565 ms | 189.21 us | 1.300 ms | 1.890 ms | OK |
| **Timsort (built-in)** | Floats | 720.19 us | 4.98 us | 709.33 us | 740.00 us | OK |
| **Timsort (custom)** | Floats | 11.973 ms | 294.36 us | 11.697 ms | 12.741 ms | OK |
| **Merge Sort** | Floats | 14.717 ms | 230.42 us | 14.322 ms | 15.157 ms | OK |
| **Insertion Sort** | Floats | 1.3298 s | 26.955 ms | 1.2770 s | 1.4215 s | OK |
| **Quick Sort** | Floats | 15.377 ms | 471.29 us | 14.539 ms | 17.395 ms | OK |
| **Timsort (built-in)** | Strings | 1.025 ms | 4.46 us | 1.014 ms | 1.040 ms | OK |
| **Timsort (custom)** | Strings | 12.454 ms | 74.66 us | 12.328 ms | 12.705 ms | OK |
| **Merge Sort** | Strings | 14.890 ms | 64.94 us | 14.793 ms | 15.095 ms | OK |
| **Insertion Sort** | Strings | 1.3557 s | 10.104 ms | 1.3246 s | 1.3871 s | OK |
| **Quick Sort** | Strings | 16.162 ms | 561.62 us | 15.227 ms | 18.066 ms | OK |

---

## Size: 100,000  x  10 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Timsort (built-in)** | Random Ints | 8.607 ms | 29.57 us | 8.571 ms | 8.674 ms | OK |
| **Timsort (custom)** | Random Ints | 161.412 ms | 4.332 ms | 154.914 ms | 166.849 ms | OK |
| **Merge Sort** | Random Ints | 180.794 ms | 3.439 ms | 176.803 ms | 184.605 ms | OK |
| Insertion Sort | Random Ints | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Random Ints | 184.733 ms | 4.560 ms | 179.006 ms | 193.539 ms | OK |
| **Timsort (built-in)** | Sorted Ints | 194.09 us | 29.19 us | 176.79 us | 275.17 us | OK |
| **Timsort (custom)** | Sorted Ints | 95.880 ms | 1.727 ms | 94.050 ms | 99.476 ms | OK |
| **Merge Sort** | Sorted Ints | 141.793 ms | 908.72 us | 139.778 ms | 143.146 ms | OK |
| Insertion Sort | Sorted Ints | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Sorted Ints | 177.154 ms | 5.141 ms | 171.146 ms | 186.636 ms | OK |
| **Timsort (built-in)** | Reverse Sorted | 207.68 us | 29.19 us | 192.17 us | 289.58 us | OK |
| **Timsort (custom)** | Reverse Sorted | 155.555 ms | 1.080 ms | 154.083 ms | 157.632 ms | OK |
| **Merge Sort** | Reverse Sorted | 143.506 ms | 826.00 us | 142.330 ms | 144.960 ms | OK |
| Insertion Sort | Reverse Sorted | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Reverse Sorted | 179.018 ms | 4.335 ms | 171.870 ms | 184.839 ms | OK |
| **Timsort (built-in)** | Almost Sorted | 1.554 ms | 36.60 us | 1.518 ms | 1.627 ms | OK |
| **Timsort (custom)** | Almost Sorted | 116.252 ms | 531.96 us | 115.287 ms | 117.276 ms | OK |
| **Merge Sort** | Almost Sorted | 161.030 ms | 570.41 us | 160.083 ms | 161.801 ms | OK |
| Insertion Sort | Almost Sorted | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Almost Sorted | 178.663 ms | 4.362 ms | 171.995 ms | 184.660 ms | OK |
| **Timsort (built-in)** | Half Sorted | 4.486 ms | 26.26 us | 4.449 ms | 4.531 ms | OK |
| **Timsort (custom)** | Half Sorted | 126.253 ms | 2.489 ms | 124.137 ms | 132.476 ms | OK |
| **Merge Sort** | Half Sorted | 160.743 ms | 2.894 ms | 157.961 ms | 167.632 ms | OK |
| Insertion Sort | Half Sorted | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Half Sorted | 167.800 ms | 4.334 ms | 159.760 ms | 173.615 ms | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 3.131 ms | 27.55 us | 3.111 ms | 3.194 ms | OK |
| **Timsort (custom)** | Flat (Few Unique) | 139.749 ms | 676.48 us | 138.834 ms | 141.117 ms | OK |
| **Merge Sort** | Flat (Few Unique) | 169.434 ms | 732.94 us | 168.553 ms | 170.707 ms | OK |
| Insertion Sort | Flat (Few Unique) | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Flat (Few Unique) | 15.044 ms | 1.839 ms | 13.302 ms | 18.855 ms | OK |
| **Timsort (built-in)** | Floats | 9.261 ms | 30.34 us | 9.228 ms | 9.333 ms | OK |
| **Timsort (custom)** | Floats | 161.763 ms | 4.190 ms | 155.362 ms | 167.944 ms | OK |
| **Merge Sort** | Floats | 183.270 ms | 2.595 ms | 176.941 ms | 186.698 ms | OK |
| Insertion Sort | Floats | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Floats | 186.506 ms | 3.682 ms | 180.548 ms | 192.192 ms | OK |
| **Timsort (built-in)** | Strings | 12.627 ms | 416.16 us | 12.138 ms | 13.140 ms | OK |
| **Timsort (custom)** | Strings | 163.558 ms | 453.61 us | 162.780 ms | 164.342 ms | OK |
| **Merge Sort** | Strings | 183.612 ms | 324.54 us | 183.135 ms | 184.090 ms | OK |
| Insertion Sort | Strings | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Strings | 196.207 ms | 3.349 ms | 190.333 ms | 200.842 ms | OK |

---

## Size: 1,000,000  x  3 iterations

| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- |
| **Timsort (built-in)** | Random Ints | 115.308 ms | 457.16 us | 114.853 ms | 115.767 ms | OK |
| **Timsort (custom)** | Random Ints | 2.0615 s | 36.367 ms | 2.0355 s | 2.1030 s | OK |
| **Merge Sort** | Random Ints | 2.2236 s | 46.390 ms | 2.1701 s | 2.2526 s | OK |
| Insertion Sort | Random Ints | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Random Ints | 2.2027 s | 40.302 ms | 2.1663 s | 2.2460 s | OK |
| **Timsort (built-in)** | Sorted Ints | 1.913 ms | 130.15 us | 1.790 ms | 2.049 ms | OK |
| **Timsort (custom)** | Sorted Ints | 1.1663 s | 478.96 us | 1.1658 s | 1.1668 s | OK |
| **Merge Sort** | Sorted Ints | 1.6682 s | 7.042 ms | 1.6620 s | 1.6759 s | OK |
| Insertion Sort | Sorted Ints | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Sorted Ints | 2.0856 s | 59.095 ms | 2.0186 s | 2.1305 s | OK |
| **Timsort (built-in)** | Reverse Sorted | 2.106 ms | 129.29 us | 1.990 ms | 2.245 ms | OK |
| **Timsort (custom)** | Reverse Sorted | 1.9262 s | 8.831 ms | 1.9176 s | 1.9353 s | OK |
| **Merge Sort** | Reverse Sorted | 1.6702 s | 1.303 ms | 1.6690 s | 1.6716 s | OK |
| Insertion Sort | Reverse Sorted | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Reverse Sorted | 2.1106 s | 59.600 ms | 2.0537 s | 2.1726 s | OK |
| **Timsort (built-in)** | Almost Sorted | 20.759 ms | 573.02 us | 20.210 ms | 21.353 ms | OK |
| **Timsort (custom)** | Almost Sorted | 1.4581 s | 707.05 us | 1.4573 s | 1.4586 s | OK |
| **Merge Sort** | Almost Sorted | 1.9361 s | 12.146 ms | 1.9258 s | 1.9495 s | OK |
| Insertion Sort | Almost Sorted | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Almost Sorted | 2.0909 s | 22.934 ms | 2.0659 s | 2.1109 s | OK |
| **Timsort (built-in)** | Half Sorted | 58.769 ms | 843.00 us | 58.273 ms | 59.742 ms | OK |
| **Timsort (custom)** | Half Sorted | 1.5741 s | 12.040 ms | 1.5602 s | 1.5811 s | OK |
| **Merge Sort** | Half Sorted | 1.9262 s | 40.273 ms | 1.9007 s | 1.9726 s | OK |
| Insertion Sort | Half Sorted | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Half Sorted | 2.0301 s | 14.297 ms | 2.0146 s | 2.0427 s | OK |
| **Timsort (built-in)** | Flat (Few Unique) | 32.914 ms | 184.66 us | 32.702 ms | 33.041 ms | OK |
| **Timsort (custom)** | Flat (Few Unique) | 1.7240 s | 8.329 ms | 1.7174 s | 1.7333 s | OK |
| **Merge Sort** | Flat (Few Unique) | 1.9765 s | 999.64 us | 1.9754 s | 1.9774 s | OK |
| Insertion Sort | Flat (Few Unique) | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Flat (Few Unique) | 163.925 ms | 20.031 ms | 146.518 ms | 185.820 ms | OK |
| **Timsort (built-in)** | Floats | 120.843 ms | 862.04 us | 120.162 ms | 121.812 ms | OK |
| **Timsort (custom)** | Floats | 2.0594 s | 56.939 ms | 2.0216 s | 2.1249 s | OK |
| **Merge Sort** | Floats | 2.2339 s | 48.406 ms | 2.1780 s | 2.2622 s | OK |
| Insertion Sort | Floats | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Floats | 2.2284 s | 11.968 ms | 2.2182 s | 2.2415 s | OK |
| **Timsort (built-in)** | Strings | 181.973 ms | 3.565 ms | 177.912 ms | 184.588 ms | OK |
| **Timsort (custom)** | Strings | 2.2699 s | 36.437 ms | 2.2420 s | 2.3111 s | OK |
| **Merge Sort** | Strings | 2.4068 s | 7.363 ms | 2.4000 s | 2.4146 s | OK |
| Insertion Sort | Strings | — | — | — | — | Skipped (O(n^2) too slow) |
| **Quick Sort** | Strings | 2.4560 s | 47.595 ms | 2.4015 s | 2.4895 s | OK |

---

