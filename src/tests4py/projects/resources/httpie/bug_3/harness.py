import sys

from httpie.sessions import Session


if __name__ == "__main__":
    # Each argv token is "name=value"; the sentinel value "__NONE__" means the
    # header is explicitly unset (None). Byte-valued headers are the normal case.
    s = Session("/tmp/t4p_httpie_bug3_session.json")
    s["headers"] = {}
    headers = {}
    for token in sys.argv[1:]:
        name, _, value = token.partition("=")
        headers[name] = None if value == "__NONE__" else value.encode("utf8")
    s.update_headers(headers)
    print("OK")
