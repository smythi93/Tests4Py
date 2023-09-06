import unittest

from tests4py.framework.config import tests4py_config_set


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        tests4py_config_set("cache", True)

    @staticmethod
    def get_identifier(project_name: str, bug_id: int):
        return f"{project_name}_{bug_id}"
