import sys

import spacy.errors as errs


def main():
    cls_name = sys.argv[1]
    code = sys.argv[2]
    cls = getattr(errs, cls_name)
    try:
        value = getattr(cls, code)
    except Exception as e:
        print("ERR " + type(e).__name__)
        return
    print(value)


if __name__ == "__main__":
    main()
