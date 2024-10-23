from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "'This is sentence 53. This is sentence 324. And sentence 3.' 5"

    def test_diversity_2(self):
        return "'This is sentence 122. This is sentence 63. And sentence 767.' 5"

    def test_diversity_3(self):
        return "'This is sentence 34. This is sentence 13. And sentence 22.' 5"

    def test_diversity_4(self):
        return "'This is sentence 22. This is sentence 555. And sentence 23.' 5"

    def test_diversity_5(self):
        return "'This is sentence 3. This is sentence 23. And sentence 1.' 5"

    def test_diversity_6(self):
        return "'This is sentence 7. This is sentence 4246. And sentence 32.' 5"

    def test_diversity_7(self):
        return "'This is sentence 412. This is sentence 4246. And sentence 53.' 5"

    def test_diversity_8(self):
        return "'This is sentence 25. This is sentence 4246. And sentence 643.' 5"

    def test_diversity_9(self):
        return "'This is sentence 26. This is sentence 142. And sentence 432.' 5"

    def test_diversity_10(self):
        return "'This is sentence 4565. This is sentence 123. And sentence 2131.' 5"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "'This is sentence 123. This is sentence 423. And sentence 23.' 3"

    def test_diversity_2(self):
        return "'This is sentence 3. This is sentence 33. And sentence 8676.' 3"

    def test_diversity_3(self):
        return "'This is sentence 331. This is sentence 55. And sentence 6997.' 3"

    def test_diversity_4(self):
        return "'This is sentence 35. This is sentence 1. And sentence 32.' 3"

    def test_diversity_5(self):
        return "'This is sentence 23. This is sentence 4246. And sentence 3321.' 3"

    def test_diversity_6(self):
        return "'This is sentence 77. This is sentence 123. And sentence 1122.' 3"

    def test_diversity_7(self):
        return "'This is sentence 64. This is sentence 246. And sentence 66.' 3"

    def test_diversity_8(self):
        return "'This is sentence 16. This is sentence 242. And sentence 53.' 3"

    def test_diversity_9(self):
        return "'This is sentence 84. This is sentence 73. And sentence 23.' 3"

    def test_diversity_10(self):
        return "'This is sentence 37. This is sentence 15. And sentence 786.' 3"
