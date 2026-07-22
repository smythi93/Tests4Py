"""Comprehensive per-subject acceptance tests.

For every *fully enabled* subject bug this module validates, on the buggy
version, every aspect that makes a subject complete in Tests4Py:

  * grammar       -- the input grammar is a valid grammar
  * diversity     -- the 10 passing / 10 failing *manual* system tests and the
                     10 passing / 10 failing *manual* unit tests behave as
                     labelled against the oracle (20 unit + 20 system per bug)
  * generation    -- the system- and unit-test generators produce and verify
                     passing and failing tests on demand
  * oracle/harness -- exercised implicitly by running the diversity system
                     tests through the harness and oracle

These tests check out and build real projects and are therefore slow. They are
excluded from the normal GitHub workflow via the ``subjects`` marker
(the CI command runs ``pytest -m "not subjects"``); run them locally with::

    pytest -m subjects tests/test_subjects.py

A subject bug is considered *fully enabled* (and thus collected here) when the
project registers unit- and system-test generators, an oracle, a valid grammar,
ships the manual diversity suites, and provides a harness (or uses a CLI API,
which needs none). New subjects join automatically as they are completed.
"""
import os
from pathlib import Path

import pytest

import tests4py.api as t4p
from tests4py import projects
from tests4py.api.utils import setup
from tests4py.constants import DEFAULT_WORK_DIR
from tests4py.grammars.fuzzer import is_valid_grammar
from tests4py.projects import Project
from tests4py.tests.utils import API, TestResult

pytestmark = pytest.mark.subjects

RESOURCES = Path(projects.__file__).parent / "resources"


def _has_resource(name: str, bug_id: int, filename: str) -> bool:
    return (RESOURCES / name / f"bug_{bug_id}" / filename).exists()


def _is_fully_enabled(project: Project) -> bool:
    if project.unittests is None or project.systemtests is None or project.api is None:
        return False
    if not project.grammar or not is_valid_grammar(project.grammar):
        return False
    name, bug_id = project.project_name, project.bug_id
    if not _has_resource(name, bug_id, "systemtests.py"):
        return False
    if not _has_resource(name, bug_id, "unittests.py"):
        return False
    # A harness is required only when the oracle runs the program through the
    # generic ``API.execute`` (which invokes ``tests4py_harness.py``). APIs that
    # override ``execute`` (CLI drivers, cookiecutter, ...) need none.
    needs_harness = type(project.api).execute is API.execute
    if needs_harness and not _has_resource(name, bug_id, "harness.py"):
        # Fall back to a project-level default harness, if any.
        if not (RESOURCES / name / "harness.py").exists():
            return False
    return True


def _discover():
    setup()
    enabled = []
    for name, bugs in sorted(projects.bugs.items()):
        if name == "pandas":  # excluded: builds take far too long
            continue
        for bug_id, project in sorted(bugs.items()):
            if _is_fully_enabled(project):
                enabled.append(project)
    return enabled


FULLY_ENABLED = _discover()
IDS = [p.get_identifier() for p in FULLY_ENABLED]

# Cache of built work dirs so the five aspect-tests of one subject build once.
_BUILT: dict = {}


def _build(project: Project) -> Path:
    identifier = project.get_identifier()
    if identifier in _BUILT:
        return _BUILT[identifier]
    work_dir = DEFAULT_WORK_DIR / identifier
    report = t4p.checkout(project, DEFAULT_WORK_DIR)
    if report.raised:
        raise report.raised
    report = t4p.build(work_dir)
    if report.raised:
        raise report.raised
    _BUILT[identifier] = work_dir
    return work_dir


@pytest.mark.parametrize("project", FULLY_ENABLED, ids=IDS)
def test_grammar_valid(project: Project):
    assert project.grammar, f"{project.get_identifier()} has no grammar"
    assert is_valid_grammar(project.grammar)


@pytest.mark.parametrize("project", FULLY_ENABLED, ids=IDS)
def test_diversity_systemtests(project: Project):
    work_dir = _build(project)
    report = t4p.systemtest_test(work_dir, diversity=True)
    if report.raised:
        raise report.raised
    correct_pass = correct_fail = wrong = 0
    for path, (result, _feedback) in report.results.items():
        base = os.path.basename(str(path))
        if base.startswith("passing"):
            correct_pass += result == TestResult.PASSING
            wrong += result != TestResult.PASSING
        elif base.startswith("failing"):
            correct_fail += result == TestResult.FAILING
            wrong += result != TestResult.FAILING
    assert wrong == 0, f"{wrong} diversity system tests behaved unexpectedly"
    assert correct_pass == 10, f"expected 10 passing diversity system tests, got {correct_pass}"
    assert correct_fail == 10, f"expected 10 failing diversity system tests, got {correct_fail}"


@pytest.mark.parametrize("project", FULLY_ENABLED, ids=IDS)
def test_diversity_unittests(project: Project):
    work_dir = _build(project)
    report = t4p.unittest_test(work_dir, diversity=True)
    if report.raised:
        raise report.raised
    # Buggy version: the 10 TestsPassing pass, the 10 TestsFailing fail.
    assert report.passing == 10, f"expected 10 passing diversity unit tests, got {report.passing}"
    assert report.failing == 10, f"expected 10 failing diversity unit tests, got {report.failing}"


@pytest.mark.parametrize("project", FULLY_ENABLED, ids=IDS)
def test_systemtest_generation(project: Project):
    work_dir = _build(project)
    report = t4p.systemtest_generate(work_dir, n=4, p=0.5, verify=True)
    if report.raised:
        raise report.raised
    assert report.total == 4
    assert report.passing == 2
    assert report.failing == 2
    assert report.verify_passing == 2
    assert report.verify_failing == 2


@pytest.mark.parametrize("project", FULLY_ENABLED, ids=IDS)
def test_unittest_generation(project: Project):
    work_dir = _build(project)
    report = t4p.unittest_generate(work_dir, n=4, p=0.5, verify=True)
    if report.raised:
        raise report.raised
    assert report.total == 4
    assert report.passing == 2
    assert report.failing == 2
    assert report.verify_passing == 2
    assert report.verify_failing == 2
