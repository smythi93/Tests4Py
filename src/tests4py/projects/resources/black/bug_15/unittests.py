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
        self.assertEqual('# fmt: off\n@parametrize([\n    (5, 8, 5, 9)\n])\ndef dlk(fbvhwh):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@parametrize([\n    (5, 8, 5, 9)\n])\ndef dlk(fbvhwh):\n    pass\n# fmt: on\n'))

    def test_diversity_2(self):
        self.assertEqual('# fmt: off\n@parametrize([\n    (2, 5)\n])\ndef ychtdv(sfglw):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@parametrize([\n    (2, 5)\n])\ndef ychtdv(sfglw):\n    pass\n# fmt: on\n'))

    def test_diversity_3(self):
        self.assertEqual('# fmt: off\n@route([\n    (0, 8, 0)\n])\ndef wcwdk(wocndm):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@route([\n    (0, 8, 0)\n])\ndef wcwdk(wocndm):\n    pass\n# fmt: on\n'))

    def test_diversity_4(self):
        self.assertEqual('# fmt: off\n@parametrize([\n    (5, 3, 6)\n])\ndef qaiqltk(tdti):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@parametrize([\n    (5, 3, 6)\n])\ndef qaiqltk(tdti):\n    pass\n# fmt: on\n'))

    def test_diversity_5(self):
        self.assertEqual('# fmt: off\n@mark([\n    (5, 0, 6, 3)\n])\ndef qgtox(qabs):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@mark([\n    (5, 0, 6, 3)\n])\ndef qgtox(qabs):\n    pass\n# fmt: on\n'))

    def test_diversity_6(self):
        self.assertEqual('# fmt: off\n@given([\n    (1, 9, 4)\n])\ndef pqbfg(tvdyivcx):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@given([\n    (1, 9, 4)\n])\ndef pqbfg(tvdyivcx):\n    pass\n# fmt: on\n'))

    def test_diversity_7(self):
        self.assertEqual('# fmt: off\n@mark([\n    (0, 6, 8, 0)\n])\ndef mrmrnp(askdojf):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@mark([\n    (0, 6, 8, 0)\n])\ndef mrmrnp(askdojf):\n    pass\n# fmt: on\n'))

    def test_diversity_8(self):
        self.assertEqual('# fmt: off\n@deco([\n    (5, 0, 2, 9)\n])\ndef tzyio(efw):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@deco([\n    (5, 0, 2, 9)\n])\ndef tzyio(efw):\n    pass\n# fmt: on\n'))

    def test_diversity_9(self):
        self.assertEqual('# fmt: off\n@register([\n    (9, 7)\n])\ndef gpxdohdr(orfd):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@register([\n    (9, 7)\n])\ndef gpxdohdr(orfd):\n    pass\n# fmt: on\n'))

    def test_diversity_10(self):
        self.assertEqual('# fmt: off\n@mark([\n    (5, 6, 6)\n])\ndef vzj(ryutnps):\n    pass\n# fmt: on\n', self.run_black('# fmt: off\n@mark([\n    (5, 6, 6)\n])\ndef vzj(ryutnps):\n    pass\n# fmt: on\n'))

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
        self.assertEqual('# fmt: off\ntearzobp = [4,   8]\n# fmt: on\n', self.run_black('# fmt: off\ntearzobp = [4,   8]\n# fmt: on\n'))

    def test_diversity_2(self):
        self.assertEqual('import alzrtitx\n\n\ndef dhzufra(vsdtrt):\n    pass\n', self.run_black('import alzrtitx\n\n\ndef dhzufra(vsdtrt):\n    pass\n'))

    def test_diversity_3(self):
        self.assertEqual('sgld = 784\n', self.run_black('sgld = 784\n'))

    def test_diversity_4(self):
        self.assertEqual('cttr = 581\n', self.run_black('cttr = 581\n'))

    def test_diversity_5(self):
        self.assertEqual('import oblbxma\n\n\ndef naatyj(jpzb):\n    pass\n', self.run_black('import oblbxma\n\n\ndef naatyj(jpzb):\n    pass\n'))

    def test_diversity_6(self):
        self.assertEqual('# fmt: off\nvgvp = [0,   7]\n# fmt: on\n', self.run_black('# fmt: off\nvgvp = [0,   7]\n# fmt: on\n'))

    def test_diversity_7(self):
        self.assertEqual('# fmt: off\nuoud = [6,   3]\n# fmt: on\n', self.run_black('# fmt: off\nuoud = [6,   3]\n# fmt: on\n'))

    def test_diversity_8(self):
        self.assertEqual('# fmt: off\ntsapqz = [7,   9]\n# fmt: on\n', self.run_black('# fmt: off\ntsapqz = [7,   9]\n# fmt: on\n'))

    def test_diversity_9(self):
        self.assertEqual('def sxchu():\n    return 120\n', self.run_black('def sxchu():\n    return 120\n'))

    def test_diversity_10(self):
        self.assertEqual('def jcnfjpy():\n    return 703\n', self.run_black('def jcnfjpy():\n    return 703\n'))
