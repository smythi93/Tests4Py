import enum
from os import PathLike


class TestResult(enum.Enum):
    FAILING = 0
    PASSING = 1
    UNKNOWN = 2


class API:

    def __init__(self, default_timeout=5):
        self.default_timeout = default_timeout

    def run(self, system_test_path: PathLike) -> TestResult:
        return NotImplemented
