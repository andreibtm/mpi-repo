import re

import matplotlib.pyplot as plt


def parse_benchmark_markdown(md_path, data_shape="Random Ints"):
    """Parse benchmark markdown output into the dict shape expected by plot_results."""
    results_data = {}
    current_size = None

    with open(md_path, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()

            # Capture section headers like: ## Data Size: 1,000 elements or 1000 elements
            size_match = re.match(r"##\s+Data Size:\s+([\d,]+)\s+elements", line)
            if size_match:
                # Remove commas and convert to int
                current_size = int(size_match.group(1).replace(",", ""))
                continue

            # Parse markdown table rows.
            if not line.startswith("|"):
                continue

            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) != 4:
                continue

            algorithm, shape, avg_time, _status = cells

            # Skip header/separator rows.
            if algorithm in {"Algorithm", ":---"}:
                continue

            # Only include the selected data shape and valid numeric times.
            if shape != data_shape:
                continue
            if current_size is None or avg_time in {"N/A", "Error"}:
                continue

            try:
                numeric_time = float(avg_time)
            except ValueError:
                continue

            clean_algorithm = algorithm.replace("**", "")
            bucket = results_data.setdefault(clean_algorithm, {"sizes": [], "times": []})
            bucket["sizes"].append(current_size)
            bucket["times"].append(numeric_time)

    return results_data


def plot_results(results_data, output_path="sorting_graph.png", show_plot=False):
    """
    results_data should look like:
    {
        "Merge Sort": {"sizes": [50, 1000, 10000], "times": [0.001, 0.05, 0.6]},
        "Bubble Sort": {"sizes": [50, 1000, 10000], "times": [0.005, 0.8, 15.0]}
    }
    """
    plt.figure(figsize=(10, 6))

    for alg_name, data in results_data.items():
        plt.plot(data["sizes"], data["times"], marker="o", label=alg_name)

    plt.title("Sorting Algorithm Performance (Random Data)")
    plt.xlabel("Number of Elements (N)")
    plt.ylabel("Time (Seconds)")
    plt.legend()
    plt.grid(True)

    # Use a logarithmic scale for the X-axis so small and large sizes fit nicely.
    plt.xscale("log")

    # Save the plot, and optionally show an interactive window.
    plt.savefig(output_path)
    if show_plot:
        plt.show()
    plt.close()


if __name__ == "__main__":
    import sys
    import os
    
    # Try to find a benchmark markdown file
    default_files = ["benchmark_results.md", "comprehensive_benchmark.md"]
    md_file = None
    
    for filename in default_files:
        if os.path.exists(filename):
            md_file = filename
            break
    
    if not md_file:
        print(f"❌ No benchmark markdown file found. Looked for: {', '.join(default_files)}")
        print("💡 Run: python3 cli.py --output benchmark_results.md")
        sys.exit(1)
    
    print(f"📊 Generating graph from: {md_file}")
    parsed_results = parse_benchmark_markdown(md_file, data_shape="Random Ints")
    
    if not parsed_results:
        print("❌ No data found in markdown file.")
        sys.exit(1)
    
    plot_results(parsed_results)
    print(f"✅ Graph saved to: sorting_graph.png")