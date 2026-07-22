import unittest

# noinspection PyUnresolvedReferences
from scrapy.utils.response import response_status_message


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('466 Unknown Status', response_status_message(466))
        self.assertEqual('213 Unknown Status', response_status_message(213))
        self.assertEqual('268 Unknown Status', response_status_message(268))

    def test_diversity_2(self):
        self.assertEqual('516 Unknown Status', response_status_message(516))
        self.assertEqual('288 Unknown Status', response_status_message(288))
        self.assertEqual('460 Unknown Status', response_status_message(460))

    def test_diversity_3(self):
        self.assertEqual('337 Unknown Status', response_status_message(337))
        self.assertEqual('575 Unknown Status', response_status_message(575))
        self.assertEqual('352 Unknown Status', response_status_message(352))

    def test_diversity_4(self):
        self.assertEqual('545 Unknown Status', response_status_message(545))
        self.assertEqual('564 Unknown Status', response_status_message(564))
        self.assertEqual('325 Unknown Status', response_status_message(325))

    def test_diversity_5(self):
        self.assertEqual('531 Unknown Status', response_status_message(531))
        self.assertEqual('390 Unknown Status', response_status_message(390))
        self.assertEqual('458 Unknown Status', response_status_message(458))

    def test_diversity_6(self):
        self.assertEqual('572 Unknown Status', response_status_message(572))
        self.assertEqual('330 Unknown Status', response_status_message(330))
        self.assertEqual('550 Unknown Status', response_status_message(550))

    def test_diversity_7(self):
        self.assertEqual('479 Unknown Status', response_status_message(479))
        self.assertEqual('317 Unknown Status', response_status_message(317))
        self.assertEqual('369 Unknown Status', response_status_message(369))

    def test_diversity_8(self):
        self.assertEqual('337 Unknown Status', response_status_message(337))
        self.assertEqual('397 Unknown Status', response_status_message(397))
        self.assertEqual('453 Unknown Status', response_status_message(453))

    def test_diversity_9(self):
        self.assertEqual('435 Unknown Status', response_status_message(435))
        self.assertEqual('265 Unknown Status', response_status_message(265))
        self.assertEqual('245 Unknown Status', response_status_message(245))

    def test_diversity_10(self):
        self.assertEqual('389 Unknown Status', response_status_message(389))
        self.assertEqual('349 Unknown Status', response_status_message(349))
        self.assertEqual('560 Unknown Status', response_status_message(560))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('300 Multiple Choices', response_status_message(300))
        self.assertEqual('307 Temporary Redirect', response_status_message(307))
        self.assertEqual('301 Moved Permanently', response_status_message(301))

    def test_diversity_2(self):
        self.assertEqual('500 Internal Server Error', response_status_message(500))
        self.assertEqual('202 Accepted', response_status_message(202))
        self.assertEqual('502 Bad Gateway', response_status_message(502))

    def test_diversity_3(self):
        self.assertEqual('303 See Other', response_status_message(303))
        self.assertEqual('400 Bad Request', response_status_message(400))
        self.assertEqual('500 Internal Server Error', response_status_message(500))

    def test_diversity_4(self):
        self.assertEqual('403 Forbidden', response_status_message(403))
        self.assertEqual('500 Internal Server Error', response_status_message(500))
        self.assertEqual('307 Temporary Redirect', response_status_message(307))

    def test_diversity_5(self):
        self.assertEqual('500 Internal Server Error', response_status_message(500))
        self.assertEqual('501 Not Implemented', response_status_message(501))
        self.assertEqual('401 Unauthorized', response_status_message(401))

    def test_diversity_6(self):
        self.assertEqual('203 Non-Authoritative Information', response_status_message(203))
        self.assertEqual('303 See Other', response_status_message(303))
        self.assertEqual('404 Not Found', response_status_message(404))

    def test_diversity_7(self):
        self.assertEqual('406 Not Acceptable', response_status_message(406))
        self.assertEqual('203 Non-Authoritative Information', response_status_message(203))
        self.assertEqual('503 Service Unavailable', response_status_message(503))

    def test_diversity_8(self):
        self.assertEqual('202 Accepted', response_status_message(202))
        self.assertEqual('505 HTTP Version not supported', response_status_message(505))
        self.assertEqual('410 Gone', response_status_message(410))

    def test_diversity_9(self):
        self.assertEqual('303 See Other', response_status_message(303))
        self.assertEqual('201 Created', response_status_message(201))
        self.assertEqual('300 Multiple Choices', response_status_message(300))

    def test_diversity_10(self):
        self.assertEqual('503 Service Unavailable', response_status_message(503))
        self.assertEqual('302 Found', response_status_message(302))
        self.assertEqual('202 Accepted', response_status_message(202))
