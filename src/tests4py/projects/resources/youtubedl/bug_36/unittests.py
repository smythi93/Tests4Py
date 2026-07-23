import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/eabipoxw?koixrrf=thnso#!/video/embed?v=527213022449336'))

    def test_diversity_2(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/nddzc?gpzopghh=vgut#!/video/embed?v=736575035113129'))

    def test_diversity_3(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/gnjwbduo?kvvute=iocs#!/photo.php?video_id=900638231843219'))

    def test_diversity_4(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/zyxj?iaibyouq=rmbu#!/video/video.php?video_id=977157942369240'))

    def test_diversity_5(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/rtlbua?trufhkxj=uqql#!/photo.php?v=213214628576462'))

    def test_diversity_6(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/sqssdcaa?ypjev=fudthuz#!/video/video.php?video_id=842851343720927'))

    def test_diversity_7(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/znjygqlk?brbk=joav#!/video/video.php?video_id=559667798650059'))

    def test_diversity_8(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/tmwq?vccjf=kykn#!/photo.php?video_id=403177462768822'))

    def test_diversity_9(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/dtrxnmutk?gacikld=enxuin#!/photo.php?video_id=192419036571183'))

    def test_diversity_10(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/gferdmxk?lpblcnusb=aouuwtbr#!/video/video.php?video_id=535730132549174'))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/baiiy#!/video/embed?video_id=36057902775328'))

    def test_diversity_2(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/photo.php?v=832259077203398'))

    def test_diversity_3(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/vauboaws#!/video/video.php?video_id=742953139361961'))

    def test_diversity_4(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/photo.php?video_id=447925729823448'))

    def test_diversity_5(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/video/embed?v=871855896968490'))

    def test_diversity_6(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/kowq#!/photo.php?video_id=310450376806320'))

    def test_diversity_7(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/photo.php?video_id=164795643693522'))

    def test_diversity_8(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/video/video.php?video_id=797887815289023'))

    def test_diversity_9(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/bntmash#!/video/embed?video_id=59411368631003'))

    def test_diversity_10(self):
        from youtube_dl.extractor.facebook import FacebookIE
        self.assertEqual(True, FacebookIE.suitable('https://www.facebook.com/photo.php?v=976835304582719'))
