import sys
import pytest
from spacy.matcher import Matcher
from spacy.util import get_lang_class

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

    matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
    with pytest.raises(ValueError):
        matcher.add(all_values[0], [], [{all_values[1]: 'test'}])
        print(all_values[0])
