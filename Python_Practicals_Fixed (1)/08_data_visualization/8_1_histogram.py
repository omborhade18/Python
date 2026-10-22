"""Practical 8.1 - Histogram."""
import matplotlib.pyplot as plt


def main():
    # Original had the marks as strings ('40', '50'...) - they must be numbers.
    marks = [40, 50, 60, 70, 80, 90]
    plt.hist(marks, bins=5, edgecolor="black")
    plt.title("Histogram")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()


if __name__ == "__main__":
    main()
