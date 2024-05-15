"""
This module contains the classes that represent the reports of the Tests4Py API.
"""

import abc
import json
import os
from typing import Optional, List, Tuple, Dict

from tests4py.constants import (
    CHECKOUT,
    BUILD,
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
    CLEAR,
    GET_TESTS,
)
from tests4py.projects import Project
from tests4py.tests.utils import TestResult


class Report(abc.ABC):
    """
    Abstract class for reports.
    """

    def __init__(self, command: str, subcommand: Optional[str] = None):
        """
        Initialize the report.
        :param str command: The command that was executed.
        :param Optional[str] subcommand: The subcommand that was executed.
        """
        self.command: str = command
        self.subcommand: Optional[str] = subcommand
        self.successful: Optional[bool] = None
        self.raised: Optional[BaseException] = None

    def to_dict(self) -> dict:
        """
        Convert the report to a dictionary.
        :return dict: The dictionary representation of the report.
        """
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
        """
        Get the string representation of the report.
        """
        return json.dumps(self.to_dict(), indent=4)

    def __str__(self):
        """
        Get the string representation of the report.
        """
        return self.__repr__()


class ProjectReport(Report, abc.ABC):
    """
    Abstract class for reports that are associated with a project.
    """

    def __init__(self, command: str, subcommand: Optional[str] = None):
        """
        Initialize the report.
        :param str command: The command that was executed.
        :param Optional[str] subcommand: The subcommand that was executed.
        """
        self.project: Optional[Project] = None
        super().__init__(command, subcommand=subcommand)

    def to_dict(self):
        """
        Convert the report to a dictionary.
        :return dict: The dictionary representation of the report.
        """
        dictionary = super().to_dict()
        if self.project:
            dictionary["project"] = f"{self.project.project_name}_{self.project.bug_id}"
        return dictionary


class LocationReport(ProjectReport, abc.ABC):
    """
    Abstract class for reports that are associated with a location.
    """

    def __init__(self, command: str, subcommand: Optional[str] = None):
        """
        Initialize the report.
        :param str command: The command that was executed.
        :param Optional[str] subcommand: The subcommand that was executed.
        """
        super().__init__(command=command, subcommand=subcommand)
        self.location: Optional[os.PathLike] = None

    def to_dict(self) -> dict:
        """
        Convert the report to a dictionary.
        :return dict: The dictionary representation of the report.
        """
        dictionary = super().to_dict()
        if self.location:
            dictionary["location"] = repr(self.location)
        return dictionary


class CheckoutReport(LocationReport):
    """
    Report for the checkout of a project.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(CHECKOUT)


class CompileReport(LocationReport):
    """
    Report for the compilation of a project.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(BUILD)
        self.env: Optional[Environment] = None

    def to_dict(self) -> dict:
        """
        Convert the report to a dictionary.
        :return dict: The dictionary representation of the report.
        """
        dictionary = super().to_dict()
        if self.env:
            dictionary["env"] = "\n".join(
                f"{name}={value}" for name, value in self.env.items()
            )
        return dictionary


class InfoReport(ProjectReport):
    """
    Report for the information of a project.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(INFO)
        self.example = False

    def to_dict(self) -> dict:
        """
        Convert the report to a dictionary.
        :return dict: The dictionary representation of the report.
        """
        dictionary = super().to_dict()
        if self.example:
            dictionary["project"] = self.project.project_name
        return dictionary


class RunReport(LocationReport):
    """
    Report for running system tests for a project.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        self.input: Optional[str] = None
        self.test_result: Optional[TestResult] = None
        self.feedback: Optional[str] = None
        self.stdout: Optional[str] = None
        self.stderr: Optional[str] = None
        super().__init__(RUN)

    def to_dict(self) -> dict:
        """
        Convert the report to a dictionary.
        :return dict: The dictionary representation of the report.
        """
        dictionary = super().to_dict()
        if self.input:
            dictionary["input"] = self.input
        if self.test_result:
            dictionary["test_result"] = self.test_result.name
        if self.feedback:
            dictionary["feedback"] = self.feedback
        if self.feedback:
            dictionary["stdout"] = self.stdout
        if self.feedback:
            dictionary["stderr"] = self.stderr
        return dictionary


class TestingReport(LocationReport, abc.ABC):
    """
    Abstract class for reports that are associated with testing.
    """

    def __init__(self, command: str, subcommand: Optional[str] = None):
        """
        Initialize the report.
        :param str command: The command that was executed.
        :param Optional[str] subcommand: The subcommand that was executed.
        """
        self.total: Optional[int] = None
        self.passing: Optional[int] = None
        self.failing: Optional[int] = None
        super().__init__(command, subcommand=subcommand)

    def to_dict(self) -> dict:
        """
        Convert the report to a dictionary.
        :return dict: The dictionary representation of the report.
        """
        dictionary = super().to_dict()
        if self.total:
            dictionary["total"] = self.total
        if self.passing:
            dictionary["passing"] = self.passing
        if self.failing:
            dictionary["failing"] = self.failing
        return dictionary


class TestReport(TestingReport):
    """
    Report for the test command.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(TEST)
        self.results: Optional[List[Tuple[str, TestResult]]] = None


class CacheReport(Report):
    """
    Report for the cache command.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(CACHE)
        self.checkout_reports = dict()
        self.compile_reports = dict()


class ClearReport(ProjectReport):
    """
    Report for the clear command.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(CLEAR)


class ConfigReport(Report):
    """
    Report for the config command.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(CONFIG)


class GrammarReport(ProjectReport):
    """
    Report for the grammar command.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(GRAMMAR)


class GetTestReport(ProjectReport):
    """
    Report for the get-tests command.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(GET_TESTS)
        self.passing_tests: Optional[List[List[str]] | List[str]] = None
        self.failing_tests: Optional[List[List[str]] | List[str]] = None


class GenerateReport(TestingReport):
    """
    Abstract class for reports that are associated with test generation.
    """

    def __init__(self, command: str, subcommand: Optional[str] = None):
        """
        Initialize the report.
        :param str command: The command that was executed.
        :param Optional[str] subcommand: The subcommand that was executed.
        """
        self.verify_passing: Optional[int] = None
        self.verify_failing: Optional[int] = None
        super().__init__(command, subcommand=subcommand)


class SystemtestGenerateReport(GenerateReport):
    """
    Report for the generate command for system tests.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(
            SYSTEMTEST,
            subcommand=GENERATE,
        )
        self.passing_tests: Optional[List[List[str]]] = None
        self.failing_tests: Optional[List[List[str]]] = None


class SystemtestTestReport(TestingReport):
    """
    Report for the test command for system tests.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(
            SYSTEMTEST,
            subcommand=TEST,
        )
        self.results: Optional[Dict[str, Tuple[TestResult, str]]] = None


class UnittestGenerateReport(GenerateReport):
    """
    Report for the generate command for unit tests.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(
            UNITTEST,
            subcommand=GENERATE,
        )


class UnittestTestReport(TestingReport):
    """
    Report for the test command for unit tests.
    """

    def __init__(self):
        """
        Initialize the report.
        """
        super().__init__(
            UNITTEST,
            subcommand=TEST,
        )
