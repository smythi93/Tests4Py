import sys


def _local_limit_length(s, length):
    ellipses = "..."
    if s is None:
        return None
    if len(s) > length:
        return s[: length - len(ellipses)] + ellipses
    return s


if __name__ == "__main__":
    mode = sys.argv[1]
    length = int(sys.argv[2])
    word = sys.argv[3]
    if mode == "ytdl":
        # noinspection PyUnresolvedReferences
        from youtube_dl.utils import limit_length

        result = limit_length(word, length)
    else:
        result = _local_limit_length(word, length)
    print(repr(result))
