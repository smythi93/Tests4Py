import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'mqkfvrz', 'gnbpnjc', '*')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection mqkfvrz.gnbpnjc does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)

    def test_diversity_2(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'wqq', 'feoov', '*')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection wqq.feoov does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)

    def test_diversity_3(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'nqtzkka', 'tcdkbhc', '0.3.7')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection nqtzkka.tcdkbhc does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)

    def test_diversity_4(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'guj', 'ntwxc', '*')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection guj.ntwxc does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)

    def test_diversity_5(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'jll', 'hhmy', '*')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection jll.hhmy does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)

    def test_diversity_6(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'yutornc', 'lyu', '1.5.4')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection yutornc.lyu does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)

    def test_diversity_7(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'bfv', 'jjivhyh', '6.6.9')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection bfv.jjivhyh does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)

    def test_diversity_8(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'svnbbbp', 'fqvl', '7.3.0')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection svnbbbp.fqvl does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)

    def test_diversity_9(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'bcaeu', 'gnlpwxz', '*')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection bcaeu.gnlpwxz does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)

    def test_diversity_10(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('nomanifest', 'lckh', 'wao', '*')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Collection lckh.wao does not appear to have a MANIFEST.json. A MANIFEST.json is expected if the collection has been built and installed via ansible-galaxy.', actual)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'yfwotbx', 'wnss', '0.8.8')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection yfwotbx.wnss:0.8.8 on any of the galaxy servers', actual)

    def test_diversity_2(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'wmvd', 'tamsww', '7.0.4')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection wmvd.tamsww:7.0.4 on any of the galaxy servers', actual)

    def test_diversity_3(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'wdgcszt', 'gjsyg', '9.6.6')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection wdgcszt.gjsyg:9.6.6 on any of the galaxy servers', actual)

    def test_diversity_4(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'bvlzne', 'nqqrxqv', '9.4.8')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection bvlzne.nqqrxqv:9.4.8 on any of the galaxy servers', actual)

    def test_diversity_5(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'gaxj', 'bnotfmd', '6.1.4')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection gaxj.bnotfmd:6.1.4 on any of the galaxy servers', actual)

    def test_diversity_6(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'qvgzfki', 'jlhby', '5.6.4')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection qvgzfki.jlhby:5.6.4 on any of the galaxy servers', actual)

    def test_diversity_7(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'kbvmc', 'fjsvppt', '8.2.7')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection kbvmc.fjsvppt:8.2.7 on any of the galaxy servers', actual)

    def test_diversity_8(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'oruvl', 'tjr', '9.3.8')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection oruvl.tjr:9.3.8 on any of the galaxy servers', actual)

    def test_diversity_9(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'lipj', 'xijfmm', '3.9.9')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection lipj.xijfmm:3.9.9 on any of the galaxy servers', actual)

    def test_diversity_10(self):
        import os, json, tempfile
        from ansible.errors import AnsibleError
        from ansible.galaxy.collection import verify_collections
        mode, namespace, name, version = ('manifest', 'xfpcra', 'ctilrku', '8.2.3')
        root = tempfile.mkdtemp()
        cdir = os.path.join(root, namespace, name)
        os.makedirs(cdir)
        if mode == 'manifest':
            with open(os.path.join(cdir, 'MANIFEST.json'), 'w') as fh:
                json.dump({'collection_info': {'namespace': namespace, 'name': name, 'version': '1.0.0', 'dependencies': {}}}, fh)
        try:
            verify_collections([('%s.%s' % (namespace, name), version, None)], [root], [], False, False)
            actual = 'NO_ERROR'
        except AnsibleError as e:
            actual = e.message
        self.assertEqual('Failed to find remote collection xfpcra.ctilrku:8.2.3 on any of the galaxy servers', actual)
