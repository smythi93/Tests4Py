import sys
import pytest
from spacy.language import Language
from spacy.lookups import Lookups

if __name__ == "__main__":
    assert (len(sys.argv) == 2) or (len(sys.argv) == 3)
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    if (len(all_values) == 2) and (all_values[1] == "UserWarning"):
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table(all_values[0])
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list
            print("Pytest Warning is not raised.")
    elif len(all_values) == 1:
        nlp = Language()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe('tagger')
        tagger.begin_training()
        nlp.add_pipe(tagger)
        nlp.begin_training()
        nlp.vocab.lookups.add_table(all_values[0])
        with pytest.warns(None) as record:
            nlp.begin_training()
            assert not record.list
        print(all_values[0])
    else:
        print("Something is wrong, index out of range!!!")
