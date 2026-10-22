"""Practical 8.4 - Correlation matrix using seaborn."""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
    data = {
        "A": [1, 2, 3, 4],
        "B": [4, 3, 2, 1],
        "C": [2, 3, 4, 5],
    }
    df = pd.DataFrame(data)
    print(df.corr())
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation Matrix")
    plt.show()


if __name__ == "__main__":
    main()
