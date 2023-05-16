import unittest

import json
from youtube_dl.utils import js_to_json


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        inp = '''"The CW\\'s \\'Crazy Ex-Girlfriend\\'"'''
        self.assertEqual(js_to_json(inp), '''"The CW's 'Crazy Ex-Girlfriend'"''')

    def test_diversity_2(self):
        inp = '''"The CW Crazy Ex-Girlfriend\\'"'''
        self.assertEqual(js_to_json(inp), '''"The CW Crazy Ex-Girlfriend'"''')

    def test_diversity_3(self):
        inp = '''"a\\'a"'''
        self.assertEqual(js_to_json(inp), '''"a'a"''')

    def test_diversity_4(self):
        inp = '''"a\\'\\'a"'''
        self.assertEqual(js_to_json(inp), '''"a''a"''')

    def test_diversity_5(self):
        inp = '''"\\'abc\\'"'''
        self.assertEqual(js_to_json(inp), '''"'abc'"''')

    def test_diversity_6(self):
        inp = '''"abc\\'"'''
        self.assertEqual(js_to_json(inp), '''"abc'"''')

    def test_diversity_7(self):
        inp = '''"abc\\'\\'""'''
        self.assertEqual(js_to_json(inp), '''"abc''""''')

    def test_diversity_8(self):
        inp = '''"this is a test\\'s output"'''
        self.assertEqual(js_to_json(inp), '''"this is a test's output"''')

    def test_diversity_9(self):
        inp = '''"tuaszdcg893z182\\'%&%/&("'''
        self.assertEqual(js_to_json(inp), '''"tuaszdcg893z182'%&%/&("''')

    def test_diversity_10(self):
        inp = '''"§$%&=)(\\'%&%/&("'''
        self.assertEqual(js_to_json(inp), '''"§$%&=)('%&%/&("''')


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        inp = '''{
            'clip':{'provider':'pseudo'}
        }'''
        self.assertEqual(js_to_json(inp), '''{
            "clip":{"provider":"pseudo"}
        }''')

    def test_diversity_2(self):
        inp = '''{'playlist':[{'controls':{'all':null}}]}'''
        self.assertEqual(js_to_json(inp), '''{"playlist":[{"controls":{"all":null}}]}''')

    def test_diversity_3(self):
        inp = '"SAND Number: SAND 2013-7800P\\nPresenter: Tom Russo\\nHabanero Software Training - Xyce Software\\nXyce, Sandia\\u0027s"'
        json_code = js_to_json(inp)
        self.assertEqual(json.loads(json_code), json.loads(inp))

    def test_diversity_4(self):
        on = js_to_json("{abc_def:'1\\'\\\\2\\\\\\'3\"4'}")
        self.assertEqual(json.loads(on), {"abc_def": "1'\\2\\'3\"4"})

    def test_diversity_5(self):
        on = js_to_json('{"abc": true}')
        self.assertEqual(json.loads(on), {'abc': True})

    def test_diversity_6(self):
        on = js_to_json('{"abc": "def",}')
        self.assertEqual(on, '{"abc": "def"}')

    def test_diversity_7(self):
        inp = '''"abc""'''
        self.assertEqual(js_to_json(inp), '''"abc""''')

    def test_diversity_8(self):
        inp = '''"abc"'''
        self.assertEqual(js_to_json(inp), '''"abc"''')

    def test_diversity_9(self):
        inp = '''"tuaszdcg893z182\'%&%/&("'''
        self.assertEqual(js_to_json(inp), '''"tuaszdcg893z182\'%&%/&("''')

    def test_diversity_10(self):
        inp = '''"§$%&=)(\'%&%/&("'''
        self.assertEqual(js_to_json(inp), '''"§$%&=)(\'%&%/&("''')
