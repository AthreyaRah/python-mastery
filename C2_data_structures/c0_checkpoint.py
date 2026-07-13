def main():
    count_down(5)


def count_down(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff")


if __name__ == '__main__':
    main()


s = "data_engineering"
print(s[len(s)-1::-1])
print(s[::-1])

print(slice(None, None, -1).indices(len(s)))