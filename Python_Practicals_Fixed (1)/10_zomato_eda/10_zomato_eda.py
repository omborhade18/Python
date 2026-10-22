"""Practical 10 - Exploratory data analysis and visualization on the Zomato dataset.

Objectives
  * Understand restaurant trends
  * Analyse rating and online delivery
  * Visualise restaurant distribution

Put Zomato.csv next to this script. If it is missing, a small synthetic dataset
is generated so the script still runs end to end.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # works in scripts and Colab/Jupyter
CSV_PATH = BASE_DIR / "Zomato.csv"


def load_data(path=CSV_PATH):
    if path.exists():
        return pd.read_csv(path)
    print(f"[note] {path.name} not found - using generated sample data.\n")
    rng = np.random.default_rng(42)
    n = 300
    return pd.DataFrame({
        "name": [f"Restaurant {i}" for i in range(n)],
        "online_order": rng.choice(["Yes", "No"], n, p=[0.6, 0.4]),
        "rate": [f"{r:.1f}/5" for r in rng.normal(3.7, 0.4, n).clip(1, 5)],
        "votes": rng.integers(0, 2000, n),
    })


def clean_rating(series):
    """Zomato ratings look like '4.1/5', 'NEW' or '-'. Convert to float (NaN if invalid)."""
    return pd.to_numeric(series.astype(str).str.split("/").str[0].str.strip(), errors="coerce")


def main():
    zomato = load_data()
    print(zomato.head())
    zomato.info()

    # The original plotted Zomato['rate'] directly; it is text ('4.1/5'), so clean it first.
    zomato["rate"] = clean_rating(zomato["rate"])
    print("\nMissing ratings:", zomato["rate"].isna().sum())

    plt.figure(figsize=(7, 4))
    sns.histplot(zomato["rate"].dropna(), bins=20, kde=True)
    plt.title("Distribution of restaurant ratings")
    plt.xlabel("Rating")
    plt.show()

    plt.figure(figsize=(5, 4))
    sns.countplot(x="online_order", data=zomato)
    plt.title("Restaurants offering online ordering")
    plt.show()

    print("\nAverage rating by online order:")
    print(zomato.groupby("online_order")["rate"].mean().round(2))


if __name__ == "__main__":
    main()
