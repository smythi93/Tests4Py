import os.path
import sys
import unittest
import shutil
from abc import ABC

from cookiecutter import hooks
from cookiecutter import exceptions


class DefaultTests(unittest.TestCase, ABC):
    # noinspection SqlDialectInspection,SqlNoDataSourceInspection
    @staticmethod
    def get_hook(n):
        if sys.platform.startswith("win"):
            hook = f"exit \\b {n}\n"
        else:
            hook = "#!/bin/sh\n"
            hook += f"exit {n}\n"
        return hook

    def write_hooks(self, exits_pre: list = None, exits_post: list = None):
        exits_pre = exits_pre or []
        exits_post = exits_post or []
        if os.path.exists("hooks"):
            shutil.rmtree("hooks")
        os.makedirs("hooks")
        for i, e in enumerate(exits_pre):
            with open(os.path.join("hooks", f"pre_gen_project.{i}"), "w") as fp:
                fp.write(self.get_hook(e))
        for i, e in enumerate(exits_post):
            with open(os.path.join("hooks", f"post_gen_project.{i}"), "w") as fp:
                fp.write(self.get_hook(e))

    def tearDown(self) -> None:
        if os.path.exists("hooks"):
            shutil.rmtree("hooks")


class TestsFailing(DefaultTests):
    def test_diversity_1(self):
        self.write_hooks(exits_pre=[1], exits_post=[])
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "pre_gen_project",
            os.getcwd(),
            {},
        )
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_2(self):
        self.write_hooks(exits_pre=[0, 1], exits_post=[0])
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "pre_gen_project",
            os.getcwd(),
            {},
        )
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_3(self):
        self.write_hooks(exits_pre=[42], exits_post=[])
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "pre_gen_project",
            os.getcwd(),
            {},
        )
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_4(self):
        self.write_hooks(exits_pre=[0, 42], exits_post=[])
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "pre_gen_project",
            os.getcwd(),
            {},
        )
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_5(self):
        self.write_hooks(exits_pre=[1, 42], exits_post=[])
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "pre_gen_project",
            os.getcwd(),
            {},
        )
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_6(self):
        self.write_hooks(exits_pre=[0, 1, 0], exits_post=[])
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "pre_gen_project",
            os.getcwd(),
            {},
        )
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_7(self):
        self.write_hooks(exits_pre=[0, 1, 2], exits_post=[0])
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "pre_gen_project",
            os.getcwd(),
            {},
        )
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_8(self):
        self.write_hooks(exits_pre=[0, 0], exits_post=[1])
        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "post_gen_project",
            os.getcwd(),
            {},
        )

    def test_diversity_9(self):
        self.write_hooks(exits_pre=[1], exits_post=[1])
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "pre_gen_project",
            os.getcwd(),
            {},
        )
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "post_gen_project",
            os.getcwd(),
            {},
        )

    def test_diversity_10(self):
        self.write_hooks(exits_pre=[0, 1], exits_post=[1, 0])
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "pre_gen_project",
            os.getcwd(),
            {},
        )
        self.assertRaises(
            exceptions.FailedHookException,
            hooks.run_hook,
            "post_gen_project",
            os.getcwd(),
            {},
        )


class TestsPassing(DefaultTests):
    def test_diversity_1(self):
        self.write_hooks(exits_pre=[0], exits_post=[])
        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_2(self):
        self.write_hooks(exits_pre=[0, 0], exits_post=[0])
        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_3(self):
        self.write_hooks(exits_pre=[0], exits_post=[0])
        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_4(self):
        self.write_hooks(exits_pre=[], exits_post=[0])
        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_5(self):
        self.write_hooks(exits_pre=[], exits_post=[0, 0])
        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_6(self):
        self.write_hooks(exits_pre=[0, 0], exits_post=[0, 0])
        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_7(self):
        self.write_hooks(exits_pre=[0] * 10, exits_post=[0] * 10)
        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_8(self):
        self.write_hooks(exits_pre=[], exits_post=[])
        hooks.run_hook("pre_gen_project", os.getcwd(), {})
        hooks.run_hook("post_gen_project", os.getcwd(), {})

    def test_diversity_9(self):
        self.write_hooks(exits_pre=[0], exits_post=[1])
        hooks.run_hook("pre_gen_project", os.getcwd(), {})

    def test_diversity_10(self):
        self.write_hooks(exits_pre=[1], exits_post=[0])
        hooks.run_hook("post_gen_project", os.getcwd(), {})
