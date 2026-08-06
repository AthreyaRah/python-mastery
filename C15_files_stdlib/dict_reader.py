import csv
import json
import logging
from datetime import datetime
import time


def main():
    logging.basicConfig(level=logging.WARNING, filename="app.log")
    start = time.time()
    final_json_array = list(read_people("people.csv"))
    end = time.time()
    # csv_to_json("people.csv", "people.json")
    print(f"took {end-start} seconds")


def read_people(file_path):
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration as e:
            raise ValueError("empty file input with no data") from e
        for row in reader:
            if len(header) != len(row):
                logging.warning(
                    f"Columns mismatch for rows with values {row} against headers: {header}")
                continue
            people_dict = dict(zip(header, row))
            try:
                people_dict["date_joined"] = datetime.strptime(people_dict["date_joined"],
                                                               "%d-%m-%Y")
            except ValueError:
                logging.warning(
                    f"invalid value for date: {people_dict['date_joined']}")
                continue
            yield people_dict


def csv_to_json(csv_filepath, json_filepath):
    csv_data = list(read_people(csv_filepath))
    for item in csv_data:
        item["years_experience"] = int(item["years_experience"])
    with open(json_filepath, 'w') as jf:
        json.dump(csv_data, jf)


# def dict_reader_testing(file_path):
#     with open(file_path, 'r') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             yield row


if __name__ == "__main__":
    main()

# gen = read_people("people.csv")
# first_row = next(gen)
# print(first_row)
# print("did we get here without finishing the loop")
