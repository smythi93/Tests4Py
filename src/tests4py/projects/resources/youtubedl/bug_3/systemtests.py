from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):

    def test_diversity_1(self):
        return "-q !is_live\n-d {'is_live': False}"

    def test_diversity_2(self):
        return "-q !test\n-d {'test': False}"

    def test_diversity_3(self):
        return "-q !like_count & dislike_count <? 50 & description\n-d {'like_count': False, 'dislike_count': 10, 'description': ''}"

    def test_diversity_4(self):
        return "-q like_count > 100 & dislike_count <? 50 & !description\n-d {'like_count': 190, 'dislike_count': 23, 'description': False}"

    def test_diversity_5(self):
        return "-q like_count > 100 & !description\n-d {'like_count': 190, 'dislike_count': 4, 'description': False}"

    def test_diversity_6(self):
        return "-q !other & !description\n-d {'other': False, 'dislike_count': 1, 'description': False}"

    def test_diversity_7(self):
        return "-q !description\n-d {'other': False, 'dislike_count': 99999, 'description': False}"

    def test_diversity_8(self):
        return "-q !title\n-d {'title': False, 'description': False}"

    def test_diversity_9(self):
        return "-q description >? 10 & !title\n-d {'title': False}"

    def test_diversity_10(self):
        return "-q !is_live & description\n-d {'is_live': False, 'description': True}"


class TestsPassing(PassingSystemtests):

    def test_diversity_1(self):
        return "%20;"

    def test_diversity_2(self):
        return "&#x2F;"

    def test_diversity_3(self):
        return "&#47;"

    def test_diversity_4(self):
        return "&eacute;}"

    def test_diversity_5(self):
        return "-q &#2013266066"

    def test_diversity_6(self):
        return "-q like_count > 100 & dislike_count <? 50 & description\n-d {'like_count': 190, 'dislike_count': 10, 'description': True}"

    def test_diversity_7(self):
        return "-q dislike_count >? 50 & description\n-d {'like_count': 190, 'dislike_count': 10, 'description': True}"

    def test_diversity_8(self):
        return "-q like_count > 100\n-d {'like_count': 190, 'title': False}"

    def test_diversity_9(self):
        return "-q !title\n-d {'title': 'abc'}"

    def test_diversity_10(self):
        return "-q is_live\n-d {}"
