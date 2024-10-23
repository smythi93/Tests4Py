import unittest
from spacy.errors import Errors


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(Errors.E124, '[E124] error description')

    def test_diversity_2(self):
        self.assertEqual(Errors.E123, '[E123] error description')

    def test_diversity_3(self):
        self.assertEqual(Errors.E168, '[E168] error description')

    def test_diversity_4(self):
        self.assertEqual(Errors.E158, '[E158] error description')

    def test_diversity_5(self):
        self.assertEqual(Errors.E181, '[E181] error description')

    def test_diversity_6(self):
        self.assertEqual(Errors.E160, '[E160] error description')

    def test_diversity_7(self):
        self.assertEqual(Errors.E070, '[E070] error description')

    def test_diversity_8(self):
        self.assertEqual(Errors.E024, '[E024] error description')

    def test_diversity_9(self):
        self.assertEqual(Errors.E062, '[E062] error description')

    def test_diversity_10(self):
        self.assertEqual(Errors.E066, '[E066] error description')


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(Errors.E095,
                         "[E095] Can't write to frozen dictionary. This is likely an internal error. Are you writing to a default function argument?")

    def test_diversity_2(self):
        self.assertEqual(Errors.E193,
                         '[E193] Unable to resize vectors in place if the resized vector dimension ({new_dim}) is not the same as the current vector dimension ({curr_dim}).')

    def test_diversity_3(self):
        self.assertEqual(Errors.E054, "[E054] No valid '{setting}' setting found in model meta.json.")

    def test_diversity_4(self):
        self.assertEqual(Errors.E177, '[E177] Ill-formed IOB input detected: {tag}')

    def test_diversity_5(self):
        self.assertEqual(Errors.E022, "[E022] Could not find a transition with the name '{name}' in the NER model.")

    def test_diversity_6(self):
        self.assertEqual(Errors.E024,
                         "[E024] Could not find an optimal move to supervise the parser. Usually, this means that the model can't be updated in a way that's valid and satisfies the correct annotations specified in the GoldParse. For example, are all labels added to the model? If you're training a named entity recognizer, also make sure that none of your annotated entity spans have leading or trailing whitespace or punctuation. You can also use the experimental `debug-data` command to validate your JSON-formatted training data. For details, run:\npython -m spacy debug-data --help")

    def test_diversity_7(self):
        self.assertEqual(Errors.E132,
                         "[E132] The vectors for entities and probabilities for alias '{alias}' should have equal length, but found {entities_length} and {probabilities_length} respectively.")

    def test_diversity_8(self):
        self.assertEqual(Errors.E051,
                         "[E051] Cant' load '{name}'. If you're using a shortcut link, make sure it points to a valid package (not just a data directory).")

    def test_diversity_9(self):
        self.assertEqual(Errors.E155,
                         '[E155] The pipeline needs to include a tagger in order to use Matcher or PhraseMatcher with the attributes POS, TAG, or LEMMA. Try using nlp() instead of nlp.make_doc() or list(nlp.pipe()) instead of list(nlp.tokenizer.pipe()).')

    def test_diversity_10(self):
        self.assertEqual(Errors.E096,
                         '[E096] Invalid object passed to displaCy: Can only visualize Doc or Span objects, or dicts if set to manual=True.')
