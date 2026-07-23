import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(257);return false;">4:17</a> - spfw XvbRobF dXhIRbTh<br /><a href="#" onclick="yt.www.watch.player.seekTo(1792);return false;">29:52</a> - VaBtCq UXH<br /><a href="#" onclick="yt.www.watch.player.seekTo(1805);return false;">30:05</a> - epPyZGiT rAim', 1991)
        self.assertEqual([{'start_time': 257.0, 'end_time': 1792.0, 'title': 'spfw XvbRobF dXhIRbTh'}, {'start_time': 1792.0, 'end_time': 1805.0, 'title': 'VaBtCq UXH'}, {'start_time': 1805.0, 'end_time': 1991, 'title': 'epPyZGiT rAim'}], _res)

    def test_diversity_2(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(1356);return false;">22:36</a> - VPJ nRRBCC<br /><a href="#" onclick="yt.www.watch.player.seekTo(1416);return false;">23:36</a> - qkQO', 1562)
        self.assertEqual([{'start_time': 1356.0, 'end_time': 1416.0, 'title': 'VPJ nRRBCC'}, {'start_time': 1416.0, 'end_time': 1562, 'title': 'qkQO'}], _res)

    def test_diversity_3(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(197);return false;">3:17</a> - bwfh DXCAH pMC', 210)
        self.assertEqual([{'start_time': 197.0, 'end_time': 210, 'title': 'bwfh DXCAH pMC'}], _res)

    def test_diversity_4(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(2011);return false;">33:31</a> - uCzbb', 2419)
        self.assertEqual([{'start_time': 2011.0, 'end_time': 2419, 'title': 'uCzbb'}], _res)

    def test_diversity_5(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(1567);return false;">26:07</a> - CLTyaxwu<br /><a href="#" onclick="yt.www.watch.player.seekTo(2013);return false;">33:33</a> - AmtxWwc AmjUpV', 2458)
        self.assertEqual([{'start_time': 1567.0, 'end_time': 2013.0, 'title': 'CLTyaxwu'}, {'start_time': 2013.0, 'end_time': 2458, 'title': 'AmtxWwc AmjUpV'}], _res)

    def test_diversity_6(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(2140);return false;">35:40</a> - ade<br /><a href="#" onclick="yt.www.watch.player.seekTo(2338);return false;">38:58</a> - vHCOrvz<br /><a href="#" onclick="yt.www.watch.player.seekTo(2347);return false;">39:07</a> - MYFrcw', 2366)
        self.assertEqual([{'start_time': 2140.0, 'end_time': 2338.0, 'title': 'ade'}, {'start_time': 2338.0, 'end_time': 2347.0, 'title': 'vHCOrvz'}, {'start_time': 2347.0, 'end_time': 2366, 'title': 'MYFrcw'}], _res)

    def test_diversity_7(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(477);return false;">7:57</a> - lrhVmSw RDfnKJC TsD<br /><a href="#" onclick="yt.www.watch.player.seekTo(2260);return false;">37:40</a> - qFWd ikDBB wljWRZD<br /><a href="#" onclick="yt.www.watch.player.seekTo(2789);return false;">46:29</a> - YZV', 3056)
        self.assertEqual([{'start_time': 477.0, 'end_time': 2260.0, 'title': 'lrhVmSw RDfnKJC TsD'}, {'start_time': 2260.0, 'end_time': 2789.0, 'title': 'qFWd ikDBB wljWRZD'}, {'start_time': 2789.0, 'end_time': 3056, 'title': 'YZV'}], _res)

    def test_diversity_8(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(1202);return false;">20:02</a> - YomxEyB<br /><a href="#" onclick="yt.www.watch.player.seekTo(1482);return false;">24:42</a> - aNUr<br /><a href="#" onclick="yt.www.watch.player.seekTo(1645);return false;">27:25</a> - MkcJss mEiXJG vxOfC', 1948)
        self.assertEqual([{'start_time': 1202.0, 'end_time': 1482.0, 'title': 'YomxEyB'}, {'start_time': 1482.0, 'end_time': 1645.0, 'title': 'aNUr'}, {'start_time': 1645.0, 'end_time': 1948, 'title': 'MkcJss mEiXJG vxOfC'}], _res)

    def test_diversity_9(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(259);return false;">4:19</a> - lMUy<br /><a href="#" onclick="yt.www.watch.player.seekTo(370);return false;">6:10</a> - XDMvv geilOcft tCywpX', 380)
        self.assertEqual([{'start_time': 259.0, 'end_time': 370.0, 'title': 'lMUy'}, {'start_time': 370.0, 'end_time': 380, 'title': 'XDMvv geilOcft tCywpX'}], _res)

    def test_diversity_10(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters_from_description('<a href="#" onclick="yt.www.watch.player.seekTo(133);return false;">2:13</a> - BfD RrVEj<br /><a href="#" onclick="yt.www.watch.player.seekTo(1514);return false;">25:14</a> - NtpIwqbd rULU<br /><a href="#" onclick="yt.www.watch.player.seekTo(2029);return false;">33:49</a> - aXgbmkza', 2294)
        self.assertEqual([{'start_time': 133.0, 'end_time': 1514.0, 'title': 'BfD RrVEj'}, {'start_time': 1514.0, 'end_time': 2029.0, 'title': 'NtpIwqbd rULU'}, {'start_time': 2029.0, 'end_time': 2294, 'title': 'aXgbmkza'}], _res)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(503);return false;">8:23</a> - ogzuhQ GgisHds<br /><a href="#" onclick="yt.www.watch.player.seekTo(1102);return false;">18:22</a> - lYw vwyym InHw<br /><a href="#" onclick="yt.www.watch.player.seekTo(2221);return false;">37:01</a> - VHNoH', 2555)
        self.assertEqual([{'start_time': 503.0, 'end_time': 1102.0, 'title': 'ogzuhQ GgisHds'}, {'start_time': 1102.0, 'end_time': 2221.0, 'title': 'lYw vwyym InHw'}, {'start_time': 2221.0, 'end_time': 2555, 'title': 'VHNoH'}], _res)

    def test_diversity_2(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(695);return false;">11:35</a> - dlXaT', 1161)
        self.assertEqual([{'start_time': 695.0, 'end_time': 1161, 'title': 'dlXaT'}], _res)

    def test_diversity_3(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(1359);return false;">22:39</a> - AOlpIMq hIBzsTX<br /><a href="#" onclick="yt.www.watch.player.seekTo(2940);return false;">49:00</a> - uIba YiSapEf yzktOWu<br /><a href="#" onclick="yt.www.watch.player.seekTo(2965);return false;">49:25</a> - NOvJJ qUjIBlV oDqrc', 3249)
        self.assertEqual([{'start_time': 1359.0, 'end_time': 2940.0, 'title': 'AOlpIMq hIBzsTX'}, {'start_time': 2940.0, 'end_time': 2965.0, 'title': 'uIba YiSapEf yzktOWu'}, {'start_time': 2965.0, 'end_time': 3249, 'title': 'NOvJJ qUjIBlV oDqrc'}], _res)

    def test_diversity_4(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(529);return false;">8:49</a> - xtIFJJwU eddiQzg<br /><a href="#" onclick="yt.www.watch.player.seekTo(791);return false;">13:11</a> - OMLHA', 882)
        self.assertEqual([{'start_time': 529.0, 'end_time': 791.0, 'title': 'xtIFJJwU eddiQzg'}, {'start_time': 791.0, 'end_time': 882, 'title': 'OMLHA'}], _res)

    def test_diversity_5(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(837);return false;">13:57</a> - Ssepymb<br /><a href="#" onclick="yt.www.watch.player.seekTo(2679);return false;">44:39</a> - SSleLs JpjjF oPn<br /><a href="#" onclick="yt.www.watch.player.seekTo(2951);return false;">49:11</a> - ipowY mxPg', 3205)
        self.assertEqual([{'start_time': 837.0, 'end_time': 2679.0, 'title': 'Ssepymb'}, {'start_time': 2679.0, 'end_time': 2951.0, 'title': 'SSleLs JpjjF oPn'}, {'start_time': 2951.0, 'end_time': 3205, 'title': 'ipowY mxPg'}], _res)

    def test_diversity_6(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(45);return false;">0:45</a> - OlHbqOuy McDe odk<br /><a href="#" onclick="yt.www.watch.player.seekTo(450);return false;">7:30</a> - MVQ<br /><a href="#" onclick="yt.www.watch.player.seekTo(1496);return false;">24:56</a> - uHOP RPwbT', 1651)
        self.assertEqual([{'start_time': 45.0, 'end_time': 450.0, 'title': 'OlHbqOuy McDe odk'}, {'start_time': 450.0, 'end_time': 1496.0, 'title': 'MVQ'}, {'start_time': 1496.0, 'end_time': 1651, 'title': 'uHOP RPwbT'}], _res)

    def test_diversity_7(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(522);return false;">8:42</a> - lDfghzHi xGnXIvR<br /><a href="#" onclick="yt.www.watch.player.seekTo(537);return false;">8:57</a> - IrQoRh', 823)
        self.assertEqual([{'start_time': 522.0, 'end_time': 537.0, 'title': 'lDfghzHi xGnXIvR'}, {'start_time': 537.0, 'end_time': 823, 'title': 'IrQoRh'}], _res)

    def test_diversity_8(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(472);return false;">7:52</a> - jwtm tadVJpc<br /><a href="#" onclick="yt.www.watch.player.seekTo(941);return false;">15:41</a> - wViAdNL iTkGIrw<br /><a href="#" onclick="yt.www.watch.player.seekTo(2952);return false;">49:12</a> - zAEY Tvb rweF', 3380)
        self.assertEqual([{'start_time': 472.0, 'end_time': 941.0, 'title': 'jwtm tadVJpc'}, {'start_time': 941.0, 'end_time': 2952.0, 'title': 'wViAdNL iTkGIrw'}, {'start_time': 2952.0, 'end_time': 3380, 'title': 'zAEY Tvb rweF'}], _res)

    def test_diversity_9(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(1190);return false;">19:50</a> - hgeH<br /><a href="#" onclick="yt.www.watch.player.seekTo(2319);return false;">38:39</a> - zIAppX', 2402)
        self.assertEqual([{'start_time': 1190.0, 'end_time': 2319.0, 'title': 'hgeH'}, {'start_time': 2319.0, 'end_time': 2402, 'title': 'zIAppX'}], _res)

    def test_diversity_10(self):
        from youtube_dl.extractor import YoutubeIE
        _res = YoutubeIE._extract_chapters('<a href="#" onclick="yt.www.watch.player.seekTo(1769);return false;">29:29</a> - MzoTJpy uEhjrs FFrKg', 1842)
        self.assertEqual([{'start_time': 1769.0, 'end_time': 1842, 'title': 'MzoTJpy uEhjrs FFrKg'}], _res)
