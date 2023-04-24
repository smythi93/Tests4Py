import unittest

from tests4py.framework.config import tests4py_config_set


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        tests4py_config_set("cache", True)
