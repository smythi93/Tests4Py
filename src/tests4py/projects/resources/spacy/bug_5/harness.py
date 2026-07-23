import sys

from spacy.language import Language
from spacy.vocab import Vocab


def plain_pipe(doc):
    return doc


class PipeWithPipe(object):
    name = "withpipe"

    def __call__(self, doc):
        return doc

    def pipe(self, docs, **kwargs):
        for doc in docs:
            yield doc


def main():
    mode = sys.argv[1]
    text = " ".join(sys.argv[2:]) or "hello world"
    annots = {"cats": {"POSITIVE": 1.0, "NEGATIVE": 0.0}}
    nlp = Language(Vocab())
    if mode == "nopipe":
        nlp.add_pipe(plain_pipe, name="plain")
    elif mode == "withpipe":
        nlp.add_pipe(PipeWithPipe(), name="withpipe")
    try:
        nlp.evaluate([(text, annots)])
        print("RESULT:OK")
    except Exception as e:
        print("RESULT:ERR:" + type(e).__name__)


if __name__ == "__main__":
    main()
