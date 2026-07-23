import unittest

from io import BytesIO
from scrapy.exporters import XmlItemExporter


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'ozqiiq': True})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><ozqiiq>True</ozqiiq></item></items>', fp.getvalue())

    def test_diversity_2(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'bdleoian': -157})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><bdleoian>-157</bdleoian></item></items>', fp.getvalue())

    def test_diversity_3(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'kggglou': False})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><kggglou>False</kggglou></item></items>', fp.getvalue())

    def test_diversity_4(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'msqgt': 11.47})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><msqgt>11.47</msqgt></item></items>', fp.getvalue())

    def test_diversity_5(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'ezire': True})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><ezire>True</ezire></item></items>', fp.getvalue())

    def test_diversity_6(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'frodjob': True})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><frodjob>True</frodjob></item></items>', fp.getvalue())

    def test_diversity_7(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'gzofhhh': True})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><gzofhhh>True</gzofhhh></item></items>', fp.getvalue())

    def test_diversity_8(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'cteee': 604})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><cteee>604</cteee></item></items>', fp.getvalue())

    def test_diversity_9(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'advlu': -430})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><advlu>-430</advlu></item></items>', fp.getvalue())

    def test_diversity_10(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'jae': -34.95})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><jae>-34.95</jae></item></items>', fp.getvalue())


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'lytncj': 'qmcp'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><lytncj>qmcp</lytncj></item></items>', fp.getvalue())

    def test_diversity_2(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'rhc': 'jeqf'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><rhc>jeqf</rhc></item></items>', fp.getvalue())

    def test_diversity_3(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'nenlwgd': 'tsehvj'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><nenlwgd>tsehvj</nenlwgd></item></items>', fp.getvalue())

    def test_diversity_4(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'mdcoqaga': 'bvftcdc'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><mdcoqaga>bvftcdc</mdcoqaga></item></items>', fp.getvalue())

    def test_diversity_5(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'yiqc': 'cth'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><yiqc>cth</yiqc></item></items>', fp.getvalue())

    def test_diversity_6(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'otauoeub': 'tbo'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><otauoeub>tbo</otauoeub></item></items>', fp.getvalue())

    def test_diversity_7(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'tdnfqsg': 'ytzaid'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><tdnfqsg>ytzaid</tdnfqsg></item></items>', fp.getvalue())

    def test_diversity_8(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'shyde': 'rmuyidf'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><shyde>rmuyidf</shyde></item></items>', fp.getvalue())

    def test_diversity_9(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'bxdtvpwj': 'qgyynd'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><bxdtvpwj>qgyynd</bxdtvpwj></item></items>', fp.getvalue())

    def test_diversity_10(self):
        fp = BytesIO()
        ie = XmlItemExporter(fp)
        ie.start_exporting()
        ie.export_item({'bts': 'xtlwa'})
        ie.finish_exporting()
        self.assertEqual(b'<?xml version="1.0" encoding="utf-8"?>\n<items><item><bts>xtlwa</bts></item></items>', fp.getvalue())
