"""
This is directly taken from:
https://www.fuzzingbook.org/html/Fuzzer.html
https://www.fuzzingbook.org/html/Grammars.html
https://www.fuzzingbook.org/html/GrammarFuzzer.html
"""
import random
import re
import subprocess
import sys
from typing import Dict, Any, Union, Tuple, List, Optional, Set, Callable

Outcome = str
Option = Dict[str, Any]
Expansion = Union[str, Tuple[str, Option]]
Grammar = Dict[str, List[Expansion]]

DerivationTree = Tuple[str, Optional[List[Any]]]

START_SYMBOL = "<start>"

RE_NONTERMINAL = re.compile(r"(<[^<> ]*>)")


def srange(characters: str) -> List[Expansion]:
    """Construct a list with all characters in the string"""
    return [c for c in characters]


def crange(character_start: str, character_end: str) -> List[Expansion]:
    return [chr(i) for i in range(ord(character_start), ord(character_end) + 1)]


def is_nonterminal(s):
    return RE_NONTERMINAL.match(s)


def nonterminals(expansion):
    # In later chapters, we allow expansions to be tuples,
    # with the expansion being the first element
    if isinstance(expansion, tuple):
        expansion = expansion[0]

    return RE_NONTERMINAL.findall(expansion)


def all_terminals(tree: DerivationTree) -> str:
    (symbol, children) = tree
    if children is None:
        # This is a nonterminal symbol not expanded yet
        return symbol

    if len(children) == 0:
        # This is a terminal symbol
        return symbol

    # This is an expanded symbol:
    # Concatenate all terminal symbols from all children
    return "".join([all_terminals(c) for c in children])


def tree_to_string(tree: DerivationTree) -> str:
    symbol, children, *_ = tree
    if children:
        return "".join(tree_to_string(c) for c in children)
    else:
        return "" if is_nonterminal(symbol) else symbol


def def_used_nonterminals(
    grammar: Grammar, start_symbol: str = START_SYMBOL
) -> Tuple[Optional[Set[str]], Optional[Set[str]]]:
    """Return a pair (`defined_nonterminals`, `used_nonterminals`) in `grammar`.
    In case of error, return (`None`, `None`)."""

    defined_nonterminals = set()
    used_nonterminals = {start_symbol}

    for defined_nonterminal in grammar:
        defined_nonterminals.add(defined_nonterminal)
        expansions = grammar[defined_nonterminal]
        if not isinstance(expansions, list):
            print(
                repr(defined_nonterminal) + ": expansion is not a list", file=sys.stderr
            )
            return None, None

        if len(expansions) == 0:
            print(repr(defined_nonterminal) + ": expansion list empty", file=sys.stderr)
            return None, None

        for expansion in expansions:
            if isinstance(expansion, tuple):
                expansion = expansion[0]
            if not isinstance(expansion, str):
                print(
                    repr(defined_nonterminal)
                    + ": "
                    + repr(expansion)
                    + ": not a string",
                    file=sys.stderr,
                )
                return None, None

            for used_nonterminal in nonterminals(expansion):
                used_nonterminals.add(used_nonterminal)

    return defined_nonterminals, used_nonterminals


def reachable_nonterminals(
    grammar: Grammar, start_symbol: str = START_SYMBOL
) -> Set[str]:
    reachable = set()

    def _find_reachable_nonterminals(g, symbol):
        nonlocal reachable
        reachable.add(symbol)
        for expansion in g.get(symbol, []):
            for nonterminal in nonterminals(expansion):
                if nonterminal not in reachable:
                    _find_reachable_nonterminals(g, nonterminal)

    _find_reachable_nonterminals(grammar, start_symbol)
    return reachable


def unreachable_nonterminals(grammar: Grammar, start_symbol=START_SYMBOL) -> Set[str]:
    return grammar.keys() - reachable_nonterminals(grammar, start_symbol)


def exp_string(expansion: Expansion) -> str:
    """Return the string to be expanded"""
    if isinstance(expansion, str):
        return expansion
    return expansion[0]


