import os.path
import sys
import unittest
import shutil
from abc import ABC

from cookiecutter import hooks


class DefaultTests(unittest.TestCase, ABC):

    REPO_PATH = "tests4py_test_repo"

    @staticmethod
    def _default_config(
        full_name='"Marius Smytzek"',
        email='"mariussmtzek@cispa.de"',
        github_username='"smythi93"',
        project_name='"Test4Py Project"',
        repo_name='"t4p"',
        project_short_description='"The t4p project"',
        release_date='"2022-12-25"',
        year='"2022"',
        version='"0.1"',
    ):
        return (
            f'{{"full_name":{full_name},'
            f'"email":{email},'
            f'"github_username":{github_username},'
            f'"project_name":{project_name},'
            f'"repo_name":{repo_name},'
            f'"project_short_description":{project_short_description},'
            f'"release_date":{release_date},'
            f'"year":{year},'
            f'"version":{version}}}'
        )

    def project_setup(self, config):
        if os.path.exists(self.REPO_PATH):
            if os.path.isdir(self.REPO_PATH):
                shutil.rmtree(self.REPO_PATH, ignore_errors=True)
            else:
                os.remove(self.REPO_PATH)

        os.makedirs(self.REPO_PATH)

        with open(os.path.join(self.REPO_PATH, "cookiecutter.json"), "w") as fp:
            fp.write(config)

        repo_path = os.path.join(self.REPO_PATH, "{{cookiecutter.repo_name}}")
        os.makedirs(repo_path)

        with open(os.path.join(repo_path, "README.rst"), "w") as fp:
            fp.write(
                "============\nFake Project\n============\n\n"
                "Project name: **{{ cookiecutter.project_name }}**\n\n"
                "Blah!!!!\n"
            )

    def tearDown(self) -> None:
        if os.path.exists(self.REPO_PATH):
            if os.path.isdir(self.REPO_PATH):
                shutil.rmtree(self.REPO_PATH, ignore_errors=True)
            else:
                os.remove(self.REPO_PATH)


class TestsFailing(DefaultTests):
    def test_diversity_1(self):
        self.write_hooks(pre_gen_hooks=2)

        expected = {
            os.path.abspath(os.path.join("hooks", "pre_gen_project.0")),
            os.path.abspath(os.path.join("hooks", "pre_gen_project.1")),
        }
        actual_hook_path = hooks.find_hook("pre_gen_project")
        self.assertEqual(expected, set(actual_hook_path))

    def test_diversity_2(self):
        self.write_hooks(post_gen_hooks=2)

        expected = {
            os.path.abspath(os.path.join("hooks", "post_gen_project.0")),
            os.path.abspath(os.path.join("hooks", "post_gen_project.1")),
        }
        actual_hook_path = hooks.find_hook("post_gen_project")
        self.assertEqual(expected, set(actual_hook_path))

    def test_diversity_3(self):
        self.write_hooks(pre_gen_hooks=2, post_gen_hooks=2)

        expected = {
            os.path.abspath(os.path.join("hooks", "pre_gen_project.0")),
            os.path.abspath(os.path.join("hooks", "pre_gen_project.1")),
        }
        actual_hook_path = hooks.find_hook("pre_gen_project")
        self.assertEqual(expected, set(actual_hook_path))

        expected = {
            os.path.abspath(os.path.join("hooks", "post_gen_project.0")),
            os.path.abspath(os.path.join("hooks", "post_gen_project.1")),
        }
        actual_hook_path = hooks.find_hook("post_gen_project")
        self.assertEqual(expected, set(actual_hook_path))

    def test_diversity_4(self):
        self.write_hooks(pre_gen_hooks=1)

        expected = os.path.abspath(os.path.join("hooks", "pre_gen_project.0"))
        actual_hook_path = hooks.find_hook("pre_gen_project")
        self.assertEqual(expected, actual_hook_path[0])

    def test_diversity_5(self):
        self.write_hooks(pre_gen_hooks=1, post_gen_hooks=1)

        expected = os.path.abspath(os.path.join("hooks", "pre_gen_project.0"))
        actual_hook_path = hooks.find_hook("pre_gen_project")
        self.assertEqual(expected, actual_hook_path[0])

        expected = os.path.abspath(os.path.join("hooks", "post_gen_project.0"))
        actual_hook_path = hooks.find_hook("post_gen_project")
        self.assertEqual(expected, actual_hook_path[0])

    def test_diversity_6(self):
        self.write_hooks(pre_gen_hooks=2)

        hooks.run_hook("pre_gen_project", os.getcwd(), {})

        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "pre_0")))
        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "pre_1")))

    def test_diversity_7(self):
        self.write_hooks(post_gen_hooks=2)

        hooks.run_hook("post_gen_project", os.getcwd(), {})

        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "post_0")))
        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "post_1")))

    def test_diversity_8(self):
        self.write_hooks(pre_gen_hooks=2, post_gen_hooks=2)

        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "pre_0")))
        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "pre_1")))
        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "post_0")))
        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "post_1")))

    def test_diversity_9(self):
        self.write_hooks(pre_gen_hooks=2, post_gen_hooks=1)

        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "pre_0")))
        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "pre_1")))
        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "post_0")))

    def test_diversity_10(self):
        self.write_hooks(pre_gen_hooks=10)

        hooks.run_hook("pre_gen_project", os.getcwd(), {})

        for i in range(10):
            self.assertTrue(
                os.path.exists(os.path.join("test4py_tmp_tests", f"pre_{i}"))
            )


