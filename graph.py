"""
graph.py — visualise benchmark results from the CSV output of cli.py

Usage
-----
# Plot all algorithms on Random Ints data
python graph.py

# Plot a specific data shape
python graph.py --shape "Reverse Sorted"

# Plot only specific algorithms
python graph.py --algorithms "Quick Sort" "Merge Sort" "Python Timsort"

# Use a custom CSV file
python graph.py --input my_results.csv

# Save to a file instead of showing interactively
python graph.py --save sorting_graph.png
"""

import argparse
import sys
from pathlib import Path

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
except ImportError:
    print("Please install dependencies:  pip install pandas matplotlib")
    sys.exit(1)


def load_results(csv_path):
    df = pd.read_csv(csv_path)
    # Keep only successful rows
    df = df[df["Status"] == "Success"].copy()
    df["Avg Time (s)"] = pd.to_numeric(df["Avg Time (s)"], errors="coerce")
    df = df.dropna(subset=["Avg Time (s)"])
    return df


def plot(df, shape, algorithms, save_path=None):
    df = df[df["Data Shape"] == shape]
    if algorithms:
        df = df[df["Algorithm"].isin(algorithms)]

    if df.empty:
        print(f"No data for shape='{shape}' and selected algorithms.")
        return

    fig, ax = plt.subplots(figsize=(12, 7))

    for alg, group in df.groupby("Algorithm"):
        group = group.sort_values("Size")
        ax.plot(group["Size"], group["Avg Time (s)"],
                marker="o", label=alg, linewidth=2, markersize=5)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Input size (n)", fontsize=12)
    ax.set_ylabel("Average time (seconds)", fontsize=12)
    ax.set_title(f"Sorting Algorithm Comparison — {shape}", fontsize=14, fontweight="bold")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(
        lambda x, _: f"{int(x):,}"
    ))
    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150)
        print(f"Saved to {save_path}")
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(description="Plot benchmark results from CSV.")
    parser.add_argument("--input", default="benchmark_results.csv",
                        help="CSV file produced by cli.py")
    parser.add_argument("--shape", default="Random Ints",
                        help="Data shape to plot (default: 'Random Ints')")
    parser.add_argument("--algorithms", nargs="+", default=None,
                        help="Algorithms to include (default: all)")
    parser.add_argument("--save", default=None,
                        help="Save graph to this filename instead of displaying")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"File not found: {args.input}")
        print("Run `python cli.py` first to generate results.")
        sys.exit(1)

    df = load_results(args.input)
    available_shapes = df["Data Shape"].unique().tolist()
    print(f"Available data shapes: {available_shapes}")
    plot(df, shape=args.shape, algorithms=args.algorithms, save_path=args.save)


if __name__ == "__main__":
    main()
