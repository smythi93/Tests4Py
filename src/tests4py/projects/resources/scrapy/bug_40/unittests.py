import unittest

from scrapy.exporters import PythonItemExporter


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'level': 512, 'boolean': 11.685})
        self.assertEqual({'level': 512, 'boolean': 11.685}, exported)

    def test_diversity_2(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'boolean': 74.216, 'count': True, 'amount': 325, 'level': -249})
        self.assertEqual({'boolean': 74.216, 'count': True, 'amount': 325, 'level': -249}, exported)

    def test_diversity_3(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'level': True, 'ratio': False})
        self.assertEqual({'level': True, 'ratio': False}, exported)

    def test_diversity_4(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'number': -284, 'flag': 12.481})
        self.assertEqual({'number': -284, 'flag': 12.481}, exported)

    def test_diversity_5(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'flag': -786, 'number': -1.749, 'ratio': 145})
        self.assertEqual({'flag': -786, 'number': -1.749, 'ratio': 145}, exported)

    def test_diversity_6(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'count': False, 'flag': -39.658})
        self.assertEqual({'count': False, 'flag': -39.658}, exported)

    def test_diversity_7(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'amount': -914, 'ratio': -7.536, 'count': 402})
        self.assertEqual({'amount': -914, 'ratio': -7.536, 'count': 402}, exported)

    def test_diversity_8(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'number': 36.57, 'amount': -612, 'ratio': -700})
        self.assertEqual({'number': 36.57, 'amount': -612, 'ratio': -700}, exported)

    def test_diversity_9(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'count': 37.712, 'number': False, 'flag': 405, 'amount': -65.768})
        self.assertEqual({'count': 37.712, 'number': False, 'flag': 405, 'amount': -65.768}, exported)

    def test_diversity_10(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'boolean': 850, 'count': False, 'amount': True})
        self.assertEqual({'boolean': 850, 'count': False, 'amount': True}, exported)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'label': 'lwkwy', 'slug': 'jpox'})
        self.assertEqual({'label': 'lwkwy', 'slug': 'jpox'}, exported)

    def test_diversity_2(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'title': 'givadvl', 'name': 'nky', 'label': 'czjaezl'})
        self.assertEqual({'title': 'givadvl', 'name': 'nky', 'label': 'czjaezl'}, exported)

    def test_diversity_3(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'tag': 'cjd', 'label': 'mcpcwke', 'code': 'ntgtn'})
        self.assertEqual({'tag': 'cjd', 'label': 'mcpcwke', 'code': 'ntgtn'}, exported)

    def test_diversity_4(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'name': 'mdalts', 'code': 'mvza'})
        self.assertEqual({'name': 'mdalts', 'code': 'mvza'}, exported)

    def test_diversity_5(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'kind': 'wzr', 'code': 'gawbvftc', 'title': 'ssyi', 'slug': 'rscthzot'})
        self.assertEqual({'kind': 'wzr', 'code': 'gawbvftc', 'title': 'ssyi', 'slug': 'rscthzot'}, exported)

    def test_diversity_6(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'slug': 'kcjqtbo', 'title': 'tdnfqsg'})
        self.assertEqual({'slug': 'kcjqtbo', 'title': 'tdnfqsg'}, exported)

    def test_diversity_7(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'tag': 'eia', 'title': 'assxnrmu', 'kind': 'idf'})
        self.assertEqual({'tag': 'eia', 'title': 'assxnrmu', 'kind': 'idf'}, exported)

    def test_diversity_8(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'name': 'tvpwjj', 'code': 'gyyndahn', 'label': 'hkpkfcjp', 'title': 'tscdj'})
        self.assertEqual({'name': 'tvpwjj', 'code': 'gyyndahn', 'label': 'hkpkfcjp', 'title': 'tscdj'}, exported)

    def test_diversity_9(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'label': 'cfjtaa', 'code': 'spq', 'title': 'bbqnh'})
        self.assertEqual({'label': 'cfjtaa', 'code': 'spq', 'title': 'bbqnh'}, exported)

    def test_diversity_10(self):
        ie = PythonItemExporter(binary=False)
        exported = ie.export_item({'kind': 'vzqkzxt', 'tag': 'arvush'})
        self.assertEqual({'kind': 'vzqkzxt', 'tag': 'arvush'}, exported)
