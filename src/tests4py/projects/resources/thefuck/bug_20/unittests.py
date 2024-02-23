import unittest
from thefuck.types import Command
from thefuck.rules.dirty_unzip import _zip_file
from thefuck.rules.dirty_unzip import get_new_command


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('lgeWWVqTUfOdIc, lxkQWl', _zip_file(Command('unzip lgeWWVqTUfOdIc.zip, lxkQWl.zip', '', '')))

    def test_diversity_2(self):
        self.assertEqual("unzip 'wrIzCEo kTbdO.zip' -d 'wrIzCEo kTbdO'",
                         get_new_command(Command("unzip 'wrIzCEo kTbdO.zip'", '', '')))

    def test_diversity_3(self):
        self.assertEqual("unzip 'QoLBjfJvcv iMkng.zip' -d 'QoLBjfJvcv iMkng'",
                         get_new_command(Command("unzip 'QoLBjfJvcv iMkng.zip'", '', '')))

    def test_diversity_4(self):
        self.assertEqual('abGYJ, NfMFixvKoZhvND', _zip_file(Command('unzip abGYJ.zip, NfMFixvKoZhvND.zip', '', '')))

    def test_diversity_5(self):
        self.assertEqual('KweNZAOyhvB, bYogNneZlkGDYKU',
                         _zip_file(Command('unzip KweNZAOyhvB.zip, bYogNneZlkGDYKU.zip', '', '')))

    def test_diversity_6(self):
        self.assertEqual("unzip 'sgFyxBNW SvsZqnTA.zip' -d 'sgFyxBNW SvsZqnTA'",
                         get_new_command(Command("unzip 'sgFyxBNW SvsZqnTA.zip'", '', '')))

    def test_diversity_7(self):
        self.assertEqual('oKrja, AvIHK', _zip_file(Command('unzip oKrja.zip, AvIHK.zip', '', '')))

    def test_diversity_8(self):
        self.assertEqual("unzip xaMGlDBopY\\ dZmlixXEjixM.zip -d 'xaMGlDBopY dZmlixXEjixM'",
                         get_new_command(Command('unzip xaMGlDBopY\\ dZmlixXEjixM.zip', '', '')))

    def test_diversity_9(self):
        self.assertEqual('jYYbrDwaWptJ, uyopElXi', _zip_file(Command('unzip jYYbrDwaWptJ.zip, uyopElXi.zip', '', '')))

    def test_diversity_10(self):
        self.assertEqual("unzip KUlVMKuah\\ WwAvJuXzJw.zip -d 'KUlVMKuah WwAvJuXzJw'",
                         get_new_command(Command('unzip KUlVMKuah\\ WwAvJuXzJw.zip', '', '')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('unzip gyLCwqHJI.zip -d gyLCwqHJI', get_new_command(Command('unzip gyLCwqHJI.zip', '', '')))

    def test_diversity_2(self):
        self.assertEqual('VaMMPHbhihP.zip', _zip_file(Command('unzip VaMMPHbhihP.zip', '', '')))

    def test_diversity_3(self):
        self.assertEqual('GdFeLDvcOP.zip', _zip_file(Command('unzip GdFeLDvcOP.zip', '', '')))

    def test_diversity_4(self):
        self.assertEqual('unzip cCtXqphc.zip -d cCtXqphc', get_new_command(Command('unzip cCtXqphc.zip', '', '')))

    def test_diversity_5(self):
        self.assertEqual('unzip vuJRTjLAeYK -d vuJRTjLAeYK', get_new_command(Command('unzip vuJRTjLAeYK', '', '')))

    def test_diversity_6(self):
        self.assertEqual('iOQPbebeU.zip', _zip_file(Command('unzip iOQPbebeU.zip', '', '')))

    def test_diversity_7(self):
        self.assertEqual('sXxFlJICq.zip', _zip_file(Command('unzip sXxFlJICq.zip', '', '')))

    def test_diversity_8(self):
        self.assertEqual('TcpSnB.zip', _zip_file(Command('unzip TcpSnB', '', '')))

    def test_diversity_9(self):
        self.assertEqual('unzip JoFFeu -d JoFFeu', get_new_command(Command('unzip JoFFeu', '', '')))

    def test_diversity_10(self):
        self.assertEqual('wWwSdecb.zip', _zip_file(Command('unzip wWwSdecb.zip', '', '')))
