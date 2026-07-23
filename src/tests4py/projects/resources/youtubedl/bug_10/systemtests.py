from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJjb2RlIjogIntcImRjeXVhc1wiOlwidGdhXFxuaXFxXCJ9IiwgImV4cGVjdGVkIjogeyJkY3l1YXMiOiAidGdhXG5pcXEifX0='

    def test_diversity_2(self):
        return 'eyJjb2RlIjogIntcImNzdm5cIjpcImJvbXBcXG5uYnZcIn0iLCAiZXhwZWN0ZWQiOiB7ImNzdm4iOiAiYm9tcFxubmJ2In19'

    def test_diversity_3(self):
        return 'eyJjb2RlIjogIntcInFtalwiOlwicmZ3clxcbmFkbVwifSIsICJleHBlY3RlZCI6IHsicW1qIjogInJmd3JcbmFkbSJ9fQ=='

    def test_diversity_4(self):
        return 'eyJjb2RlIjogIntcImVibWJmYVwiOlwidXlkaGJcXG5yYmhod1wifSIsICJleHBlY3RlZCI6IHsiZWJtYmZhIjogInV5ZGhiXG5yYmhodyJ9fQ=='

    def test_diversity_5(self):
        return 'eyJjb2RlIjogIntcImJraml2bVwiOlwid3BldG5sXFxuZGVsZG5cIn0iLCAiZXhwZWN0ZWQiOiB7ImJraml2bSI6ICJ3cGV0bmxcbmRlbGRuIn19'

    def test_diversity_6(self):
        return 'eyJjb2RlIjogIntcImp2Z2Vjc1wiOlwicHl6d1xcbnVsYmtiXCJ9IiwgImV4cGVjdGVkIjogeyJqdmdlY3MiOiAicHl6d1xudWxia2IifX0='

    def test_diversity_7(self):
        return 'eyJjb2RlIjogIntcInVmdnV5XCI6XCJobHB3clxcbmNmeGxcIn0iLCAiZXhwZWN0ZWQiOiB7InVmdnV5IjogImhscHdyXG5jZnhsIn19'

    def test_diversity_8(self):
        return 'eyJjb2RlIjogIntcInZqd25cIjpcImVwaHZubVxcbmlkcXl2YlwifSIsICJleHBlY3RlZCI6IHsidmp3biI6ICJlcGh2bm1cbmlkcXl2YiJ9fQ=='

    def test_diversity_9(self):
        return 'eyJjb2RlIjogIntcImVyYmN1XCI6XCJia2l6XFxueXhocWhpXCJ9IiwgImV4cGVjdGVkIjogeyJlcmJjdSI6ICJia2l6XG55eGhxaGkifX0='

    def test_diversity_10(self):
        return 'eyJjb2RlIjogIntcInZjZ2tcIjpcIm5zaGh2XFxuYndsdWVpXCJ9IiwgImV4cGVjdGVkIjogeyJ2Y2drIjogIm5zaGh2XG5id2x1ZWkifX0='


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
