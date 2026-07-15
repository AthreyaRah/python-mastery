def main():
    words = ["data", "", "ml", None, "backend"]
    print(dict_maker(words))


def dict_maker(words):
    return {index: value for index, value in enumerate(words) if value is not None}


if __name__ == "__main__":
    main()
