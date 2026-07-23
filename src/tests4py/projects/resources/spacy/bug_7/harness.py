import sys

from spacy.util import filter_spans
from spacy.tokens import Doc
from spacy.vocab import Vocab


def main():
    n = int(sys.argv[1])
    a0, a1, b0, b1 = (int(x) for x in sys.argv[2:6])
    doc = Doc(Vocab(), words=[str(i) for i in range(n)])
    spans = [doc[a0:a1], doc[b0:b1]]
    kept = [(s.start, s.end) for s in filter_spans(spans)]
    print(kept)


if __name__ == "__main__":
    main()
