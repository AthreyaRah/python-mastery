def main():
    # print(load_config_value("nope.txt"))
    print(load_config_value("test_input2.txt"))
    # print(load_config_value("test_input.txt"))


def load_config_value(filepath):
    try:
        with open(filepath) as f:
            try:
                value = int(f.read())
            except ValueError as e:
                raise ValueError(
                    "Invalid input for integer in the file") from e
    except TypeError as e:
        raise TypeError("Open expects a valid filepath as string") from e
    except FileNotFoundError as e:
        raise FileNotFoundError(
            "Invalid file or file not found in path specified") from e
    return value


if __name__ == "__main__":
    main()
