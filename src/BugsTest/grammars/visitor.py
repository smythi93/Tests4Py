import re
from typing import Callable, Any

from isla.derivation_tree import DerivationTree

ILLEGAL_CHARS = re.compile(r'[^A-Za-z0-9_]')


class GrammarVisitor:

    @staticmethod
    def get_name(value: str):
        return ILLEGAL_CHARS.sub('', value)

    def generic_visit(self, node: DerivationTree) -> Any:
        for child in node.children:
            self.visit(child)

    def visit(self, node: DerivationTree) -> Any:
        method = 'visit_' + self.get_name(node.value)
        visitor: Callable[[DerivationTree], None] = getattr(self, method, self.generic_visit)
        return visitor(node)
