"""Data generators for sorting algorithm benchmarks."""

import random
import string


def generate_random_ints(n):
    """Generate n random integers."""
    return [random.randint(0, n * 10) for _ in range(n)]


def generate_sorted_ints(n):
    """Generate n integers in ascending order."""
    return list(range(n))


def generate_reverse_sorted_ints(n):
    """Generate n integers in descending order."""
    return list(range(n, 0, -1))


def generate_almost_sorted(n, randomness=0.02):
    """Generate nearly sorted array — 98% sorted, 2% randomly swapped."""
    arr = list(range(n))
    num_swaps = max(1, int(n * randomness))
    for _ in range(num_swaps):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def generate_half_sorted(n):
    """First half is sorted, second half is random."""
    sorted_half = list(range(n // 2))
    random_half = [random.randint(0, n) for _ in range(n - n // 2)]
    return sorted_half + random_half


def generate_flat_ints(n):
    """Generate array with very few unique values (high duplicates)."""
    return [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]


def generate_floats(n):
    """Generate n random floats."""
    return [random.uniform(0.0, 1000.0) for _ in range(n)]


def generate_strings(n):
    """Generate n random 5-character lowercase strings."""
    return [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(n)]


# Registry — all generators available to the benchmark system.
# Note: Floats and Strings are excluded from integer-only algorithms (e.g. Radix Sort)
# via skip logic in the benchmark runner.
GENERATORS = {
    "Random Ints":       generate_random_ints,
    "Sorted Ints":       generate_sorted_ints,
    "Reverse Sorted":    generate_reverse_sorted_ints,
    "Almost Sorted":     generate_almost_sorted,
    "Half Sorted":       generate_half_sorted,
    "Flat (Few Unique)": generate_flat_ints,
    "Floats":            generate_floats,
    "Strings":           generate_strings,
}
