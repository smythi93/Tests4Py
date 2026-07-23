import sys

# noinspection PyUnresolvedReferences
from scrapy.crawler import CrawlerProcess

# noinspection PyUnresolvedReferences
from scrapy.settings import Settings, default_settings

if __name__ == "__main__":
    mode = sys.argv[1]
    key = sys.argv[2]
    val = sys.argv[3]
    arg = {key: val} if mode == "dict" else Settings({key: val})
    try:
        rp = CrawlerProcess(arg)
        ok = (
            rp.settings[key] == val
            and rp.settings["RETRY_ENABLED"] == default_settings.RETRY_ENABLED
        )
        result = "OK" if ok else "BAD"
    except Exception as exception:  # noqa: BLE001
        result = "ERR:" + type(exception).__name__
    print(result)
