import unittest



class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(40028, struct_unpack('!H', struct.pack('!H', 40028))[0])

    def test_diversity_2(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(7678471501789694888, struct_unpack('!Q', struct.pack('!Q', 7678471501789694888))[0])

    def test_diversity_3(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(90, struct_unpack('!B', struct.pack('!B', 90))[0])

    def test_diversity_4(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(663875320, struct_unpack('!I', struct.pack('!I', 663875320))[0])

    def test_diversity_5(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(60883, struct_unpack('!H', struct.pack('!H', 60883))[0])

    def test_diversity_6(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(197, struct_unpack('!B', struct.pack('!B', 197))[0])

    def test_diversity_7(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(2129688544, struct_unpack('!I', struct.pack('!I', 2129688544))[0])

    def test_diversity_8(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(5454313257518522816, struct_unpack('!Q', struct.pack('!Q', 5454313257518522816))[0])

    def test_diversity_9(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(95, struct_unpack('!B', struct.pack('!B', 95))[0])

    def test_diversity_10(self):
        import struct
        from youtube_dl.utils import struct_unpack
        self.assertEqual(14186696757779471686, struct_unpack('!Q', struct.pack('!Q', 14186696757779471686))[0])


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        import struct
        self.assertEqual(248, struct.unpack('!B', struct.pack('!B', 248))[0])

    def test_diversity_2(self):
        import struct
        self.assertEqual(11825156822349038587, struct.unpack('!Q', struct.pack('!Q', 11825156822349038587))[0])

    def test_diversity_3(self):
        import struct
        self.assertEqual(4137753490, struct.unpack('!I', struct.pack('!I', 4137753490))[0])

    def test_diversity_4(self):
        import struct
        self.assertEqual(4174413472, struct.unpack('!I', struct.pack('!I', 4174413472))[0])

    def test_diversity_5(self):
        import struct
        self.assertEqual(303971524, struct.unpack('!I', struct.pack('!I', 303971524))[0])

    def test_diversity_6(self):
        import struct
        self.assertEqual(14820154409811446657, struct.unpack('!Q', struct.pack('!Q', 14820154409811446657))[0])

    def test_diversity_7(self):
        import struct
        self.assertEqual(11490, struct.unpack('!H', struct.pack('!H', 11490))[0])

    def test_diversity_8(self):
        import struct
        self.assertEqual(1979267679, struct.unpack('!I', struct.pack('!I', 1979267679))[0])

    def test_diversity_9(self):
        import struct
        self.assertEqual(3678668333, struct.unpack('!I', struct.pack('!I', 3678668333))[0])

    def test_diversity_10(self):
        import struct
        self.assertEqual(3724338189944670516, struct.unpack('!Q', struct.pack('!Q', 3724338189944670516))[0])
