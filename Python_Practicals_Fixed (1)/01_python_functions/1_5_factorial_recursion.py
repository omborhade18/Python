"""Practical 1.5 - Factorial using recursion."""


def factorial(n):
    """Return n! recursively. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def main():
    while True:
        try:
            num = int(input("Enter no.: "))
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if num < 0:
            print("  Factorial is not defined for negative numbers.")
            continue
        try:
            print("Factorial is =", factorial(num))
        except RecursionError:
            print("  Number too large for recursion.")
        break


if __name__ == "__main__":
    main()
