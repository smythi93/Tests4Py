import sys
import spacy
import pytest
from spacy.language import Language, component

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

    spacy.language.ENABLE_PIPELINE_ANALYSIS = True
    random_value1 = all_values[0]
    random_value2 = all_values[1]
    assertion_criteria = all_values[2]

    @component(random_value1, assigns=['token.tag'])
    def c1(doc):
        return doc


    @component(random_value2, requires=['token.pos'])
    def c2(doc):
        return doc


    nlp = Language()
    nlp.add_pipe(c1)
    with pytest.warns(UserWarning):
        nlp.add_pipe(c2)
    with pytest.warns(None) as record:
        nlp.remove_pipe(random_value2)
    if assertion_criteria == "1":
        assert record.list
        print(random_value1)
    elif assertion_criteria == "0":
        assert not record.list
        print("AssertionError: assert not record.list")
    else:
        print("Incorrect Input")