def exp_opts(expansion: Expansion) -> Dict[str, Any]:
    """Return the options of an expansion.  If options are not defined, return {}"""
    if isinstance(expansion, str):
        return {}
    return expansion[1]


def opts_used(grammar: Grammar) -> Set[str]:
    used_opts = set()
    for symbol in grammar:
        for expansion in grammar[symbol]:
            used_opts |= set(exp_opts(expansion).keys())
    return used_opts


def is_valid_grammar(
    grammar: Grammar, start_symbol: str = START_SYMBOL, supported_opts: Set[str] = None
) -> bool:
    """Check if the given `grammar` is valid.
    `start_symbol`: optional start symbol (default: `<start>`)
    `supported_opts`: options supported (default: none)"""

    defined_nonterminals, used_nonterminals = def_used_nonterminals(
        grammar, start_symbol
    )
    if defined_nonterminals is None or used_nonterminals is None:
        return False

    # Do not complain about '<start>' being not used,
    # even if start_symbol is different
    if START_SYMBOL in grammar:
        used_nonterminals.add(START_SYMBOL)

    for unused_nonterminal in defined_nonterminals - used_nonterminals:
        print(repr(unused_nonterminal) + ": defined, but not used", file=sys.stderr)
    for undefined_nonterminal in used_nonterminals - defined_nonterminals:
        print(repr(undefined_nonterminal) + ": used, but not defined", file=sys.stderr)

    # Symbols must be reachable either from <start> or given start symbol
    unreachable = unreachable_nonterminals(grammar, start_symbol)
    msg_start_symbol = start_symbol

    if START_SYMBOL in grammar:
        unreachable -= reachable_nonterminals(grammar, START_SYMBOL)
        if start_symbol != START_SYMBOL:
            msg_start_symbol += " or " + START_SYMBOL

    for unreachable_nonterminal in unreachable:
        print(
            repr(unreachable_nonterminal) + ": unreachable from " + msg_start_symbol,
            file=sys.stderr,
        )

    supported_opts = set() if supported_opts is None else supported_opts
    if len(supported_opts) > 0:
        used_but_not_supported_opts = opts_used(grammar).difference(supported_opts)
        for opt in used_but_not_supported_opts:
            print("warning: option " + repr(opt) + " is not supported", file=sys.stderr)

    return used_nonterminals == defined_nonterminals and len(unreachable) == 0


class Runner:
    """Base class for testing inputs."""

    # Test outcomes
    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"

    def __init__(self) -> None:
        """Initialize"""
        pass

    def run(self, inp: str) -> Any:
        """Run the runner with the given input"""
        return inp, Runner.UNRESOLVED


class PrintRunner(Runner):
    """Simple runner, printing the input."""

    def run(self, inp) -> Any:
        """Print the given input"""
        print(inp)
        return inp, Runner.UNRESOLVED


