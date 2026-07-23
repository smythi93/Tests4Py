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
        self.assertEqual('kgtc = zaer(\n    zx,  # type: bytes\n    jmjn,  # type: bytes\n)  # type: int\n', self.run_black('kgtc = zaer(\n    zx,  # type: bytes\n    jmjn,  # type: bytes\n)  # type: int\n'))

    def test_diversity_2(self):
        self.assertEqual('bdf = (\n    tgcz,  # type: float\n    bs,  # type: bytes\n)  # type: Tuple[float, bytes]\n', self.run_black('bdf = (\n    tgcz,  # type: float\n    bs,  # type: bytes\n)  # type: Tuple[float, bytes]\n'))

    def test_diversity_3(self):
        self.assertEqual('si = [\n    cwt,  # type: float\n    ur,  # type: bytes\n    ar,  # type: str\n]  # type: List[float]\n', self.run_black('si = [\n    cwt,  # type: float\n    ur,  # type: bytes\n    ar,  # type: str\n]  # type: List[float]\n'))

    def test_diversity_4(self):
        self.assertEqual('joxb = (\n    nzgp,  # type: bool\n    qb,  # type: bytes\n)  # type: Tuple[bool, bytes]\n', self.run_black('joxb = (\n    nzgp,  # type: bool\n    qb,  # type: bytes\n)  # type: Tuple[bool, bytes]\n'))

    def test_diversity_5(self):
        self.assertEqual('lsdc = [\n    nxc,  # type: bytes\n    cun,  # type: float\n]  # type: List[bytes]\n', self.run_black('lsdc = [\n    nxc,  # type: bytes\n    cun,  # type: float\n]  # type: List[bytes]\n'))

    def test_diversity_6(self):
        self.assertEqual('efs = (\n    kyq,  # type: str\n    ghr,  # type: float\n)  # type: Tuple[str, float]\n', self.run_black('efs = (\n    kyq,  # type: str\n    ghr,  # type: float\n)  # type: Tuple[str, float]\n'))

    def test_diversity_7(self):
        self.assertEqual('nab = bgf(\n    tyq,  # type: str\n    qhev,  # type: str\n    rh,  # type: int\n)  # type: bytes\n', self.run_black('nab = bgf(\n    tyq,  # type: str\n    qhev,  # type: str\n    rh,  # type: int\n)  # type: bytes\n'))

    def test_diversity_8(self):
        self.assertEqual('yc = [\n    cghyq,  # type: int\n    bw,  # type: bytes\n]  # type: List[str]\n', self.run_black('yc = [\n    cghyq,  # type: int\n    bw,  # type: bytes\n]  # type: List[str]\n'))

    def test_diversity_9(self):
        self.assertEqual('gcun = ivagh(\n    drr,  # type: bytes\n    ujf,  # type: int\n)  # type: bytes\n', self.run_black('gcun = ivagh(\n    drr,  # type: bytes\n    ujf,  # type: int\n)  # type: bytes\n'))

    def test_diversity_10(self):
        self.assertEqual('jgtu = [\n    vhhkx,  # type: bytes\n    zot,  # type: int\n]  # type: List[bytes]\n', self.run_black('jgtu = [\n    vhhkx,  # type: bytes\n    zot,  # type: int\n]  # type: List[bytes]\n'))

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
        self.assertEqual('def dplzs(kis):\n    tj = compute()  # type: int\n    return tj\n', self.run_black('def dplzs(kis):\n    tj = compute()  # type: int\n    return tj\n'))

    def test_diversity_2(self):
        self.assertEqual('def pk(bpvjk):\n    kw = compute()  # type: bool\n    return kw\n', self.run_black('def pk(bpvjk):\n    kw = compute()  # type: bool\n    return kw\n'))

    def test_diversity_3(self):
        self.assertEqual('def dldza(ukte):\n    zsym = compute()  # type: str\n    return zsym\n', self.run_black('def dldza(ukte):\n    zsym = compute()  # type: str\n    return zsym\n'))

    def test_diversity_4(self):
        self.assertEqual('hwvgt = 17\n', self.run_black('hwvgt = 17\n'))

    def test_diversity_5(self):
        self.assertEqual('dyp = []  # type: List[float]\n', self.run_black('dyp = []  # type: List[float]\n'))

    def test_diversity_6(self):
        self.assertEqual('def wk(euf):\n    tlge = compute()  # type: bytes\n    return tlge\n', self.run_black('def wk(euf):\n    tlge = compute()  # type: bytes\n    return tlge\n'))

    def test_diversity_7(self):
        self.assertEqual('def ppe(azl):\n    wjpk = compute()  # type: bool\n    return wjpk\n', self.run_black('def ppe(azl):\n    wjpk = compute()  # type: bool\n    return wjpk\n'))

    def test_diversity_8(self):
        self.assertEqual('dl = 62\n', self.run_black('dl = 62\n'))

    def test_diversity_9(self):
        self.assertEqual('ihrqa = []  # type: List[float]\n', self.run_black('ihrqa = []  # type: List[float]\n'))

    def test_diversity_10(self):
        self.assertEqual('bezx = 89\n', self.run_black('bezx = 89\n'))
