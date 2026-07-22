from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


def _config(full_name, repo_name="t4p", project_name="Prj"):
    return (
        f'{{"full_name":"{full_name}",'
        f'"repo_name":"{repo_name}",'
        f'"project_name":"{project_name}"}}'
    )


class TestsFailing(FailingSystemtests):
    # A cookiecutter.json whose full_name contains non-ASCII characters. Read
    # under an ASCII locale the buggy generate_context raises a decoding error.
    def test_diversity_1(self):
        return _config("café")

    def test_diversity_2(self):
        return _config("résumé")

    def test_diversity_3(self):
        return _config("Müller")

    def test_diversity_4(self):
        return _config("José Niño")

    def test_diversity_5(self):
        return _config("ångström unit")

    def test_diversity_6(self):
        return _config("naïve soul")

    def test_diversity_7(self):
        return _config("François")

    def test_diversity_8(self):
        return _config("straße 12")

    def test_diversity_9(self):
        return _config("øresund bridge")

    def test_diversity_10(self):
        return _config("zürich äöü")


class TestsPassing(PassingSystemtests):
    # A pure-ASCII cookiecutter.json reads correctly on the buggy build.
    def test_diversity_1(self):
        return _config("John Doe")

    def test_diversity_2(self):
        return _config("Jane Smith")

    def test_diversity_3(self):
        return _config("Marius Smytzek")

    def test_diversity_4(self):
        return _config("Alan Turing")

    def test_diversity_5(self):
        return _config("Grace Hopper")

    def test_diversity_6(self):
        return _config("Ada Lovelace")

    def test_diversity_7(self):
        return _config("Linus T")

    def test_diversity_8(self):
        return _config("Donald Knuth")

    def test_diversity_9(self):
        return _config("Barbara Liskov")

    def test_diversity_10(self):
        return _config("Edsger Dijkstra")
