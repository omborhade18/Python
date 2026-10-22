"""Practical 4 - Control structures and functional abstraction: grade calculator."""


def calculate_grade(marks):
    """Convert marks (0-100) into a grade."""
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    return "Fail"


def read_int(prompt, low=None, high=None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Invalid input - please enter a whole number.")
            continue
        if (low is not None and value < low) or (high is not None and value > high):
            print(f"  Value must be between {low} and {high}.")
            continue
        return value


def main():
    # Original assigned to `student` but looped over `students` -> NameError.
    students = read_int("Enter no. of students: ", low=1)
    for i in range(1, students + 1):
        marks = read_int(f"Enter marks of student {i} (0-100): ", 0, 100)
        print("Grade:", calculate_grade(marks))


if __name__ == "__main__":
    main()
