"""Practical 7.2 - Customer data analysis using pandas."""
import pandas as pd


def main():
    data = {
        "Customer": ["A", "B", "C"],
        "Subscription": ["Active", "Inactive", "Active"],
        "Monthly Charge": [500, 700, 450],
    }
    df = pd.DataFrame(data)
    print(df)
    print(df.describe())
    print("\nAverage charge by subscription:")
    print(df.groupby("Subscription")["Monthly Charge"].mean())


if __name__ == "__main__":
    main()
