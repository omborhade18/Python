"""Practical 3.4 - Sort a list of tuples by the float value of the 2nd element."""


def main():
    price = [("item1", "12.20"), ("item2", "15.10"), ("item3", "24.5")]
    # Strings sort alphabetically ("24.5" > "15.10" only by luck), so convert to float.
    price.sort(key=lambda x: float(x[1]), reverse=True)
    print(price)
    # -> [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]


if __name__ == "__main__":
    main()
