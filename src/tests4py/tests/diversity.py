import os
import unittest
from abc import abstractmethod, ABC
from pathlib import Path

from fuzzingbook.Grammars import Grammar
from fuzzingbook.Parser import EarleyParser


class DiversityTest:
    @abstractmethod
    def test_diversity_1(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @abstractmethod
    def test_diversity_2(self):
        raise NotImplementedError("Diversity test 2 is missing")

    @abstractmethod
    def test_diversity_3(self):
        raise NotImplementedError("Diversity test 3 is missing")

    @abstractmethod
    def test_diversity_4(self):
        raise NotImplementedError("Diversity test 4 is missing")

    @abstractmethod
    def test_diversity_5(self):
        raise NotImplementedError("Diversity test 5 is missing")

    @abstractmethod
    def test_diversity_6(self):
        raise NotImplementedError("Diversity test 6 is missing")

    @abstractmethod
    def test_diversity_7(self):
        raise NotImplementedError("Diversity test 7 is missing")

    @abstractmethod
    def test_diversity_8(self):
        raise NotImplementedError("Diversity test 8 is missing")

    @abstractmethod
    def test_diversity_9(self):
        raise NotImplementedError("Diversity test 9 is missing")

    @abstractmethod
    def test_diversity_10(self):
        raise NotImplementedError("Diversity test 10 is missing")


class Systemtests(DiversityTest, ABC):
    def __init__(self, passing: bool = True):
        self.passing = passing
        self.tests = [
            self.test_diversity_1(),
            self.test_diversity_2(),
            self.test_diversity_3(),
            self.test_diversity_4(),
            self.test_diversity_5(),
            self.test_diversity_6(),
            self.test_diversity_7(),
            self.test_diversity_8(),
            self.test_diversity_9(),
            self.test_diversity_10(),
        ]

    def parse(self, test: str) -> str:
        return test

    # noinspection PyMethodMayBeStatic
    def verify(self, test: str, grammar: Grammar = None) -> str:
        if grammar is not None:
            for _ in EarleyParser(grammar).parse(test):
                pass
        return test

    def write(self, path: Path, grammar: Grammar = None):
        if not path.exists():
            os.makedirs(path, exist_ok=True)
        if not path.is_dir():
            raise ValueError(f"Cannot write systemtests {path} is a dir")
        for i, test in enumerate(self.tests):
            with (
                path / f'{"passing" if self.passing else "failing"}_test_diversity_{i}'
            ).open("w") as fp:
                fp.write(self.verify(self.parse(test), grammar=grammar))


class Unittests(unittest.TestCase, DiversityTest):
    @unittest.skip
    def test_diversity_1(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @unittest.skip
    def test_diversity_2(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @unittest.skip
    def test_diversity_3(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @unittest.skip
    def test_diversity_4(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @unittest.skip
    def test_diversity_5(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @unittest.skip
    def test_diversity_6(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @unittest.skip
    def test_diversity_7(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @unittest.skip
    def test_diversity_8(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @unittest.skip
    def test_diversity_9(self):
        raise NotImplementedError("Diversity test 1 is missing")

    @unittest.skip
    def test_diversity_10(self):
        raise NotImplementedError("Diversity test 1 is missing")


class FailingSystemtests(Systemtests, ABC):
    def __init__(self):
        super().__init__(passing=False)


class PassingSystemtests(Systemtests, ABC):
    def __init__(self):
        super().__init__(passing=True)