class GrammarFuzzer:
    """Produce strings from grammars efficiently, using derivation trees."""

    def __init__(
        self,
        grammar: Grammar,
        start_symbol: str = START_SYMBOL,
        min_nonterminals: int = 0,
        max_nonterminals: int = 10,
        disp: bool = False,
        log: Union[bool, int] = False,
    ) -> None:
        """Produce strings from `grammar`, starting with `start_symbol`.
        If `min_nonterminals` or `max_nonterminals` is given, use them as limits
        for the number of nonterminals produced.
        If `disp` is set, display the intermediate derivation trees.
        If `log` is set, show intermediate steps as text on standard output."""

        self.expand_node = None
        self.derivation_tree = None
        self.grammar = grammar
        self.start_symbol = start_symbol
        self.min_nonterminals = min_nonterminals
        self.max_nonterminals = max_nonterminals
        self.disp = disp
        self.log = log
        self.check_grammar()  # Invokes is_valid_grammar()

    def check_grammar(self) -> None:
        """Check the grammar passed"""
        assert self.start_symbol in self.grammar
        assert is_valid_grammar(
            self.grammar,
            start_symbol=self.start_symbol,
            supported_opts=self.supported_opts(),
        )

    @staticmethod
    def supported_opts() -> Set[str]:
        """Set of supported options. To be overloaded in subclasses."""
        return set()  # We don't support specific options

    def init_tree(self) -> DerivationTree:
        return self.start_symbol, None

    # noinspection PyUnusedLocal
    @staticmethod
    def choose_node_expansion(
        node: DerivationTree, children_alternatives: List[List[DerivationTree]]
    ) -> int:
        """Return index of expansion in `children_alternatives` to be selected.
        'children_alternatives': a list of possible children for `node`.
        Defaults to random. To be overloaded in subclasses."""
        return random.randrange(0, len(children_alternatives))

    @staticmethod
    def expansion_to_children(expansion: Expansion) -> List[DerivationTree]:
        # print("Converting " + repr(expansion))
        # strings contains all substrings -- both terminals and nonterminals such
        # that ''.join(strings) == expansion

        expansion = exp_string(expansion)
        assert isinstance(expansion, str)

        if expansion == "":  # Special case: epsilon expansion
            return [("", [])]

        strings = re.split(RE_NONTERMINAL, expansion)
        return [
            (s, None) if is_nonterminal(s) else (s, []) for s in strings if len(s) > 0
        ]

    def expand_node_randomly(self, node: DerivationTree) -> DerivationTree:
        """Choose a random expansion for `node` and return it"""
        (symbol, children) = node
        assert children is None

        if self.log:
            print("Expanding", all_terminals(node), "randomly")

        # Fetch the possible expansions from grammar...
        expansions = self.grammar[symbol]
        children_alternatives: List[List[DerivationTree]] = [
            self.expansion_to_children(expansion) for expansion in expansions
        ]

        # ... and select a random expansion
        index = self.choose_node_expansion(node, children_alternatives)
        chosen_children = children_alternatives[index]

        # Process children (for subclasses)
        chosen_children = self.process_chosen_children(
            chosen_children, expansions[index]
        )

        # Return with new children
        return symbol, chosen_children

    # noinspection PyUnusedLocal
    @staticmethod
    def process_chosen_children(
        chosen_children: List[DerivationTree], expansion: Expansion
    ) -> List[DerivationTree]:
        """Process children after selection.  By default, does nothing."""
        return chosen_children

    def possible_expansions(self, node: DerivationTree) -> int:
        (symbol, children) = node
        if children is None:
            return 1

        return sum(self.possible_expansions(c) for c in children)

    def any_possible_expansions(self, node: DerivationTree) -> bool:
        (symbol, children) = node
        if children is None:
            return True

        return any(self.any_possible_expansions(c) for c in children)

    # noinspection PyUnusedLocal
    @staticmethod
    def choose_tree_expansion(
        tree: DerivationTree, children: List[DerivationTree]
    ) -> int:
        """Return index of subtree in `children` to be selected for expansion.
        Defaults to random."""
        return random.randrange(0, len(children))

    def expand_tree_once(self, tree: DerivationTree) -> DerivationTree:
        """Choose an unexpanded symbol in tree; expand it.
        Can be overloaded in subclasses."""
        (symbol, children) = tree
        if children is None:
            # Expand this node
            return self.expand_node(tree)

        # Find all children with possible expansions
        expandable_children = [c for c in children if self.any_possible_expansions(c)]

        # `index_map` translates an index in `expandable_children`
        # back into the original index in `children`
        index_map = [i for (i, c) in enumerate(children) if c in expandable_children]

        # Select a random child
        child_to_be_expanded = self.choose_tree_expansion(tree, expandable_children)

        # Expand in place
        children[index_map[child_to_be_expanded]] = self.expand_tree_once(
            expandable_children[child_to_be_expanded]
        )

        return tree

    def symbol_cost(self, symbol: str, seen: Set[str] = None) -> Union[int, float]:
        return min(
            self.expansion_cost(e, (set() if seen is None else seen) | {symbol})
            for e in self.grammar[symbol]
        )

    def expansion_cost(
        self, expansion: Expansion, seen: Set[str] = None
    ) -> Union[int, float]:
        seen = set() if seen is None else seen
        symbols = nonterminals(expansion)
        if len(symbols) == 0:
            return 1  # no symbol

        if any(s in seen for s in symbols):
            return float("inf")

        # the value of an expansion is the sum of all expandable variables
        # inside + 1
        return sum(self.symbol_cost(s, seen) for s in symbols) + 1

    def expand_node_by_cost(
        self, node: DerivationTree, choose: Callable = min
    ) -> DerivationTree:
        (symbol, children) = node
        assert children is None

        # Fetch the possible expansions from grammar...
        expansions = self.grammar[symbol]

        children_alternatives_with_cost = [
            (
                self.expansion_to_children(expansion),
                self.expansion_cost(expansion, {symbol}),
                expansion,
            )
            for expansion in expansions
        ]

        costs = [cost for (child, cost, expansion) in children_alternatives_with_cost]
        chosen_cost = choose(costs)
        children_with_chosen_cost = [
            child
            for (child, child_cost, _) in children_alternatives_with_cost
            if child_cost == chosen_cost
        ]
        expansion_with_chosen_cost = [
            expansion
            for (_, child_cost, expansion) in children_alternatives_with_cost
            if child_cost == chosen_cost
        ]

        index = self.choose_node_expansion(node, children_with_chosen_cost)

        chosen_children = children_with_chosen_cost[index]
        chosen_expansion = expansion_with_chosen_cost[index]
        chosen_children = self.process_chosen_children(
            chosen_children, chosen_expansion
        )

        # Return with a new list
        return symbol, chosen_children

    def expand_node_min_cost(self, node: DerivationTree) -> DerivationTree:
        if self.log:
            print("Expanding", all_terminals(node), "at minimum cost")

        return self.expand_node_by_cost(node, min)

    def expand_node_max_cost(self, node: DerivationTree) -> DerivationTree:
        if self.log:
            print("Expanding", all_terminals(node), "at maximum cost")

        return self.expand_node_by_cost(node, max)

    def expand_tree_with_strategy(
        self,
        tree: DerivationTree,
        expand_node_method: Callable,
        limit: Optional[int] = None,
    ):
        """Expand tree using `expand_node_method` as node expansion function
        until the number of possible expansions reaches `limit`."""
        self.expand_node = expand_node_method
        while (
            limit is None or self.possible_expansions(tree) < limit
        ) and self.any_possible_expansions(tree):
            tree = self.expand_tree_once(tree)
        return tree

    def expand_tree(self, tree: DerivationTree) -> DerivationTree:
        """Expand `tree` in a three-phase strategy until all expansions are complete."""
        tree = self.expand_tree_with_strategy(
            tree, self.expand_node_max_cost, self.min_nonterminals
        )
        tree = self.expand_tree_with_strategy(
            tree, self.expand_node_randomly, self.max_nonterminals
        )
        tree = self.expand_tree_with_strategy(tree, self.expand_node_min_cost)

        assert self.possible_expansions(tree) == 0

        return tree

    def fuzz_tree(self) -> DerivationTree:
        """Produce a derivation tree from the grammar."""
        return self.expand_tree(self.init_tree())

    def fuzz(self) -> str:
        """Produce a string from the grammar."""
        return all_terminals(self.fuzz_tree())

    def run(
        self, runner: Runner = Runner()
    ) -> Tuple[subprocess.CompletedProcess, Outcome]:
        """Run `runner` with fuzz input"""
        return runner.run(self.fuzz())

    def runs(
        self, runner: Runner = PrintRunner(), trials: int = 10
    ) -> List[Tuple[subprocess.CompletedProcess, Outcome]]:
        """Run `runner` with fuzz input, `trials` times"""
        return [self.run(runner) for _ in range(trials)]
