import re
from abc import ABC, abstractmethod
from typing import Callable, Any

from fuzzingbook.Grammars import Grammar

# noinspection PyPackageRequirements
from isla.derivation_tree import DerivationTree

# noinspection PyPackageRequirements
from isla.parser import EarleyParser

ILLEGAL_CHARS = re.compile(r"[^A-Za-z0-9_]")


class GrammarVisitor(ABC):
    def __init__(self, grammar: Grammar):
        self.grammar = grammar
        self.parser = EarleyParser(self.grammar)

    def visit_source(self, source: str):
        for tree in self.parser.parse(source):
            return self.visit(DerivationTree.from_parse_tree(tree))
        else:
            raise SyntaxError(
                f'"{source}" is not parsable with the grammar {self.grammar}'
            )

    @staticmethod
    def get_name(value: str):
        return ILLEGAL_CHARS.sub("", value)

    def generic_visit(self, node: DerivationTree) -> Any:
        for child in node.children:
            self.visit(child)

    def visit(self, node: DerivationTree) -> Any:
        method = "visit_" + self.get_name(node.value)
        visitor: Callable[[DerivationTree], None] = getattr(
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
