import sys
import tempfile

import spacy
from spacy.language import Language
from spacy.lang.en import English


class MyComponent(object):
    name = "my_component"

    def __init__(self, nlp, **cfg):
        self.nlp = nlp
        self.categories = cfg.get("categories", "all_categories")

    def __call__(self, doc):
        return doc

    def to_disk(self, path, **kwargs):
        pass

    def from_disk(self, path, **cfg):
        return self


def main():
    override = sys.argv[1]
    Language.factories["my_component"] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
    nlp = English()
    nlp.add_pipe(nlp.create_pipe("my_component"))
    tmpdir = tempfile.mkdtemp()
    nlp.to_disk(tmpdir)
    nlp2 = spacy.load(tmpdir, categories=override)
    print("RESULT:" + str(nlp2.get_pipe("my_component").categories))


if __name__ == "__main__":
    main()
