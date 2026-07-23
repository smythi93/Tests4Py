import unittest

# noinspection PyUnresolvedReferences
import sys
import types
import warnings
from scrapy.crawler import CrawlerRunner
from scrapy.spiderloader import SpiderLoader


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        modname = 'customloader_adqeb'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_2(self):
        modname = 'customloader_ejfugme'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_3(self):
        modname = 'customloader_lcgwsys'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_4(self):
        modname = 'customloader_axtlbxkw'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_5(self):
        modname = 'customloader_awyhq'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_6(self):
        modname = 'customloader_bsyr'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_7(self):
        modname = 'customloader_evhtdp'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_8(self):
        modname = 'customloader_bwrhhec'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_9(self):
        modname = 'customloader_lfgm'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_10(self):
        modname = 'customloader_laxhogvwi'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_MANAGER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        modname = 'customloader_eiljzblf'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_2(self):
        modname = 'customloader_jnnelbr'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_3(self):
        modname = 'customloader_tfmpo'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_4(self):
        modname = 'customloader_wpcghphpz'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_5(self):
        modname = 'customloader_vrfiqbhs'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_6(self):
        modname = 'customloader_mycfa'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_7(self):
        modname = 'customloader_mqaqnicbd'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_8(self):
        modname = 'customloader_tmcykocgf'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_9(self):
        modname = 'customloader_jphdydpt'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)

    def test_diversity_10(self):
        modname = 'customloader_shpacmjmd'
        mod = types.ModuleType(modname)
        
        class CustomSpiderLoader(SpiderLoader):
            pass
        mod.CustomSpiderLoader = CustomSpiderLoader
        sys.modules[modname] = mod
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            runner = CrawlerRunner({'SPIDER_LOADER_CLASS': modname + '.CustomSpiderLoader'})
            loader = runner.spider_loader
        self.assertIsInstance(loader, CustomSpiderLoader)
