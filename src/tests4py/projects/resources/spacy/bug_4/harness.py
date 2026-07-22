import sys

from spacy.cli.converters.conllu2json import read_conllx


def main():
    heads = sys.argv[1:]
    rows = []
    for i, h in enumerate(heads):
        cols = [str(i + 1), "w%d" % i, "_", "NOUN", "NN", "_", h, "dep", "_", "_"]
        rows.append("\t".join(cols))
    text = "\n".join(rows)
    try:
        result = list(read_conllx(text))
        print("PARSED_OK" if result else "PARSED_EMPTY")
    except Exception as e:
        print("PARSE_ERROR:" + type(e).__name__)


if __name__ == "__main__":
    main()
