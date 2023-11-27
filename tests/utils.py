import unittest

from tests4py.api.config import config_set


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        config_set("cache", True)

    @staticmethod
    def get_identifier(project_name: str, bug_id: int):
        return f"{project_name}_{bug_id}"
