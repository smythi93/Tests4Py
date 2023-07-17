from os import PathLike
from typing import List, Union, Any, Callable

from fuzzingbook.Grammars import Grammar, RE_NONTERMINAL, is_nonterminal

from tests4py.grammars.utils import GrammarVisitor


class Antlr4AST:
    def __str__(self):
        return repr(self)


class Antlr4NonTerminal(Antlr4AST):
    def __repr__(self):
        return self.symbol

    def __init__(self, symbol: str):
        self.symbol = symbol


class Antlr4Terminal(Antlr4AST):
    def __repr__(self):
        return repr(self.symbol)

    def __init__(self, symbol: str):
        self.symbol = symbol


class Antlr4Concatenation(Antlr4AST):
    def __repr__(self):
        return " ".join(repr(symbol) for symbol in self.symbols)

    def __init__(self, symbols: List[Union[Antlr4Terminal, Antlr4NonTerminal]]):
        self.symbols = symbols


class Antlr4Alternatives(Antlr4AST):
    def __repr__(self):
        return " | ".join(repr(alternative) for alternative in self.alternatives)

    def __init__(self, alternatives: List[Antlr4Concatenation]):
        self.alternatives = alternatives


class Antlr4Rule(Antlr4AST):
    def __repr__(self):
        return f"{self.name} : {repr(self.expansion)} ;"

    def __init__(
        self, name: str, expansion: Union[Antlr4Alternatives, Antlr4Concatenation]
    ):
        self.name = name
        self.expansion = expansion


class Antlr4Grammar(Antlr4AST):
    def __repr__(self):
        return f"grammar {self.name};\n\n" + "\n\n".join(
            repr(rule) for rule in self.rules
        )

    def __init__(self, name: str, rules: List[Antlr4Rule]):
        self.name = name
        self.rules = rules


class Antlr4Visitor:
    def generic_visit(self, node: Antlr4AST) -> Any:
        for attr in dir(node):
            attr = getattr(node, attr, None)
            if isinstance(attr, Antlr4AST):
                self.visit(attr)
            elif isinstance(attr, list):
                for item in attr:
                    if isinstance(item, Antlr4AST):
                        self.visit(item)

    def visit(self, node: Antlr4AST) -> Any:
        method = "visit_" + node.__class__.__name__
        visitor: Callable[[Antlr4AST], Any] = getattr(self, method, self.generic_visit)
        return visitor(node)


class TerminalFinder(Antlr4Visitor):
    def __init__(self):
        self.terminal_symbols = list()
        self.non_terminal_symbol_found = False

    def visit_Antlr4NonTerminal(self, node: Antlr4NonTerminal):
        self.non_terminal_symbol_found = True

    def visit_Antlr4Rule(self, node: Antlr4Rule):
        self.non_terminal_symbol_found = False
        self.visit(node.expansion)
        if not self.non_terminal_symbol_found:
            self.terminal_symbols.append(node.name)


class LexerReplacer(Antlr4Visitor):
    def __init__(self, terminal_symbols: List[str]):
        self.terminal_symbols = terminal_symbols

    def visit_Antlr4NonTerminal(self, node: Antlr4NonTerminal):
        if node.symbol in self.terminal_symbols:
            node.symbol = node.symbol.upper()
        else:
            node.symbol.lower()

    def visit_Antlr4Rule(self, node: Antlr4Rule):
        if node.name in self.terminal_symbols:
            node.name = node.name.upper()
        else:
            node.name = node.name.lower()
        self.visit(node.expansion)


def _parse_concatenation(concatenation: str) -> Antlr4Concatenation:
    symbols: List[Union[Antlr4Terminal, Antlr4NonTerminal]] = list()
    for token in RE_NONTERMINAL.split(concatenation):
        if token:
            if is_nonterminal(token):
                symbols.append(Antlr4NonTerminal(GrammarVisitor.get_name(token)))
            else:
                symbols.append(Antlr4Terminal(token))
    return Antlr4Concatenation(symbols)


def _parse_alternatives(alternatives: List[str]) -> Antlr4Alternatives:
    return Antlr4Alternatives(
        [_parse_concatenation(concatenation) for concatenation in alternatives]
    )


def _parse_rule(rule: str, expansions: List[str]) -> Antlr4Rule:
    if isinstance(expansions, tuple):
        expansions = expansions[0]
    if len(expansions) == 1:
        expansion = _parse_concatenation(expansions[0])
    else:
        expansion = _parse_alternatives(expansions)
    return Antlr4Rule(GrammarVisitor.get_name(rule), expansion)


def to_antlr4(grammar: Grammar, name: str = "TMP") -> Antlr4Grammar:
    rules: List[Antlr4Rule] = list()
    for rule in grammar:
        rules.append(_parse_rule(rule, grammar[rule]))
    g = Antlr4Grammar(name, rules)
    terminal_finder = TerminalFinder()
    terminal_finder.visit(g)
    LexerReplacer(terminal_finder.terminal_symbols).visit(g)
    return g


def to_antlr4_string(grammar: Grammar, name: str = "TMP") -> str:
    return str(to_antlr4(grammar, name))


def to_antlr4_file(file: PathLike, grammar: Grammar, name: str = "TMP"):
    with open(file, "w") as fp:
        fp.write(to_antlr4_string(grammar, name))
