from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '<body>PHP "Error" is difficult.<body>'

    def test_diversity_2(self):
        return '<video>PHP "Project" is hard.<video>'

    def test_diversity_3(self):
        return '<embed>PHP "Fundamental" is easy.<embed>'

    def test_diversity_4(self):
        return '<p>Ruby "Syntax" is easy.<p>'

    def test_diversity_5(self):
        return '<img>PHP "Book" is good.<img>'

    def test_diversity_6(self):
        return '<h1>JavaScript "Error" is good.<h1>'

    def test_diversity_7(self):
        return '<span>C "Project" is difficult.<span>'

    def test_diversity_8(self):
        return '<i>C# "Code" is difficult.<i>'

    def test_diversity_9(self):
        return '<i>C# "Error" is cool.<i>'

    def test_diversity_10(self):
        return '<canvas>C# "Fundamental" is difficult.<canvas>'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "<article>JavaScript 'Syntax' is complex.<article>"

    def test_diversity_2(self):
        return "<title>Python 'Language' is hard.<title>"

    def test_diversity_3(self):
        return "<li>Python 'Project' is easy.<li>"

    def test_diversity_4(self):
        return "<i>JavaScript 'Fundamental' is complex.<i>"

    def test_diversity_5(self):
        return "<details>JavaScript 'Book' is controversial.<details>"

    def test_diversity_6(self):
        return "<ul>R 'Project' is easy.<ul>"

    def test_diversity_7(self):
        return "<canvas>C# 'Code' is easy.<canvas>"

    def test_diversity_8(self):
        return "<output>Python 'Fundamental' is hard.<output>"

    def test_diversity_9(self):
        return "<progress>C# 'Error' is hard.<progress>"

    def test_diversity_10(self):
        return "<article>Pearl 'Book' is controversial.<article>"
