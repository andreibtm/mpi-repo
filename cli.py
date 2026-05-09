"""
Sorting Algorithm Benchmark Suite
==================================
Usage examples
--------------
# Full run (all algorithms, all shapes, default sizes)
python cli.py

# Fast algorithms only
python cli.py --category fast --sizes 10000 100000 1000000

# O(n^2) algorithms, small sizes
python cli.py --category slow --sizes 20 30 50 100 1000

# Timsort comparison only
python cli.py --category timsort

# Linked list comparison
python cli.py --category linked --sizes 1000 10000 100000

# Parallel sort
python cli.py --category parallel --sizes 100000 1000000

# Custom
python cli.py --algorithms "Quick Sort" "Merge Sort" --sizes 100000
"""

import argparse
import csv
import sys
import time
import statistics

from algorithms import ALGORITHMS
from generators import GENERATORS

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

INTEGER_ONLY = {"Radix Sort", "Counting Sort"}

# Default sizes and their iteration counts.
# For small n, many iterations are needed because a single sort is too fast
# to measure reliably even with nanosecond resolution.
DEFAULT_SIZES = {
    20:          100_000,
    30:          100_000,
    50:          100_000,
    100:         100_000,
    1_000:       1_000,
    10_000:      100,
    100_000:     10,
    1_000_000:   3,
}

CATEGORIES = {
    "all":     sorted(ALGORITHMS.keys()),
    "fast":    ["Shell Sort", "Heap Sort", "Merge Sort", "Quick Sort",
                "Timsort (built-in)", "Timsort (custom)", "Radix Sort", "Counting Sort"],
    "slow":    ["Bubble Sort", "Selection Sort", "Insertion Sort"],
    "timsort": ["Timsort (built-in)", "Timsort (custom)", "Merge Sort",
                "Insertion Sort", "Quick Sort"],
    "linked":  ["LL Merge Sort", "LL Insertion Sort", "Merge Sort", "Insertion Sort"],
    "parallel":["Parallel Merge Sort", "Timsort (built-in)", "Merge Sort"],
    "integer": ["Radix Sort", "Counting Sort", "Quick Sort", "Merge Sort",
                "Timsort (built-in)", "Timsort (custom)"],
}

# ---------------------------------------------------------------------------
# Skip logic
# ---------------------------------------------------------------------------

def should_skip(alg_name, complexity, gen_name, size):
    """Return a reason string if this combination should be skipped, else None."""
    if complexity == "n2" and size > 10_000:
        return "Skipped (O(n^2) too slow)"
    if complexity == "linked" and size > 500_000:
        return "Skipped (LL overhead too high)"
    if complexity == "parallel" and size < 10_000:
        return "Skipped (parallel overhead dominates)"
    if alg_name in INTEGER_ONLY and gen_name in ("Floats", "Strings"):
        return "Skipped (integers only)"
    # LL Insertion Sort is extremely slow on large sorted/almost-sorted inputs
    if alg_name == "LL Insertion Sort" and size >= 100_000 and gen_name not in ("Reverse Sorted",):
        return "Skipped (LL Insertion Sort too slow at this size)"
    return None

# ---------------------------------------------------------------------------
# Timing
# ---------------------------------------------------------------------------

def run_benchmark(func, generator, size, iterations):
    """
    Run func on `iterations` independently generated arrays of length `size`.

    Timing uses time.perf_counter_ns() (nanosecond resolution) to avoid
    the 0 ns results that occur with second-resolution timers on fast
    algorithms at small sizes. The average time is returned in nanoseconds.

    A fresh array is generated for every iteration so that:
      - Already-sorted algorithms do not benefit from a pre-sorted residue
      - Results reflect the true distribution of inputs, not one fixed sample
    """
    total_ns = 0
    times_ns = []

    for _ in range(iterations):
        data = generator(size)
        t0 = time.perf_counter_ns()
        func(data)
        elapsed = time.perf_counter_ns() - t0
        total_ns += elapsed
        times_ns.append(elapsed)

    avg_ns  = total_ns / iterations
    std_ns  = statistics.stdev(times_ns) if len(times_ns) > 1 else 0
    min_ns  = min(times_ns)
    max_ns  = max(times_ns)

    return avg_ns, std_ns, min_ns, max_ns

# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def fmt_ns(ns):
    """Format nanoseconds into a human-readable string."""
    if ns < 1_000:
        return f"{ns:.1f} ns"
    elif ns < 1_000_000:
        return f"{ns/1_000:.2f} us"
    elif ns < 1_000_000_000:
        return f"{ns/1_000_000:.3f} ms"
    else:
        return f"{ns/1_000_000_000:.4f} s"

def ns_to_s(ns):
    return ns / 1_000_000_000

# ---------------------------------------------------------------------------
# Main benchmark suite
# ---------------------------------------------------------------------------

