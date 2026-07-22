import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//uitc/xbo/wiwy', 'atmx/ieoyy/gemjdo', 'gatpn', 'wtc/hlv/gbuls']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_2(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//azqxjq/yowsdo/cdbz', 'zylz/zcaggb/qjmsk', 'nbongp/qyub', 'dyfei']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_3(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//nnx/fahaab/vlnqyt', 'koxmls']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_4(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//vwecq/akkde/qrph', 'qyx', 'qwik/orvbu/dqm']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_5(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//apo/bljw/oiu/tqnqq', 'xfkk', 'pnjh']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_6(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//lfdzi/xuj/dbapv/zldmpa', 'xyimg/xyylbb']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_7(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//rvq/ntvxpt/qhb/myokj', 'fpytw/avrh/pgotz', 'eacs', 'yuctvb/pex/ambw']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_8(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//smvpkx/lcsls/mxzs', 'anp', 'slyea/gkqkds/hku', 'wkcx/kaq/purtxk']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_9(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//rckwgh/yuscb/xwxx/pyyd', 'gzm/tgjqgf']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_10(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['//uym/pzj/ghdvia/hbpjr', 'hqmv/pwjhpf', 'htphw']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['occpnr/ijf/rakc', 'xnxxn/odi', 'uwru', 'jaato/abrs']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_2(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['jidnzc/jsjxiw/uiccp', 'ukdouk/xivwxo/xhsrx', 'kzhqjv/sidegu']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_3(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['zephm', 'axef/caa', 'uzbna/kivn/yumk']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_4(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['hlqsuk/ffcnd', 'avuia/pjbdi', 'tbfbrd']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_5(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['qvgpb/maqr', 'rsuyd/rar/caoem', 'rlps']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_6(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['pawqaz', 'mukljj/wvtdg']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_7(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['vispl/whpobj/xivcc', 'dznud/afq/wfpp']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_8(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['kykj/dcwow', 'vuhbon/tuhkb/vay', 'gjv/habvu/qbw', 'yjg/bofg']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_9(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['zdfnfa/ccwj/jsga', 'flb/wyehd']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))

    def test_diversity_10(self):
        import ntpath
        from ansible.plugins.shell.powershell import ShellModule
        args = ['sdeltu/xvkt', 'tqv', 'oistt/pivi', 'koxa/sdq']
        normed = [ntpath.normpath(a) for a in args]
        expected = ntpath.join(normed[0], *[p.strip(chr(92)) for p in normed[1:]])
        self.assertEqual(expected, ShellModule().join_path(*args))
