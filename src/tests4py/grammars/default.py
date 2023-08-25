import string
from typing import List

from tests4py.grammars.fuzzer import srange, Grammar, crange, is_valid_grammar

PRINTABLE = srange(string.printable)
PRINTABLE_ESCAPED = srange(string.printable.replace('"', "")) + ['\\"']
PRINTABLE_CLI = srange(string.printable.replace('"', "").replace("-", ""))
PRINTABLE_WITHOUT_WS = srange(string.digits + string.ascii_letters + string.punctuation)
DIGITS = crange("0", "9")
NON_ZERO_DIGITS = crange("1", "9")


def get_string_rule(possible_chars: List[str], suffix: str = ""):
    string_rule = f"<string{suffix}>"
    chars_rule = f"<chars{suffix}>"
    char_rule = f"<char{suffix}>"
    return {
        string_rule: [chars_rule],
        chars_rule: ["", char_rule + chars_rule],
        char_rule: possible_chars,
    }


STRING: Grammar = get_string_rule(PRINTABLE_WITHOUT_WS)
STRING_WS: Grammar = get_string_rule(PRINTABLE, suffix="_ws")
STRING_WS_ESCAPED: Grammar = get_string_rule(PRINTABLE_ESCAPED, suffix="_ws_escaped")
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


CLI_GRAMMAR = dict(
    {
        "<start>": ["<options> <args>", "<options>", "<args>"],
        "<options>": ["", "<option_list>"],
        "<option_list>": ["<option>", "<option> <option_list>"],
        "<args>": ["", "<arg_list>"],
        "<arg_list>": ["<arg>", "<arg> <arg_list>"],
        "<arg>": [
            "<unescaped>",
            '"<string_ws_escaped>"',
        ],
        "<unescaped>": ["<unescaped_start><string>"],
        "<unescaped_start>": srange(PRINTABLE_CLI),
        "<option>": [
            "<flag>",
            "<op>",
        ],
        "<flag>": ["-<short_flag>", "--<long_flag>"],
        "<op>": [
            "-<short_op> <arg>",
            "-<short_op>=<arg>",
            "--<long_op> <arg>",
            "--<long_op>=<arg>",
        ],
        "<short_flag>": [
            "<unescaped>",
        ],
        "<long_flag>": [
            "<unescaped>",
        ],
        "<short_op>": [
            "<unescaped>",
        ],
        "<long_op>": [
            "<unescaped>",
        ],
    },
    **STRING,
    **STRING_WS_ESCAPED,
)

assert is_valid_grammar(STRING, "<string>")
assert is_valid_grammar(STRING_WS, "<string_ws>")
assert is_valid_grammar(STRING_WS_ESCAPED, "<string_ws_escaped>")
assert is_valid_grammar(NUMBER, "<number>")
assert is_valid_grammar(INTEGER, "<integer>")
assert is_valid_grammar(FLOAT, "<float>")
assert is_valid_grammar(CLI_GRAMMAR)
