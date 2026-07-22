import base64
import sys

try:
    # noinspection PyUnresolvedReferences
    from youtube_dl.utils import fix_xml_ampersands as fix
except ImportError:
    # noinspection PyUnresolvedReferences
    from youtube_dl.utils import fix_xml_all_ampersand as fix

if __name__ == "__main__":
    s = base64.urlsafe_b64decode(sys.argv[1]).decode("utf-8")
    print(repr(fix(s)))
