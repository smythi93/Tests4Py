import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '912714', 'ext': 'm4a', 'title': 'uapzmn $T4PVAR hpefyu'})
        self.assertEqual('uapzmn $T4PVAR hpefyu.m4a', _fn)

    def test_diversity_2(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '440028', 'ext': 'm4a', 'title': 'ntkkn $T4PVAR nxrmz'})
        self.assertEqual('ntkkn $T4PVAR nxrmz.m4a', _fn)

    def test_diversity_3(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '216634', 'ext': 'mkv', 'title': 'ogas $T4PVAR drklx'})
        self.assertEqual('ogas $T4PVAR drklx.mkv', _fn)

    def test_diversity_4(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '732143', 'ext': 'webm', 'title': 'azth $T4PVAR mbjjxku'})
        self.assertEqual('azth $T4PVAR mbjjxku.webm', _fn)

    def test_diversity_5(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '422164', 'ext': 'webm', 'title': 'wxtz $T4PVAR uqt'})
        self.assertEqual('wxtz $T4PVAR uqt.webm', _fn)

    def test_diversity_6(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '363626', 'ext': 'webm', 'title': 'vrjcp $T4PVAR cmtqnyu'})
        self.assertEqual('vrjcp $T4PVAR cmtqnyu.webm', _fn)

    def test_diversity_7(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '415151', 'ext': 'mkv', 'title': 'tjivbvz $T4PVAR kwe'})
        self.assertEqual('tjivbvz $T4PVAR kwe.mkv', _fn)

    def test_diversity_8(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '810257', 'ext': 'mkv', 'title': 'hvj $T4PVAR sfzg'})
        self.assertEqual('hvj $T4PVAR sfzg.mkv', _fn)

    def test_diversity_9(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '883465', 'ext': 'mp4', 'title': 'fqydg $T4PVAR rsbfnb'})
        self.assertEqual('fqydg $T4PVAR rsbfnb.mp4', _fn)

    def test_diversity_10(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '564139', 'ext': 'm4a', 'title': 'nbm $T4PVAR wsgdyb'})
        self.assertEqual('nbm $T4PVAR wsgdyb.m4a', _fn)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '375895', 'ext': 'm4a', 'title': 'pwec clhcov'})
        self.assertEqual('pwec clhcov.m4a', _fn)

    def test_diversity_2(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s-%(id)s.%(ext)s'}).prepare_filename({'id': '571292', 'ext': 'mkv', 'title': 'rgdb gkws'})
        self.assertEqual('rgdb gkws-571292.mkv', _fn)

    def test_diversity_3(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '491902', 'ext': 'mkv', 'title': 'xgbuyod jtjq'})
        self.assertEqual('xgbuyod jtjq.mkv', _fn)

    def test_diversity_4(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s-%(id)s.%(ext)s'}).prepare_filename({'id': '323637', 'ext': 'm4a', 'title': 'ryknf nucqmfd'})
        self.assertEqual('ryknf nucqmfd-323637.m4a', _fn)

    def test_diversity_5(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s-%(id)s.%(ext)s'}).prepare_filename({'id': '267983', 'ext': 'm4a', 'title': 'aqhav qzpvxax'})
        self.assertEqual('aqhav qzpvxax-267983.m4a', _fn)

    def test_diversity_6(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s-%(id)s.%(ext)s'}).prepare_filename({'id': '879381', 'ext': 'mkv', 'title': 'jkbbplw esh'})
        self.assertEqual('jkbbplw esh-879381.mkv', _fn)

    def test_diversity_7(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s-%(id)s.%(ext)s'}).prepare_filename({'id': '444689', 'ext': 'mp4', 'title': 'nbjp iampvld'})
        self.assertEqual('nbjp iampvld-444689.mp4', _fn)

    def test_diversity_8(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '349986', 'ext': 'mp4', 'title': 'uxrzatz tozojsn'})
        self.assertEqual('uxrzatz tozojsn.mp4', _fn)

    def test_diversity_9(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s-%(id)s.%(ext)s'}).prepare_filename({'id': '345227', 'ext': 'mp4', 'title': 'gbxbntd xzhf'})
        self.assertEqual('gbxbntd xzhf-345227.mp4', _fn)

    def test_diversity_10(self):
        import os
        os.environ['T4PVAR'] = 'XPANDED'
        from youtube_dl import YoutubeDL
        _fn = YoutubeDL({'outtmpl': '%(title)s.%(ext)s'}).prepare_filename({'id': '714852', 'ext': 'm4a', 'title': 'ojiauwd yxrsroq'})
        self.assertEqual('ojiauwd yxrsroq.m4a', _fn)
