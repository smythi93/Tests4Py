import os
from pathlib import Path
from typing import List

from BugsTest.projects import Project, Status, TestingFramework


class Ansible(Project):

    def __init__(self, bug_id: int, python_version: str, python_path: str,
                 buggy_commit_id: str, fixed_commit_id: str, test_file: List[Path], test_cases: List[str]):
        super().__init__(bug_id=bug_id, project_name='ansible', github_url='https://github.com/ansible/ansible',
                         status=Status.OK, cause='N.A.',
                         python_version=python_version, python_path=python_path, buggy_commit_id=buggy_commit_id,
                         fixed_commit_id=fixed_commit_id, testing_framework=TestingFramework.PYTEST,
                         test_file=test_file, test_cases=test_cases)


# REGISTER BUGS

def register():
    Ansible(
        bug_id=1,
        python_version='3.6.9',
        python_path='ansible/build/lib/',
        buggy_commit_id='25c5388fdec9e56517a93feb5e8d485680946c25',
        fixed_commit_id='343ffaa18b63c92e182b16c3ad84b8d81ca4df69',
        test_file=[Path('test', 'units', 'galaxy', 'test_collection.py')],
        test_cases=['test/units/galaxy/test_collection.py::test_verify_collections_no_version']
    )
