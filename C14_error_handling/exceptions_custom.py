def main():
    # print(load_config_value("nope.txt"))
    # print(load_config_value("test_input2.txt"))
    # print(load_config_value("test_input.txt"))
    print(load_config_value(123))


class ConfigError(Exception):
    pass


class ConfigNotFoundError(ConfigError):
    pass


class ConfigTypeError(ConfigError):
    pass


class ConfigParseError(ConfigError):
    pass


def load_config_value(filepath):
    try:
        with open(filepath) as f:
            try:
                value = int(f.read())
            except ValueError as e:
                raise ConfigParseError(
                    "Invalid input for integer in the file") from e
    except TypeError as e:
        raise ConfigTypeError("Open expects a valid filepath as string") from e
    except FileNotFoundError as e:
        raise ConfigNotFoundError(
            "Invalid file or file not found in path specified") from e
    except OSError as e:
        raise ConfigTypeError(
            "Invalid file descriptor    ") from e
    return value


if __name__ == "__main__":
    main()
