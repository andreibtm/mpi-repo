"""
graph.py - Visualise benchmark results from the CSV output of cli.py

Usage
-----
python graph.py                                          # Random Ints, all algs
python graph.py --shape "Sorted Ints"
python graph.py --category timsort                       # Timsort comparison
python graph.py --algorithms "Quick Sort" "Merge Sort"
python graph.py --save chart.png
python graph.py --compare file1.csv file2.csv --labels "Mac M4" "Windows x86"
"""

import argparse
import sys
from pathlib import Path

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker
except ImportError:
    print("Install dependencies:  pip install pandas matplotlib")
    sys.exit(1)

ALG_COLORS = {
    "Timsort (built-in)":  "#2ecc71",
    "Timsort (custom)":    "#27ae60",
    "Heap Sort":           "#3498db",
    "Radix Sort":          "#9b59b6",
    "Counting Sort":       "#8e44ad",
    "Quick Sort":          "#e67e22",
    "Merge Sort":          "#e74c3c",
    "Shell Sort":          "#1abc9c",
    "Insertion Sort":      "#f39c12",
    "Selection Sort":      "#95a5a6",
    "Bubble Sort":         "#c0392b",
    "LL Merge Sort":       "#16a085",
    "LL Insertion Sort":   "#d35400",
    "Parallel Merge Sort": "#2980b9",
}

TIMSORT_ALGS = ["Timsort (built-in)", "Timsort (custom)", "Merge Sort",
                "Insertion Sort", "Quick Sort"]


def load(csv_path):
    df = pd.read_csv(csv_path)
    df = df[df["Status"] == "Success"].copy()
    df["Avg (ns)"] = pd.to_numeric(df["Avg (ns)"], errors="coerce")
    df["Avg (s)"]  = pd.to_numeric(df["Avg (s)"],  errors="coerce")
    return df.dropna(subset=["Avg (ns)"])


def fmt_x(x, _):
    if x >= 1_000_000: return f"{int(x/1_000_000)}M"
    if x >= 1_000:     return f"{int(x/1_000)}K"
    return str(int(x))


def fmt_y_ns(y, _):
    """Format Y axis in the most readable unit for the visible range."""
    if y >= 1_000_000_000: return f"{y/1_000_000_000:.1f}s"
    if y >= 1_000_000:     return f"{y/1_000_000:.0f}ms"
    if y >= 1_000:         return f"{y/1_000:.0f}us"
    return f"{y:.0f}ns"


def plot_shape(df, shape, algorithms, save_path=None, title_suffix=""):
    sub = df[df["Data Shape"] == shape]
    if algorithms:
        sub = sub[sub["Algorithm"].isin(algorithms)]
    if sub.empty:
        print(f"No data for shape='{shape}'")
        return

    fig, ax = plt.subplots(figsize=(12, 7))
    for alg, grp in sub.groupby("Algorithm"):
        grp = grp.sort_values("Size")
        ax.plot(grp["Size"], grp["Avg (ns)"],
                marker="o", label=alg,
                color=ALG_COLORS.get(alg, "#888888"),
                linewidth=2, markersize=5)

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Input size (n)", fontsize=12)
    ax.set_ylabel("Average time (log scale)", fontsize=12)
    ax.set_title(f"Sorting Algorithms — {shape}{title_suffix}",
                 fontsize=14, fontweight="bold")
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(fmt_x))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(fmt_y_ns))
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, which="both", linestyle="--", alpha=0.4)
    fig.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=150)
        print(f"Saved: {save_path}")
    else:
        plt.show()
    plt.close()


