"""Practical 1.2 - Numbers divisible by 7 but not a multiple of 5 in a range."""


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Invalid input - please enter a whole number.")


def display_numbers(x, y):
    """Print numbers in [x, y] divisible by 7 but NOT by 5."""
    found = []
    for i in range(x, y + 1):
        # Original had `i % 5 == 0`, which selects multiples of 5 - the opposite
        # of what the aim says. It must be `!= 0`.
        if i % 7 == 0 and i % 5 != 0:
            found.append(i)
    if found:
        print(*found)
    else:
        print("No such numbers in the given range.")
    return found


def main():
    start = read_int("Enter starting range: ")
    end = read_int("Enter ending range: ")
    if start > end:
        start, end = end, start
        print(f"(Range swapped to {start}..{end})")
    display_numbers(start, end)


if __name__ == "__main__":
    main()
