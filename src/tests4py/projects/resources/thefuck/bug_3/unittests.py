import unittest
from thefuck.shells.fish import Fish
from thefuck.shells.fish import info


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())

    def test_diversity_2(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())

    def test_diversity_3(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())

    def test_diversity_4(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())

    def test_diversity_5(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())

    def test_diversity_6(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())

    def test_diversity_7(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())

    def test_diversity_8(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())

    def test_diversity_9(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())

    def test_diversity_10(self):
        f = Fish()
        self.assertEqual("Error Retrieving Shell", f.info())


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        f = Fish()
        self.assertEqual('Fish Shell 3.6.1', f.info())

    def test_diversity_2(self):
        f = Fish()
        self.assertEqual('Fish Shell 3.6.0', f.info())

    def test_diversity_3(self):
        f = Fish()
        self.assertEqual('Fish Shell 3.5.1', f.info())

    def test_diversity_4(self):
        f = Fish()
        self.assertEqual('Fish Shell 3.5.0', f.info())

    def test_diversity_5(self):
        f = Fish()
        self.assertEqual('Fish Shell 3.4.1', f.info())

    def test_diversity_6(self):
        f = Fish()
        self.assertEqual('Fish Shell 3.4.0', f.info())

    def test_diversity_7(self):
        f = Fish()
        self.assertEqual('Fish Shell 2.4.1', f.info())

    def test_diversity_8(self):
        f = Fish()
        self.assertEqual('Fish Shell 2.4.0', f.info())

    def test_diversity_9(self):
        f = Fish()
        self.assertEqual('Fish Shell 2.3.1', f.info())

    def test_diversity_10(self):
        f = Fish()
        self.assertEqual('Fish Shell 2.3.0', f.info())