def plot_timsort_comparison(df, save_path=None):
    """
    Special panel comparing built-in Timsort vs custom Timsort vs competitors
    across all data shapes.
    """
    shapes = ["Random Ints", "Sorted Ints", "Reverse Sorted",
              "Almost Sorted", "Flat (Few Unique)", "Half Sorted"]
    algs   = TIMSORT_ALGS

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    axes = axes.flatten()

    for i, shape in enumerate(shapes):
        ax = axes[i]
        sub = df[(df["Data Shape"] == shape) & (df["Algorithm"].isin(algs))]
        for alg, grp in sub.groupby("Algorithm"):
            grp = grp.sort_values("Size")
            style = "--" if alg == "Timsort (custom)" else "-"
            lw    = 2.5 if "Timsort" in alg else 1.5
            ax.plot(grp["Size"], grp["Avg (ns)"],
                    marker="o", label=alg,
                    color=ALG_COLORS.get(alg, "#888"),
                    linestyle=style, linewidth=lw, markersize=4)
        ax.set_xscale("log"); ax.set_yscale("log")
        ax.set_title(shape, fontsize=11, fontweight="bold")
        ax.set_xlabel("n"); ax.set_ylabel("Time")
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(fmt_x))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(fmt_y_ns))
        ax.grid(True, which="both", linestyle="--", alpha=0.4)
        if i == 0:
            ax.legend(fontsize=8)

    fig.suptitle(
        "Timsort (built-in) vs Timsort (custom) vs Competitors — All Shapes",
        fontsize=14, fontweight="bold"
    )
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150); print(f"Saved: {save_path}")
    else:
        plt.show()
    plt.close()


def plot_compare_machines(csv1, csv2, label1, label2, shape, algorithms, save_path=None):
    """Compare two CSVs (e.g. Mac vs Windows) side by side."""
    df1 = load(csv1); df1["Machine"] = label1
    df2 = load(csv2); df2["Machine"] = label2
    df  = pd.concat([df1, df2])

    if algorithms:
        df = df[df["Algorithm"].isin(algorithms)]

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    for ax, machine in zip(axes, [label1, label2]):
        sub = df[(df["Machine"] == machine) & (df["Data Shape"] == shape)]
        for alg, grp in sub.groupby("Algorithm"):
            grp = grp.sort_values("Size")
            ax.plot(grp["Size"], grp["Avg (ns)"],
                    marker="o", label=alg,
                    color=ALG_COLORS.get(alg, "#888"),
                    linewidth=2, markersize=5)
        ax.set_xscale("log"); ax.set_yscale("log")
        ax.set_title(machine, fontsize=12, fontweight="bold")
        ax.set_xlabel("n"); ax.set_ylabel("Time")
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(fmt_x))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(fmt_y_ns))
        ax.legend(fontsize=9)
        ax.grid(True, which="both", linestyle="--", alpha=0.4)

    fig.suptitle(f"{label1} vs {label2} — {shape}", fontsize=13, fontweight="bold")
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150); print(f"Saved: {save_path}")
    else:
        plt.show()
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Plot benchmark results.")
    parser.add_argument("--input",      default="benchmark_results.csv")
    parser.add_argument("--shape",      default="Random Ints")
    parser.add_argument("--algorithms", nargs="+", default=None)
    parser.add_argument("--category",   choices=["timsort"], default=None)
    parser.add_argument("--save",       default=None)
    parser.add_argument("--compare",    nargs=2, default=None,
                        metavar=("FILE1", "FILE2"),
                        help="Compare two CSV files side by side.")
    parser.add_argument("--labels",     nargs=2, default=["Machine 1", "Machine 2"])
    args = parser.parse_args()

    if args.compare:
        plot_compare_machines(
            args.compare[0], args.compare[1],
            args.labels[0],  args.labels[1],
            args.shape, args.algorithms, args.save
        )
        return

    if not Path(args.input).exists():
        print(f"File not found: {args.input}")
        print("Run `python cli.py` first.")
        sys.exit(1)

    df = load(args.input)
    print(f"Shapes available: {sorted(df['Data Shape'].unique())}")
    print(f"Algorithms: {sorted(df['Algorithm'].unique())}")

    if args.category == "timsort":
        plot_timsort_comparison(df, args.save)
    else:
        plot_shape(df, args.shape, args.algorithms, args.save)


if __name__ == "__main__":
    main()
