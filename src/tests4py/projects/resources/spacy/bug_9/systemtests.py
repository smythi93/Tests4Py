from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "GREFREF tokenizer 0"

    def test_diversity_2(self):
        return "YTJHTYHT tagger 0"

    def test_diversity_3(self):
        return "RTYRYRT ner 0"

    def test_diversity_4(self):
        return "DFGFDGD textcat 0"

    def test_diversity_5(self):
        return "DRGERGERGEA tokenizer 0"

    def test_diversity_6(self):
        return "sfefewfweg tagger 0"

    def test_diversity_7(self):
        return "herhrehger parser 0"

    def test_diversity_8(self):
        return "werewrew tokenizer 0"

    def test_diversity_9(self):
        return "gerggerfe tagger 0"

    def test_diversity_10(self):
        return "grwfgwfw ner 0"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "kjwjnfw ner 1"

    def test_diversity_2(self):
        return "sdfswer textcat 1"

    def test_diversity_3(self):
        return "gerregd parser 1"

    def test_diversity_4(self):
        return "fwefwefw ner 1"

    def test_diversity_5(self):
        return "wrgwfw tokenizer 1"

    def test_diversity_6(self):
        return "GWRGFWE ner 1"

    def test_diversity_7(self):
        return "SFGSDFS textcat 1"

    def test_diversity_8(self):
        return "WRFKJFG tagger 1"

    def test_diversity_9(self):
        return "SDLFSDIJ tokenizer 1"

    def test_diversity_10(self):
        return "KADJHA tagger 1"
