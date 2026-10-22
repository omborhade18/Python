"""Practical 3.1 - Find repeated items in a tuple."""


def find_repeated(data):
    repeated = []
    for item in data:
        if data.count(item) > 1 and item not in repeated:
            repeated.append(item)
    return repeated


def main():
    tuple_data = (1, 2, 3, 2, 4, 5, 2)
    print("Repeated items:", find_repeated(tuple_data))


if __name__ == "__main__":
    main()
