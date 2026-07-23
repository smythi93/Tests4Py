import sys

# noinspection PyUnresolvedReferences
from scrapy.item import Field, Item

if __name__ == "__main__":
    mode = sys.argv[1]
    field = sys.argv[2]
    default = sys.argv[3]
    value = sys.argv[4]
    if mode == "explicit":
        class T(Item):
            fields = {field: Field(default=default)}
    else:
        T = type("T", (Item,), {field: Field(default=default)})
    try:
        item = T(**{field: value})
        result = item[field]
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK:" + str(result))
