import sys
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

    random_value = all_values[0]
    operator = all_values[1]
    if len(random_value) < 5:
        random_value = int(random_value)
    matcher = Matcher(get_lang_class('en').Defaults.create_vocab())
    pattern = [{'ORTH': random_value}, {'OP': operator}]
    assert len(matcher) == 0
    matcher.add('Rule', None, pattern)
    assert 'Rule' in matcher
    if operator == "-" and random_value is int:
        print("ValueError: [E011] Unknown operator: \'-\'. Options: *, +, ?, 1, !\n' OR ValueError: [E153] The value type int is not supported for token patterns. Please use the option validate=True with Matcher, PhraseMatcher, or EntityRuler for more details.")
    else:
        print(random_value)
