def main():
    gen = count_up_to(3)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


if __name__ == "__main__":
    main()
