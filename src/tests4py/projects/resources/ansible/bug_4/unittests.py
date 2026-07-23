import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = '{{rgl}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)

    def test_diversity_2(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = '{{rrlu}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)

    def test_diversity_3(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'yeop.{{kavoyu}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)

    def test_diversity_4(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'llducj.{{ixrlp}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)

    def test_diversity_5(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'heq.{{lupo}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)

    def test_diversity_6(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'nivn.{{qjbx}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)

    def test_diversity_7(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = '{{ihf}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)

    def test_diversity_8(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = '{{ydfq}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)

    def test_diversity_9(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = '{{sokmdy}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)

    def test_diversity_10(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'cdjy.{{swiu}}'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('WARN', actual)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'dutiu.qamps'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)

    def test_diversity_2(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'ukq.gqjqua'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)

    def test_diversity_3(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'kdaa'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)

    def test_diversity_4(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'eyarg'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)

    def test_diversity_5(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'frn'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)

    def test_diversity_6(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'zyw.hudzw'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)

    def test_diversity_7(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'grz'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)

    def test_diversity_8(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'xpcl'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)

    def test_diversity_9(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'jwnjss'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)

    def test_diversity_10(self):
        import io, contextlib
        from ansible.playbook.collectionsearch import CollectionSearch
        name = 'vlcji.ajpyj'
        cs = CollectionSearch()
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            result = cs._load_collections(None, [name])
        err = buf.getvalue()
        actual = 'WARN' if 'is not templatable' in err and name in err else 'NOWARN'
        self.assertEqual('NOWARN', actual)
