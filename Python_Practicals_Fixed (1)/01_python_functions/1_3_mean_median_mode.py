"""Practical 1.3 - Mean, median and mode."""
from statistics import mean, median, multimode


def main():
    numbers = [10, 20, 30, 40, 50, 20]
    print("Numbers:", numbers)
    print("Mean  :", mean(numbers))
    print("Median:", median(numbers))
    # multimode returns every most-common value, so ties are handled properly.
    print("Mode  :", multimode(numbers))


if __name__ == "__main__":
    main()
