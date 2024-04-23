import unittest
from thefuck.types import SortedCorrectedCommandsSequence
from thefuck.types import CorrectedCommand
from thefuck.types import Settings


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit tdJGcrSt', None, ''), CorrectedCommand('git checkout aaOAzA', None, ''),
             CorrectedCommand('git branch OqWqEwsJaEd', None, '')]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_2(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(
            iter([CorrectedCommand('git commit CYAbcaqbFExlTR', None, None),
                  CorrectedCommand('git checkout FTCAMxhcnkpPNVh', None,
                                   None),
                  CorrectedCommand('git branch qaRbErMwxbtMfRz', None,
                                   None)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_3(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit DBjXsaD', None, ''), CorrectedCommand('git checkout qPImVeNeRgL', None, ''),
             CorrectedCommand('git branch FiCRSJ', None, '')]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_4(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit weCCa', None, ''), CorrectedCommand('git checkout JCLvyqHqY', None, ''),
             CorrectedCommand('git branch JjQJP', None, '')]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_5(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit vcUOAypSx', None, None),
             CorrectedCommand('git checkout BHeqoLyqu', None, None),
             CorrectedCommand('git branch foxJeWMLdy', None, None)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_6(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit oLGNgCnLJe', None, ''), CorrectedCommand('git checkout mWyvqXzwyR', None, ''),
             CorrectedCommand('git branch EURlP', None, '')]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_7(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit MwYgddVmTZ', None, None), CorrectedCommand('git checkout hXEcXl', None, None),
             CorrectedCommand('git branch utaVlR', None, None)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_8(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(
            iter([CorrectedCommand('git commit XRaLfxIHfIIxviQ', None, ''),
                  CorrectedCommand('git checkout laInHSXvQU', None, ''),
                  CorrectedCommand('git branch WJKzPNfNmpwdC', None, '')]),
            Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_9(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit lEsguhjxulYTrjn', None, None),
             CorrectedCommand('git checkout GogHnJtKbKmTOR', None, None),
             CorrectedCommand('git branch xINCXYcviQJVQ', None, None)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_10(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit dcEOFx', None, ''), CorrectedCommand('git checkout kyzJaNFBvCFTgH', None, ''),
             CorrectedCommand('git branch lTPdRW', None, '')]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter([CorrectedCommand('git commit RtmaqNgdctEC', None, 33),
                                                                  CorrectedCommand('git checkout VDKGpstjbVZQIHC', None,
                                                                                   31),
                                                                  CorrectedCommand('git branch DdWDvntHpVeKX', None,
                                                                                   980)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_2(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit uAEZwzRVy', None, 569), CorrectedCommand('git checkout SMWAPZFjt', None, 865),
             CorrectedCommand('git branch drbBcstDKU', None, 121)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_3(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit dyGYY', None, 960), CorrectedCommand('git checkout aHkxDvvf', None, 23),
             CorrectedCommand('git branch IYVYyRiqYNfYvmx', None, 187)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_4(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit bjbsK', None, 741), CorrectedCommand('git checkout WYyKArTFd', None, 186),
             CorrectedCommand('git branch EsskS', None, 179)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_5(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit nmqdbmvdjoBK', None, 914), CorrectedCommand('git checkout rqxQbO', None, 594),
             CorrectedCommand('git branch ZELYtW', None, 698)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_6(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter([CorrectedCommand('git commit uAKrOzS', None, 548),
                                                                  CorrectedCommand('git checkout pQuDJiuViHMw', None,
                                                                                   316),
                                                                  CorrectedCommand('git branch ACcTWMoafb', None,
                                                                                   794)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_7(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit PnzrmW', None, 328), CorrectedCommand('git checkout vpVoumZvxng', None, 999),
             CorrectedCommand('git branch dqfwpETvVR', None, 629)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_8(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit GISsUhbe', None, 925), CorrectedCommand('git checkout wfSoQNp', None, 210),
             CorrectedCommand('git branch AiZWsWHYlM', None, 4)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_9(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter([CorrectedCommand('git commit fskMPmCX', None, 891),
                                                                  CorrectedCommand('git checkout fgXhbHaHXfQyhD', None,
                                                                                   264),
                                                                  CorrectedCommand('git branch BwoIpqFTKXHRvtA', None,
                                                                                   883)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())

    def test_diversity_10(self):
        sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
            [CorrectedCommand('git commit LaPGTdXLPeYjn', None, 855),
             CorrectedCommand('git checkout lOlkSvFYmu', None, 68),
             CorrectedCommand('git branch afkXbyethUhL', None, 33)]), Settings({'key': 'val'}))
        self.assertEqual(None, sort_corr_cmd_seq._realise())
