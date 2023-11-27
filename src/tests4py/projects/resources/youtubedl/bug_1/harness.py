import argparse
import ast
import operator
import re


# noinspection PyUnresolvedReferences
from youtube_dl.utils import match_str, parse_filesize
# noinspection PyUnresolvedReferences
from youtube_dl.compat import compat_str


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


def dict_type(s):
    try:
        # Safely evaluate the string as a Python literal
        return ast.literal_eval(s)
    except ValueError:
        raise argparse.ArgumentTypeError("Not a valid Python dictionary")


if __name__ == "__main__":
    arguments = argparse.ArgumentParser()
    arguments.add_argument("-q", dest="query", default=None)
    arguments.add_argument("-d", dest="dict", type=dict_type, default=None)

    args = arguments.parse_args()

    query = args.query
    dictionary = eval(args.dict)

    result_buggy = match_str(query, dictionary)
    result_fixed = match_str_fixed(query, dictionary)

    if result_buggy != result_fixed:
        raise AssertionError("Input does not match the expected outcome!")