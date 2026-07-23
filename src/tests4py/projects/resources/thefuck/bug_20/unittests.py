import unittest
from thefuck.rules.dirty_unzip import get_new_command
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual("unzip 'okkb zcvp.zip' -d 'okkb zcvp'", get_new_command(Command("unzip 'okkb zcvp.zip'", '', '')))

    def test_diversity_2(self):
        self.assertEqual("unzip 'kwdn jzye.zip' -d 'kwdn jzye'", get_new_command(Command("unzip 'kwdn jzye.zip'", '', '')))

    def test_diversity_3(self):
        self.assertEqual("unzip 'zhdj wtlr.zip' -d 'zhdj wtlr'", get_new_command(Command("unzip 'zhdj wtlr.zip'", '', '')))

    def test_diversity_4(self):
        self.assertEqual("unzip 'klkw tcoz.zip' -d 'klkw tcoz'", get_new_command(Command("unzip 'klkw tcoz.zip'", '', '')))

    def test_diversity_5(self):
        self.assertEqual("unzip 'zivz gxth.zip' -d 'zivz gxth'", get_new_command(Command("unzip 'zivz gxth.zip'", '', '')))

    def test_diversity_6(self):
        self.assertEqual("unzip 'rzgw ikgw.zip' -d 'rzgw ikgw'", get_new_command(Command("unzip 'rzgw ikgw.zip'", '', '')))

    def test_diversity_7(self):
        self.assertEqual("unzip 'arqi rznj.zip' -d 'arqi rznj'", get_new_command(Command("unzip 'arqi rznj.zip'", '', '')))

    def test_diversity_8(self):
        self.assertEqual("unzip 'vkyv zgga.zip' -d 'vkyv zgga'", get_new_command(Command("unzip 'vkyv zgga.zip'", '', '')))

    def test_diversity_9(self):
        self.assertEqual("unzip 'pyyo mxgu.zip' -d 'pyyo mxgu'", get_new_command(Command("unzip 'pyyo mxgu.zip'", '', '')))

    def test_diversity_10(self):
        self.assertEqual("unzip 'rqhi xjuk.zip' -d 'rqhi xjuk'", get_new_command(Command("unzip 'rqhi xjuk.zip'", '', '')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('unzip vshkrv.zip -d vshkrv', get_new_command(Command('unzip vshkrv.zip', '', '')))

    def test_diversity_2(self):
        self.assertEqual('unzip piklmw.zip -d piklmw', get_new_command(Command('unzip piklmw.zip', '', '')))

    def test_diversity_3(self):
        self.assertEqual('unzip hcrxdh.zip -d hcrxdh', get_new_command(Command('unzip hcrxdh.zip', '', '')))

    def test_diversity_4(self):
        self.assertEqual('unzip ylqjbz.zip -d ylqjbz', get_new_command(Command('unzip ylqjbz.zip', '', '')))

    def test_diversity_5(self):
        self.assertEqual('unzip pwrrye.zip -d pwrrye', get_new_command(Command('unzip pwrrye.zip', '', '')))

    def test_diversity_6(self):
        self.assertEqual('unzip xqwymq.zip -d xqwymq', get_new_command(Command('unzip xqwymq.zip', '', '')))

    def test_diversity_7(self):
        self.assertEqual('unzip jmvpxg.zip -d jmvpxg', get_new_command(Command('unzip jmvpxg.zip', '', '')))

    def test_diversity_8(self):
        self.assertEqual('unzip drqmll.zip -d drqmll', get_new_command(Command('unzip drqmll.zip', '', '')))

    def test_diversity_9(self):
        self.assertEqual('unzip btihei.zip -d btihei', get_new_command(Command('unzip btihei.zip', '', '')))

    def test_diversity_10(self):
        self.assertEqual('unzip uhjgzj.zip -d uhjgzj', get_new_command(Command('unzip uhjgzj.zip', '', '')))
