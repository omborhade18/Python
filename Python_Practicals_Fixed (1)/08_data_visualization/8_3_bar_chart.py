"""Practical 8.3 - Bar chart."""
import matplotlib.pyplot as plt


def main():
    subjects = ["Python", "DBMS", "AI"]
    marks = [85, 78, 92]
    # Original called plt.bar(Subject, marks) - `Subject` was undefined (NameError).
    plt.bar(subjects, marks)
    plt.title("Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.show()


if __name__ == "__main__":
    main()
