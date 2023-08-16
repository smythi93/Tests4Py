import re
from abc import ABC, abstractmethod
from typing import Callable, Any

from tests4py.grammars.fuzzer import Grammar
from tests4py.grammars.parser import EarleyParser
from tests4py.grammars.tree import ComplexDerivationTree

ILLEGAL_CHARS = re.compile(r"[^A-Za-z0-9_]")


class GrammarVisitor(ABC):
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.parser = EarleyParser(self.grammar)

    def visit_source(self, source: str):
        for tree in self.parser.parse(source):
            return self.visit(ComplexDerivationTree.from_parse_tree(tree))
        else:
            raise SyntaxError(
                f'"{source}" is not parsable with the grammar {self.grammar}'
            )

    @staticmethod
    def get_name(value: str):
        return ILLEGAL_CHARS.sub("", value)

    def generic_visit(self, node: ComplexDerivationTree) -> Any:
        for child in node.children:
            self.visit(child)

    def visit(self, node: ComplexDerivationTree) -> Any:
        method = "visit_" + self.get_name(node.value)
        visitor: Callable[[ComplexDerivationTree], None] = getattr(
            self, method, self.generic_visit
        )
        return visitor(node)


class Generator:
    @abstractmethod
    def generate(self):
        raise NotImplementedError()

    @abstractmethod
    def reset(self):
        raise NotImplementedError()
