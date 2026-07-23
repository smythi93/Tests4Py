import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:51:32,000 --> 00:54:03,000\nznmkcx htzsjlzl\n\n2\n00:53:55,000 --> 00:56:25,000\npevvyxf\n\n3\n00:06:40,000 --> 00:08:50,000\nvarvuld\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="3092" end="3243">znmkcx htzsjlzl</p>\n<p begin="3235" end="3385">pevvyxf</p>\n<p begin="400" end="530">varvuld</p>\n</div></body></tt>'.encode('utf-8')))

    def test_diversity_2(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:06:06,000 --> 00:06:50,000\nvaz fgop\n\n2\n00:13:44,000 --> 00:16:36,000\nina iuvj\n\n3\n00:13:08,000 --> 00:15:57,000\ngxofjl\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="366" end="410">vaz fgop</p>\n<p begin="824" end="996">ina iuvj</p>\n<p begin="788" end="957">gxofjl</p>\n</div></body></tt>'.encode('utf-8')))

    def test_diversity_3(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:19:32,000 --> 00:21:31,000\nuazyzitl ckc\n\n2\n00:54:38,000 --> 00:57:08,000\npsxbxa\n\n3\n00:50:14,000 --> 00:51:41,000\nbph\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="1172" end="1291">uazyzitl ckc</p>\n<p begin="3278" end="3428">psxbxa</p>\n<p begin="3014" end="3101">bph</p>\n</div></body></tt>'.encode('utf-8')))

    def test_diversity_4(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:33:12,000 --> 00:34:29,000\nkcpokqas\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="1992" end="2069">kcpokqas</p>\n</div></body></tt>'.encode('utf-8')))

    def test_diversity_5(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:29:37,000 --> 00:32:21,000\nctmmjpkp\n\n2\n00:07:27,000 --> 00:09:38,000\nhnmaulsl\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="1777" end="1941">ctmmjpkp</p>\n<p begin="447" end="578">hnmaulsl</p>\n</div></body></tt>'.encode('utf-8')))

    def test_diversity_6(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:10:22,000 --> 00:13:13,000\narx\n\n2\n00:36:55,000 --> 00:37:22,000\nbpyt tuadjft\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="622" end="793">arx</p>\n<p begin="2215" end="2242">bpyt tuadjft</p>\n</div></body></tt>'.encode('utf-8')))

    def test_diversity_7(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:10:18,000 --> 00:12:03,000\nszbh jwxvxn\n\n2\n00:25:40,000 --> 00:26:16,000\ntweti xozp\n\n3\n00:18:36,000 --> 00:19:37,000\nmdz\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="618" end="723">szbh jwxvxn</p>\n<p begin="1540" end="1576">tweti xozp</p>\n<p begin="1116" end="1177">mdz</p>\n</div></body></tt>'.encode('utf-8')))

    def test_diversity_8(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:22:26,000 --> 00:25:30,000\nasvpus\n\n2\n00:28:29,000 --> 00:29:50,000\nhsvpdcp bgjlz\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="1346" end="1530">asvpus</p>\n<p begin="1709" end="1790">hsvpdcp bgjlz</p>\n</div></body></tt>'.encode('utf-8')))

    def test_diversity_9(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:47:15,000 --> 00:47:42,000\ncyut vpomje\n\n2\n00:22:18,000 --> 00:24:17,000\nlmq ddue\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="2835" end="2862">cyut vpomje</p>\n<p begin="1338" end="1457">lmq ddue</p>\n</div></body></tt>'.encode('utf-8')))

    def test_diversity_10(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:36:41,000 --> 00:37:18,000\nvjyeur uja\n\n2\n00:53:36,000 --> 00:56:28,000\ndloye zxkp\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="2201" end="2238">vjyeur uja</p>\n<p begin="3216" end="3388">dloye zxkp</p>\n</div></body></tt>'.encode('utf-8')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:24:16,000 --> 00:25:25,000\ntitmi xvlmiohv\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="1456" end="1525">titmi xvlmiohv</p>\n</div></body></tt>'))

    def test_diversity_2(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:14:01,000 --> 00:15:57,000\nkggztk\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="841" end="957">kggztk</p>\n</div></body></tt>'))

    def test_diversity_3(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:52:14,000 --> 00:54:48,000\nappx\n\n2\n00:41:25,000 --> 00:44:44,000\nguhqtat tyn\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="3134" end="3288">appx</p>\n<p begin="2485" end="2684">guhqtat tyn</p>\n</div></body></tt>'))

    def test_diversity_4(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:34:51,000 --> 00:36:16,000\nmwau msnq\n\n2\n00:50:02,000 --> 00:52:17,000\nmxhvoioj\n\n3\n00:38:00,000 --> 00:38:35,000\nzpvrrvha\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="2091" end="2176">mwau msnq</p>\n<p begin="3002" end="3137">mxhvoioj</p>\n<p begin="2280" end="2315">zpvrrvha</p>\n</div></body></tt>'))

    def test_diversity_5(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:54:20,000 --> 00:56:31,000\nnpowivn\n\n2\n00:46:22,000 --> 00:47:48,000\npmyl uewpvtl\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="3260" end="3391">npowivn</p>\n<p begin="2782" end="2868">pmyl uewpvtl</p>\n</div></body></tt>'))

    def test_diversity_6(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:29:49,000 --> 00:30:38,000\nvqer oeca\n\n2\n00:22:43,000 --> 00:25:45,000\nxqwnp\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="1789" end="1838">vqer oeca</p>\n<p begin="1363" end="1545">xqwnp</p>\n</div></body></tt>'))

    def test_diversity_7(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:32:15,000 --> 00:34:27,000\nplp dlh\n\n2\n00:01:13,000 --> 00:04:05,000\nhgf\n\n3\n00:52:25,000 --> 00:55:15,000\njiodvf bosevqhe\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="1935" end="2067">plp dlh</p>\n<p begin="73" end="245">hgf</p>\n<p begin="3145" end="3315">jiodvf bosevqhe</p>\n</div></body></tt>'))

    def test_diversity_8(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:45:58,000 --> 00:46:24,000\niba yicn\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="2758" end="2784">iba yicn</p>\n</div></body></tt>'))

    def test_diversity_9(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:27:24,000 --> 00:27:28,000\nlkibngqz\n\n2\n00:46:01,000 --> 00:48:39,000\nbuhxuhty\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="1644" end="1648">lkibngqz</p>\n<p begin="2761" end="2919">buhxuhty</p>\n</div></body></tt>'))

    def test_diversity_10(self):
        from youtube_dl.utils import dfxp2srt
        self.assertEqual('1\n00:18:59,000 --> 00:20:46,000\nzlrxijus\n\n', dfxp2srt('<?xml version="1.0" encoding="UTF-8"?>\n<tt xmlns="http://www.w3.org/ns/ttml" xml:lang="en">\n<body><div xml:lang="en">\n<p begin="1139" end="1246">zlrxijus</p>\n</div></body></tt>'))
