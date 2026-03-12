"""
Command-line interface for sorting algorithm benchmarks.

Features:
  - Compare basic array-based sorting algorithms
  - Compare linked list implementations (sequential access vs array random access)
  - Test parallel multi-core sorting (uses multiprocessing)
  - Supports custom input sizes and data patterns

Examples:
  # Basic comparison: classic algorithms
  python cli.py --algorithms "Bubble Sort" "Quick Sort" --sizes 1000 10000 100000

  # All algorithms with default sizes
  python cli.py --algorithms all

  # Linked list comparison: array vs linked structures
  python cli.py --category linked-list --sizes 10000 100000

  # Parallel sorting: single-core vs multi-core (requires large sizes to show benefit)
  python cli.py --category parallel --sizes 100000 1000000 --iterations 2

  # Radix sort and other integer-based algorithms
  python cli.py --algorithms "Radix Sort" "Quick Sort" "Merge Sort" --sizes 50000 500000

  # Custom output file and iterations
  python cli.py --algorithms all --output my_results.md --iterations 3
"""

import argparse
import sys
import time
import copy
from algorithms import ALGORITHMS
from generators import GENERATORS


# Algorithm categories for easy selection
ALGORITHM_CATEGORIES = {
    "basic": [
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Shell Sort",
        "Heap Sort",
        "Merge Sort",
        "Quick Sort",
        "Python Timsort",
    ],
    "integer": [
        "Radix Sort",
        "Merge Sort",
        "Quick Sort",
        "Python Timsort",
    ],
    "linked-list": [
        "LL Merge Sort",
        "LL Insertion Sort",
    ],
    "parallel": [
        "Parallel Merge Sort",
        "Python Timsort",
        "Merge Sort",
    ],
    "comparison": [
        # Array-based algorithms
        "Merge Sort",
        # Linked list equivalents
        "LL Merge Sort",
        # Parallel variant
        "Parallel Merge Sort",
    ],
}


def run_benchmark(sort_function, data, iterations=1):
    """Run benchmark for a sorting algorithm."""
    total_time = 0
    for _ in range(iterations):
        data_copy = copy.deepcopy(data)
        start_time = time.perf_counter()
        sort_function(data_copy)
        end_time = time.perf_counter()
        total_time += (end_time - start_time)
    return total_time / iterations


def benchmark_suite(algorithms, sizes, iterations=1, output_file="benchmark_results.md"):
    """
    Run a complete benchmark suite.
    
    Args:
        algorithms: List of algorithm names to test
        sizes: List of input sizes to test
        iterations: Number of iterations per test
        output_file: Output markdown filename
    """
    print(f"\n📊 Sorting Algorithm Benchmark Suite")
    print(f"   Output: {output_file}")
    print(f"   Algorithms: {len(algorithms)}")
    print(f"   Sizes: {sizes}")
    print(f"   Iterations per test: {iterations}\n")
    
    # Validate algorithms
    available = set(ALGORITHMS.keys())
    for alg in algorithms:
        if alg not in available:
            print(f"❌ Algorithm '{alg}' not found.")
            print(f"   Available: {', '.join(sorted(available))}")
            sys.exit(1)
    
    with open(output_file, "w") as md_file:
        md_file.write("# Sorting Algorithm Benchmark Results\n\n")
        
        for size in sizes:
            print(f"🔄 Testing size: {size:,} elements...")
            md_file.write(f"## Data Size: {size:,} elements\n")
            md_file.write("| Algorithm | Data Shape | Avg Time (s) | Status |\n")
            md_file.write("| :--- | :--- | :--- | :--- |\n")
            
            for gen_name, generator in GENERATORS.items():
                base_data = generator(size)
                
                for alg_name in algorithms:
                    func, complexity = ALGORITHMS[alg_name]
                    
                    # Safety checks
                    if complexity == "n2" and size > 10000:
                        print(f"   ⏭️  {alg_name:20} | {gen_name:20} → Skipped (too slow)")
                        md_file.write(f"| {alg_name} | {gen_name} | N/A | Skipped (O(n²) too slow) |\n")
                        continue
                    
                    # Parallel algorithms need at least 10K for meaningful results
                    if "parallel" in complexity.lower() and size < 10000:
                        print(f"   ⏭️  {alg_name:20} | {gen_name:20} → Skipped (parallel overhead too high)")
                        md_file.write(f"| {alg_name} | {gen_name} | N/A | Skipped (parallel overhead) |\n")
                        continue
                    
                    try:
                        avg_time = run_benchmark(func, base_data, iterations)
                        print(f"   ✓  {alg_name:20} | {gen_name:20} → {avg_time:.6f}s")
                        md_file.write(f"| **{alg_name}** | {gen_name} | {avg_time:.6f} | Success |\n")
                    except RecursionError:
                        print(f"   ❌ {alg_name:20} | {gen_name:20} → RecursionError")
                        md_file.write(f"| {alg_name} | {gen_name} | Error | RecursionError |\n")
                    except Exception as e:
                        print(f"   ❌ {alg_name:20} | {gen_name:20} → {type(e).__name__}")
                        md_file.write(f"| {alg_name} | {gen_name} | Error | {type(e).__name__} |\n")
            
            md_file.write("\n---\n\n")
    
    print(f"\n✅ Done! Results saved to: {output_file}\n")



