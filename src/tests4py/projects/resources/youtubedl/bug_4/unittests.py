import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(582, JSInterpreter('function czr(){return 582;}\nfunction nysg(){return czr();}').call_function('nysg'))

    def test_diversity_2(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(673, JSInterpreter('function kpf(){return 673;}\nfunction qb(){return kpf();}').call_function('qb'))

    def test_diversity_3(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(84, JSInterpreter('function ooiy(){return 84;}\nfunction xq(){return ooiy();}').call_function('xq'))

    def test_diversity_4(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(761, JSInterpreter('function plssk(){return 761;}\nfunction ik(){return plssk();}').call_function('ik'))

    def test_diversity_5(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(214, JSInterpreter('function xge(){return 214;}\nfunction ivjrk(){return xge();}').call_function('ivjrk'))

    def test_diversity_6(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(380, JSInterpreter('function aqr(){return 380;}\nfunction riyfx(){return aqr();}').call_function('riyfx'))

    def test_diversity_7(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(549, JSInterpreter('function fxtg(){return 549;}\nfunction sxe(){return fxtg();}').call_function('sxe'))

    def test_diversity_8(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(172, JSInterpreter('function otmk(){return 172;}\nfunction szoyd(){return otmk();}').call_function('szoyd'))

    def test_diversity_9(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(563, JSInterpreter('function ezfl(){return 563;}\nfunction wsy(){return ezfl();}').call_function('wsy'))

    def test_diversity_10(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(990, JSInterpreter('function br(){return 990;}\nfunction xx(){return br();}').call_function('xx'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(60, JSInterpreter('function yk(a){return a+49;}\nfunction egb(){return yk(11);}').call_function('egb'))

    def test_diversity_2(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(146, JSInterpreter('function dlx(a){return a+86;}\nfunction tmjk(){return dlx(60);}').call_function('tmjk'))

    def test_diversity_3(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(157, JSInterpreter('function has(a){return a+95;}\nfunction xmnd(){return has(62);}').call_function('xmnd'))

    def test_diversity_4(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(135, JSInterpreter('function phpb(a){return a+84;}\nfunction zwtqn(){return phpb(51);}').call_function('zwtqn'))

    def test_diversity_5(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(97, JSInterpreter('function vqlr(a){return a+66;}\nfunction aueuj(){return vqlr(31);}').call_function('aueuj'))

    def test_diversity_6(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(90, JSInterpreter('function ciy(a){return a+53;}\nfunction wobk(){return ciy(37);}').call_function('wobk'))

    def test_diversity_7(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(37, JSInterpreter('function uvhw(a){return a+32;}\nfunction xwe(){return uvhw(5);}').call_function('xwe'))

    def test_diversity_8(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(50, JSInterpreter('function hkbkr(a){return a+44;}\nfunction druq(){return hkbkr(6);}').call_function('druq'))

    def test_diversity_9(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(37, JSInterpreter('function xdk(a){return a+10;}\nfunction lpf(){return xdk(27);}').call_function('lpf'))

    def test_diversity_10(self):
        from youtube_dl.jsinterp import JSInterpreter
        self.assertEqual(122, JSInterpreter('function qyj(a){return a+31;}\nfunction eu(){return qyj(91);}').call_function('eu'))
