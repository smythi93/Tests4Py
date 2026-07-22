import sys
import warnings

import spacy.language
from spacy.language import Language, component

spacy.language.ENABLE_PIPELINE_ANALYSIS = True


@component("c1", assigns=["token.tag"])
def c1(doc):
    return doc


@component("c2", requires=["token.pos"])
def c2(doc):
    return doc


@component("c3", requires=["token.tag"])
def c3(doc):
    return doc


def main():
    mode = sys.argv[1]
    nlp = Language()
    nlp.add_pipe(c1)
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        nlp.add_pipe(c2 if mode == "unsat" else c3)
    with warnings.catch_warnings(record=True) as rec:
        warnings.simplefilter("always")
        nlp.remove_pipe("c2" if mode == "unsat" else "c3")
    warned = any(
        "requires" in str(w.message) and "to be assigned" in str(w.message)
        for w in rec
    )
    print("RESULT:WARN" if warned else "RESULT:NOWARN")


if __name__ == "__main__":
    main()
