import json


def load_profile(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data


def main():
    profile = load_profile("data.json")
    print(type(profile))
    print(profile)
    print(type(profile["skills"]))
    print(profile["skills"])


if __name__ == "__main__":
    main()
