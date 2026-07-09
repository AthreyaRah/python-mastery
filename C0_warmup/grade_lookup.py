PASSING_MARKS = 40


def main():
    scores = {"Adam": 65, "Dallas": 60, "Anna": 33, "Marie": 95, "Taylor": 42, "Shaun": 30}
    failed_student = find_first_failing(scores)
    if failed_student is not None:
        print(f"{failed_student} has failed the exam")
    else:
        print("All students have passed the exam")


def find_first_failing(scores):
    for name, score in scores.items():
        if score < PASSING_MARKS:
            return name
    return None


if __name__ == "__main__":
    main()