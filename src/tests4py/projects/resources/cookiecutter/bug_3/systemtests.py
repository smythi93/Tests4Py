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
        full_name = '["Marius Smytzek","Martin Eberlein"]'
        return f"{self._default_config(full_name=full_name)}\npre:echo,pre1"

    def test_diversity_2(self):
        email = '["mariussmytzek@cispa.de","martineberlein@huberlin.de"]'
        return f"{self._default_config(email=email)}\npost:exit,0"

    def test_diversity_3(self):
        repo_name = '["t4p","p4t"]'
        return f"{self._default_config(repo_name=repo_name)}\n"

    def test_diversity_4(self):
        full_name = '["Marius Smytzek","Martin Eberlein","Michael Mera"]'
        return f"{self._default_config(full_name=full_name)}\npre:echo,pre1\npost:echo,post1"

    def test_diversity_5(self):
        full_name = '["Marius Smytzek","Martin Eberlein","Michael Mera"]'
        repo_name = '["t4p","p4t"]'
        return f"{self._default_config(full_name=full_name, repo_name=repo_name)}\npre:echo,pre1\npost:exit,0"

    def test_diversity_6(self):
        email = '["mariussmytzek@cispa.de","martineberlein@huberlin.de"]'
        repo_name = '["t4p","p4t"]'
        return f"{self._default_config(email=email, repo_name=repo_name)}\n"

    def test_diversity_7(self):
        full_name = '["Marius Smytzek","Martin Eberlein","Michael Mera"]'
        email = '["mariussmytzek@cispa.de","martineberlein@huberlin.de"]'
        repo_name = '["t4p","p4t"]'
        return f"{self._default_config(full_name=full_name, email=email, repo_name=repo_name)}\n"

    def test_diversity_8(self):
        year = '["2022","2023"]'
        return f"{self._default_config(year=year)}\npost:echo,post1"

    def test_diversity_9(self):
        year = '["2022","2023","2024","2025"]'
        return f"{self._default_config(year=year)}\npre:echo,pre1"

    def test_diversity_10(self):
        full_name = '["Marius Smytzek","Martin Eberlein","Michael Mera"]'
        email = '["mariussmytzek@cispa.de","martineberlein@huberlin.de"]'
        project_name = '["tests4py","py4tests"]'
        repo_name = '["t4p","p4t"]'
        project_short_description = '["description","No description"]'
        release_date = '["2022-06-23","2023-01-22"]'
        year = '["2022","2023","2024","2025"]'
        version = '["0.3","1.8.2"]'
        config = self._default_config(
            full_name=full_name,
            email=email,
            project_name=project_name,
            repo_name=repo_name,
            project_short_description=project_short_description,
            release_date=release_date,
            year=year,
            version=version,
        )
        return f"{config}\npre:echo,This is a more complex example of a pre hook_ Will this work"


class TestsPassing(DefaultTests):
    def __init__(self):
        super().__init__(passing=True)

    def test_diversity_1(self):
        full_name = '"Martin Eberlein"'
        return f"{self._default_config(full_name=full_name)}\npre:echo,pre1"

    def test_diversity_2(self):
        email = '"martineberlein@huberlin.de"'
        return f"{self._default_config(email=email)}\npost:exit,0"

    def test_diversity_3(self):
        repo_name = '"p4t"'
        return f"{self._default_config(repo_name=repo_name)}\n"

    def test_diversity_4(self):
        full_name = '"Michael Mera"'
        return f"{self._default_config(full_name=full_name)}\npre:echo,pre1\npost:echo,post1"

    def test_diversity_5(self):
        full_name = '"Michael Mera"'
        repo_name = '"p4t"'
        return f"{self._default_config(full_name=full_name, repo_name=repo_name)}\npre:echo,pre1\npost:exit,0"

    def test_diversity_6(self):
        email = '"martineberlein@huberlin.de"'
        repo_name = '"p4t"'
        return f"{self._default_config(email=email, repo_name=repo_name)}\n"

    def test_diversity_7(self):
        full_name = '"Michael Mera"'
        email = '"martineberlein@huberlin.de"'
        repo_name = '"p4t"'
        return f"{self._default_config(full_name=full_name, email=email, repo_name=repo_name)}\n"

    def test_diversity_8(self):
        year = '"2023"'
        return f"{self._default_config(year=year)}\npost:echo,post1"

    def test_diversity_9(self):
        year = '"2025"'
        return f"{self._default_config(year=year)}\npre:echo,pre1"

    def test_diversity_10(self):
        full_name = '"Michael Mera"'
        email = '"martineberlein@huberlin.de"'
        project_name = '"py4tests"'
        repo_name = '"p4t"'
        project_short_description = '"No description"'
        release_date = '"2023-01-22"'
        year = '"2025"'
        version = '"1.8.2"'
        config = self._default_config(
            full_name=full_name,
            email=email,
            project_name=project_name,
            repo_name=repo_name,
            project_short_description=project_short_description,
            release_date=release_date,
            year=year,
            version=version,
        )
        return f"{config}\npre:echo,This is a more complex example of a pre hook_ Will this work"
