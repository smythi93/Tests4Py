import sys

from spacy.errors import add_codes


def main():
    mode = sys.argv[1]
    if mode == "dunder":
        attr = sys.argv[2]
        wrapped = add_codes(type("Errors", (object,), {"E001": "message"}))
        value = getattr(wrapped, attr)
        if isinstance(value, str) and value.startswith("[" + attr + "]"):
            print("WRAPPED")
        else:
            print("GENUINE")
    elif mode == "code":
        code = sys.argv[2]
        message = " ".join(sys.argv[3:])
        wrapped = add_codes(type("Errors", (object,), {code: message}))
        print(getattr(wrapped, code))


if __name__ == "__main__":
    main()
