import unittest
from spacy.cli.converters.conllu2json import conllu2json


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\tPMVbQPhcs\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tGBWycCKHzd\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')

    def test_diversity_2(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\tdniHDMO\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tLNeVk\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')

    def test_diversity_3(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\tthHTp\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tdWhUYc\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')

    def test_diversity_4(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\tnQoLhQWBicwFU\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tbTSKhnhDQ\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')

    def test_diversity_5(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\thfSHXBvP\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tfethoilyuFsEvW\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')

    def test_diversity_6(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\tgzAMWZOIVc\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tyXvkwTZ\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')

    def test_diversity_7(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\tHEBdQf\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tVlwSPeuICNMzvWR\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')

    def test_diversity_8(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\tOdUoWHa\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tfFTTYFnB\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')

    def test_diversity_9(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\tpUdkWimNC\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tGBTHifkPI\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')

    def test_diversity_10(self):
        conllu2json(
            '\n        1\t[\tPUNCT\t-\t-LRB-\t_\t_\tpunct\t_\t_\n        2\tThis\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        3\tUxWhGmlyyeqO\t_\tNOUN\tNN\t_\t_\tnsubj\t_\t_\n        4\tof\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        5\ta\t_\tDET\tDT\t_\t_\tdet\t_\t_\n        6\trespected\t_\tADJ\tJJ\t_\t_\tamod\t_\t_\n        7\tcleric\t_\tNOUN\tNN\t_\t_\tnmod\t_\t_\n        8\twill\t_\tAUX\tMD\t_\t_\taux\t_\t_\n        9\tbe\t_\tAUX\tVB\t_\t_\taux\t_\t_\n        10\tcausing\t_\tVERB\tVBG\t_\t_\troot\t_\t_\n        11\tus\t_\tPRON\tPRP\t_\t_\tiobj\t_\t_\n        12\tcHODDhQ\t_\tNOUN\tNN\t_\t_\tdobj\t_\t_\n        13\tfor\t_\tADP\tIN\t_\t_\tcase\t_\t_\n        14\tyears\t_\tNOUN\tNNS\t_\t_\tnmod\t_\t_\n        15\tto\t_\tPART\tTO\t_\t_\tmark\t_\t_\n        16\tcome\t_\tVERB\tVB\t_\t_\tacl\t_\t_\n        17\t.\t_\tPUNCT\t.\t_\t_\tpunct\t_\t_\n        18\t]\t_\tPUNCT\t-RRB-\t_\t_\tpunct\t_\t_\n        ')


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tGDzhe\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\tfVyOzolPKyeT\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')

    def test_diversity_2(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tRSyfzS\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\tNojPLEP\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')

    def test_diversity_3(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tOUInUo\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\trJRxmYEmDXO\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')

    def test_diversity_4(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tgTBKjWD\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\tbPunJsUqVvGmiH\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')

    def test_diversity_5(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tpJHRyCbhOhB\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\tclefouLzvKPugq\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')

    def test_diversity_6(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tZvDlfYWMlQsDyN\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\tWdpLSkhbZN\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')

    def test_diversity_7(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tjSDKYzb\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\tjWUbLA\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')

    def test_diversity_8(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tgiqyKbSliMlxhc\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\tpccAYouYwput\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')

    def test_diversity_9(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tIPOcSSLhsSFWj\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\tQFUfKYMHkVHJWR\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')

    def test_diversity_10(self):
        conllu2json(
            '\n1\t[\t_\tPUNCT\t-LRB-\t_\t10\tpunct\t_\t_\n2\tThis\t_\tDET\tDT\t_\t3\tdet\t_\t_\n3\tmgVNjPd\t_\tNOUN\tNN\t_\t10\tnsubj\t_\t_\n4\tof\t_\tADP\tIN\t_\t7\tcase\t_\t_\n5\ta\t_\tDET\tDT\t_\t7\tdet\t_\t_\n6\trespected\t_\tADJ\tJJ\t_\t7\tamod\t_\t_\n7\tcleric\t_\tNOUN\tNN\t_\t10\tnmod\t_\t_\n8\twill\t_\tAUX\tMD\t_\t10\taux\t_\t_\n9\tbe\t_\tAUX\tVB\t_\t10\taux\t_\t_\n10\tcausing\t_\tVERB\tVBG\t_\t0\troot\t_\t_\n11\tus\t_\tPRON\tPRP\t_\t10\tiobj\t_\t_\n12\tJKyuYQHU\t_\tNOUN\tNN\t_\t10\tdobj\t_\t_\n13\tfor\t_\tADP\tIN\t_\t14\tcase\t_\t_\n14\tyears\t_\tNOUN\tNNS\t_\t10\tnmod\t_\t_\n15\tto\t_\tPART\tTO\t_\t16\tmark\t_\t_\n16\tcome\t_\tVERB\tVB\t_\t10\tacl\t_\t_\n17\t.\t_\tPUNCT\t.\t_\t10\tpunct\t_\t_\n        ')
