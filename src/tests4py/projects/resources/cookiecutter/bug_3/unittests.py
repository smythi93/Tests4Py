import unittest
import click

from cookiecutter.prompt import read_user_choice


class DefaultTest(unittest.TestCase):
    def run_test(self, options, user_choice, name, with_args=True):
        expected = (
            f"Select {name}:\n"
            + "\n".join(f"{i} - {c}" for i, c in enumerate(options, 1))
            + f"\nChoose from {', '.join(str(i) for i in range(1, len(options) + 1))}"
        )

        with unittest.mock.patch("click.Choice") as choice:
            choice.return_value = click.Choice(options)

            with unittest.mock.patch("click.prompt") as prompt:
                prompt.return_value = "{}".format(user_choice)

                self.assertEqual(
                    read_user_choice(name, options), options[user_choice - 1]
                )

                if with_args:
                    prompt.assert_called_once_with(
                        expected,
                        type=click.Choice(options),
                        default="1",
                        show_choices=False,
                    )
                else:
                    prompt.assert_called_once()


class TestsFailing(DefaultTest):
    def test_diversity_1(self):
        options = ["a", "b", "c"]
        user_choice = 1
        name = "name"
        self.run_test(options, user_choice, name)

    def test_diversity_2(self):
        options = ["a", "b", "c"]
        user_choice = 2
        name = "name"
        self.run_test(options, user_choice, name)

    def test_diversity_3(self):
        options = ["a", "b", "c"]
        user_choice = 3
        name = "name"
        self.run_test(options, user_choice, name)

    def test_diversity_4(self):
        options = [str(i) for i in range(100)]
        user_choice = 100
        name = "name"
        self.run_test(options, user_choice, name)

    def test_diversity_5(self):
        options = ["a", "b", "c"]
        user_choice = 3
        name = "varname"
        self.run_test(options, user_choice, name)

    def test_diversity_6(self):
        options = ["a", "b", "c"]
        user_choice = 3
        name = "varname"
        self.run_test(options, user_choice, name)

    def test_diversity_7(self):
        options = ["a", "b", "c", "d"]
        user_choice = 3
        name = "varname"
        self.run_test(options, user_choice, name)

    def test_diversity_8(self):
        options = ["a", "b", "c", "d", "e"]
        user_choice = 4
        name = "var"
        self.run_test(options, user_choice, name)

    def test_diversity_9(self):
        options = ["a"]
        user_choice = 1
        name = "varname"
        self.run_test(options, user_choice, name)

    def test_diversity_10(self):
        options = ["a", "b"]
        user_choice = 2
        name = "varname"
        self.run_test(options, user_choice, name)


class TestsPassing(DefaultTest):
    def test_diversity_1(self):
        options = ["a", "b", "c"]
        user_choice = 1
        name = "name"
        self.run_test(options, user_choice, name, with_args=False)

    def test_diversity_2(self):
        options = ["a", "b", "c"]
        user_choice = 2
        name = "name"
        self.run_test(options, user_choice, name, with_args=False)

    def test_diversity_3(self):
        options = ["a", "b", "c"]
        user_choice = 3
        name = "name"
        self.run_test(options, user_choice, name, with_args=False)

    def test_diversity_4(self):
        options = [str(i) for i in range(100)]
        user_choice = 100
        name = "name"
        self.run_test(options, user_choice, name, with_args=False)

    def test_diversity_5(self):
        options = ["a", "b", "c"]
        user_choice = 3
        name = "varname"
        self.run_test(options, user_choice, name, with_args=False)

    def test_diversity_6(self):
        options = ["a", "b", "c"]
        user_choice = 3
        name = "varname"
        self.run_test(options, user_choice, name, with_args=False)

    def test_diversity_7(self):
        options = ["a", "b", "c", "d"]
        user_choice = 3
        name = "varname"
        self.run_test(options, user_choice, name, with_args=False)

    def test_diversity_8(self):
        options = ["a", "b", "c", "d", "e"]
        user_choice = 4
        name = "var"
        self.run_test(options, user_choice, name, with_args=False)

    def test_diversity_9(self):
        self.assertRaises(TypeError, read_user_choice, "name", 1)

    def test_diversity_10(self):
        self.assertRaises(ValueError, read_user_choice, "name", [])
