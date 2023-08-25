"""
This is directly taken from:
https://www.fuzzingbook.org/html/Parser.html
"""
import itertools
import random
import re
from typing import List, Tuple, Iterable, Generator, Dict, Collection

from tests4py.grammars.fuzzer import (
    Grammar,
    START_SYMBOL,
    DerivationTree,
    tree_to_string,
    RE_NONTERMINAL,
)

CanonicalGrammar = Dict[str, List[List[str]]]


class Column:
    def __init__(self, index, letter):
        self.index, self.letter = index, letter
        self.states, self._unique = [], {}

    def __str__(self):
        return "%s chart[%d]\n%s" % (
            self.letter,
            self.index,
            "\n".join(str(state) for state in self.states if state.finished()),
        )

    def add(self, state):
        if state in self._unique:
            return self._unique[state]
        self._unique[state] = state
        self.states.append(state)
        state.e_col = self
        return self._unique[state]


class Item:
    def __init__(self, name, expr, dot):
        self.name, self.expr, self.dot = name, expr, dot

    def finished(self):
        return self.dot >= len(self.expr)

    def advance(self):
        return Item(self.name, self.expr, self.dot + 1)

    def at_dot(self):
        return self.expr[self.dot] if self.dot < len(self.expr) else None


class State(Item):
    def __init__(self, name, expr, dot, s_col, e_col=None):
        super().__init__(name, expr, dot)
        self.s_col, self.e_col = s_col, e_col

    def __str__(self):
        def idx(var):
            return var.index if var else -1

        return (
            self.name
            + ":= "
            + " ".join(
                [str(p) for p in [*self.expr[: self.dot], "|", *self.expr[self.dot :]]]
            )
            + "(%d,%d)" % (idx(self.s_col), idx(self.e_col))
        )

    def copy(self):
        return State(self.name, self.expr, self.dot, self.s_col, self.e_col)

    def _t(self):
        return self.name, self.expr, self.dot, self.s_col.index

    def __hash__(self):
        return hash(self._t())

    def __eq__(self, other):
        return self._t() == other._t()

    def advance(self):
        return State(self.name, self.expr, self.dot + 1, self.s_col)


def single_char_tokens(grammar: Grammar) -> Dict[str, List[List[Collection[str]]]]:
    g_ = {}
    for key in grammar:
        rules_ = []
        for rule in grammar[key]:
            rule_ = []
            for token in rule:
                if token in grammar:
                    rule_.append(token)
                else:
                    rule_.extend(token)
            rules_.append(rule_)
        g_[key] = rules_
    return g_


def canonical(grammar: Grammar) -> CanonicalGrammar:
    def split(expansion):
        if isinstance(expansion, tuple):
            expansion = expansion[0]

        return [token for token in re.split(RE_NONTERMINAL, expansion) if token]

    return {
        k: [split(expression) for expression in alternatives]
        for k, alternatives in grammar.items()
    }


def non_canonical(grammar):
    new_grammar = {}
    for k in grammar:
        rules = grammar[k]
        new_rules = []
        for rule in rules:
            new_rules.append("".join(rule))
        new_grammar[k] = new_rules
    return new_grammar


class Parser:
    """Base class for parsing."""

    def __init__(self, grammar, **kwargs):
        self._start_symbol = kwargs.get("start_symbol", START_SYMBOL)
        self.log = kwargs.get("log", False)
        self.tokens = kwargs.get("tokens", set())
        self.coalesce_tokens = kwargs.get("coalesce", True)
        canonical_grammar = kwargs.get("canonical", False)
        if canonical_grammar:
            self.c_grammar = single_char_tokens(grammar)
            self._grammar = non_canonical(grammar)
        else:
            self._grammar = dict(grammar)
            self.c_grammar = single_char_tokens(canonical(grammar))
        # we do not require a single rule for the start symbol
        if len(grammar.get(self._start_symbol, [])) != 1:
            self.c_grammar["<>"] = [[self._start_symbol]]

    def grammar(self) -> Grammar:
        """Return the grammar of this parser."""
        return self._grammar

    def start_symbol(self) -> str:
        """Return the start symbol of this parser."""
        return self._start_symbol

    def parse_prefix(self, text: str) -> Tuple[int, Iterable[DerivationTree]]:
        """Return pair (cursor, forest) for longest prefix of text.
        To be defined in subclasses."""
        raise NotImplementedError

    def parse(self, text: str) -> Iterable[DerivationTree]:
        """Parse `text` using the grammar.
        Return an iterable of parse trees."""
        cursor, forest = self.parse_prefix(text)
        if cursor < len(text):
            raise SyntaxError("at " + repr(text[cursor:]))
        return [self.prune_tree(tree) for tree in forest]

    def parse_on(self, text: str, start_symbol: str) -> Generator:
        old_start = self._start_symbol
        try:
            self._start_symbol = start_symbol
            yield from self.parse(text)
        finally:
            self._start_symbol = old_start

    def coalesce(self, children: List[DerivationTree]) -> List[DerivationTree]:
        last = ""
        new_lst: List[DerivationTree] = []
        for cn, cc in children:
            if cn not in self._grammar:
                last += cn
            else:
                if last:
                    new_lst.append((last, []))
                    last = ""
                new_lst.append((cn, cc))
        if last:
            new_lst.append((last, []))
        return new_lst

    def prune_tree(self, tree):
        name, children = tree
        if name == "<>":
            assert len(children) == 1
            return self.prune_tree(children[0])
        if self.coalesce_tokens:
            children = self.coalesce(children)
        if name in self.tokens:
            return name, [(tree_to_string(tree), [])]
        else:
            return name, [self.prune_tree(c) for c in children]


