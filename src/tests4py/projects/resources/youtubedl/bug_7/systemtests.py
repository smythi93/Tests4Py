from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):

    def test_diversity_1(self):
        return '''"The CW\\'s \\'Crazy Ex-Girlfriend\\'"'''

    def test_diversity_2(self):
        return '''"The CW Crazy Ex-Girlfriend\\'"'''

    def test_diversity_3(self):
        return '''"a\\'a"'''

    def test_diversity_4(self):
        return '''"a\\'\\'a"'''

    def test_diversity_5(self):
        return '''"\\'abc\\'"'''

    def test_diversity_6(self):
        return '''"abc\\'"'''

    def test_diversity_7(self):
        return '''"abc\\'\\'""'''

    def test_diversity_8(self):
        return '''"this is a test\\'s output"'''

    def test_diversity_9(self):
        return '''"tuaszdcg893z182\\'%&%/&("'''

    def test_diversity_10(self):
        return '''"§$%&=)(\\'%&%/&("'''


class TestsPassing(PassingSystemtests):

    def test_diversity_1(self):
        return '''{
            'clip':{'provider':'pseudo'}
        }'''

    def test_diversity_2(self):
        return '''{'playlist':[{'controls':{'all':null}}]}'''

    def test_diversity_3(self):
        return '"SAND Number: SAND 2013-7800P\\nPresenter: Tom Russo\\nHabanero Software Training - Xyce Software\\nXyce, Sandia\\u0027s"'

    def test_diversity_4(self):
        return "{abc_def:'1\\'\\\\2\\\\\\'3\"4'}"

    def test_diversity_5(self):
        return '{"abc": true}'

    def test_diversity_6(self):
        return '{"abc": "def",}'

    def test_diversity_7(self):
        return '''"abc""'''

    def test_diversity_8(self):
        return '''"abc"'''

    def test_diversity_9(self):
        return '''"tuaszdcg893z182\'%&%/&("'''

    def test_diversity_10(self):
        return '''"§$%&=)(\'%&%/&("'''
