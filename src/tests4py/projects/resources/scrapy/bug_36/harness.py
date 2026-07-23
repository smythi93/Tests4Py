import sys

# noinspection PyUnresolvedReferences
from scrapy.utils.misc import create_instance


def build(method, returns_none):
    if method == "from_crawler":
        class Obj(object):
            @classmethod
            def from_crawler(cls, crawler, *args, **kwargs):
                return None if returns_none else cls()

        return Obj

    class Obj(object):
        @classmethod
        def from_settings(cls, settings, *args, **kwargs):
            return None if returns_none else cls()

    return Obj


if __name__ == "__main__":
    mode = sys.argv[1]
    method = sys.argv[2]
    returns_none = mode == "none"
    settings = object()
    objcls = build(method, returns_none)
    if method == "from_crawler":
        crawler = type("C", (object,), {"settings": settings})()
        call_args = (objcls, settings, crawler)
    else:
        call_args = (objcls, settings, None)
    try:
        result = create_instance(*call_args)
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + ("None" if result is None else "instance"))
