def add_many_points(points_set, *args):
    for point in args:
        points_set.add(point)


def main():
    points = set()
    add_many_points(points, (0, 0), (1, 1), (2, 2),
                    (1, 1), (2, 2), (3, 3), (4, 5))
    print(points)


if __name__ == "__main__":
    main()
