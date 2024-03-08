import unittest
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.open import get_new_command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('gnome-open http://sicxqt.io',
                         get_new_command(Command('gnome-open sicxqt.io', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual('xdg-open http://rfblcuad.io',
                         get_new_command(Command('xdg-open rfblcuad.io', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual('gnome-open http://ayyzixm.io',
                         get_new_command(Command('gnome-open ayyzixm.io', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual('gnome-open http://kshtg.io',
                         get_new_command(Command('gnome-open kshtg.io', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual('xdg-open http://uldxeq.io',
                         get_new_command(Command('xdg-open uldxeq.io', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual('gnome-open http://izbhcxwb.io',
                         get_new_command(Command('gnome-open izbhcxwb.io', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual('gnome-open http://ljnhspjwk.io',
                         get_new_command(Command('gnome-open ljnhspjwk.io', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual('xdg-open http://xiimpol.io',
                         get_new_command(Command('xdg-open xiimpol.io', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual('gnome-open http://eepuecz.io',
                         get_new_command(Command('gnome-open eepuecz.io', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual('gnome-open http://ywuemdekc.io',
                         get_new_command(Command('gnome-open ywuemdekc.io', '', ''), Settings()))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('open http://kcciqmpat.io', get_new_command(Command('open kcciqmpat.io', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual('open http://izhky.com', get_new_command(Command('open izhky.com', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual('open http://obzllm.com', get_new_command(Command('open obzllm.com', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual('open http://ozcmazs.com', get_new_command(Command('open ozcmazs.com', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual('open http://fukfgi.io', get_new_command(Command('open fukfgi.io', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual('open http://qkifgjvleh.com', get_new_command(Command('open qkifgjvleh.com', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual('open http://tlqtgwn.io', get_new_command(Command('open tlqtgwn.io', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual('open http://zhloaxv.com', get_new_command(Command('open zhloaxv.com', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual('open http://hbijsaust.com', get_new_command(Command('open hbijsaust.com', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual('open http://kswnxuu.com', get_new_command(Command('open kswnxuu.com', '', ''), Settings()))
