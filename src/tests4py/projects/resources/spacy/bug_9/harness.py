import sys
import pytest
from spacy.lang.en import English
from spacy.lookups import Lookups

if __name__ == "__main__":
    assert len(sys.argv) == 4
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

        text = all_values[0]

    if all_values[2] == "1":
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe(all_values[1])
        print(all_values[0])
    else:
        nlp = English()
        nlp.vocab.lookups = Lookups()
        assert not len(nlp.vocab.lookups)
        tagger = nlp.create_pipe(all_values[0])
        with pytest.warns(UserWarning):
            tagger.begin_training()
        nlp.add_pipe(tagger)
        with pytest.warns(UserWarning):
            nlp.begin_training()
        nlp.vocab.lookups.add_table('lemma_lookup')
        with None as record:
            nlp.begin_training()
            assert not record.list
        print(all_values[0])
