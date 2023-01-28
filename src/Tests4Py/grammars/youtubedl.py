import sys

from fuzzingbook.Grammars import Grammar, is_valid_grammar
from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from tmp.youtubedl_1.youtube_dl.utils import match_str, parse_filesize
from tmp.youtubedl_1.youtube_dl.compat import compat_str
import string
import operator
import re

GRAMMAR: Grammar = {
    "<start>": ["(<par><stmt_list><par>, {<dict_list>})"],
    "<stmt_list>": ["<stmt> & <stmt_list>", "<stmt>"],
    "<stmt>": ["<bool_stmt>", "<comp_stmt>"],
    "<bool_stmt>": ["<unary_op><name>"],
    "<unary_op>": ["!", ""],
    "<comp_stmt>": ["<name> <comp_op><optional> <int>"],
    "<optional>": ["?"],
    "<comp_op>": ["<", ">", "<=", ">=", "=", "!="],
    "<dict_list>": ["<kv>, <dict_list>", "<kv>"],
    "<kv>": ["<par><key><par>: <value>"],
    "<par>": ["'"],
    "<key>": ["is_live", "like_count", "description", "title", "dislike_count"],
    "<value>": ['<bool>', "<int>"],
    "<bool>": ["True", "False"],
    "<name>": ["is_live", "like_count", "description", "title", "dislike_count"],
    "<int>": [str(i) for i in range(10)],
}

DICT_GRAMMAR: Grammar = {
    "<start>": ["{<dict_list>}"],
    "<dict_list>": ["<kv>, <dict_list>", "<kv>"],
    "<kv>": ["<a><key><a>: <value>"],
    "<a>": ["'"],
    "<key>": ["is_live", "like_count", "description", "title", "dislike_count"],
    "<value>": ['<bool>', "<int>"],
    "<bool>": ["True", "False"],
    "<int>": [str(i) for i in range(10)],
}


def _match_one(filter_part, dct):
    COMPARISON_OPERATORS = {
        '<': operator.lt,
        '<=': operator.le,
        '>': operator.gt,
        '>=': operator.ge,
        '=': operator.eq,
        '!=': operator.ne,
    }
    operator_rex = re.compile(r'''(?x)\s*
        (?P<key>[a-z_]+)
        \s*(?P<op>%s)(?P<none_inclusive>\s*\?)?\s*
        (?:
            (?P<intval>[0-9.]+(?:[kKmMgGtTpPeEzZyY]i?[Bb]?)?)|
            (?P<quote>["\'])(?P<quotedstrval>(?:\\.|(?!(?P=quote)|\\).)+?)(?P=quote)|
            (?P<strval>(?![0-9.])[a-z0-9A-Z]*)
        )
        \s*$
        ''' % '|'.join(map(re.escape, COMPARISON_OPERATORS.keys())))
    m = operator_rex.search(filter_part)
    if m:
        op = COMPARISON_OPERATORS[m.group('op')]
        actual_value = dct.get(m.group('key'))
        if (m.group('quotedstrval') is not None
            or m.group('strval') is not None
            # If the original field is a string and matching comparisonvalue is
            # a number we should respect the origin of the original field
            # and process comparison value as a string (see
            # https://github.com/ytdl-org/youtube-dl/issues/11082).
            or actual_value is not None and m.group('intval') is not None
                and isinstance(actual_value, compat_str)):
            if m.group('op') not in ('=', '!='):
                raise ValueError(
                    'Operator %s does not support string values!' % m.group('op'))
            comparison_value = m.group('quotedstrval') or m.group('strval') or m.group('intval')
            quote = m.group('quote')
            if quote is not None:
                comparison_value = comparison_value.replace(r'\%s' % quote, quote)
        else:
            try:
                comparison_value = int(m.group('intval'))
            except ValueError:
                comparison_value = parse_filesize(m.group('intval'))
                if comparison_value is None:
                    comparison_value = parse_filesize(m.group('intval') + 'B')
                if comparison_value is None:
                    raise ValueError(
                        'Invalid integer value %r in filter part %r' % (
                            m.group('intval'), filter_part))
        if actual_value is None:
            return m.group('none_inclusive')
        return op(actual_value, comparison_value)

    UNARY_OPERATORS = {
        '': lambda v: (v is True) if isinstance(v, bool) else (v is not None),
        '!': lambda v: (v is False) if isinstance(v, bool) else (v is None),
    }
    operator_rex = re.compile(r'''(?x)\s*
        (?P<op>%s)\s*(?P<key>[a-z_]+)
        \s*$
        ''' % '|'.join(map(re.escape, UNARY_OPERATORS.keys())))
    m = operator_rex.search(filter_part)
    if m:
        op = UNARY_OPERATORS[m.group('op')]
        actual_value = dct.get(m.group('key'))
        return op(actual_value)

    raise ValueError('Invalid filter part %r' % filter_part)


def match_str_fixed(filter_str, dct):
    """ Filter a dictionary with a simple string syntax. Returns True (=passes filter) or false """

    return all(
        _match_one(filter_part, dct) for filter_part in filter_str.split('&'))


def prop(inp: str) -> bool:
    filter_string, dictionary = eval(inp)
    result_buggy = match_str(filter_string, dictionary)
    result_fixed = match_str_fixed(filter_string, dictionary)
    if result_buggy != result_fixed:
        # True == BUG
        return True
    # False == NO_BUG
    return False


if __name__ == "__main__":
    assert is_valid_grammar(GRAMMAR)
    fuzzer = GrammarFuzzer(GRAMMAR)
    filter_string, dictionary = eval(fuzzer.fuzz())
    print(filter_string)
    print(dictionary)

    fuzzer = GrammarFuzzer(GRAMMAR)
    for i in range(1000):
        filter_string, dictionary = eval(fuzzer.fuzz())
        re_old = match_str(filter_string, dictionary)
        re_fixed = match_str_fixed(filter_string, dictionary)
        if re_old != re_fixed:
            print(f"{re_old} != {re_fixed} for {filter_string} and dict: {dictionary}")
