import unittest
from thefuck.rules.git_fix_stash import match
from thefuck.types import Command


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git show KEUAmYJaUlmh', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git drop klbrkzYVl', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('git save imhMkXlSJsZ', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git apply gRejJUGaJ', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git branch bajUM', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('git show KoreXG', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_7(self):
        self.assertEqual(True, match(Command('git branch EMSua', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('git pop oKYnUQNRKUqf', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('git show qCnYTfVIHdnxaNM', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('git apply TgyTWHtif', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        self.assertEqual(True, match(Command('git stash drop ukedQE', '', '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_2(self):
        self.assertEqual(True, match(Command('git stash apply enGqi', '', '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_3(self):
        self.assertEqual(True, match(Command('git stash apply FthZtUnV', '', '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_4(self):
        self.assertEqual(True, match(Command('git stash pop rRqwxl', '', '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_5(self):
        self.assertEqual(True, match(Command('git stash save jjiWtrvZW', '', '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_6(self):
        self.assertEqual(True, match(Command('git stash show dFmuo', '', '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))
    def test_diversity_7(self):
        self.assertEqual(True, match(Command('git stash list UdWOfDTJOgb', '', '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_8(self):
        self.assertEqual(True, match(Command('git stash pop eWreQNiXM', '', '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_9(self):
        self.assertEqual(True, match(Command('git stash show mFUgxptqrN', '', '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))

    def test_diversity_10(self):
        self.assertEqual(True, match(Command('git stash show mFUgxptqrN', '',
                                             '\n        usage: git stash list [<options>]\n           or: git stash show [<stash>]\n           or: git stash drop [-q|--quiet] [<stash>]\n           or: git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]\n           or: git stash branch <branchname> [<stash>]\n           or: git stash [save [--patch] [-k|--[no-]keep-index] [-q|--quiet]\n        \t\t       [-u|--include-untracked] [-a|--all] [<message>]]\n           or: git stash clear\n        ')))
