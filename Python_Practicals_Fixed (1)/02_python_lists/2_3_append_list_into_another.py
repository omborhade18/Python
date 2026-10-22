"""Practical 2.3 - Append one list into another."""


def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)  # adds every element of list2 to list1
    print("Combined list =", list1)

    # Difference between append and extend:
    a = [1, 2, 3]
    a.append([4, 5, 6])
    print("Using append  =", a, "(nested list)")


if __name__ == "__main__":
    main()
