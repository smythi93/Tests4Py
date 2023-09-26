import ast
import re
import unittest
from typing import List

from tests4py.grammars import antlr, python
from tests4py.grammars.default import (
    NUMBER,
    INTEGER,
    FLOAT,
    STRING,
    STRING_WS,
    STRING_WS_ESCAPED_DOUBLE,
    CLI_GRAMMAR,
)
from tests4py.grammars.fuzzer import Grammar, is_valid_grammar
from tests4py.grammars.parser import EarleyParser
from tests4py.grammars.tree import ComplexDerivationTree
from tests4py.grammars.utils import GrammarVisitor

EXPR_GRAMMAR: Grammar = {
    "<start>": ["<expr>"],
    "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"],
    "<term>": ["<factor> * <term>", "<factor> / <term>", "<factor>"],
    "<factor>": [
        "+<factor>",
        "-<factor>",
        "(<expr>)",
        "<integer>.<integer>",
        "<integer>",
    ],
    "<integer>": ["<digit><integer>", "<digit>"],
    "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
}


class ExprVisitor(GrammarVisitor):
    pass


class TestVisitor(unittest.TestCase):
    def setUp(self) -> None:
        self.grammar: Grammar = EXPR_GRAMMAR

    def test_visit(self):
        expr = "7 / +48.5"
        parser = EarleyParser(self.grammar)
        tree = None
        for tree in parser.parse(expr):
            break
        self.assertIsNotNone(tree)
        tree = ComplexDerivationTree.from_parse_tree(tree)

        class TermVisitor(ExprVisitor):
            def __init__(self, grammar: Grammar):
                super().__init__(grammar)
                self.term_correct = False

            def visit_term(self, node: ComplexDerivationTree):
                if node.children[1].value == " / ":
                    self.term_correct = True

        visitor = TermVisitor(self.grammar)
        visitor.visit(tree)
        self.assertTrue(visitor.term_correct)


