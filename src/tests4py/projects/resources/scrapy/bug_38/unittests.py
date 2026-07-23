import unittest
from urllib.parse import urlparse, parse_qs

# noinspection PyUnresolvedReferences
from scrapy.http import HtmlResponse, FormRequest


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="lsbsjp" value="pisq"><input type="image" name="mzpfp" value="mlgjsxw"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('lsbsjp=pisq&mzpfp=mlgjsxw', canon)

    def test_diversity_2(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="ndccdld" value="helkhg"><input type="image" name="grscno" value="tawly"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('grscno=tawly&ndccdld=helkhg', canon)

    def test_diversity_3(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="vatnx" value="xwpajry"><input type="image" name="epo" value="ddn"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('epo=ddn&vatnx=xwpajry', canon)

    def test_diversity_4(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="rsfigtu" value="srfgka"><input type="image" name="sjcox" value="sphqugk"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('rsfigtu=srfgka&sjcox=sphqugk', canon)

    def test_diversity_5(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="lekspi" value="yapxf"><input type="image" name="bepjl" value="ykq"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('bepjl=ykq&lekspi=yapxf', canon)

    def test_diversity_6(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="fjcw" value="pgwcxbq"><input type="image" name="ijhtlk" value="ytleyt"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('fjcw=pgwcxbq&ijhtlk=ytleyt', canon)

    def test_diversity_7(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="wvlzgfk" value="yvw"><input type="image" name="hgehagi" value="dbv"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('hgehagi=dbv&wvlzgfk=yvw', canon)

    def test_diversity_8(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="tbx" value="xrrxke"><input type="image" name="exqy" value="fdhwbqy"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('exqy=fdhwbqy&tbx=xrrxke', canon)

    def test_diversity_9(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="lnwngaz" value="vpq"><input type="image" name="agtnaiv" value="tzj"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('agtnaiv=tzj&lnwngaz=vpq', canon)

    def test_diversity_10(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="lteopnk" value="zaw"><input type="image" name="izwer" value="zinavuh"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('izwer=zinavuh&lteopnk=zaw', canon)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="ucyid" value="iqa"><input type="submit" name="wdfpdxb" value="gaywmgl"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('ucyid=iqa&wdfpdxb=gaywmgl', canon)

    def test_diversity_2(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="mwgv" value="eyljqe"><input type="submit" name="vqgba" value="eig"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('mwgv=eyljqe&vqgba=eig', canon)

    def test_diversity_3(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="iwmwrmx" value="rrpb"><input type="submit" name="gnt" value="nnbiul"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('gnt=nnbiul&iwmwrmx=rrpb', canon)

    def test_diversity_4(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="cwv" value="yvjbih"><input type="submit" name="yozpa" value="gycmh"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('cwv=yvjbih&yozpa=gycmh', canon)

    def test_diversity_5(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="espqk" value="wjwq"><input type="submit" name="zdfe" value="cchxfjg"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('espqk=wjwq&zdfe=cchxfjg', canon)

    def test_diversity_6(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="rws" value="evpzdy"><input type="submit" name="lzrlum" value="xtxdpp"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('lzrlum=xtxdpp&rws=evpzdy', canon)

    def test_diversity_7(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="nkxvobw" value="tbrkgm"><input type="submit" name="pqe" value="dwv"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('nkxvobw=tbrkgm&pqe=dwv', canon)

    def test_diversity_8(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="klpu" value="qgnrave"><input type="submit" name="xugey" value="pomn"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('klpu=qgnrave&xugey=pomn', canon)

    def test_diversity_9(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="gghz" value="yhlm"><input type="submit" name="wwjr" value="dphxzos"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('gghz=yhlm&wwjr=dphxzos', canon)

    def test_diversity_10(self):
        response = HtmlResponse(url='http://example.com', body=b'<form><input type="text" name="vzu" value="wjytpw"><input type="submit" name="xvw" value="ynt"></form>', encoding='utf-8')
        req = FormRequest.from_response(response)
        params = parse_qs(urlparse(req.url).query)
        canon = '&'.join('%s=%s' % (k, v) for k in sorted(params) for v in params[k])
        self.assertEqual('vzu=wjytpw&xvw=ynt', canon)

