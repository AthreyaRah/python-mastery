from collections import Counter


def main():
    print(char_frequency_counter(""))
    print("*-*"*25)
    print(Counter("mississippi"))
    print(Counter("sip"))
    print(Counter("mississippi") - Counter("sip"))
    print(Counter("sip") - Counter("mississippi"))


def char_frequency_counter(word):
    result = Counter(word)
    return result


if __name__ == "__main__":
    main()
