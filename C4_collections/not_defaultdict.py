def main():
    inp = "This is a string input to group words by their lengths"
    print(group_by_length(inp.split()))


def group_by_length(words):
    not_defaultdict = {}
    for word in words:
        if len(word) not in not_defaultdict:
            not_defaultdict[len(word)] = [word]
        else:
            not_defaultdict[len(word)].append(word)
    return not_defaultdict


if __name__ == "__main__":
    main()
