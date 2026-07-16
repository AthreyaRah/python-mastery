from collections import defaultdict


def main():
    inp = "This is a string input to group words by their lengths"
    print(group_by_length(inp.split()))


def group_by_length(words):
    grouped_words = defaultdict(list)
    for word in words:
        grouped_words[len(word)].append(word)

    return grouped_words


if __name__ == "__main__":
    main()
