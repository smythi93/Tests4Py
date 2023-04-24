import os.path
import sys
import unittest
import shutil
from abc import ABC

from cookiecutter import hooks


class DefaultTests(unittest.TestCase, ABC):
    # noinspection SqlDialectInspection,SqlNoDataSourceInspection
    @staticmethod
    def get_hook(prefix, n):
        if sys.platform.startswith("win"):
            hook = "@echo off\n"
            hook += "IF NOT EXIST test4py_tmp_tests mkdir test4py_tmp_tests\n"
        else:
            hook = "#!/bin/sh\n"
            hook += 'if [ ! -d "test4py_tmp_tests" ]; then\n'
            hook += '    mkdir "test4py_tmp_tests"\n'
            hook += "fi\n"
        file = os.path.join("test4py_tmp_tests", f"{prefix}_{n}")
        hook += f"echo {n} > {file}\n"
        return hook

    def write_hooks(self, pre_gen_hooks=0, post_gen_hooks=0):
        if os.path.exists("hooks"):
            shutil.rmtree("hooks")
        os.makedirs("hooks")
        for i in range(pre_gen_hooks):
            with open(os.path.join("hooks", f"pre_gen_project.{i}"), "w") as fp:
                fp.write(self.get_hook("pre", i))
        for i in range(post_gen_hooks):
            with open(os.path.join("hooks", f"post_gen_project.{i}"), "w") as fp:
                fp.write(self.get_hook("post", i))

    def tearDown(self) -> None:
        if os.path.exists("hooks"):
            shutil.rmtree("hooks")
        if os.path.exists("test4py_tmp_tests"):
            shutil.rmtree("test4py_tmp_tests")


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