class TestAntlr(unittest.TestCase):
    def test_to_antlr(self):
        result = antlr.to_antlr4(EXPR_GRAMMAR, name="expr")
        self.assertEqual("expr", result.name)
        self.assertEqual(6, len(result.rules))
        for rule in result.rules:
            match rule.name:
                case "start":
                    self.assertIsInstance(rule.expansion, antlr.Antlr4Concatenation)
                    self.assertEqual(1, len(rule.expansion.symbols))
                    self.assertIsInstance(
                        rule.expansion.symbols[0], antlr.Antlr4NonTerminal
                    )
                    self.assertEqual("expr", rule.expansion.symbols[0].symbol)

                case "expr":
                    self.assertIsInstance(rule.expansion, antlr.Antlr4Alternatives)
                    self.assertEqual(3, len(rule.expansion.alternatives))

                    self.assertEqual(3, len(rule.expansion.alternatives[0].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "term", rule.expansion.alternatives[0].symbols[0].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[1], antlr.Antlr4Terminal
                    )
                    self.assertEqual(
                        " + ", rule.expansion.alternatives[0].symbols[1].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[2],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "expr", rule.expansion.alternatives[0].symbols[2].symbol
                    )

                    self.assertEqual(3, len(rule.expansion.alternatives[1].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[1].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "term", rule.expansion.alternatives[1].symbols[0].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[1].symbols[1], antlr.Antlr4Terminal
                    )
                    self.assertEqual(
                        " - ", rule.expansion.alternatives[1].symbols[1].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[1].symbols[2],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "expr", rule.expansion.alternatives[1].symbols[2].symbol
                    )

                    self.assertEqual(1, len(rule.expansion.alternatives[2].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[2].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "term", rule.expansion.alternatives[2].symbols[0].symbol
                    )

                case "term":
                    self.assertIsInstance(rule.expansion, antlr.Antlr4Alternatives)
                    self.assertEqual(3, len(rule.expansion.alternatives))

                    self.assertEqual(3, len(rule.expansion.alternatives[0].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "factor", rule.expansion.alternatives[0].symbols[0].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[1], antlr.Antlr4Terminal
                    )
                    self.assertEqual(
                        " * ", rule.expansion.alternatives[0].symbols[1].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[2],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "term", rule.expansion.alternatives[0].symbols[2].symbol
                    )

                    self.assertEqual(3, len(rule.expansion.alternatives[1].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[1].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "factor", rule.expansion.alternatives[1].symbols[0].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[1].symbols[1], antlr.Antlr4Terminal
                    )
                    self.assertEqual(
                        " / ", rule.expansion.alternatives[1].symbols[1].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[1].symbols[2],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "term", rule.expansion.alternatives[1].symbols[2].symbol
                    )

                    self.assertEqual(1, len(rule.expansion.alternatives[2].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[2].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "factor", rule.expansion.alternatives[2].symbols[0].symbol
                    )

                case "factor":
                    self.assertIsInstance(rule.expansion, antlr.Antlr4Alternatives)
                    self.assertEqual(5, len(rule.expansion.alternatives))

                    self.assertEqual(2, len(rule.expansion.alternatives[0].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[0], antlr.Antlr4Terminal
                    )
                    self.assertEqual(
                        "+", rule.expansion.alternatives[0].symbols[0].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[1],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "factor", rule.expansion.alternatives[0].symbols[1].symbol
                    )

                    self.assertEqual(2, len(rule.expansion.alternatives[1].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[1].symbols[0], antlr.Antlr4Terminal
                    )
                    self.assertEqual(
                        "-", rule.expansion.alternatives[1].symbols[0].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[1].symbols[1],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "factor", rule.expansion.alternatives[1].symbols[1].symbol
                    )

                    self.assertEqual(3, len(rule.expansion.alternatives[2].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[2].symbols[0], antlr.Antlr4Terminal
                    )
                    self.assertEqual(
                        "(", rule.expansion.alternatives[2].symbols[0].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[2].symbols[1],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "expr", rule.expansion.alternatives[2].symbols[1].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[2].symbols[2], antlr.Antlr4Terminal
                    )
                    self.assertEqual(
                        ")", rule.expansion.alternatives[2].symbols[2].symbol
                    )

                    self.assertEqual(3, len(rule.expansion.alternatives[3].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[3].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "integer", rule.expansion.alternatives[3].symbols[0].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[3].symbols[1], antlr.Antlr4Terminal
                    )
                    self.assertEqual(
                        ".", rule.expansion.alternatives[3].symbols[1].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[3].symbols[2],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "integer", rule.expansion.alternatives[3].symbols[2].symbol
                    )

                    self.assertEqual(1, len(rule.expansion.alternatives[4].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[4].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "integer", rule.expansion.alternatives[4].symbols[0].symbol
                    )

                case "integer":
                    self.assertIsInstance(rule.expansion, antlr.Antlr4Alternatives)
                    self.assertEqual(2, len(rule.expansion.alternatives))

                    self.assertEqual(2, len(rule.expansion.alternatives[0].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "DIGIT", rule.expansion.alternatives[0].symbols[0].symbol
                    )
                    self.assertIsInstance(
                        rule.expansion.alternatives[0].symbols[1],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "integer", rule.expansion.alternatives[0].symbols[1].symbol
                    )

                    self.assertEqual(1, len(rule.expansion.alternatives[1].symbols))
                    self.assertIsInstance(
                        rule.expansion.alternatives[1].symbols[0],
                        antlr.Antlr4NonTerminal,
                    )
                    self.assertEqual(
                        "DIGIT", rule.expansion.alternatives[1].symbols[0].symbol
                    )

                case "DIGIT":
                    self.assertIsInstance(rule.expansion, antlr.Antlr4Alternatives)
                    self.assertEqual(10, len(rule.expansion.alternatives))

                    for i in range(0, 10):
                        self.assertEqual(1, len(rule.expansion.alternatives[i].symbols))
                        self.assertIsInstance(
                            rule.expansion.alternatives[i].symbols[0],
                            antlr.Antlr4Terminal,
                        )
                        self.assertEqual(
                            f"{i}", rule.expansion.alternatives[i].symbols[0].symbol
                        )

                case _:
                    self.fail(f"Cannot find rule {rule} in expectations")


PYTHON_PROGRAM_1 = """
def test():
    pass

test()
"""

PYTHON_PROGRAM_2 = """
class A():
    def __init__(self, x):
        self.x = x
        
    def add(self, x):
        return self.x + x
    
a = A(1)

if a.add(3) == 2:
    pass
"""

PYTHON_PROGRAM_3 = """
class A():
    def __init__(self, x):
        self.x = x
    
x = 1
del x
x = 1
x: int

for i in range(x):
    if i == 1:
        break
    continue
    
while i < 1:
    i += 1
    
with a as b:
    match a:
        case 0:
            pass
        case _:
            pass

raise a
assert a

try:
    A(1)
except:
    pass
    
import a
from b import c

global a

-(1 & 2 ^ 3)
c = [1, 2, 3]
()
{}
c[2:0:2]
"""

WHITESPACES = re.compile(r"\s")


class TestPython(unittest.TestCase):
    def _test_translation(self, program: str):
        tree = ast.parse(program)
        grammar_source = python.ToGrammarVisitor().visit(tree)
        for derivation_tree in EarleyParser(python.GRAMMAR).parse(grammar_source):
            new_tree = python.ToASTVisitor(python.GRAMMAR).visit(
                ComplexDerivationTree.from_parse_tree(derivation_tree)
            )
            self.assertEqual(
                WHITESPACES.sub("", ast.unparse(tree)),
                WHITESPACES.sub("", ast.unparse(new_tree)),
            )

    def test_valid_grammars(self):
        self.assertTrue(is_valid_grammar(python.GRAMMAR))
        self.assertTrue(is_valid_grammar(python.GENERATIVE_GRAMMAR))

    def _test_grammar(self, tree: str, start: str = "<start>", full=True):
        if full:
            grammar = python.GRAMMAR
        else:
            grammar = python.GENERATIVE_GRAMMAR
        successful = False
        for _ in EarleyParser(grammar, start_symbol=start).parse(tree):
            successful = True
        self.assertTrue(successful)

    def test_grammar_1(self):
        self._test_grammar("Module([],[])")

    def test_grammar_2(self):
        self._test_grammar("Expression(Call(Name(test),[],[]))")

    def test_grammar_3(self):
        self._test_grammar("Expression(Constant(0,))")

    def test_grammar_4(self):
        self._test_grammar(
            "Module([FunctionDef(test,arguments([],[],,[],[],,[]),[Pass()],[],,),"
            "Expr(Call(Name(test),[],[]))],[])"
        )

    def test_grammar_5(self):
        self._test_grammar("ExceptHandler(,,[Pass()])", "<ExceptHandler>")

    def test_translation_1(self):
        self._test_translation(PYTHON_PROGRAM_1)

    def test_translation_2(self):
        self._test_translation(PYTHON_PROGRAM_2)

    def test_translation_3(self):
        self._test_translation(PYTHON_PROGRAM_3)


class TestDefaultGrammar(unittest.TestCase):
    def __test_parse__(
        self, grammar: Grammar, start: str, members: List[str], no_members: List[str]
    ):
        parser = EarleyParser(grammar, start_symbol=start)
        for word in members:
            tree = None
            for tree in parser.parse(word):
                break
            self.assertIsNotNone(tree, f"Cannot parse {word}")
        for word in no_members:
            try:
                tree = None
                for tree in parser.parse(word):
                    break
            except SyntaxError:
                pass
            else:
                self.fail(f"Can parse {word}: {tree}")

    def test_numbers(self):
        self.__test_parse__(
            NUMBER,
            "<number>",
            ["1", "0", "31635473145237"],
            [
                "-0",
                "-49251865",
                "1.0",
                "-0.0000004",
                "a",
                "ab24",
                "abasg#",
                "abd ",
                "65&a\n asd",
                '46542 \\"asd' 'a"b',
            ],
        )

    def test_integer(self):
        self.__test_parse__(
            INTEGER,
            "<integer>",
            ["1", "-0", "0", "-49251865", "31635473145237"],
            [
                "1.0",
                "-0.0000004",
                "a",
                "ab24",
                "abasg#",
                "abd ",
                "65&a\n asd",
                '46542 \\"asd' 'a"b',
            ],
        )

    def test_float(self):
        self.__test_parse__(
            FLOAT,
            "<float>",
            ["1", "-0", "0", "-49251865", "31635473145237", "1.0", "-0.0000004"],
            ["a", "ab24", "abasg#", "abd ", "65&a\n asd", '46542 \\"asd' 'a"b'],
        )

    def test_string(self):
        self.__test_parse__(
            STRING,
            "<string>",
            [
                "1",
                "-0",
                "0",
                "-49251865",
                "31635473145237",
                "1.0",
                "-0.0000004",
                "a",
                "ab24",
                "abasg#",
            ],
            ["abd ", "65&a\n asd", '46542 \\"asd' 'a"b'],
        )

    def test_string_ws_escaped(self):
        self.__test_parse__(
            STRING_WS_ESCAPED_DOUBLE,
            "<string_ws_escaped_double>",
            [
                "1",
                "-0",
                "0",
                "-49251865",
                "31635473145237",
                "1.0",
                "-0.0000004",
                "a",
                "ab24",
                "abasg#",
                "abd ",
                "65&a\n asd",
                '46542 \\"asd',
            ],
            ['a"b'],
        )

    def test_string_ws(self):
        self.__test_parse__(
            STRING_WS,
            "<string_ws>",
            [
                "1",
                "-0",
                "0",
                "-49251865",
                "31635473145237",
                "1.0",
                "-0.0000004",
                "a",
                "ab24",
                "abasg#",
                "abd ",
                "65&a\n asd",
                '46542 \\"asd' 'a"b',
            ],
            [],
        )

    def test_cli(self):
        self.__test_parse__(
            CLI_GRAMMAR,
            "<start>",
            [
                "-a",
                "-a abc -b -c def abcdef",
                '-a "a b"',
                '"\\"This is a test\\""',
                "-c /test/",
            ],
            ["a -b c", '""This is a test""'],
        )

    def test_parser(self):
        self.__test_parse__(
            {
                "<s>": ["<a><a>", "<a>"],
                "<a>": ["a"],
            },
            "<s>",
            [
                "a",
                "aa",
            ],
            ["", "aaa"],
        )
