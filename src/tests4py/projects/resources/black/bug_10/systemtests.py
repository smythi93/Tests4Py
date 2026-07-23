from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'aWYgMjoKCWlmIDE6CgkJemp6ID0gMAoJIyBpbWtwCglwYXNzCg== aWYgMjoKICAgIGlmIDE6CiAgICAgICAgemp6ID0gMAogICAgIyBpbWtwCiAgICBwYXNzCg=='

    def test_diversity_2(self):
        return 'aWYgNDoKCWlmIDE6CgkJcGFzcwoJIyB3a2cKCXBhc3MK aWYgNDoKICAgIGlmIDE6CiAgICAgICAgcGFzcwogICAgIyB3a2cKICAgIHBhc3MK'

    def test_diversity_3(self):
        return 'aWYgNDoKCWlmIDQ6CgkJcGFzcwoJIyBud2VlbGNuYQoJaWFqZGJkbCA9IDEK aWYgNDoKICAgIGlmIDQ6CiAgICAgICAgcGFzcwogICAgIyBud2VlbGNuYQogICAgaWFqZGJkbCA9IDEK'

    def test_diversity_4(self):
        return 'aWYgNDoKCWlmIDQ6CgkJcGFzcwoJIyBmbHAKCWxkayA9IDcK aWYgNDoKICAgIGlmIDQ6CiAgICAgICAgcGFzcwogICAgIyBmbHAKICAgIGxkayA9IDcK'

    def test_diversity_5(self):
        return 'aWYgNDoKCWlmIDQ6CgkJcGFzcwoJIyB4bWZ4CglwYXNzCg== aWYgNDoKICAgIGlmIDQ6CiAgICAgICAgcGFzcwogICAgIyB4bWZ4CiAgICBwYXNzCg=='

    def test_diversity_6(self):
        return 'aWYgMzoKCWlmIDQ6CgkJYmtsbmNnaiA9IDkKCSMgdG9hbnkKCXBhc3MK aWYgMzoKICAgIGlmIDQ6CiAgICAgICAgYmtsbmNnaiA9IDkKICAgICMgdG9hbnkKICAgIHBhc3MK'

    def test_diversity_7(self):
        return 'aWYgMToKCWlmIDE6CgkJa2RzaG54amUgPSAzCgkjIGd2agoJcGFzcwo= aWYgMToKICAgIGlmIDE6CiAgICAgICAga2RzaG54amUgPSAzCiAgICAjIGd2agogICAgcGFzcwo='

    def test_diversity_8(self):
        return 'aWYgMjoKCWlmIDU6CgkJbHRndWhoID0gNwoJIyBoY3lvb2lkcAoJeXd2diA9IDYK aWYgMjoKICAgIGlmIDU6CiAgICAgICAgbHRndWhoID0gNwogICAgIyBoY3lvb2lkcAogICAgeXd2diA9IDYK'

    def test_diversity_9(self):
        return 'aWYgMjoKCWlmIDI6CgkJa3BuZmNtID0gMwoJIyBnYnNwdG4KCXBhc3MK aWYgMjoKICAgIGlmIDI6CiAgICAgICAga3BuZmNtID0gMwogICAgIyBnYnNwdG4KICAgIHBhc3MK'

    def test_diversity_10(self):
        return 'aWYgNDoKCWlmIDE6CgkJbnpkd2NoenMgPSA1CgkjIGlldXQKCXlrdiA9IDkK aWYgNDoKICAgIGlmIDE6CiAgICAgICAgbnpkd2NoenMgPSA1CiAgICAjIGlldXQKICAgIHlrdiA9IDkK'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'aWYgMzoKICAgIGlmIDI6CiAgICAgICAgaGZxY2lvID0gNAogICAgICAgICMgYXRvCiAgICByZm54bGttdSA9IDQK aWYgMzoKICAgIGlmIDI6CiAgICAgICAgaGZxY2lvID0gNAogICAgICAgICMgYXRvCiAgICByZm54bGttdSA9IDQK'

    def test_diversity_2(self):
        return 'aWYgNDoKICAgIGlmIDE6CiAgICAgICAga3FteHN3b3IgPSA2CiAgICAgICAgIyB1ZHdjbwogICAgcGFzcwo= aWYgNDoKICAgIGlmIDE6CiAgICAgICAga3FteHN3b3IgPSA2CiAgICAgICAgIyB1ZHdjbwogICAgcGFzcwo='

    def test_diversity_3(self):
        return 'aWYgMzoKICAgIGlmIDU6CiAgICAgICAgaGZiID0gNAogICAgICAgICMgeXZ3CiAgICBpYnZ6YWkgPSA5Cg== aWYgMzoKICAgIGlmIDU6CiAgICAgICAgaGZiID0gNAogICAgICAgICMgeXZ3CiAgICBpYnZ6YWkgPSA5Cg=='

    def test_diversity_4(self):
        return 'aWYgMToKCWlmIDQ6CgkJcGFzcwoJCSMgd2hqcXd1ZXIKCXBhc3MK aWYgMToKICAgIGlmIDQ6CiAgICAgICAgcGFzcwogICAgICAgICMgd2hqcXd1ZXIKICAgIHBhc3MK'

    def test_diversity_5(self):
        return 'aWYgNDoKCWlmIDQ6CgkJZXNocnF3eXogPSA0CgkJIyB1Z2JmdAoJcGFzcwo= aWYgNDoKICAgIGlmIDQ6CiAgICAgICAgZXNocnF3eXogPSA0CiAgICAgICAgIyB1Z2JmdAogICAgcGFzcwo='

    def test_diversity_6(self):
        return 'aWYgNToKICAgIGlmIDQ6CiAgICAgICAgempsamFwID0gOQogICAgICAgICMgZGFkY2llb2sKICAgIHBhc3MK aWYgNToKICAgIGlmIDQ6CiAgICAgICAgempsamFwID0gOQogICAgICAgICMgZGFkY2llb2sKICAgIHBhc3MK'

    def test_diversity_7(self):
        return 'aWYgNToKICAgIGlmIDU6CiAgICAgICAgcGFzcwogICAgICAgICMgdHVoand3CiAgICBwYXNzCg== aWYgNToKICAgIGlmIDU6CiAgICAgICAgcGFzcwogICAgICAgICMgdHVoand3CiAgICBwYXNzCg=='

    def test_diversity_8(self):
        return 'aWYgMzoKICAgIGlmIDE6CiAgICAgICAgcGFzcwogICAgICAgICMgYWRubAogICAgcGFzcwo= aWYgMzoKICAgIGlmIDE6CiAgICAgICAgcGFzcwogICAgICAgICMgYWRubAogICAgcGFzcwo='

    def test_diversity_9(self):
        return 'aWYgMToKCWlmIDE6CgkJcGFzcwoJCSMgbHFwenB4ZgoJcGFzcwo= aWYgMToKICAgIGlmIDE6CiAgICAgICAgcGFzcwogICAgICAgICMgbHFwenB4ZgogICAgcGFzcwo='

    def test_diversity_10(self):
        return 'aWYgMzoKCWlmIDU6CgkJcGFzcwoJCSMgdmpxbgoJZnh3YnAgPSA1Cg== aWYgMzoKICAgIGlmIDU6CiAgICAgICAgcGFzcwogICAgICAgICMgdmpxbgogICAgZnh3YnAgPSA1Cg=='
