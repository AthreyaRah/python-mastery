def main():
    print(find_matching_end('{"a": {"b": 1}}',0,"{","}"))
    print(find_matching_end('{"x": "\\""}',0,'{','}'))
    print(find_matching_end('{"a": 1',0,'{','}'))


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


def find_matching_end(raw,start,open_char,close_char):
    depth = 1
    inside_string = False
    i = start+1
    while i < len(raw) and depth > 0:
        if raw[i] == '"':
            i+=1
            if inside_string:
                inside_string = False
            else:
                inside_string = True
        elif not inside_string:
            if raw[i] == open_char:
                i+=1
                depth+=1
            elif raw[i] == close_char:
                i+=1
                depth-=1
            else:
                i+=1
        elif raw[i] == '\\' and inside_string:
            i+=2
        else:
            i+=1
    if depth != 0:
        raise ValueError("Unterminated object/array")
    return i


if __name__ == "__main__":
    main()