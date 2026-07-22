import unittest
from bin.wiki_entity_linking.wikipedia_processor import _process_wp_text



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        clean_text, entities = _process_wp_text('CCOO', '<text bytes="11456" xml:space="preserve">xvUbea cWDzQWCI DPqRA</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_2(self):
        clean_text, entities = _process_wp_text('VdLPl', '<text bytes="11456" xml:space="preserve">jpK gpQ jNAyA pfCSLu ArAfgno cUmB</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_3(self):
        clean_text, entities = _process_wp_text('PhvjLFL', '<text bytes="11456" xml:space="preserve">UuKz NYf nLxBivx MhfPY</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_4(self):
        clean_text, entities = _process_wp_text('rFzHwzU', '<text bytes="11456" xml:space="preserve">uPFgVRU Uzil EARVg NMECU iXL</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_5(self):
        clean_text, entities = _process_wp_text('ZqWbt', '<text bytes="11456" xml:space="preserve">EzS ZoVJOL</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_6(self):
        clean_text, entities = _process_wp_text('gRR', '<text bytes="11456" xml:space="preserve">mqgNR qYdDc</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_7(self):
        clean_text, entities = _process_wp_text('rur', '<text bytes="11456" xml:space="preserve">hmBbzhsX VkkM WwLojtO</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_8(self):
        clean_text, entities = _process_wp_text('pEtb', '<text bytes="11456" xml:space="preserve">YQyIKujB hKnITON OWxzGE DMemdA TFfWjZWV</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_9(self):
        clean_text, entities = _process_wp_text('AeiZNTQ', '<text bytes="11456" xml:space="preserve">Tju WHxLT hcUVfiTp zrHnni XMVY QJXXrwI</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_10(self):
        clean_text, entities = _process_wp_text('Vnjx', '<text bytes="11456" xml:space="preserve">boD IoFZl Wdcydkf jGQ cym</text>', {})
        self.assertIsNotNone(clean_text)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        clean_text, entities = _process_wp_text('LKwNH', '<text xml:space="preserve">zZr OVlADvqz GWkvG</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_2(self):
        clean_text, entities = _process_wp_text('dur', '<text xml:space="preserve">hUQAE tLXjL bVIRREw</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_3(self):
        clean_text, entities = _process_wp_text('pNcIofud', '<text xml:space="preserve">bgYXecQk Fwsm sTPXkHjz ULTWVQAo sQHqcIrz Uaw</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_4(self):
        clean_text, entities = _process_wp_text('AbE', '<text xml:space="preserve">Lej TpItlfp FhOu xPqqs gwXULXnS vjGnQ</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_5(self):
        clean_text, entities = _process_wp_text('GPmB', '<text xml:space="preserve">UBPfdwqw tytS Fxx sfChTN</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_6(self):
        clean_text, entities = _process_wp_text('nfZD', '<text xml:space="preserve">kIhgB nvj</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_7(self):
        clean_text, entities = _process_wp_text('etoEv', '<text xml:space="preserve">ZfjE nszDRZ DGYGa</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_8(self):
        clean_text, entities = _process_wp_text('OQzIAmch', '<text xml:space="preserve">miylWT iXYEFSh wddydKNE</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_9(self):
        clean_text, entities = _process_wp_text('Ynqqrd', '<text xml:space="preserve">UUn UgDK rxfhDh NjibXH IyweIJ ugbmKp</text>', {})
        self.assertIsNotNone(clean_text)

    def test_diversity_10(self):
        clean_text, entities = _process_wp_text('plmMIrty', '<text xml:space="preserve">XgI PiUbl CRqyctPM XFSn</text>', {})
        self.assertIsNotNone(clean_text)
