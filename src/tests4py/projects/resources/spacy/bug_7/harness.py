import sys
from spacy.util import get_lang_class
from spacy.tests.util import get_doc
from spacy.util import filter_spans

if __name__ == "__main__":
    assert len(sys.argv) == 3
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    text = all_values[0]
    heads = [1, 0, 1, -2, -3, 1, 0, 1, -2, -3, 0, 1, -2, -1]
    deps = ['nsubj', 'ROOT', 'det', 'attr', 'punct', 'nsubj', 'ROOT', 'det', 'attr', 'punct', 'ROOT', 'det', 'npadvmod',
            'punct']
    tokenizer = get_lang_class('en').Defaults.create_tokenizer()
    tokens = tokenizer(text)
    doc = get_doc(tokens.vocab, words=[t.text for t in tokens], heads=heads, deps=deps)
    spans = [doc[1:4], doc[6:8], doc[1:4], doc[10:14]]
    filtered = filter_spans(spans)
    if len(filtered) == int(all_values[1]):
        print(all_values[0])
    else:
        print("Assertion Error, len(filtered) == 3")
