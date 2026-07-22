from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcImRjeXVhc1wiOlwidGdhXFwnaXFxXCJ9IiwgImV4cGVjdGVkIjogeyJkY3l1YXMiOiAidGdhJ2lxcSJ9fQ=='

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcImNzdm5cIjpcImJvbXBcXCduYnZcIn0iLCAiZXhwZWN0ZWQiOiB7ImNzdm4iOiAiYm9tcCduYnYifX0='

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcInFtalwiOlwicmZ3clxcJ2FkbVwifSIsICJleHBlY3RlZCI6IHsicW1qIjogInJmd3InYWRtIn19'

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcImVibWJmYVwiOlwidXlkaGJcXCdyYmhod1wifSIsICJleHBlY3RlZCI6IHsiZWJtYmZhIjogInV5ZGhiJ3JiaGh3In19'

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcImJraml2bVwiOlwid3BldG5sXFwnZGVsZG5cIn0iLCAiZXhwZWN0ZWQiOiB7ImJraml2bSI6ICJ3cGV0bmwnZGVsZG4ifX0='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcImp2Z2Vjc1wiOlwicHl6d1xcJ3VsYmtiXCJ9IiwgImV4cGVjdGVkIjogeyJqdmdlY3MiOiAicHl6dyd1bGJrYiJ9fQ=='

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcInVmdnV5XCI6XCJobHB3clxcJ2NmeGxcIn0iLCAiZXhwZWN0ZWQiOiB7InVmdnV5IjogImhscHdyJ2NmeGwifX0='

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcInZqd25cIjpcImVwaHZubVxcJ2lkcXl2YlwifSIsICJleHBlY3RlZCI6IHsidmp3biI6ICJlcGh2bm0naWRxeXZiIn19'

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcImVyYmN1XCI6XCJia2l6XFwneXhocWhpXCJ9IiwgImV4cGVjdGVkIjogeyJlcmJjdSI6ICJia2l6J3l4aHFoaSJ9fQ=='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcInZjZ2tcIjpcIm5zaGh2XFwnYndsdWVpXCJ9IiwgImV4cGVjdGVkIjogeyJ2Y2drIjogIm5zaGh2J2J3bHVlaSJ9fQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcIm1odlwiOlwiZXFlcHJqXCJ9IiwgImV4cGVjdGVkIjogeyJtaHYiOiAiZXFlcHJqIn19'

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcIm55bHJcIjpcInVzclwifSIsICJleHBlY3RlZCI6IHsibnlsciI6ICJ1c3IifX0='

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcImF6bVwiOlwieHhpalwifSIsICJleHBlY3RlZCI6IHsiYXptIjogInh4aWoifX0='

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcImhyaXloXCI6XCJudGJzXCJ9IiwgImV4cGVjdGVkIjogeyJocml5aCI6ICJudGJzIn19'

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcImlpaWdcIjpcInZnZFwifSIsICJleHBlY3RlZCI6IHsiaWlpZyI6ICJ2Z2QifX0='

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcImtyYlwiOlwicnpubFwifSIsICJleHBlY3RlZCI6IHsia3JiIjogInJ6bmwifX0='

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcInZ5Z1wiOlwieGZucXZyXCJ9IiwgImV4cGVjdGVkIjogeyJ2eWciOiAieGZucXZyIn19'

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcIndmbXJyXCI6XCJ3cWJuXCJ9IiwgImV4cGVjdGVkIjogeyJ3Zm1yciI6ICJ3cWJuIn19'

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcInJ4dHJcIjpcIndpc29ucFwifSIsICJleHBlY3RlZCI6IHsicnh0ciI6ICJ3aXNvbnAifX0='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcImJianZrYlwiOlwiaXFmXCJ9IiwgImV4cGVjdGVkIjogeyJiYmp2a2IiOiAiaXFmIn19'
