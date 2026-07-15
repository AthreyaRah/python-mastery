def main():
    unique_words = tag_unique_words("the cat sat on the mat the cat ran")
    print(unique_words)


def tag_unique_words(sentence):
    """
    Given a sentence, return a dict mapping each unique word (lowercased)
    to the number of times it appears. Punctuation-free input, assume
    words are separated by single spaces.
    """
    word_counts = {}
    for word in sentence.split():
        key = word.lower()
        word_counts[key] = word_counts.get(key, 0) + 1

    return word_counts


if __name__ == "__main__":
    main()
