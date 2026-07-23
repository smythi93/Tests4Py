import sys
import types
import warnings

# noinspection PyUnresolvedReferences
from scrapy.crawler import CrawlerRunner

# noinspection PyUnresolvedReferences
from scrapy.spiderloader import SpiderLoader

if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    modname = "customloader_%s" % word
    mod = types.ModuleType(modname)

    class CustomSpiderLoader(SpiderLoader):
        pass

    mod.CustomSpiderLoader = CustomSpiderLoader
    sys.modules[modname] = mod
    path = "%s.CustomSpiderLoader" % modname
    setting = "SPIDER_MANAGER_CLASS" if mode == "manager" else "SPIDER_LOADER_CLASS"
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            runner = CrawlerRunner({setting: path})
            loader = runner.spider_loader
        print("OK:%d" % (1 if isinstance(loader, CustomSpiderLoader) else 0))
    except Exception as exception:  # noqa: BLE001
        print("ERR:" + type(exception).__name__)
