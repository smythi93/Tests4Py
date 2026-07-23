import unittest
import os
import tempfile
from tornado.web import Application, StaticFileHandler, HTTPError
from tornado.httputil import HTTPServerRequest, HTTPConnection
class _T4PFakeConn(HTTPConnection):

    def set_close_callback(self, cb):
        pass
def run_validate(rootname, reqpath):
    base = tempfile.mkdtemp()
    root = os.path.join(base, rootname)
    os.makedirs(root, exist_ok=True)
    app = Application()
    req = HTTPServerRequest(method='GET', uri='/x', connection=_T4PFakeConn())
    h = StaticFileHandler(app, req, path=root)
    h.path = reqpath
    absolute_path = h.get_absolute_path(root, reqpath)
    parent = os.path.dirname(absolute_path)
    if parent and (not os.path.isdir(parent)):
        os.makedirs(parent, exist_ok=True)
    with open(absolute_path, 'w') as fp:
        fp.write('data')
    try:
        h.validate_absolute_path(root, absolute_path)
        return 'OK'
    except HTTPError as e:
        return str(e.status_code)



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('403', run_validate('www', '../www_tk.txt'))

    def test_diversity_2(self):
        self.assertEqual('403', run_validate('public', '../public_bxvz.txt'))

    def test_diversity_3(self):
        self.assertEqual('403', run_validate('media', '../media_peb.txt'))

    def test_diversity_4(self):
        self.assertEqual('403', run_validate('assets', '../assetsyzpk.txt'))

    def test_diversity_5(self):
        self.assertEqual('403', run_validate('files', '../files_xltzyk.txt'))

    def test_diversity_6(self):
        self.assertEqual('403', run_validate('www', '../www_trikw.txt'))

    def test_diversity_7(self):
        self.assertEqual('403', run_validate('files', '../files_mwauqn.txt'))

    def test_diversity_8(self):
        self.assertEqual('403', run_validate('dist', '../dist_lawmxp.txt'))

    def test_diversity_9(self):
        self.assertEqual('403', run_validate('files', '../files_rjtze.txt'))

    def test_diversity_10(self):
        self.assertEqual('403', run_validate('assets', '../assets_frvfhf.txt'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('OK', run_validate('assets', 'csfl.txt'))

    def test_diversity_2(self):
        self.assertEqual('OK', run_validate('public', 'owjlnbgb.txt'))

    def test_diversity_3(self):
        self.assertEqual('OK', run_validate('files', 'hrkq.txt'))

    def test_diversity_4(self):
        self.assertEqual('OK', run_validate('public', 'dyjrye.txt'))

    def test_diversity_5(self):
        self.assertEqual('OK', run_validate('files', 'tweztir.txt'))

    def test_diversity_6(self):
        self.assertEqual('OK', run_validate('public', 'elqpgxq.txt'))

    def test_diversity_7(self):
        self.assertEqual('OK', run_validate('www', 'jewbkf.txt'))

    def test_diversity_8(self):
        self.assertEqual('OK', run_validate('dist', 'agntixlj.txt'))

    def test_diversity_9(self):
        self.assertEqual('OK', run_validate('files', 'jvyw.txt'))

    def test_diversity_10(self):
        self.assertEqual('OK', run_validate('assets', 'zgzcp.txt'))
