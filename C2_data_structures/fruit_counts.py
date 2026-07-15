def main():
    data = [("apple", 3), ("banana", 5), ("apple", 7)]
    print(latest_counts(data))


def latest_counts(data):
    counts = {}
    for key, value in data:
        if key not in counts:
            counts[key] = value
    return counts


if __name__ == "__main__":
    main()
