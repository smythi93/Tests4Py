import ast
from abc import ABC

from BugsTest.grammars.python import ToGrammarVisitor
from BugsTest.tests.diversity import Systemtests


class Tests(Systemtests, ABC):

    def __init__(self, passing: bool = True):
        self.transformer = ToGrammarVisitor()
        super().__init__(passing=passing)

    def parse(self, test: str):
        tree = ast.parse(test)
        return self.transformer.visit(tree)


class TestsFailing(Tests):

    def __init__(self):
        super().__init__(passing=False)

    def test_diversity_1(self):
        return '''
import pysnooper

@pysnooper.snoop('test.log')
def function_1(foo):
    x = 42
    y = 2
    return x + y
    
result = function_1('test')
'''

    def test_diversity_2(self):
        return '''
import pysnooper

@pysnooper.snoop('test.log')
def function_2(x):
    if x < 1:
        return 1
    else:
        return x * function_2(x - 1)

result = function_2(4)
'''

    def test_diversity_3(self):
        return '''
from pysnooper import snoop

@snoop('test.log')
def function_3(x):
    return x

result = function_3(4)
'''

    def test_diversity_4(self):
        return '''
from pysnooper import snoop

@snoop('test.log')
def function_4(x, y, z):
    if y < z:
        if x < y:
            return y
        elif x < z:
            return x
    else:
        if x > y:
            return y
        elif x > z:
            return x
    return z

result = function_4(2, 3, 1)
'''

    def test_diversity_5(self):
        return '''
import pysnooper

@pysnooper.snoop('test.log')
def function_5(m, n):
    if m <= 0:
        return n + 1
    elif n <= 0:
        return function_5(m - 1, 1)
    else:
        return function_5(m - 1, function_5(m, n - 1))

result = function_5(3, 2)
'''

    def test_diversity_6(self):
        return '''
import pysnooper

@pysnooper.snoop('test.log')
def function_6(x, y):
    z = 2
    return x ** z - z * x * y + y ** z

result = function_6(2, 2)
'''

    def test_diversity_7(self):
        return '''
import pysnooper

@pysnooper.snoop('test.log')
def function_7(x):
    return x * x

result = function_7(4)
'''

    def test_diversity_8(self):
        return '''
import pysnooper

@pysnooper.snoop('test.log')
def function_8(x):
    i = 0
    j = len(x)
    i = j + 1
    return i

result = function_8('test')
'''

    def test_diversity_9(self):
        return '''
import pysnooper

@pysnooper.snoop('test.log')
def function_9(x):
    r = 0
    if len(x) > 4:
        r = 2 * len(x)
    else:
        r = len(x) 
    return r

result = function_9('test')
'''

    def test_diversity_10(self):
        return '''
import pysnooper

@pysnooper.snoop('test.log')
def function_10(n, k):
    def fac(x):
        if x <= 0:
            return 1
        return x * fac(x - 1)

    return fac(n) / (fac(k) * fac(n - k))

result = function_10(4, 2)
'''


class TestsPassing(Tests):

    def __init__(self):
        super().__init__(passing=True)

    def test_diversity_1(self):
        return '''
import pysnooper

@pysnooper.snoop()
def function_1(foo):
    x = 42
    y = 2
    return x + y

result = function_1('test')
'''

    def test_diversity_2(self):
        return '''
import pysnooper

@pysnooper.snoop()
def function_2(x):
    if x < 1:
        return 1
    else:
        return x * function_2(x - 1)

result = function_2(4)
'''

    def test_diversity_3(self):
        return '''
from pysnooper import snoop

@snoop()
def function_3(x):
    return x

result = function_3(4)
'''

    def test_diversity_4(self):
        return '''
from pysnooper import snoop

@snoop()
def function_4(x, y, z):
    if y < z:
        if x < y:
            return y
        elif x < z:
            return x
    else:
        if x > y:
            return y
        elif x > z:
            return x
    return z

result = function_4(2, 3, 1)
'''

    def test_diversity_5(self):
        return '''
import pysnooper

@pysnooper.snoop()
def function_5(m, n):
    if m <= 0:
        return n + 1
    elif n <= 0:
        return function_5(m - 1, 1)
    else:
        return function_5(m - 1, function_5(m, n - 1))

result = function_5(3, 2)
'''

    def test_diversity_6(self):
        return '''
import pysnooper

@pysnooper.snoop()
def function_6(x, y):
    z = 2
    return x ** z - z * x * y + y ** z

result = function_6(2, 2)
'''

    def test_diversity_7(self):
        return '''
import pysnooper

@pysnooper.snoop()
def function_7(x):
    return x * x

result = function_7(4)
'''

    def test_diversity_8(self):
        return '''
import pysnooper

@pysnooper.snoop()
def function_8(x):
    i = 0
    j = len(x)
    i = j + 1
    return i

result = function_8('test')
'''

    def test_diversity_9(self):
        return '''
import pysnooper

@pysnooper.snoop()
def function_9(x):
    r = 0
    if len(x) > 4:
        r = 2 * len(x)
    else:
        r = len(x) 
    return r

result = function_9('test')
'''

    def test_diversity_10(self):
        return '''
import pysnooper

@pysnooper.snoop()
def function_10(n, k):
    def fac(x):
        if x <= 0:
            return 1
        return x * fac(x - 1)

    return fac(n) / (fac(k) * fac(n - k))

result = function_10(4, 2)
'''
