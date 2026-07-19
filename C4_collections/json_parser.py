def main():
    print(split_top_level_pairs('"she said \"hi\"": {"b": [1, {"c": 2}, 3]}, "d": 5'))


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


def split_top_level_pairs(body):
    i = 0
    start = 0
    depth = 0
    inside_string = False
    split_list = []
    while i < len(body):
        if body[i] == '"':
            i+=1
            if not inside_string:
                inside_string = True
            else:
                inside_string = False
        elif body[i] == '\\' and inside_string:
            i+=2
        elif (body[i] == "{" or body[i] == "["):
            i+=1
            depth += 1
        elif (body[i] == "}" or body[i] == "]"):
            i+=1
            depth -= 1
        elif body[i] == ',' and depth == 0 and not inside_string:
            split_list.append(body[start:i])
            start = i+1
            i+=1
        else:
            i+=1
    split_list.append(body[start:])
    return split_list



if __name__ == "__main__":
    main()