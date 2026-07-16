from collections import namedtuple


def main():
    Point = namedtuple("Point", ["x", "y"])
    p = Point(3, 4)
    print(f"p.x:{p.x} and p.y:{p.y}")
    print(f"p[0]:{p[0]} and p[1]:{p[1]}")


if __name__ == "__main__":
    main()
