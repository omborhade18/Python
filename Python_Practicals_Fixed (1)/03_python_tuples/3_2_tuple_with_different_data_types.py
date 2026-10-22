"""Practical 3.2 - A tuple holding different data types."""


def main():
    sample_tuple = (1, 2, "Python", False)
    print(sample_tuple)
    for item in sample_tuple:
        print(f"{item!r:10} -> {type(item).__name__}")


if __name__ == "__main__":
    main()
