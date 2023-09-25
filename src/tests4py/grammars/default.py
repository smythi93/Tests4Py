import string
from typing import List

from tests4py.grammars.fuzzer import (
    srange,
    Grammar,
    crange,
    is_valid_grammar,
    def_used_nonterminals,
    START_SYMBOL,
    unreachable_nonterminals,
    reachable_nonterminals,
)

PRINTABLE = srange(string.printable)
ASCII = srange(string.ascii_letters + string.digits + "_")
PRINTABLE_ESCAPED_DOUBLE = srange(string.printable.replace('"', "")) + ['\\"']
PRINTABLE_ESCAPED_SINGLE = srange(string.printable.replace("'", "")) + ["\\'"]
PRINTABLE_WITHOUT_WS = srange(string.digits + string.ascii_letters + string.punctuation)
PRINTABLE_CLI = srange(
    (string.digits + string.ascii_letters + string.punctuation)
    .replace('"', "")
    .replace("'", "")
    .replace("-", "")
)
DIGITS = crange("0", "9")
NON_ZERO_DIGITS = crange("1", "9")


def get_string_rule(possible_chars: List[str], suffix: str = ""):
    string_rule = f"<string{suffix}>"
    string_not_empty_rule = f"<str{suffix}>"
    chars_rule = f"<chars{suffix}>"
    char_rule = f"<char{suffix}>"
    return {
        string_rule: ["", string_not_empty_rule],
        string_not_empty_rule: [chars_rule],
        chars_rule: [char_rule, char_rule + chars_rule],
        char_rule: possible_chars,
    }


STRING: Grammar = get_string_rule(PRINTABLE_WITHOUT_WS)
STRING_WS: Grammar = get_string_rule(PRINTABLE, suffix="_ws")
STRING_WS_ESCAPED_DOUBLE: Grammar = get_string_rule(
    PRINTABLE_ESCAPED_DOUBLE, suffix="_ws_escaped_double"
)
STRING_WS_ESCAPED_SINGLE: Grammar = get_string_rule(
    PRINTABLE_ESCAPED_SINGLE, suffix="_ws_escaped_single"
)
STRING_ASCII: Grammar = get_string_rule(ASCII, suffix="_ascii")
STRING_CLI: Grammar = get_string_rule(PRINTABLE_CLI, suffix="_cli")
NUMBER: Grammar = {
    "<number>": ["0", "<non_zero><digits>"],
    "<non_zero>": NON_ZERO_DIGITS,
    "<digits>": ["", "<digit><digits>"],
    "<digit>": DIGITS,
}
INTEGER: Grammar = dict({"<integer>": ["<number>", "-<number>", "+<number>"]}, **NUMBER)
FLOAT: Grammar = dict(
    {"<float>": ["<integer>", "<integer>.<decimal>"], "<decimal>": ["<digit><digits>"]},
    **INTEGER,
)


def get_possible_options(option: str, arg: str) -> List[str]:
    return [
        f"{option}{arg}",
        f"{option}<sep>{arg}",
        f"{option}={arg}",
    ]


CLI_GRAMMAR = dict(
    {
        "<start>": ["<options><sep><args>", "<options>", "<args>"],
        "<options>": ["", "<option_list>"],
        "<option_list>": ["<option>", "<option><sep><option_list>"],
        "<args>": ["", "<arg_list>"],
        "<arg_list>": ["<arg>", "<arg><sep><arg_list>"],
        "<arg>": [
            "<unescaped>",
            '"<escaped_double>"',
            "'<escaped_single>'",
        ],
        "<unescaped>": ["<string_cli>"],
        "<escaped_double>": ["<string_ws_escaped_double>"],
        "<escaped_single>": ["<string_ws_escaped_single>"],
        "<option>": [
            "<flag>",
            "<op>",
        ],
        "<flag>": ["-<unescaped>", "--<unescaped>"],
        "<op>": get_possible_options("-<unescaped>", "<arg>")
        + get_possible_options("--<unescaped>", "<arg>"),
        "<sep>": [" ", "\n"],
    },
    **STRING_CLI,
    **STRING_WS_ESCAPED_DOUBLE,
    **STRING_WS_ESCAPED_SINGLE,
)

assert is_valid_grammar(STRING, "<string>")
assert is_valid_grammar(STRING_WS, "<string_ws>")
assert is_valid_grammar(STRING_WS_ESCAPED_DOUBLE, "<string_ws_escaped_double>")
assert is_valid_grammar(STRING_WS_ESCAPED_SINGLE, "<string_ws_escaped_single>")
assert is_valid_grammar(NUMBER, "<number>")
assert is_valid_grammar(INTEGER, "<integer>")
assert is_valid_grammar(FLOAT, "<float>")
assert is_valid_grammar(CLI_GRAMMAR)


def clean_up(grammar: Grammar, start_symbol: str = START_SYMBOL):
    defined_nonterminals, used_nonterminals = def_used_nonterminals(
        grammar, start_symbol
    )
    if defined_nonterminals is None or used_nonterminals is None:
        raise ValueError("Cannot find defined nonterminals or used nonterminals")
    if START_SYMBOL in grammar:
        used_nonterminals.add(START_SYMBOL)
    for unused_nonterminal in defined_nonterminals - used_nonterminals:
        del grammar[unused_nonterminal]

    unreachable = unreachable_nonterminals(grammar, start_symbol)
    if START_SYMBOL in grammar:
        unreachable -= reachable_nonterminals(grammar, START_SYMBOL)
    for unreachable_nonterminal in unreachable:
        del grammar[unreachable_nonterminal]

    return grammar
