import unittest
import black

class TestsFailing(unittest.TestCase):

    @staticmethod
    def run_black(src):
        import black
        try:
            return black.format_str(src, line_length=88)
        except TypeError:
            pass
        mode = None
        for attr in ('Mode', 'FileMode'):
            if hasattr(black, attr):
                try:
                    mode = getattr(black, attr)()
                except Exception:
                    mode = None
                break
        if mode is None:
            return black.format_str(src)
        return black.format_str(src, mode=mode)

    def test_diversity_1(self):
        self.assertEqual('@rsbruwg\n# TODO: gvmgqy\n# handles bltzqkr\n@dvume\ndef nbibuum():\n    pass\n', self.run_black('@rsbruwg\n# TODO: gvmgqy\n# handles bltzqkr\n@dvume\ndef nbibuum():\n    pass\n'))

    def test_diversity_2(self):
        self.assertEqual('@qghiekt\n# TODO: fvljcvi\n# NOTE tbejguf\n# NOTE smuxh\n@ztyux\ndef usvngyy():\n    pass\n', self.run_black('@qghiekt\n# TODO: fvljcvi\n# NOTE tbejguf\n# NOTE smuxh\n@ztyux\ndef usvngyy():\n    pass\n'))

    def test_diversity_3(self):
        self.assertEqual('@ispweb\n# zjbqqiv\n# handles imkjiov\n@cewtr\ndef kmopppk():\n    pass\n', self.run_black('@ispweb\n# zjbqqiv\n# handles imkjiov\n@cewtr\ndef kmopppk():\n    pass\n'))

    def test_diversity_4(self):
        self.assertEqual('@qdbjoxc\n# hdkok\n# TODO: jqhnce\n# NOTE ydel\n@aii\ndef ofyaopok():\n    pass\n', self.run_black('@qdbjoxc\n# hdkok\n# TODO: jqhnce\n# NOTE ydel\n@aii\ndef ofyaopok():\n    pass\n'))

    def test_diversity_5(self):
        self.assertEqual('@dgli\n# NOTE jchtd\n# handles xliqr\n@login_required\ndef fttxlmut():\n    pass\n', self.run_black('@dgli\n# NOTE jchtd\n# handles xliqr\n@login_required\ndef fttxlmut():\n    pass\n'))

    def test_diversity_6(self):
        self.assertEqual('@property\n# handles ienlwqhs\n# TODO: hpr\n@lim\ndef lku():\n    pass\n', self.run_black('@property\n# handles ienlwqhs\n# TODO: hpr\n@lim\ndef lku():\n    pass\n'))

    def test_diversity_7(self):
        self.assertEqual('@dsoswtd\n# NOTE vjbtdths\n# handles aga\n# NOTE nvhidia\n@lsbppih\ndef voagmwp():\n    pass\n', self.run_black('@dsoswtd\n# NOTE vjbtdths\n# handles aga\n# NOTE nvhidia\n@lsbppih\ndef voagmwp():\n    pass\n'))

    def test_diversity_8(self):
        self.assertEqual('@dnlllz\n# FIXME dnzxa\n@npyctndk\ndef fgkdxml():\n    pass\n', self.run_black('@dnlllz\n# FIXME dnzxa\n@npyctndk\ndef fgkdxml():\n    pass\n'))

    def test_diversity_9(self):
        self.assertEqual('@kqm\n# dbycg\n# rxuee\n# pctxxb\n@pytest.fixture\ndef fxqlf():\n    pass\n', self.run_black('@kqm\n# dbycg\n# rxuee\n# pctxxb\n@pytest.fixture\ndef fxqlf():\n    pass\n'))

    def test_diversity_10(self):
        self.assertEqual('@classmethod\n# handles unvzb\n# handles hsii\n@bpxud\ndef kkgerksd():\n    pass\n', self.run_black('@classmethod\n# handles unvzb\n# handles hsii\n@bpxud\ndef kkgerksd():\n    pass\n'))

class TestsPassing(unittest.TestCase):

    @staticmethod
    def run_black(src):
        import black
        try:
            return black.format_str(src, line_length=88)
        except TypeError:
            pass
        mode = None
        for attr in ('Mode', 'FileMode'):
            if hasattr(black, attr):
                try:
                    mode = getattr(black, attr)()
                except Exception:
                    mode = None
                break
        if mode is None:
            return black.format_str(src)
        return black.format_str(src, mode=mode)

    def test_diversity_1(self):
        self.assertEqual('@wpoeww\n@iartdj\ndef evmmrrg():\n    pass\n', self.run_black('@wpoeww\n@iartdj\ndef evmmrrg():\n    pass\n'))

    def test_diversity_2(self):
        self.assertEqual('def houx(tnbgq, pjpfn):\n    return 99\n', self.run_black('def houx(tnbgq, pjpfn):\n    return 99\n'))

    def test_diversity_3(self):
        self.assertEqual('@ocnsjm\n@cached\ndef aylxfy():\n    pass\n', self.run_black('@ocnsjm\n@cached\ndef aylxfy():\n    pass\n'))

    def test_diversity_4(self):
        self.assertEqual('@functools.lru_cache\ndef xvptyn():\n    # fbgrze\n    return 78\n', self.run_black('@functools.lru_cache\ndef xvptyn():\n    # fbgrze\n    return 78\n'))

    def test_diversity_5(self):
        self.assertEqual('@byit\n@bpns\ndef udqtbulk():\n    pass\n', self.run_black('@byit\n@bpns\ndef udqtbulk():\n    pass\n'))

    def test_diversity_6(self):
        self.assertEqual('@staticmethod\ndef puot():\n    # uedwaest\n    return 97\n', self.run_black('@staticmethod\ndef puot():\n    # uedwaest\n    return 97\n'))

    def test_diversity_7(self):
        self.assertEqual('def kcy(ovgn, aroncrh):\n    return 38\n', self.run_black('def kcy(ovgn, aroncrh):\n    return 38\n'))

    def test_diversity_8(self):
        self.assertEqual('def fac(umdnqa, nnb):\n    return 37\n', self.run_black('def fac(umdnqa, nnb):\n    return 37\n'))

    def test_diversity_9(self):
        self.assertEqual('def aju(mjyll, vyh):\n    return 17\n', self.run_black('def aju(mjyll, vyh):\n    return 17\n'))

    def test_diversity_10(self):
        self.assertEqual('def jbk(hwhgnufu, prpy):\n    return 77\n', self.run_black('def jbk(hwhgnufu, prpy):\n    return 77\n'))
