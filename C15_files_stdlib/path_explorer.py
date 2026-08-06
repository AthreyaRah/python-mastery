from pathlib import Path


def main():
    explore_path(
        "/Users/athreya/Documents/0.Claude_Mentor/python-mastery/C15_files_stdlib")


def explore_path(filepath):
    filepath = Path(filepath)
    files = filepath.iterdir()
    for file in files:
        if file.is_file():
            print(f"file_name is: {file.name} and suffix is: {file.suffix}")


if __name__ == '__main__':
    main()
