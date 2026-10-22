"""Practical 3.3 - Replace the last value of each tuple in a list.

Tuples are immutable, so we build new tuples: everything except the last
element, plus the new value.
"""


def replace_last(tuples, new_value):
    return [t[:-1] + (new_value,) for t in tuples]


def main():
    lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    print("Original:", lst)
    print("Result  :", replace_last(lst, 100))
    # -> [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


if __name__ == "__main__":
    main()
