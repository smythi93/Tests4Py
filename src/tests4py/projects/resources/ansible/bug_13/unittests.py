import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'https://qflfp/wljre/ihvqdzp-0.3.1.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['https://qflfp/wljre/ihvqdzp-0.3.1.tar.gz', '*', None]], actual)

    def test_diversity_2(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'http://xunphqn/vcdqk/dxbpe-9.4.1.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['http://xunphqn/vcdqk/dxbpe-9.4.1.tar.gz', '*', None]], actual)

    def test_diversity_3(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'http://oiwfqeb/tfvwg/wybdmi-7.3.5.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['http://oiwfqeb/tfvwg/wybdmi-7.3.5.tar.gz', '*', None]], actual)

    def test_diversity_4(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'http://xbnlz/qipmvnz/mps-1.7.7.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['http://xbnlz/qipmvnz/mps-1.7.7.tar.gz', '*', None]], actual)

    def test_diversity_5(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'http://djufohp/ogts/btr-3.1.3.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['http://djufohp/ogts/btr-3.1.3.tar.gz', '*', None]], actual)

    def test_diversity_6(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'https://dtqq/lmvfono/vaqcg-9.4.7.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['https://dtqq/lmvfono/vaqcg-9.4.7.tar.gz', '*', None]], actual)

    def test_diversity_7(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'http://erg/nrepcz/yvoxjy-9.5.3.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['http://erg/nrepcz/yvoxjy-9.5.3.tar.gz', '*', None]], actual)

    def test_diversity_8(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'https://shwngg/ggqrutf/vgfjjl-7.6.5.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['https://shwngg/ggqrutf/vgfjjl-7.6.5.tar.gz', '*', None]], actual)

    def test_diversity_9(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'http://suoieb/vujn/gzdxvxf-3.7.7.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['http://suoieb/vujn/gzdxvxf-3.7.7.tar.gz', '*', None]], actual)

    def test_diversity_10(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'https://knlufv/bilqqmv/mnfphg-1.1.1.tar.gz'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['https://knlufv/bilqqmv/mnfphg-1.1.1.tar.gz', '*', None]], actual)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'mgawf.nyaqdq'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['mgawf.nyaqdq', '*', None]], actual)

    def test_diversity_2(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'xadfjn.nidkbf'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['xadfjn.nidkbf', '*', None]], actual)

    def test_diversity_3(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'hrfjaie.ecgz:7.1.3'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['hrfjaie.ecgz', '7.1.3', None]], actual)

    def test_diversity_4(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'diipnwb.cer'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['diipnwb.cer', '*', None]], actual)

    def test_diversity_5(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'gedaon.obb:1.6.6'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['gedaon.obb', '1.6.6', None]], actual)

    def test_diversity_6(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'nbagamx.gzzro:8.9.8'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['nbagamx.gzzro', '8.9.8', None]], actual)

    def test_diversity_7(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'kyempcm.vwv'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['kyempcm.vwv', '*', None]], actual)

    def test_diversity_8(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'vezote.iwq:6.8.4'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['vezote.iwq', '6.8.4', None]], actual)

    def test_diversity_9(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'zztxun.cmege'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['zztxun.cmege', '*', None]], actual)

    def test_diversity_10(self):
        import contextlib, io, json, tempfile
        from unittest import mock
        import ansible.cli.galaxy
        from ansible.cli.galaxy import GalaxyCLI
        from ansible.utils import context_objects as co
        collection_input = 'seao.wei'
        co.GlobalCLIArgs._Singleton__instance = None
        output_dir = tempfile.mkdtemp()
        captured = {}
        def fake_install(requirements, *a, **kw):
            captured['requirements'] = requirements
        with mock.patch.object(ansible.cli.galaxy, 'install_collections', side_effect=fake_install):
            buf = io.StringIO()
            try:
                with contextlib.redirect_stdout(buf):
                    GalaxyCLI(args=['ansible-galaxy', 'collection', 'install', collection_input, '--collections-path', output_dir]).run()
            except SystemExit:
                pass
        actual = json.loads(json.dumps(captured.get('requirements')))
        self.assertEqual([['seao.wei', '*', None]], actual)
