import abc
import json
import os
from typing import Optional, List, Tuple, Dict

from tests4py.constants import (
    CHECKOUT,
    COMPILE,
    Environment,
    INFO,
    TEST,
    CACHE,
    CONFIG,
    GRAMMAR,
    SYSTEMTEST,
    GENERATE,
    UNITTEST,
    RUN,
)
from tests4py.projects import Project
from tests4py.tests.utils import TestResult


class Report(abc.ABC):
    def __init__(self, command: str, subcommand: str = None):
        self.command: str = command
        self.subcommand: Optional[str] = subcommand
        self.successful: Optional[bool] = None
        self.raised: Optional[BaseException] = None

    def to_dict(self):
        dictionary = {
            "command": self.command,
        }
        if self.subcommand:
            dictionary["subcommand"] = self.subcommand
        dictionary["successful"] = self.successful
        if not self.successful and self.raised:
            dictionary["raised"] = getattr(self.raised, "message", repr(self.raised))
        return dictionary

    def __repr__(self):
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        return self.__repr__()


class ProjectReport(Report, abc.ABC):
    def __init__(self, command: str, subcommand: str = None):
        self.project: Optional[Project] = None
        super().__init__(command, subcommand=subcommand)

    def to_dict(self):
        dictionary = super().to_dict()
        if self.project:
            dictionary["project"] = f"{self.project.project_name}_{self.project.bug_id}"
        return dictionary


class LocationReport(ProjectReport, abc.ABC):
    def __init__(self, command: str, subcommand: str = None):
        super().__init__(command=command, subcommand=subcommand)
        self.location: Optional[os.PathLike] = None

    def to_dict(self):
        dictionary = super().to_dict()
        if self.location:
            dictionary["location"] = repr(self.location)
        return dictionary


class CheckoutReport(LocationReport):
    def __init__(self):
        super().__init__(CHECKOUT)


class CompileReport(LocationReport):
    def __init__(self):
        super().__init__(COMPILE)
        self.env: Optional[Environment] = None

    def to_dict(self):
        dictionary = super().to_dict()
        if self.env:
            dictionary["env"] = "\n".join(
                f"{name}={value}" for name, value in self.env.items()
            )
        return dictionary


class InfoReport(ProjectReport):
    def __init__(self):
        super().__init__(INFO)
        self.example = False

    def to_dict(self):
        dictionary = super().to_dict()
        if self.example:
            dictionary["project"] = self.project.project_name
        return dictionary


class RunReport(LocationReport):
    def __init__(self):
        self.input: Optional[str] = None
        self.test_result: Optional[TestResult] = None
        self.feedback: Optional[str] = None
        super().__init__(RUN)

    def to_dict(self):
        dictionary = super().to_dict()
        if self.input:
            dictionary["input"] = self.input
        if self.test_result:
            dictionary["test_result"] = self.test_result
        if self.feedback:
            dictionary["feedback"] = self.feedback
        return dictionary


class TestingReport(LocationReport, abc.ABC):
    def __init__(self, command: str, subcommand: str = None):
        self.total: Optional[int] = None
        self.passing: Optional[int] = None
        self.failing: Optional[int] = None
        super().__init__(command, subcommand=subcommand)

    def to_dict(self):
        dictionary = super().to_dict()
        if self.total:
            dictionary["total"] = self.total
        if self.passing:
            dictionary["passing"] = self.passing
        if self.failing:
            dictionary["failing"] = self.failing
        return dictionary


class TestReport(TestingReport):
    def __init__(self):
        super().__init__(TEST)
        self.results: Optional[List[Tuple[str, TestResult]]] = None


class CacheReport(Report):
    def __init__(self):
        super().__init__(CACHE)
        self.checkout_reports = dict()
        self.compile_reports = dict()


class ConfigReport(Report):
    def __init__(self):
        super().__init__(CONFIG)


class GrammarReport(ProjectReport):
    def __init__(self):
        super().__init__(GRAMMAR)


class GenerateReport(TestingReport):
    def __init__(self, command: str, subcommand: str = None):
        self.verify_passing: Optional[int] = None
        self.verify_failing: Optional[int] = None
        super().__init__(command, subcommand=subcommand)


class SystemtestGenerateReport(GenerateReport):
    def __init__(self):
        super().__init__(
            SYSTEMTEST,
            subcommand=GENERATE,
        )


class SystemtestTestReport(TestingReport):
    def __init__(self):
        super().__init__(
            SYSTEMTEST,
            subcommand=TEST,
        )
        self.results: Optional[Dict[str, Tuple[TestResult, str]]] = None


class UnittestGenerateReport(GenerateReport):
    """ """

    def __init__(self):
        super().__init__(
            UNITTEST,
            subcommand=GENERATE,
        )


class UnittestTestReport(TestingReport):
    """ """

    def __init__(self):
        super().__init__(
            UNITTEST,
            subcommand=TEST,
        )