class EarleyParser(Parser):
    """Earley Parser. This parser can parse any context-free grammar."""

    def __init__(self, grammar: Grammar, **kwargs) -> None:
        super().__init__(grammar, **kwargs)
        self.table = None
        self.chart: List = []  # for type checking

    def chart_parse(self, words, start):
        alt = self.c_grammar[start]
        if len(alt) > 1:
            alt = (start,)
            start = f"<parser_access_{random.randbytes(32).hex()}>"
        else:
            alt = tuple(*self.c_grammar[start])
        chart = [Column(i, tok) for i, tok in enumerate([None, *words])]
        chart[0].add(State(start, alt, 0, chart[0]))
        return self.fill_chart(chart)

    # noinspection PyUnusedLocal
    def predict(self, col, sym, state):
        for alt in self.c_grammar[sym]:
            col.add(State(sym, tuple(alt), 0, col))

    @staticmethod
    def scan(col, state, letter):
        if letter == col.letter:
            col.add(state.advance())

    def complete(self, col, state):
        return self.earley_complete(col, state)

    @staticmethod
    def earley_complete(col, state):
        parent_states = [st for st in state.s_col.states if st.at_dot() == state.name]
        for st in parent_states:
            col.add(st.advance())

    def fill_chart(self, chart):
        for i, col in enumerate(chart):
            for state in col.states:
                if state.finished():
                    self.complete(col, state)
                else:
                    sym = state.at_dot()
                    if sym in self.c_grammar:
                        self.predict(col, sym, state)
                    else:
                        if i + 1 >= len(chart):
                            continue
                        self.scan(chart[i + 1], state, sym)
            if self.log:
                print(col, "\n")
        return chart

    def parse_prefix(self, text) -> Tuple[int, List[Item]]:
        self.table = self.chart_parse(text, self.start_symbol())
        for col in reversed(self.table):
            states = [st for st in col.states if st.name == self.start_symbol()]
            if states:
                return col.index, states
        return -1, []

    def parse(self, text):
        cursor, states = self.parse_prefix(text)
        start = next((s for s in states if s.finished()), None)

        if cursor < len(text) or not start:
            raise SyntaxError("at " + repr(text[cursor:]))

        forest = self.parse_forest(self.table, start)
        for tree in self.extract_trees(forest):
            yield self.prune_tree(tree)

    def parse_paths(self, named_expr, chart, frm, til):
        def paths(state, start, k, e):
            if not e:
                return [[(state, k)]] if start == frm else []
            else:
                return [
                    [(state, k)] + r for r in self.parse_paths(e, chart, frm, start)
                ]

        *expr, var = named_expr
        if var not in self.c_grammar:
            starts = (
                [(var, til - len(var), "t")]
                if til > 0 and chart[til].letter == var
                else []
            )
        else:
            starts = [
                (s, s.s_col.index, "n")
                for s in chart[til].states
                if s.finished() and s.name == var
            ]

        return [p for s, start, k in starts for p in paths(s, start, k, expr)]

    def forest(self, s, kind, chart):
        return self.parse_forest(chart, s) if kind == "n" else (s, [])

    def parse_forest(self, chart, state):
        path_exprs = (
            self.parse_paths(state.expr, chart, state.s_col.index, state.e_col.index)
            if state.expr
            else []
        )
        return state.name, [
            [(v, k, chart) for v, k in reversed(path_expr)] for path_expr in path_exprs
        ]

    def extract_a_tree(self, forest_node):
        name, paths = forest_node
        if not paths:
            return name, []
        return name, [self.extract_a_tree(self.forest(*p)) for p in paths[0]]

    def extract_trees(self, forest_node):
        name, paths = forest_node
        if not paths:
            yield name, []

        for path in paths:
            p_trees = [self.extract_trees(self.forest(*p)) for p in path]
            for p in itertools.product(*p_trees):
                yield name, p