class TestsPassing(DefaultTests):
    def test_diversity_1(self):
        self.write_hooks(pre_gen_hooks=1)

        expected = os.path.abspath(os.path.join("hooks", "pre_gen_project.0"))
        actual_hook_path = hooks.find_hook("pre_gen_project")
        self.assertIn(expected, actual_hook_path)

    def test_diversity_2(self):
        self.write_hooks(post_gen_hooks=1)

        expected = os.path.abspath(os.path.join("hooks", "post_gen_project.0"))
        actual_hook_path = hooks.find_hook("post_gen_project")
        self.assertIn(expected, actual_hook_path)

    def test_diversity_3(self):
        self.write_hooks(pre_gen_hooks=1, post_gen_hooks=1)

        expected = os.path.abspath(os.path.join("hooks", "pre_gen_project.0"))
        actual_hook_path = hooks.find_hook("pre_gen_project")
        self.assertIn(expected, actual_hook_path)
        expected = os.path.abspath(os.path.join("hooks", "post_gen_project.0"))
        actual_hook_path = hooks.find_hook("post_gen_project")
        self.assertIn(expected, actual_hook_path)

    def test_diversity_4(self):
        self.write_hooks(pre_gen_hooks=2)

        expected = [
            os.path.abspath(os.path.join("hooks", "pre_gen_project.0")),
            os.path.abspath(os.path.join("hooks", "pre_gen_project.1")),
        ]
        actual_hook_path = hooks.find_hook("pre_gen_project")
        self.assertTrue(any(e in actual_hook_path for e in expected))

    def test_diversity_5(self):
        self.write_hooks(pre_gen_hooks=2, post_gen_hooks=2)

        expected = [
            os.path.abspath(os.path.join("hooks", "pre_gen_project.0")),
            os.path.abspath(os.path.join("hooks", "pre_gen_project.1")),
        ]
        actual_hook_path = hooks.find_hook("pre_gen_project")
        self.assertTrue(any(e in actual_hook_path for e in expected))

        expected = [
            os.path.abspath(os.path.join("hooks", "post_gen_project.0")),
            os.path.abspath(os.path.join("hooks", "post_gen_project.1")),
        ]
        actual_hook_path = hooks.find_hook("post_gen_project")
        self.assertTrue(any(e in actual_hook_path for e in expected))

    def test_diversity_6(self):
        self.write_hooks(pre_gen_hooks=1)

        hooks.run_hook("pre_gen_project", os.getcwd(), {})

        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "pre_0")))

    def test_diversity_7(self):
        self.write_hooks(post_gen_hooks=1)

        hooks.run_hook("post_gen_project", os.getcwd(), {})

        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "post_0")))

    def test_diversity_8(self):
        self.write_hooks(pre_gen_hooks=1, post_gen_hooks=1)

        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "pre_0")))
        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "post_0")))

    def test_diversity_9(self):
        self.write_hooks(pre_gen_hooks=2, post_gen_hooks=1)

        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

        self.assertTrue(
            os.path.exists(os.path.join("test4py_tmp_tests", "pre_0"))
            or os.path.exists(os.path.join("test4py_tmp_tests", "pre_1"))
        )
        self.assertTrue(os.path.exists(os.path.join("test4py_tmp_tests", "post_0")))

    def test_diversity_10(self):
        self.write_hooks(pre_gen_hooks=10)

        hooks.run_hook("pre_gen_project", os.getcwd(), {})

        self.assertTrue(
            any(
                os.path.exists(os.path.join("test4py_tmp_tests", f"pre_{i}"))
                for i in range(10)
            )
        )
