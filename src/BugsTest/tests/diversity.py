import os
import unittest
from abc import abstractmethod, ABC
from pathlib import Path


class DiversityTest:

    @abstractmethod
    def test_diversity_1(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @abstractmethod
    def test_diversity_2(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @abstractmethod
    def test_diversity_3(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @abstractmethod
    def test_diversity_4(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @abstractmethod
    def test_diversity_5(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @abstractmethod
    def test_diversity_6(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @abstractmethod
    def test_diversity_7(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @abstractmethod
    def test_diversity_8(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @abstractmethod
    def test_diversity_9(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @abstractmethod
    def test_diversity_10(self):
        raise NotImplementedError('Diversity test 1 is missing')


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

    def write(self, path: Path):
        if not path.exists():
            os.makedirs(path, exist_ok=True)
        if not path.is_dir():
            raise ValueError(f'Cannot write systemtests {path} is a dir')
        for i, test in enumerate(self.tests):
            with (path / f'{"passing" if self.passing else "failing"}_test_diversity_{i}').open('w') as fp:
                fp.write(self.parse(test))


class Unittests(unittest.TestCase, DiversityTest):

    @unittest.skip
    def test_diversity_1(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @unittest.skip
    def test_diversity_2(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @unittest.skip
    def test_diversity_3(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @unittest.skip
    def test_diversity_4(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @unittest.skip
    def test_diversity_5(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @unittest.skip
    def test_diversity_6(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @unittest.skip
    def test_diversity_7(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @unittest.skip
    def test_diversity_8(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @unittest.skip
    def test_diversity_9(self):
        raise NotImplementedError('Diversity test 1 is missing')

    @unittest.skip
    def test_diversity_10(self):
        raise NotImplementedError('Diversity test 1 is missing')
