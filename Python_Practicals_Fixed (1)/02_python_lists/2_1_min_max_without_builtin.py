"""Practical 2.1 - Minimum and maximum of a list without built-in min()/max()."""


def find_min_max(numbers):
    if not numbers:
        raise ValueError("List is empty")
    # Variable names avoid shadowing the built-ins min / max.
    smallest = largest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest


def main():
    numbers = [1, 2, 45, 2, 89, 33]
    smallest, largest = find_min_max(numbers)
    print("Minimum:", smallest)
    print("Maximum:", largest)


if __name__ == "__main__":
    main()