def main():
    parser = argparse.ArgumentParser(
        description="Benchmark sorting algorithms with different input sizes and types.",
        epilog="Categories:\n"
               "  basic       - Classic array-based algorithms (8 algorithms)\n"
               "  integer     - Optimized for integers: Radix Sort and comparison sorts\n"
               "  linked-list - Linked list variants: LL Merge Sort, LL Insertion Sort\n"
               "  parallel    - Multi-core variants using multiprocessing\n"
               "  comparison  - Compare Array vs LL vs Parallel Merge Sort\n\n"
               "Examples:\n"
               "  python cli.py --algorithms 'Bubble Sort' 'Quick Sort' --sizes 1000 10000\n"
               "  python cli.py --category linked-list --sizes 10000 100000\n"
               "  python cli.py --category parallel --sizes 100000 1000000",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--algorithms",
        nargs="+",
        default=None,
        help="Specific algorithm names. Use 'all' for all algorithms. "
             "Available: " + ", ".join(sorted(ALGORITHMS.keys()))
    )
    
    parser.add_argument(
        "--category",
        type=str,
        default=None,
        choices=list(ALGORITHM_CATEGORIES.keys()),
        help="Algorithm category preset (overrides --algorithms if both specified)"
    )
    
    parser.add_argument(
        "--sizes",
        type=int,
        nargs="+",
        default=[50, 1000, 10000, 100000, 1000000],
        help="Input sizes to test (default: 50 1000 10000 100000 1000000)"
    )
    
    parser.add_argument(
        "--iterations",
        type=int,
        default=1,
        help="Number of iterations per test (default: 1)"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default="benchmark_results.md",
        help="Output markdown filename (default: benchmark_results.md)"
    )
    
    args = parser.parse_args()
    
    # Resolve algorithms
    if args.category:
        algorithms = ALGORITHM_CATEGORIES[args.category]
        print(f"📁 Using category '{args.category}': {len(algorithms)} algorithms")
    elif args.algorithms and args.algorithms != ["all"]:
        algorithms = args.algorithms
    else:
        algorithms = sorted(ALGORITHMS.keys())
    
    # Set recursion limit for deep sorts
    sys.setrecursionlimit(20000)
    
    # Run benchmark
    benchmark_suite(
        algorithms=algorithms,
        sizes=sorted(set(args.sizes)),  # Remove duplicates and sort
        iterations=args.iterations,
        output_file=args.output
    )


if __name__ == "__main__":
    main()
