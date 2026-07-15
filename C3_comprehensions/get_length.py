def main():
    words = ["data", "", "ml", None, "backend"]
    print(get_lengths(words))
    print(word_indexer(words))


def get_lengths(words):
    return [len(word) if word is not None else None for word in words]


def word_indexer(words):
    return [f"{index}: {value}" for index, value in enumerate(words)]


if __name__ == "__main__":
    main()
