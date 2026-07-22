import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['account', 'sufficient', 'pamkar.so'], ['password', 'required', 'pamwtwi.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_2(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['auth', 'sufficient', 'pampto.so'], ['account', 'sufficient', 'pamujzn.so'], ['account', 'required', 'pamtnkean.so']]
        idx = 2
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_3(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['auth', 'requisite', 'pamgpyj.so'], ['session', 'sufficient', 'pamatqde.so'], ['password', 'required', 'pampkdily.so']]
        idx = 2
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_4(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['auth', 'sufficient', 'pamuyr.so'], ['session', 'required', 'pamxyn.so'], ['auth', 'required', 'pamskkcno.so'], ['session', 'sufficient', 'pamntunf.so']]
        idx = 3
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_5(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['session', 'sufficient', 'pamiixp.so'], ['session', 'requisite', 'pamwgzk.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_6(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['account', 'optional', 'pamtdt.so'], ['password', 'requisite', 'pamnqbks.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_7(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['account', 'optional', 'pamykjaqz.so'], ['session', 'required', 'pamyel.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_8(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['session', 'optional', 'pamrxeea.so'], ['password', 'requisite', 'pamrednh.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_9(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['account', 'sufficient', 'pamatmqxy.so'], ['auth', 'requisite', 'pambhk.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_10(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['auth', 'requisite', 'pamazvcb.so'], ['session', 'optional', 'pamhwhw.so'], ['auth', 'requisite', 'pammwoga.so']]
        idx = 2
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['auth', 'required', 'pamlcf.so'], ['auth', 'required', 'pamuhqct.so'], ['session', 'sufficient', 'pamaruww.so'], ['auth', 'required', 'pamnvlb.so']]
        idx = 2
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_2(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['password', 'sufficient', 'pamnvvp.so'], ['session', 'requisite', 'pamxndue.so'], ['account', 'optional', 'pamkvy.so'], ['session', 'requisite', 'pamrenyo.so'], ['auth', 'sufficient', 'pamaovdt.so'], ['session', 'required', 'pamnntjdk.so']]
        idx = 3
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_3(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['auth', 'required', 'pamofkxhm.so'], ['account', 'optional', 'pamdpx.so'], ['password', 'requisite', 'pampkfcy.so'], ['password', 'optional', 'pamcbzejc.so']]
        idx = 2
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_4(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['password', 'optional', 'pamjjs.so'], ['account', 'required', 'pamebphb.so'], ['password', 'requisite', 'pamxom.so'], ['account', 'required', 'pamdqcc.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_5(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['session', 'required', 'pamznpjoi.so'], ['session', 'required', 'pamkieq.so'], ['password', 'sufficient', 'pamlwyv.so'], ['auth', 'sufficient', 'pamyjh.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_6(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['session', 'optional', 'pampbwl.so'], ['session', 'sufficient', 'pamcffzml.so'], ['auth', 'optional', 'pamjcms.so'], ['password', 'optional', 'pamipqed.so'], ['account', 'optional', 'pamqoiaa.so']]
        idx = 2
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_7(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['account', 'sufficient', 'pamosw.so'], ['password', 'optional', 'pamvszkj.so'], ['auth', 'required', 'pamongn.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_8(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['account', 'required', 'pamwmk.so'], ['account', 'optional', 'pamqdp.so'], ['session', 'required', 'pamtvm.so'], ['auth', 'sufficient', 'pamcuxes.so'], ['auth', 'sufficient', 'pammknz.so']]
        idx = 1
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_9(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['account', 'required', 'pampfmovn.so'], ['auth', 'requisite', 'pamtjb.so'], ['password', 'requisite', 'pammcr.so'], ['password', 'sufficient', 'pamzpygc.so'], ['auth', 'required', 'pambmehm.so']]
        idx = 3
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)

    def test_diversity_10(self):
        from ansible.modules.system.pamd import PamdService
        rules = [['password', 'optional', 'pamsboj.so'], ['session', 'optional', 'pamtfpt.so'], ['password', 'required', 'pamrnpha.so'], ['password', 'sufficient', 'pambftz.so']]
        idx = 2
        content = chr(10).join((' '.join(r) for r in rules))
        svc = PamdService(content)
        t, c, p = rules[idx]
        try:
            changed = svc.remove(t, c, p)
            result = 'OK' if changed and (not svc.has_rule(t, c, p)) else 'FAIL'
        except Exception as e:
            result = 'ERROR:' + type(e).__name__
        self.assertEqual('OK', result)
