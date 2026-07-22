import unittest
import spacy
import tempfile
from spacy.language import Language
from spacy.lang.en import English



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        tag = 'cuyhrxxn'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='quszrrlpn')
        self.assertEqual('quszrrlpn', nlp2.get_pipe('my_component').categories)

    def test_diversity_2(self):
        tag = 'aftkrnyzsm'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='mffwledsbp')
        self.assertEqual('mffwledsbp', nlp2.get_pipe('my_component').categories)

    def test_diversity_3(self):
        tag = 'jtbcqzzq'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='mdhtpf')
        self.assertEqual('mdhtpf', nlp2.get_pipe('my_component').categories)

    def test_diversity_4(self):
        tag = 'awda'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='vngt')
        self.assertEqual('vngt', nlp2.get_pipe('my_component').categories)

    def test_diversity_5(self):
        tag = 'cttxxoiy'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='tgldfogy')
        self.assertEqual('tgldfogy', nlp2.get_pipe('my_component').categories)

    def test_diversity_6(self):
        tag = 'afrp'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='helwixld')
        self.assertEqual('helwixld', nlp2.get_pipe('my_component').categories)

    def test_diversity_7(self):
        tag = 'uvid'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='pifvl')
        self.assertEqual('pifvl', nlp2.get_pipe('my_component').categories)

    def test_diversity_8(self):
        tag = 'bnqhtfcc'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='wnjmfkaisb')
        self.assertEqual('wnjmfkaisb', nlp2.get_pipe('my_component').categories)

    def test_diversity_9(self):
        tag = 'yeilxglge'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='kqaq')
        self.assertEqual('kqaq', nlp2.get_pipe('my_component').categories)

    def test_diversity_10(self):
        tag = 'uumxuw'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='btfxbwejv')
        self.assertEqual('btfxbwejv', nlp2.get_pipe('my_component').categories)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        tag = 'kmsymlmme'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)

    def test_diversity_2(self):
        tag = 'pnblibwme'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)

    def test_diversity_3(self):
        tag = 'bneh'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)

    def test_diversity_4(self):
        tag = 'pbmjlyj'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)

    def test_diversity_5(self):
        tag = 'akab'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)

    def test_diversity_6(self):
        tag = 'ppaadfnj'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)

    def test_diversity_7(self):
        tag = 'bwrvzso'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)

    def test_diversity_8(self):
        tag = 'fxjghe'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)

    def test_diversity_9(self):
        tag = 'bujypvuhep'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)

    def test_diversity_10(self):
        tag = 'zkdctmar'
        class MyComponent(object):
            name = 'my_component'

            def __init__(self, nlp, **cfg):
                self.nlp = nlp
                self.categories = cfg.get('categories', 'all_categories')

            def __call__(self, doc):
                return doc

            def to_disk(self, path, **kwargs):
                pass

            def from_disk(self, path, **cfg):
                return self
        Language.factories['my_component'] = lambda nlp, **cfg: MyComponent(nlp, **cfg)
        nlp = English()
        nlp.add_pipe(nlp.create_pipe('my_component'))
        tmpdir = tempfile.mkdtemp()
        nlp.to_disk(tmpdir)
        nlp2 = spacy.load(tmpdir, categories='all_categories')
        self.assertEqual('all_categories', nlp2.get_pipe('my_component').categories)