def benchmark_suite(algorithms, sizes, iterations_override, md_path):
    csv_path = md_path.replace(".md", ".csv")

    print(f"\n  Sorting Benchmark Suite")
    print(f"  Algorithms : {len(algorithms)}")
    print(f"  Sizes      : {sizes}")
    print(f"  Timing     : nanosecond resolution (time.perf_counter_ns)")
    print(f"  Output     : {md_path}  +  {csv_path}\n")

    unknown = [a for a in algorithms if a not in ALGORITHMS]
    if unknown:
        print(f"Unknown algorithms: {unknown}")
        print(f"Available: {sorted(ALGORITHMS.keys())}")
        sys.exit(1)

    with open(md_path, "w") as md, open(csv_path, "w", newline="") as cf:
        writer = csv.writer(cf)
        writer.writerow([
            "Size", "Iterations", "Algorithm", "Data Shape",
            "Avg (ns)", "Avg (s)", "Std (ns)", "Min (ns)", "Max (ns)", "Status"
        ])

        md.write("# Sorting Algorithm Benchmark Results\n\n")
        md.write("> Timing: `time.perf_counter_ns()` — nanosecond resolution\n\n")

        for size in sorted(sizes):
            iters = iterations_override if iterations_override else DEFAULT_SIZES.get(size, 1)
            print(f"  Size {size:>10,}  ({iters:,} iterations each)")

            md.write(f"## Size: {size:,}  x  {iters:,} iterations\n\n")
            md.write("| Algorithm | Data Shape | Avg Time | Std Dev | Min | Max | Status |\n")
            md.write("| :--- | :--- | ---: | ---: | ---: | ---: | :--- |\n")

            for gen_name, generator in GENERATORS.items():
                for alg_name in algorithms:
                    func, complexity = ALGORITHMS[alg_name]

                    reason = should_skip(alg_name, complexity, gen_name, size)
                    if reason:
                        md.write(f"| {alg_name} | {gen_name} | — | — | — | — | {reason} |\n")
                        writer.writerow([size, iters, alg_name, gen_name,
                                         "", "", "", "", "", reason])
                        continue

                    try:
                        avg_ns, std_ns, min_ns, max_ns = run_benchmark(
                            func, generator, size, iters
                        )
                        avg_s = ns_to_s(avg_ns)
                        print(f"    OK  {alg_name:<26} | {gen_name:<20} | {fmt_ns(avg_ns)}")
                        md.write(
                            f"| **{alg_name}** | {gen_name} | {fmt_ns(avg_ns)} | "
                            f"{fmt_ns(std_ns)} | {fmt_ns(min_ns)} | {fmt_ns(max_ns)} | OK |\n"
                        )
                        writer.writerow([
                            size, iters, alg_name, gen_name,
                            f"{avg_ns:.1f}", f"{avg_s:.9f}",
                            f"{std_ns:.1f}", f"{min_ns:.1f}", f"{max_ns:.1f}", "Success"
                        ])
                    except RecursionError:
                        msg = "RecursionError"
                        print(f"    !!  {alg_name:<26} | {gen_name:<20} | {msg}")
                        md.write(f"| {alg_name} | {gen_name} | — | — | — | — | {msg} |\n")
                        writer.writerow([size, iters, alg_name, gen_name,
                                         "", "", "", "", "", msg])
                    except Exception as e:
                        msg = f"{type(e).__name__}: {e}"
                        print(f"    !!  {alg_name:<26} | {gen_name:<20} | {msg}")
                        md.write(f"| {alg_name} | {gen_name} | — | — | — | — | {msg} |\n")
                        writer.writerow([size, iters, alg_name, gen_name,
                                         "", "", "", "", "", msg])

            md.write("\n---\n\n")
            print()

    print(f"  Done!  Results saved to {md_path} and {csv_path}\n")

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Benchmark sorting algorithms with nanosecond precision.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Categories
----------
  all      - every algorithm (default)
  fast     - O(n log n) + non-comparative
  slow     - O(n^2) only
  timsort  - built-in vs custom Timsort + closest competitors
  linked   - linked list vs array equivalents
  parallel - parallel merge sort vs single-core
  integer  - integer-optimised algorithms

Examples
--------
  python cli.py
  python cli.py --category timsort --sizes 1000 10000 100000 1000000
  python cli.py --category slow --sizes 20 30 50 100 1000
  python cli.py --category fast --sizes 100000 1000000
  python cli.py --algorithms "Quick Sort" "Merge Sort" --sizes 10000
        """
    )
    parser.add_argument("--algorithms", nargs="+", default=None)
    parser.add_argument("--category", choices=list(CATEGORIES.keys()), default=None)
    parser.add_argument("--sizes", type=int, nargs="+", default=None)
    parser.add_argument("--iterations", type=int, default=None,
                        help="Override iteration count for all sizes.")
    parser.add_argument("--output", default="benchmark_results.md")
    args = parser.parse_args()

    if args.category:
        algorithms = CATEGORIES[args.category]
    elif args.algorithms:
        algorithms = args.algorithms
    else:
        algorithms = CATEGORIES["all"]

    sizes = sorted(set(args.sizes)) if args.sizes else sorted(DEFAULT_SIZES.keys())

    benchmark_suite(
        algorithms=algorithms,
        sizes=sizes,
        iterations_override=args.iterations,
        md_path=args.output,
    )


if __name__ == "__main__":
    main()
