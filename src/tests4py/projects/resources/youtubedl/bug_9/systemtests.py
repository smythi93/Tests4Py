from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW2hlaWdodD49ODU2MzIxNzY4XStiZXN0YXVkaW8vYmVzdCIsICJpZHMiOiBbInh2dGp1IiwgInBudGsiLCAiZGZyIl0sICJleHBlY3RlZCI6IFsiZGZyIl19'

    def test_diversity_2(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW3dpZHRoPj00NjQ4Nzk2NTFdK2Jlc3RhdWRpby9iZXN0IiwgImlkcyI6IFsidnhraWh0IiwgInBxY3ciLCAib2xqcCJdLCAiZXhwZWN0ZWQiOiBbIm9sanAiXX0='

    def test_diversity_3(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW3dpZHRoPj01NTY0NTQ0OThdK3dvcnN0YXVkaW8vYmVzdCIsICJpZHMiOiBbInBiZSIsICJtbG0iLCAiYWd4eSJdLCAiZXhwZWN0ZWQiOiBbImFneHkiXX0='

    def test_diversity_4(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW2Zwcz49NDMzNDA0OF0rd29yc3RhdWRpby9iZXN0IiwgImlkcyI6IFsicG9va20iLCAibXdncCIsICJ4bWFmIl0sICJleHBlY3RlZCI6IFsieG1hZiJdfQ=='

    def test_diversity_5(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW2ZpbGVzaXplPj03NDMyMTE5NjVdK2Jlc3RhdWRpby93b3JzdCIsICJpZHMiOiBbInpneW1xdSIsICJtcHZqIiwgImNmZXkiXSwgImV4cGVjdGVkIjogWyJjZmV5Il19'

    def test_diversity_6(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW3dpZHRoPj05NzIxMTgwNDBdK2Jlc3RhdWRpby93b3JzdCIsICJpZHMiOiBbIm5jemIiLCAiam1jbXEiLCAibm9hcGF2Il0sICJleHBlY3RlZCI6IFsibm9hcGF2Il19'

    def test_diversity_7(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW2hlaWdodD49OTc4ODUwNzA2XStiZXN0YXVkaW8vd29yc3QiLCAiaWRzIjogWyJja2xvIiwgIndkYWF4IiwgInhianNiIl0sICJleHBlY3RlZCI6IFsieGJqc2IiXX0='

    def test_diversity_8(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW2Zwcz49NjM4NDk0MDNdK3dvcnN0YXVkaW8vYmVzdCIsICJpZHMiOiBbImRpdG0iLCAibXdybHBxIiwgInd5d2hycyJdLCAiZXhwZWN0ZWQiOiBbInd5d2hycyJdfQ=='

    def test_diversity_9(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW2Zwcz49NzI0OTUyMjkwXStiZXN0YXVkaW8vd29yc3QiLCAiaWRzIjogWyJtZHJ5a2QiLCAicHp4Y3FlIiwgInVreWpwcyJdLCAiZXhwZWN0ZWQiOiBbInVreWpwcyJdfQ=='

    def test_diversity_10(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvW3dpZHRoPj04NTQzOTA5MDddK2Jlc3RhdWRpby93b3JzdCIsICJpZHMiOiBbImF5Z2RjIiwgIm5kengiLCAiZml4Ym8iXSwgImV4cGVjdGVkIjogWyJmaXhibyJdfQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvIiwgImlkcyI6IFsianVhY2kiLCAibmhja2J0IiwgInRpZCJdLCAiZXhwZWN0ZWQiOiBbImp1YWNpIl19'

    def test_diversity_2(self):
        return 'eyJmb3JtYXQiOiAid29yc3QiLCAiaWRzIjogWyJ6bHJsIiwgInZkaWVoIiwgIm5nYWpwbSJdLCAiZXhwZWN0ZWQiOiBbIm5nYWpwbSJdfQ=='

    def test_diversity_3(self):
        return 'eyJmb3JtYXQiOiAiYmVzdCIsICJpZHMiOiBbImlleiIsICJ3YmsiLCAiZWphcXBvIl0sICJleHBlY3RlZCI6IFsiZWphcXBvIl19'

    def test_diversity_4(self):
        return 'eyJmb3JtYXQiOiAiYmVzdCIsICJpZHMiOiBbImx1d2NqIiwgImZ3eHkiLCAiZWpxeiJdLCAiZXhwZWN0ZWQiOiBbImVqcXoiXX0='

    def test_diversity_5(self):
        return 'eyJmb3JtYXQiOiAiYmVzdCIsICJpZHMiOiBbIndwZWkiLCAicnBsYyIsICJ0bnNqcCJdLCAiZXhwZWN0ZWQiOiBbInRuc2pwIl19'

    def test_diversity_6(self):
        return 'eyJmb3JtYXQiOiAiYmVzdCIsICJpZHMiOiBbImdzcSIsICJmeWpvdWwiLCAid25veGYiXSwgImV4cGVjdGVkIjogWyJ3bm94ZiJdfQ=='

    def test_diversity_7(self):
        return 'eyJmb3JtYXQiOiAid29yc3QiLCAiaWRzIjogWyJoZGRrZmoiLCAidG1wbHgiLCAiaWlkIl0sICJleHBlY3RlZCI6IFsiaWlkIl19'

    def test_diversity_8(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvK2Jlc3RhdWRpbyIsICJpZHMiOiBbIm9zZHciLCAicHl0IiwgImRqZWtqcCJdLCAiZXhwZWN0ZWQiOiBbIm9zZHcrcHl0Il19'

    def test_diversity_9(self):
        return 'eyJmb3JtYXQiOiAid29yc3QiLCAiaWRzIjogWyJob29tbnQiLCAiZ3l1ZmEiLCAibnh2bSJdLCAiZXhwZWN0ZWQiOiBbIm54dm0iXX0='

    def test_diversity_10(self):
        return 'eyJmb3JtYXQiOiAiYmVzdHZpZGVvIiwgImlkcyI6IFsic2JobCIsICJranRrZ2UiLCAid2Z6Y24iXSwgImV4cGVjdGVkIjogWyJzYmhsIl19'
