import unittest
import luigi
from luigi.util import requires, inherits



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        Required = type('Req_pybxqcxw', (luigi.Task,), {})
        Parent = type('Par_pybxqcxw', (luigi.Task,), {})
        Child = type('Child_pybxqcxw', (Parent,), {})
        Child = requires(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_2(self):
        Required = type('Req_fcvt', (luigi.Task,), {})
        Parent = type('Par_fcvt', (luigi.Task,), {})
        Child = type('Child_fcvt', (Parent,), {})
        Child = inherits(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_3(self):
        Required = type('Req_hyb', (luigi.Task,), {})
        Parent = type('Par_hyb', (luigi.Task,), {})
        Child = type('Child_hyb', (Parent,), {})
        Child = inherits(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_4(self):
        Required = type('Req_whrdnla', (luigi.Task,), {})
        Parent = type('Par_whrdnla', (luigi.Task,), {})
        Child = type('Child_whrdnla', (Parent,), {})
        Child = requires(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_5(self):
        Required = type('Req_tszwlt', (luigi.Task,), {})
        Parent = type('Par_tszwlt', (luigi.Task,), {})
        Child = type('Child_tszwlt', (Parent,), {})
        Child = inherits(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_6(self):
        Required = type('Req_sujxom', (luigi.Task,), {})
        Parent = type('Par_sujxom', (luigi.Task,), {})
        Child = type('Child_sujxom', (Parent,), {})
        Child = requires(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_7(self):
        Required = type('Req_iunliab', (luigi.Task,), {})
        Parent = type('Par_iunliab', (luigi.Task,), {})
        Child = type('Child_iunliab', (Parent,), {})
        Child = inherits(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_8(self):
        Required = type('Req_zisptlh', (luigi.Task,), {})
        Parent = type('Par_zisptlh', (luigi.Task,), {})
        Child = type('Child_zisptlh', (Parent,), {})
        Child = inherits(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_9(self):
        Required = type('Req_ldkvcq', (luigi.Task,), {})
        Parent = type('Par_ldkvcq', (luigi.Task,), {})
        Child = type('Child_ldkvcq', (Parent,), {})
        Child = inherits(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_10(self):
        Required = type('Req_page', (luigi.Task,), {})
        Parent = type('Par_page', (luigi.Task,), {})
        Child = type('Child_page', (Parent,), {})
        Child = inherits(Required)(Child)
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        Required = type('Req_uipqjr', (luigi.Task,), {})
        Parent = type('Par_uipqjr', (luigi.Task,), {})
        Child = type('Child_uipqjr', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_2(self):
        Required = type('Req_zcgkihjl', (luigi.Task,), {})
        Parent = type('Par_zcgkihjl', (luigi.Task,), {})
        Child = type('Child_zcgkihjl', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_3(self):
        Required = type('Req_kvnsb', (luigi.Task,), {})
        Parent = type('Par_kvnsb', (luigi.Task,), {})
        Child = type('Child_kvnsb', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_4(self):
        Required = type('Req_nuwdysxx', (luigi.Task,), {})
        Parent = type('Par_nuwdysxx', (luigi.Task,), {})
        Child = type('Child_nuwdysxx', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_5(self):
        Required = type('Req_sruy', (luigi.Task,), {})
        Parent = type('Par_sruy', (luigi.Task,), {})
        Child = type('Child_sruy', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_6(self):
        Required = type('Req_jjwdvwi', (luigi.Task,), {})
        Parent = type('Par_jjwdvwi', (luigi.Task,), {})
        Child = type('Child_jjwdvwi', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_7(self):
        Required = type('Req_zgtyfayg', (luigi.Task,), {})
        Parent = type('Par_zgtyfayg', (luigi.Task,), {})
        Child = type('Child_zgtyfayg', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_8(self):
        Required = type('Req_cad', (luigi.Task,), {})
        Parent = type('Par_cad', (luigi.Task,), {})
        Child = type('Child_cad', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_9(self):
        Required = type('Req_nzm', (luigi.Task,), {})
        Parent = type('Par_nzm', (luigi.Task,), {})
        Child = type('Child_nzm', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))

    def test_diversity_10(self):
        Required = type('Req_mpqjsjpe', (luigi.Task,), {})
        Parent = type('Par_mpqjsjpe', (luigi.Task,), {})
        Child = type('Child_mpqjsjpe', (Parent,), {})
        self.assertNotEqual(str(Child.__mro__[0]), str(Child.__mro__[1]))
