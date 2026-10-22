"""Practical 11 - End-to-end data science solution for iPhone sales analysis.

Objectives
  * Understand sales trends
  * Visualise sales performance
  * Generate insights from data

Put iphone-sales.csv (columns: Model, Sales) next to this script. If it is
missing, sample data is generated so the script still runs.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # works in scripts and Colab/Jupyter
CSV_PATH = BASE_DIR / "iphone-sales.csv"


def load_data(path=CSV_PATH):
    if path.exists():
        return pd.read_csv(path)
    print(f"[note] {path.name} not found - using generated sample data.\n")
    return pd.DataFrame({
        "Model": ["iPhone 12", "iPhone 13", "iPhone 14", "iPhone 15", "iPhone 12", "iPhone 13"],
        "Sales": [120, 150, 170, 210, 90, 130],
    })


def main():
    iphone = load_data()
    print(iphone.head())

    # Total sales per model, largest first.
    sales = iphone.groupby("Model")["Sales"].sum().sort_values(ascending=False)
    print("\nTotal sales per model:\n", sales)
    print(f"\nInsight: best seller is {sales.idxmax()} with {sales.max()} units "
          f"({sales.max() / sales.sum():.0%} of all sales).")

    sales.plot(kind="bar")
    plt.title("iPhone Sales Analysis")
    plt.xlabel("Model")
    plt.ylabel("Total sales")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
