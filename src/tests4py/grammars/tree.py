import re
from typing import Optional, Sequence, Tuple, List

NON_TERMINAL_PATTERN = re.compile(r"(<[^<> ]*>)")


class ParseError(ValueError):
    pass


class ComplexDerivationTree:
    def __init__(
        self,
        value: str,
        children: Optional[Sequence["ComplexDerivationTree"]] = None,
    ):
        self._value = value
        self._children = () if children is None else tuple(children)

        self._len = len(self._children)

    @property
    def children(self) -> Tuple["ComplexDerivationTree"]:
        return self._children

    @property
    def value(self) -> str:
        return self._value

    def num_children(self) -> int:
        return 0 if self.children is None else len(self.children)

    def depth(self) -> int:
        if not self.children:
            return 1
        return 1 + max(child.depth() for child in self.children)

    def __len__(self):
        return self._len

    @staticmethod
    def from_parse_tree(tree: Tuple[str, List]):
        stack: List[Tuple[Tuple, Tuple[str, List]]] = [tree]
        flat: List[Tuple[Tuple, Tuple[str, List]]] = []
        while stack:
            symbol, children = stack.pop()
            flat.append((symbol, len(children)))
            for child in reversed(children):
                stack.append(child)

        trees: List[ComplexDerivationTree] = []
        for symbol, children in reversed(flat):
            trees.append(
                ComplexDerivationTree(symbol, [trees.pop() for _ in range(children)])
            )

        if len(trees) != 1:
            raise ParseError("Not a parse tree")

        return trees[0]

    def __iter__(self):
        return self

    def __next__(self):
        yield from self.children

    def to_string(self) -> str:
        result = []
        stack = [self]

        while stack:
            node = stack.pop(0)
            symbol = node.value
            children = node.children

            if not children:
                result.append("" if NON_TERMINAL_PATTERN.match(symbol) else symbol)
            else:
                stack = list(children) + stack

        return "".join(result)

    def __str__(self) -> str:
        return self.to_string()
