import unittest
from thefuck.shells.fish import Fish
from thefuck.shells.fish import info

f = Fish()

class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))

    def test_diversity_2(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))

    def test_diversity_3(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))

    def test_diversity_4(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))

    def test_diversity_5(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))

    def test_diversity_6(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))

    def test_diversity_7(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))

    def test_diversity_8(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))

    def test_diversity_9(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))

    def test_diversity_10(self):
        self.assertIn("Error Retrieving Shell, Error Details", info(self))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertIn("Fish Shell 3.6.1", info(self))

    def test_diversity_2(self):
        self.assertIn("Fish Shell 3.6.0", info(self))

    def test_diversity_3(self):
        self.assertIn("Fish Shell 3.5.1", info(self))

    def test_diversity_4(self):
        self.assertIn("Fish Shell 3.5.0", info(self))

    def test_diversity_5(self):
        self.assertIn("Fish Shell 3.4.1", info(self))

    def test_diversity_6(self):
        self.assertIn("Fish Shell 2.5.0", info(self))

    def test_diversity_7(self):
        self.assertIn("Fish Shell 2.4.1", info(self))

    def test_diversity_8(self):
        self.assertIn("Fish Shell 2.4.0", info(self))

    def test_diversity_9(self):
        self.assertIn("Fish Shell 2.3.1", info(self))

    def test_diversity_10(self):
        self.assertIn("Fish Shell 2.3.0", info(self))
