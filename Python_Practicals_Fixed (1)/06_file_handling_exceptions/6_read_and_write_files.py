"""Practical 6 - File handling and exception management."""
from pathlib import Path

BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # works in scripts and Colab/Jupyter
FILE_NAME = BASE_DIR / "sample.txt"


def write_file(path, text):
    # `with` closes the file automatically, even if an error occurs.
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    try:
        write_file(FILE_NAME, "welcome to python lab")
        print(read_file(FILE_NAME))
        # Demonstrate exception handling on a missing file.
        read_file(FILE_NAME.with_name("does_not_exist.txt"))
    except FileNotFoundError as err:
        print("Error: file not found ->", err.filename)
    except PermissionError:
        print("Error: no permission to access the file")
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
