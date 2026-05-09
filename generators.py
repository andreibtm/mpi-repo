"""Data generators for the sorting benchmark."""

import random
import string


def generate_random_ints(n):
    return [random.randint(0, n * 10) for _ in range(n)]


def generate_sorted_ints(n):
    return list(range(n))


def generate_reverse_sorted_ints(n):
    return list(range(n, 0, -1))


def generate_almost_sorted(n, randomness=0.02):
    """98% sorted: swap 2% of elements randomly."""
    arr = list(range(n))
    num_swaps = max(1, int(n * randomness))
    for _ in range(num_swaps):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def generate_half_sorted(n):
    """First half sorted ascending, second half random."""
    return list(range(n // 2)) + [random.randint(0, n) for _ in range(n - n // 2)]


def generate_flat_ints(n):
    """Only 5 distinct values — very high duplicate rate."""
    return [random.choice([1, 2, 3, 4, 5]) for _ in range(n)]


def generate_floats(n):
    return [random.uniform(0.0, 1_000_000.0) for _ in range(n)]


def generate_strings(n):
    return [''.join(random.choices(string.ascii_lowercase, k=6)) for _ in range(n)]


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
