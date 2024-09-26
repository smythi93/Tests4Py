import sys
from spacy.language import Language
from spacy.lang.en import English

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


    class MyComponent:
        name = all_values[0]

        def __init__(self, nlp, **cfg):
            self.nlp = nlp
            self.categories = cfg.get('categories', 'all_categories')

        def __call__(self, doc):
            pass

        def to_disk(self, path, **kwargs):
            pass

        def from_disk(self, path, **cfg):
            pass


    Language.factories[all_values[0]] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
    nlp = English()
    nlp.add_pipe(nlp.create_pipe(all_values[1]))
    if nlp.get_pipe(all_values[1]).categories == 'all_categories':
        print(all_values[0])
    else:
        print(all_values[1])
