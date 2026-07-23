import unittest

# noinspection PyUnresolvedReferences
from youtube_dl.utils import cli_bool_option


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual([], cli_bool_option({}, '--aoo-qfxa', 'gxkrmghz'))

    def test_diversity_2(self):
        self.assertEqual([], cli_bool_option({}, '--ivnurh-un', 'bxbvvjxjug'))

    def test_diversity_3(self):
        self.assertEqual([], cli_bool_option({}, '--dwulth-eufg', 'jedhm'))

    def test_diversity_4(self):
        self.assertEqual([], cli_bool_option({}, '--odf', 'vvvodk'))

    def test_diversity_5(self):
        self.assertEqual([], cli_bool_option({}, '--kkyqn', 'aywqvawvg'))

    def test_diversity_6(self):
        self.assertEqual([], cli_bool_option({}, '--kbkye', 'mahoyl'))

    def test_diversity_7(self):
        self.assertEqual([], cli_bool_option({}, '--anusab-atwfq', 'bujetuna'))

    def test_diversity_8(self):
        self.assertEqual([], cli_bool_option({}, '--viqf', 'glgktn'))

    def test_diversity_9(self):
        self.assertEqual([], cli_bool_option({}, '--toinpr', 'ahtmaeqqw'))

    def test_diversity_10(self):
        self.assertEqual([], cli_bool_option({}, '--ccsdwb-zvmw-bp', 'nkonqnn'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(['--gv-viyaoi-ifngch', 'true'], cli_bool_option({'apcrse': True}, '--gv-viyaoi-ifngch', 'apcrse'))

    def test_diversity_2(self):
        self.assertEqual(['--palfj-jjcd-jtcge', 'true'], cli_bool_option({'ahpq': True}, '--palfj-jjcd-jtcge', 'ahpq'))

    def test_diversity_3(self):
        self.assertEqual(['--ewflqs', 'false'], cli_bool_option({'ppnyljax': False}, '--ewflqs', 'ppnyljax'))

    def test_diversity_4(self):
        self.assertEqual(['--qgep-zlgjbj-nf', 'true'], cli_bool_option({'nmohhdd': True}, '--qgep-zlgjbj-nf', 'nmohhdd'))

    def test_diversity_5(self):
        self.assertEqual(['--zojh-qbpqg', 'false'], cli_bool_option({'mrkwr': False}, '--zojh-qbpqg', 'mrkwr'))

    def test_diversity_6(self):
        self.assertEqual(['--gypl-frwb', 'false'], cli_bool_option({'kjlk': False}, '--gypl-frwb', 'kjlk'))

    def test_diversity_7(self):
        self.assertEqual(['--ili-qv', 'false'], cli_bool_option({'xvudjykp': False}, '--ili-qv', 'xvudjykp'))

    def test_diversity_8(self):
        self.assertEqual(['--bh-jkq', 'false'], cli_bool_option({'kghcn': False}, '--bh-jkq', 'kghcn'))

    def test_diversity_9(self):
        self.assertEqual(['--ubgpm-czzwc-zdj', 'true'], cli_bool_option({'dvhwe': True}, '--ubgpm-czzwc-zdj', 'dvhwe'))

    def test_diversity_10(self):
        self.assertEqual(['--lbbs-nzntg', 'true'], cli_bool_option({'aufigxlz': True}, '--lbbs-nzntg', 'aufigxlz'))
