def main():
    words = ["a", "b", "c"]
    it = iter(words)
    print(next(it))
    print(next(it))
    print(next(it))
    # print(next(it))

    words = ["a", "b", "c"]
    for x in words:
        print(x)
    for x in words:
        print(x)


if __name__ == "__main__":
    main()
