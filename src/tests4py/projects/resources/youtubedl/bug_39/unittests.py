import unittest



class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('lihcxvtoi...', limit_length('lihcxvtoinprklecxipze', 12))

    def test_diversity_2(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('kinqyqispgw...', limit_length('kinqyqispgwbxlpaapcrs', 14))

    def test_diversity_3(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('gvtvi...', limit_length('gvtviyaoiotcu', 8))

    def test_diversity_4(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('uacvoirvpalfjiksa...', limit_length('uacvoirvpalfjiksadjtcgeqomc', 20))

    def test_diversity_5(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('rvkioqoselmdnmo...', limit_length('rvkioqoselmdnmohhddzrzgiheqzlgjbjus', 18))

    def test_diversity_6(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('ape...', limit_length('apevzqruiyxkylnyqifyikjlky', 6))

    def test_diversity_7(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('gypljnyejlxvu...', limit_length('gypljnyejlxvudjykpgilirqvsoel', 16))

    def test_diversity_8(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('lelmrvbhfdypezw...', limit_length('lelmrvbhfdypezwjhplmyotyczzwcd', 18))

    def test_diversity_9(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('mwwau...', limit_length('mwwaufigxlzhjfi', 8))

    def test_diversity_10(self):
        from youtube_dl.utils import limit_length
        self.assertEqual('qkjrmh...', limit_length('qkjrmhyveiavuijtlthkvs', 9))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('gzjka...', _limit('gzjkafqoubbjsmqavqrwudho', 8))

    def test_diversity_2(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('zrqbpi...', _limit('zrqbpiwlzzloiwffhqkya', 9))

    def test_diversity_3(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('law...', _limit('lawwpkecxgpfcaqkjo', 6))

    def test_diversity_4(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('tiyzcd...', _limit('tiyzcdlakkvttrvib', 9))

    def test_diversity_5(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('lfpxlswqv...', _limit('lfpxlswqvrrzhcnmyiceuckhwynph', 12))

    def test_diversity_6(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('mincogfcvus...', _limit('mincogfcvuswusfvzwt', 14))

    def test_diversity_7(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('jxxmnylfqhgsu...', _limit('jxxmnylfqhgsuyvhunwvicpmmruhkfn', 16))

    def test_diversity_8(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('qummyyzgzoc...', _limit('qummyyzgzocvcuxfrshktesfgdw', 14))

    def test_diversity_9(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('hfbqksqedwmqeml...', _limit('hfbqksqedwmqemlifcnrmwfpkjrkfyw', 18))

    def test_diversity_10(self):
        def _limit(s, length):
            ellipses = '...'
            if s is None:
                return None
            if len(s) > length:
                return s[:length - len(ellipses)] + ellipses
            return s
        self.assertEqual('plgoh...', _limit('plgohgycisqycamg', 8))
