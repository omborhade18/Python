"""Practical 1.1 - Find the maximum of three numbers."""


def read_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input - please enter a number.")


def max_of_three(a, b, c):
    """Return the largest of a, b and c (without using built-in max)."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c


def main():
    x = read_number("Enter first no.: ")
    y = read_number("Enter second no.: ")
    z = read_number("Enter third no.: ")
    # Original code passed (x, y, y) by mistake - the third argument must be z.
    print("Maximum no. is:", max_of_three(x, y, z))


if __name__ == "__main__":
    main()
