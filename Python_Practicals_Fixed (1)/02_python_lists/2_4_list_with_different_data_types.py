"""Practical 2.4 - A list holding different data types."""


def main():
    sample_list = [1, 2, "python", True]
    print(sample_list)
    for item in sample_list:
        print(f"{item!r:10} -> {type(item).__name__}")


if __name__ == "__main__":
    main()
