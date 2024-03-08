import unittest
from thefuck.types import Command
from thefuck.types import Settings
from thefuck.rules.mkdir_p import get_new_command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('hdfs dfs -mkdir -p BCG/rFGxX/tXx',
                         get_new_command(Command('hdfs dfs -mkdir BCG/rFGxX/tXx', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual('./bin/hdfs dfs -mkdir -p unuV/BdPr/egAW',
                         get_new_command(Command('./bin/hdfs dfs -mkdir unuV/BdPr/egAW', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual('hdfs dfs -mkdir -p nwN/DdH/TBpP',
                         get_new_command(Command('hdfs dfs -mkdir nwN/DdH/TBpP', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual('./bin/hdfs dfs -mkdir -p Wmue/vnlu/KZgB',
                         get_new_command(Command('./bin/hdfs dfs -mkdir Wmue/vnlu/KZgB', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual('hdfs dfs -mkdir -p pMITbN/PFrtq/tzGi',
                         get_new_command(Command('hdfs dfs -mkdir pMITbN/PFrtq/tzGi', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual('hdfs dfs -mkdir -p fXkAPD/hWcP/Hld',
                         get_new_command(Command('hdfs dfs -mkdir fXkAPD/hWcP/Hld', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual('./bin/hdfs dfs -mkdir -p UtmHC/YfX/jSqtqU',
                         get_new_command(Command('./bin/hdfs dfs -mkdir UtmHC/YfX/jSqtqU', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual('hdfs dfs -mkdir -p Rvi/xLaZb/yNxw',
                         get_new_command(Command('hdfs dfs -mkdir Rvi/xLaZb/yNxw', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual('./bin/hdfs dfs -mkdir -p Lcfhyy/CJgrnC/Ywdb',
                         get_new_command(Command('./bin/hdfs dfs -mkdir Lcfhyy/CJgrnC/Ywdb', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual('hdfs dfs -mkdir -p rHm/eqy/akYxZ',
                         get_new_command(Command('hdfs dfs -mkdir rHm/eqy/akYxZ', '', ''), Settings()))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual('mkdir -p cKj/bRa/AKQoh', get_new_command(Command('mkdir cKj/bRa/AKQoh', '', ''), Settings()))

    def test_diversity_2(self):
        self.assertEqual('mkdir -p dska/Eace/pfTfoA',
                         get_new_command(Command('mkdir dska/Eace/pfTfoA', '', ''), Settings()))

    def test_diversity_3(self):
        self.assertEqual('mkdir -p GwQ/YpPD/euEpR',
                         get_new_command(Command('mkdir GwQ/YpPD/euEpR', '', ''), Settings()))

    def test_diversity_4(self):
        self.assertEqual('mkdir -p WRa/KBzhg/ZbO', get_new_command(Command('mkdir WRa/KBzhg/ZbO', '', ''), Settings()))

    def test_diversity_5(self):
        self.assertEqual('mkdir -p tHcBbu/DAF/dpUp',
                         get_new_command(Command('mkdir tHcBbu/DAF/dpUp', '', ''), Settings()))

    def test_diversity_6(self):
        self.assertEqual('mkdir -p dZRxiX/cTBqU/YeXx',
                         get_new_command(Command('mkdir dZRxiX/cTBqU/YeXx', '', ''), Settings()))

    def test_diversity_7(self):
        self.assertEqual('mkdir -p OLg/Ebq/SMQP', get_new_command(Command('mkdir OLg/Ebq/SMQP', '', ''), Settings()))

    def test_diversity_8(self):
        self.assertEqual('mkdir -p cFz/AzoQ/zpUaHL',
                         get_new_command(Command('mkdir cFz/AzoQ/zpUaHL', '', ''), Settings()))

    def test_diversity_9(self):
        self.assertEqual('mkdir -p ZwW/lEgrZA/uAD',
                         get_new_command(Command('mkdir ZwW/lEgrZA/uAD', '', ''), Settings()))

    def test_diversity_10(self):
        self.assertEqual('mkdir -p qDsT/YKSse/HkuZ',
                         get_new_command(Command('mkdir qDsT/YKSse/HkuZ', '', ''), Settings()))

