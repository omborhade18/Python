"""Practical 2.2 - Remove duplicates from a list (keeping original order)."""


def remove_duplicates(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


def main():
    numbers = [1, 2, 3, 2, 4, 1, 5]
    print("Original list:", numbers)
    print("List after removing duplicates:", remove_duplicates(numbers))
    # One-liner alternative (Python 3.7+ keeps insertion order):
    print("Using dict.fromkeys:", list(dict.fromkeys(numbers)))


if __name__ == "__main__":
    main()
