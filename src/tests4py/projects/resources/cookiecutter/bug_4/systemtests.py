from abc import ABC

from tests4py.tests.diversity import Systemtests


class DefaultTests(Systemtests, ABC):
    def __init__(self, passing: bool = False):
        Systemtests.__init__(self, passing=passing)

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


class TestsFailing(DefaultTests):
    def __init__(self):
        super().__init__(passing=False)

    def test_diversity_1(self):
        return f"{self._default_config()}\npost:exit,42\npre:echo,pre1"

    def test_diversity_2(self):
        return f"{self._default_config()}\npre:exit,0\npost:exit,15"

    def test_diversity_3(self):
        return f"{self._default_config()}\npre:echo,pre1\npost:exit,52"

    def test_diversity_4(self):
        return f"{self._default_config()}\npost:exit,1\npre:exit,0"

    def test_diversity_5(self):
        return f"{self._default_config()}\npre:exit,0\npost:exit,1"

    def test_diversity_6(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return f"{self._default_config(full_name=full_name)}\npre:exit,0\npost:exit,42"

    def test_diversity_7(self):
        return f"{self._default_config()}\npost:exit,42424242"

    def test_diversity_8(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return (
            f"{self._default_config(full_name=full_name)}\npre:echo,pre1\npost:exit,42"
        )

    def test_diversity_9(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return (
            f"{self._default_config(full_name=full_name)}\npre:echo,pre1\npost:exit,1"
        )

    def test_diversity_10(self):
        return (
            f"{self._default_config()}\npre:echo,This is a more complex example of a pre hook_ Will this work\n"
            f"post:exit,42"
        )


class TestsPassing(DefaultTests):
    def __init__(self):
        super().__init__(passing=True)

    def test_diversity_1(self):
        return f"{self._default_config()}\npost:exit,0\npre:echo,pre1"

    def test_diversity_2(self):
        return f"{self._default_config()}\npre:exit,0"

    def test_diversity_3(self):
        return f"{self._default_config()}\npre:echo,pre1\npost:exit,0"

    def test_diversity_4(self):
        return f"{self._default_config()}\npost:echo,post1\npre:exit,0"

    def test_diversity_5(self):
        return f"{self._default_config()}\npre:exit,1\npost:exit,0"

    def test_diversity_6(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return f"{self._default_config(full_name=full_name)}\npre:exit,0\npost:exit,0"

    def test_diversity_7(self):
        return f"{self._default_config()}\npost:exit,0"

    def test_diversity_8(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return (
            f"{self._default_config(full_name=full_name)}\npre:echo,pre1\npost:exit,0"
        )

    def test_diversity_9(self):
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return (
            f"{self._default_config(full_name=full_name)}\npost:echo,post1\npre:exit,1"
        )

    def test_diversity_10(self):
        return (
            f"{self._default_config()}\npre:echo,This is a more complex example of a pre hook_ Will this work\n"
            f"post:exit,0"
        )
