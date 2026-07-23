import sys

if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    if mode == "classcell":
        src = (
            "from scrapy.item import Item\n"
            "class Item_%s(Item):\n"
            "    def method(self):\n"
            "        return super().__init__\n"
            "Item_%s()\n" % (word, word)
        )
    else:
        src = (
            "from scrapy.item import Item, Field\n"
            "class Item_%s(Item):\n"
            "    name = Field()\n"
            "Item_%s(name='x')\n" % (word, word)
        )
    try:
        exec(src, {})
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
    else:
        print("OK")
