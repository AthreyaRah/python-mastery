import csv


def main():
    print(read_people("people.csv"))


def read_people(file_path):
    final_list = []
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration as e:
            raise ValueError("empty file input with no data") from e
        for row in reader:
            if len(header) != len(row):
                raise ValueError(
                    f"Columns mismatch for rows with values {row} against headers: {header}")
            final_list.append(dict(zip(header, row)))

    return final_list


if __name__ == "__main__":
    main()
