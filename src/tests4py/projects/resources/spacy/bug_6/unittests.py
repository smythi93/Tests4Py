import unittest
import warnings
import spacy.language
from spacy.language import Language, component



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_qvxqfo', assigns=['token.tag'])
        def c1_qvxqfo(doc):
            return doc
        @component('c2_qvxqfo', requires=['token.pos'])
        def c2_qvxqfo(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_qvxqfo)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_qvxqfo)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_qvxqfo')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_2(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_rclbvzhwp', assigns=['token.tag'])
        def c1_rclbvzhwp(doc):
            return doc
        @component('c2_rclbvzhwp', requires=['token.pos'])
        def c2_rclbvzhwp(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_rclbvzhwp)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_rclbvzhwp)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_rclbvzhwp')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_3(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_hmsqdya', assigns=['token.tag'])
        def c1_hmsqdya(doc):
            return doc
        @component('c2_hmsqdya', requires=['token.pos'])
        def c2_hmsqdya(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_hmsqdya)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_hmsqdya)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_hmsqdya')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_4(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_ngpztsczo', assigns=['token.tag'])
        def c1_ngpztsczo(doc):
            return doc
        @component('c2_ngpztsczo', requires=['token.pos'])
        def c2_ngpztsczo(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_ngpztsczo)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_ngpztsczo)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_ngpztsczo')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_5(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_mwhho', assigns=['token.tag'])
        def c1_mwhho(doc):
            return doc
        @component('c2_mwhho', requires=['token.pos'])
        def c2_mwhho(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_mwhho)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_mwhho)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_mwhho')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_6(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_qmfjax', assigns=['token.tag'])
        def c1_qmfjax(doc):
            return doc
        @component('c2_qmfjax', requires=['token.pos'])
        def c2_qmfjax(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_qmfjax)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_qmfjax)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_qmfjax')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_7(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_fphhijdzdx', assigns=['token.tag'])
        def c1_fphhijdzdx(doc):
            return doc
        @component('c2_fphhijdzdx', requires=['token.pos'])
        def c2_fphhijdzdx(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_fphhijdzdx)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_fphhijdzdx)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_fphhijdzdx')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_8(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_wiudpwobm', assigns=['token.tag'])
        def c1_wiudpwobm(doc):
            return doc
        @component('c2_wiudpwobm', requires=['token.pos'])
        def c2_wiudpwobm(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_wiudpwobm)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_wiudpwobm)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_wiudpwobm')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_9(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_mxojenlm', assigns=['token.tag'])
        def c1_mxojenlm(doc):
            return doc
        @component('c2_mxojenlm', requires=['token.pos'])
        def c2_mxojenlm(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_mxojenlm)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_mxojenlm)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_mxojenlm')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_10(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_yxud', assigns=['token.tag'])
        def c1_yxud(doc):
            return doc
        @component('c2_yxud', requires=['token.pos'])
        def c2_yxud(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_yxud)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_yxud)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_yxud')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_zciwmpbqje', assigns=['token.tag'])
        def c1_zciwmpbqje(doc):
            return doc
        @component('c2_zciwmpbqje', requires=['token.tag'])
        def c2_zciwmpbqje(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_zciwmpbqje)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_zciwmpbqje)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_zciwmpbqje')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_2(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_oitwiqgpkl', assigns=['token.tag'])
        def c1_oitwiqgpkl(doc):
            return doc
        @component('c2_oitwiqgpkl', requires=['token.tag'])
        def c2_oitwiqgpkl(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_oitwiqgpkl)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_oitwiqgpkl)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_oitwiqgpkl')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_3(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_srfdulndy', assigns=['token.tag'])
        def c1_srfdulndy(doc):
            return doc
        @component('c2_srfdulndy', requires=['token.tag'])
        def c2_srfdulndy(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_srfdulndy)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_srfdulndy)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_srfdulndy')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_4(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_wrvatovhr', assigns=['token.tag'])
        def c1_wrvatovhr(doc):
            return doc
        @component('c2_wrvatovhr', requires=['token.tag'])
        def c2_wrvatovhr(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_wrvatovhr)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_wrvatovhr)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_wrvatovhr')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_5(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_jmhlmrhc', assigns=['token.tag'])
        def c1_jmhlmrhc(doc):
            return doc
        @component('c2_jmhlmrhc', requires=['token.tag'])
        def c2_jmhlmrhc(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_jmhlmrhc)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_jmhlmrhc)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_jmhlmrhc')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_6(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_dchs', assigns=['token.tag'])
        def c1_dchs(doc):
            return doc
        @component('c2_dchs', requires=['token.tag'])
        def c2_dchs(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_dchs)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_dchs)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_dchs')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_7(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_zssgkespav', assigns=['token.tag'])
        def c1_zssgkespav(doc):
            return doc
        @component('c2_zssgkespav', requires=['token.tag'])
        def c2_zssgkespav(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_zssgkespav)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_zssgkespav)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_zssgkespav')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_8(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_liwenj', assigns=['token.tag'])
        def c1_liwenj(doc):
            return doc
        @component('c2_liwenj', requires=['token.tag'])
        def c2_liwenj(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_liwenj)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_liwenj)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_liwenj')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_9(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_fwpgnqdvqs', assigns=['token.tag'])
        def c1_fwpgnqdvqs(doc):
            return doc
        @component('c2_fwpgnqdvqs', requires=['token.tag'])
        def c2_fwpgnqdvqs(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_fwpgnqdvqs)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_fwpgnqdvqs)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_fwpgnqdvqs')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)

    def test_diversity_10(self):
        spacy.language.ENABLE_PIPELINE_ANALYSIS = True
        @component('c1_wuusguqdj', assigns=['token.tag'])
        def c1_wuusguqdj(doc):
            return doc
        @component('c2_wuusguqdj', requires=['token.tag'])
        def c2_wuusguqdj(doc):
            return doc
        nlp = Language()
        nlp.add_pipe(c1_wuusguqdj)
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            nlp.add_pipe(c2_wuusguqdj)
        with warnings.catch_warnings(record=True) as rec:
            warnings.simplefilter('always')
            nlp.remove_pipe('c2_wuusguqdj')
        warned = any(('requires' in str(w.message) and 'to be assigned' in str(w.message) for w in rec))
        self.assertFalse(warned)
