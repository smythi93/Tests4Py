import unittest

from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://vvtm:zqiiq@wnfqjt.io:3995', 'http')
        self.assertEqual(b'dnZ0bTp6cWlpcQ==', creds)

    def test_diversity_2(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://nuevjzl:kggglou@oomms.io:6639', 'http')
        self.assertEqual(b'bnVldmp6bDprZ2dnbG91', creds)

    def test_diversity_3(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://bzmx:gtmrdepw@wtfr.io:8910', 'http')
        self.assertEqual(b'YnpteDpndG1yZGVwdw==', creds)

    def test_diversity_4(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://rehi:ubqgz@ciulwkw.com:6898', 'http')
        self.assertEqual(b'cmVoaTp1YnFneg==', creds)

    def test_diversity_5(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://pox:ehgiv@llt.com:1714', 'http')
        self.assertEqual(b'cG94OmVoZ2l2', creds)

    def test_diversity_6(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://izqczja:zmhh@ncjdn.com:4163', 'http')
        self.assertEqual(b'aXpxY3pqYTp6bWho', creds)

    def test_diversity_7(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://trhcdnt:fnsc@mdalts.com:8889', 'http')
        self.assertEqual(b'dHJoY2RudDpmbnNj', creds)

    def test_diversity_8(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://vzayq:dcoqaga@bvftcdc.com:6284', 'http')
        self.assertEqual(b'dnpheXE6ZGNvcWFnYQ==', creds)

    def test_diversity_9(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://rscthzot:xek@uba.com:1808', 'http')
        self.assertEqual(b'cnNjdGh6b3Q6eGVr', creds)

    def test_diversity_10(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://ooz:nfqsgwy@zaid.net:1632', 'http')
        self.assertEqual(b'b296Om5mcXNnd3k=', creds)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://ssxnr.net:1316', 'http')
        self.assertEqual(None, creds)

    def test_diversity_2(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://yidfub.net:3217', 'http')
        self.assertEqual(None, creds)

    def test_diversity_3(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://tvpwjj.io:4911', 'http')
        self.assertEqual(None, creds)

    def test_diversity_4(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://yynd.com:1875', 'http')
        self.assertEqual(None, creds)

    def test_diversity_5(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://tshkp.net:4208', 'http')
        self.assertEqual(None, creds)

    def test_diversity_6(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://cjp.net:9183', 'http')
        self.assertEqual(None, creds)

    def test_diversity_7(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://gkgbjogt.com:4225', 'http')
        self.assertEqual(None, creds)

    def test_diversity_8(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://jtaabs.net:9363', 'http')
        self.assertEqual(None, creds)

    def test_diversity_9(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://bbqnh.com:7675', 'http')
        self.assertEqual(None, creds)

    def test_diversity_10(self):
        mw = HttpProxyMiddleware.__new__(HttpProxyMiddleware)
        creds, proxy = mw._get_proxy('http://yuvzqkzx.io:7366', 'http')
        self.assertEqual(None, creds)
