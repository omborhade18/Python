"""Practical 7.1 - NumPy array operations."""
import numpy as np


def main():
    array1 = np.array([10, 20, 30, 40])
    array2 = np.array([[1, 2], [3, 4]])

    print("1D Array:", array1)
    print("2D Array:\n", array2)
    print("Maximum:", np.max(array2))
    print("Minimum:", np.min(array2))
    # np.sort returns a sorted copy; the original array is unchanged.
    print("Sorted Array:", np.sort(array1))
    print("Sum of columns:", array2.sum(axis=0))
    print("Mean:", array1.mean())


if __name__ == "__main__":
    main()
