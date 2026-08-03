def main():
    print(count_lines("test_lines.txt"))
    print(count_lines_elegant("empty_file.txt"))


def count_lines(file_path):
    line_count = 0
    with open(file_path, "r") as f:
        for line in f:
            line_count += 1
    return line_count


def count_lines_elegant(file_path):
    with open(file_path, "r") as f:
        line_count = sum(1 for line in f)
    return line_count


if __name__ == "__main__":
    main()
