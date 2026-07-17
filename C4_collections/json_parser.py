def main():
    print(detect_type('0'))


def detect_type(raw):
    raw_string = raw.strip()
    if not raw_string:
        raise ValueError("Empty String")

    if raw_string[0] == '"':
        return "string"
    elif raw_string == "true" or raw_string == "false":
        return "bool"
    elif raw_string[0] == "{":
        return "object"
    elif raw_string[0] == "[":
        return "array"
    elif raw_string == "null":
        return "null"
    else:
        try:
            int(raw_string)
            return "int"
        except ValueError:
            try:
                float(raw_string)
                return "float"
            except ValueError:
                raise ValueError("Invalid literal for a JSON object")


if __name__ == "__main__":
    main()