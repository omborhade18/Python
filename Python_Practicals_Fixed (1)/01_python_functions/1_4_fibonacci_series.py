"""Practical 1.4 - Fibonacci series."""


def fibonacci(n):
    """Print the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        # Original did `a = b; a = b; a = c` and never updated b -> wrong series.
        a, b = b, a + b
    print()


def main():
    while True:
        try:
            num = int(input("Enter no.: "))
            if num < 0:
                raise ValueError
            break
        except ValueError:
            print("  Please enter a non-negative whole number.")
    fibonacci(num)


if __name__ == "__main__":
    main()
