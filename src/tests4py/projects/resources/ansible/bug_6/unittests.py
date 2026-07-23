import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'hycq', 'lqr', 'ekfnia.ogf', '*', '5.8.5')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_2(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'fzhlc', 'uhzrqpw', 'ojnvhxc.gilmoy', '*', '3.3.6')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_3(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'bqcr', 'wfik', 'lyfsdsv.blsvjw', '*', '9.6.2')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_4(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'qplpyl', 'nzb', 'oqr.dykyzj', '*', '8.9.3')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_5(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'qieydm', 'fiigbcu', 'dyu.vqqgr', '*', '1.0.7')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_6(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'rzxiodl', 'cmmrn', 'yzh.csm', '*', '9.7.5')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_7(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'gtgl', 'gcno', 'mtd.jmn', '*', '1.2.1')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_8(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'ucytdsy', 'oghhsl', 'zeckd.dqe', '*', '4.8.4')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_9(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'vyvkmxg', 'gffdlyb', 'xox.gkoh', '*', '0.5.7')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_10(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('unknown', 'cpjrcol', 'nzinubh', 'fnosyfh.egxax', '*', '3.3.2')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('match', 'qtbvmj', 'zygoe', 'bjwcc.wsykdq', '3.9.4', '3.9.4')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK 3.9.4', actual)

    def test_diversity_2(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('match', 'lsvc', 'oyxds', 'zeo.amuexot', '4.9.2', '4.9.2')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK 4.9.2', actual)

    def test_diversity_3(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('wild', 'ivdds', 'trhzpy', 'crejmi.jjiigsb', '*', '*')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_4(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('wild', 'puvk', 'kkhuz', 'lclh.hlntp', '*', '*')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_5(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('wild', 'uqq', 'imio', 'uaatssh.psukwje', '*', '*')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_6(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('wild', 'gxihnwj', 'jrc', 'nlqym.xljc', '*', '*')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_7(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('wild', 'sjpqxxq', 'trbrux', 'xknmka.tqev', '*', '*')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_8(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('match', 'rsax', 'wxyqspg', 'dlsd.ywazt', '1.0.1', '1.0.1')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK 1.0.1', actual)

    def test_diversity_9(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('wild', 'seoosii', 'isltxmv', 'boiamzf.jihkzm', '*', '*')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK *', actual)

    def test_diversity_10(self):
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import CollectionRequirement
        mode, ns, name, parent, have, req = ('match', 'dxepkhd', 'pynrkr', 'etwbxrq.nhcf', '8.5.3', '8.5.3')
        obj = CollectionRequirement(ns, name, None, 'https://galaxy.com', [have], have, False, skip=True)
        try:
            obj.add_requirement(parent, req)
            actual = 'OK %s' % obj.latest_version
        except AnsibleError:
            actual = 'ERROR:AnsibleError'
        except Exception as e:
            actual = 'OTHER:%s' % type(e).__name__
        self.assertEqual('OK 8.5.3', actual)
