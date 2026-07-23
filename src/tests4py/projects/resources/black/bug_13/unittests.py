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
        self.assertEqual('def jopp():\n    return [wqo async for wqo in koq()]\n', self.run_black('def jopp():\n    return [wqo async for wqo in koq()]\n'))

    def test_diversity_2(self):
        self.assertEqual('def zgrepd():\n    return (clfuv async for clfuv in nhpjmwlh())\n', self.run_black('def zgrepd():\n    return (clfuv async for clfuv in nhpjmwlh())\n'))

    def test_diversity_3(self):
        self.assertEqual('def bwthuvp():\n    return [rkaswtf async for rkaswtf in gwxfo()]\n', self.run_black('def bwthuvp():\n    return [rkaswtf async for rkaswtf in gwxfo()]\n'))

    def test_diversity_4(self):
        self.assertEqual('naejjg = [nqyqadnn async for nqyqadnn in npg()]\n', self.run_black('naejjg = [nqyqadnn async for nqyqadnn in npg()]\n'))

    def test_diversity_5(self):
        self.assertEqual('def grasjya():\n    return (mqum async for mqum in pmzk())\n', self.run_black('def grasjya():\n    return (mqum async for mqum in pmzk())\n'))

    def test_diversity_6(self):
        self.assertEqual('def zzz():\n    return {mishdnp async for mishdnp in zhoflhp()}\n', self.run_black('def zzz():\n    return {mishdnp async for mishdnp in zhoflhp()}\n'))

    def test_diversity_7(self):
        self.assertEqual('raxs = [vvot async for vvot in sll()]\n', self.run_black('raxs = [vvot async for vvot in sll()]\n'))

    def test_diversity_8(self):
        self.assertEqual('def hdqqh():\n    return (ohlvcw async for ohlvcw in xlruxtbr())\n', self.run_black('def hdqqh():\n    return (ohlvcw async for ohlvcw in xlruxtbr())\n'))

    def test_diversity_9(self):
        self.assertEqual('def luojrgg():\n    return (rdobse async for rdobse in grhn())\n', self.run_black('def luojrgg():\n    return (rdobse async for rdobse in grhn())\n'))

    def test_diversity_10(self):
        self.assertEqual('def mlwbr():\n    return [phdgigd async for phdgigd in edtecux()]\n', self.run_black('def mlwbr():\n    return [phdgigd async for phdgigd in edtecux()]\n'))

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
        self.assertEqual('async def lpjat():\n    return [qknuit async for qknuit in ano()]\n', self.run_black('async def lpjat():\n    return [qknuit async for qknuit in ano()]\n'))

    def test_diversity_2(self):
        self.assertEqual('oakkatpf = 0\n', self.run_black('oakkatpf = 0\n'))

    def test_diversity_3(self):
        self.assertEqual('async def tfutoufz():\n    return [loiu async for loiu in wmihrtc()]\n', self.run_black('async def tfutoufz():\n    return [loiu async for loiu in wmihrtc()]\n'))

    def test_diversity_4(self):
        self.assertEqual('async def jlhne():\n    return [rncesqpv async for rncesqpv in vjqtp()]\n', self.run_black('async def jlhne():\n    return [rncesqpv async for rncesqpv in vjqtp()]\n'))

    def test_diversity_5(self):
        self.assertEqual('def vkb():\n    return [rvrjyx for rvrjyx in lkvh()]\n', self.run_black('def vkb():\n    return [rvrjyx for rvrjyx in lkvh()]\n'))

    def test_diversity_6(self):
        self.assertEqual('async def tuhyutua():\n    return [qyd async for qyd in eraf()]\n', self.run_black('async def tuhyutua():\n    return [qyd async for qyd in eraf()]\n'))

    def test_diversity_7(self):
        self.assertEqual('tgrzbca = 1\n', self.run_black('tgrzbca = 1\n'))

    def test_diversity_8(self):
        self.assertEqual('async def trlb():\n    return [bahbz async for bahbz in pnto()]\n', self.run_black('async def trlb():\n    return [bahbz async for bahbz in pnto()]\n'))

    def test_diversity_9(self):
        self.assertEqual('vzuz = 9\n', self.run_black('vzuz = 9\n'))

    def test_diversity_10(self):
        self.assertEqual('async def wpbq():\n    return [defpo async for defpo in lzlmph()]\n', self.run_black('async def wpbq():\n    return [defpo async for defpo in lzlmph()]\n'))
