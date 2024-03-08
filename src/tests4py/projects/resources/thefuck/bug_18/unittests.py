import unittest
from thefuck.types import Command
from thefuck.rules.sudo import match


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(False, match(Command('sudo cb -b', ' NPM ERR! ERROR: EACCES, UNLINK ', '')))

    def test_diversity_2(self):
        self.assertEqual(False, match(Command('sudo ee -c', ' NPM ERR! ERROR: EACCES, UNLINK ', '')))

    def test_diversity_3(self):
        self.assertEqual(False, match(Command('sudo xx -c', '',
                                              " ERROR: [ERRNO 13] PERMISSION DENIED: '/USR/LOCAL/LIB/PYTHON2.7/DIST-PACKAGES/IPADDR.PY' ")))

    def test_diversity_4(self):
        self.assertEqual(False, match(Command('sudo eu -v', ' NEED TO BE ROOT ', '')))

    def test_diversity_5(self):
        self.assertEqual(False, match(Command('sudo mq -q', ' PERMISSION DENIED ', '')))

    def test_diversity_6(self):
        self.assertEqual(False, match(Command('sudo nh -b', ' NEED ROOT ', '')))

    def test_diversity_7(self):
        self.assertEqual(False, match(Command('sudo vo -h', ' PERMISSION DENIED ', '')))

    def test_diversity_8(self):
        self.assertEqual(False, match(Command('sudo oq -e', " YOU DON'T HAVE ACCESS TO THE HISTORY DB. ", '')))

    def test_diversity_9(self):
        self.assertEqual(False, match(Command('sudo rh -j', ' NPM ERR! ERROR: EACCES, UNLINK ', '')))

    def test_diversity_10(self):
        self.assertEqual(False, match(Command('sudo rv -z', ' REQUESTED OPERATION REQUIRES SUPERUSER PRIVILEGE ', '')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('sudo gr -w', 'Permission denied', '')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('sudo kn -s', 'requested operation requires superuser privilege', '')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('sudo nf -e', 'need root', '')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('sudo am -k', '',
                                             "error: [Errno 13] Permission denied: '/usr/local/lib/python2.7/dist-packages/ipaddr.py'")))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('sudo qd -x', 'need root', '')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('sudo tt -f', 'permission denied', '')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('sudo sd -l', 'requested operation requires superuser privilege', '')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('sudo jo -j', "You don't have access to the history DB.", '')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('sudo qf -x', 'need root', '')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('sudo zq -f', 'must be root', '')))
