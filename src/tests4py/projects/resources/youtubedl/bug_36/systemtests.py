from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2l1c3VkYT90YXJrYXhsYXo9YnF0dXNlcCMhL3ZpZGVvL3ZpZGVvLnBocD92aWRlb19pZD0zODE5MDcwNDYyODU4NzUiLCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_2(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2VwZWE_ZWtqdnJoZz1mZWpvZWFuZyMhL3ZpZGVvL2VtYmVkP3ZpZGVvX2lkPTk0MzU4MTIwODUyNTcxNyIsICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_3(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2lpaWV1Y3k_b3BlaHp1dT1yYm55a29zYmojIS9waG90by5waHA_dj02MDA4MTczNDkwNzU1NjIiLCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_4(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3Vlc20_cWdubml3PWJuemkjIS9waG90by5waHA_dj01NTYyNjU1MjUxMjQzMTkiLCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_5(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2l6aHBiY2s_bXlsamI9dmRpeiMhL3ZpZGVvL2VtYmVkP3Y9MzExMzQ0NzEwNTk4MjU2IiwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_6(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL25ld3N5cWxvYz9jYm9vc249enZzbmx6cm12IyEvdmlkZW8vZW1iZWQ_dj01MDQ3MjgzODkwNTI0MjciLCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_7(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3BmZ21ldD90aW5ldnJsdD1zYnJ0Ym9kdncjIS92aWRlby9lbWJlZD92PTEyMjAyNDI3NTQ4NDg0NSIsICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_8(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3Z3eHQ_YmFzZ2JocGw9b3V2cSMhL3Bob3RvLnBocD92PTQzNjY0MjQxODcyOTA2MSIsICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_9(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2hqZHhwdnR2bD9xZGVwdng9dWhxam0jIS92aWRlby9lbWJlZD92PTI0NjU4NzU3OTE3MzIyOSIsICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_10(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3ZzeGJhP2V1Y2c9ZmJscmUjIS9waG90by5waHA_dmlkZW9faWQ9NDk3ODM5MjA0MDQxMTA1IiwgImV4cGVjdGVkIjogdHJ1ZX0='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2JxZ253eCMhL3ZpZGVvL2VtYmVkP3ZpZGVvX2lkPTgxNzU5MjQ1ODgzMTgzNSIsICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_2(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2t4b3gjIS9waG90by5waHA_dj0yOTk3NjkwMTYyMzYzMjUiLCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_3(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL252eXF2cSMhL3Bob3RvLnBocD92aWRlb19pZD01MzMyNzQwMjU4MTg3MTgiLCAiZXhwZWN0ZWQiOiB0cnVlfQ=='

    def test_diversity_4(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2N4eGtvYncjIS92aWRlby9lbWJlZD92PTY3MDI4MzM2NjgyNzcwMyIsICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_5(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3ltY2ZrIyEvdmlkZW8vZW1iZWQ_dmlkZW9faWQ9MTI4MDg0OTI1MDkzNzQ5IiwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_6(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3ZpZGVvL2VtYmVkP3Y9MTUxMjYyNTIwMDA3OTE1IiwgImV4cGVjdGVkIjogdHJ1ZX0='

    def test_diversity_7(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3ZpZGVvL3ZpZGVvLnBocD92PTg3MDA0ODE0ODAyMTE0NyIsICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_8(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL2lwcmloYyMhL3ZpZGVvL2VtYmVkP3ZpZGVvX2lkPTMzOTM5NjQyMzk3MTg4NCIsICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_9(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3Bob3RvLnBocD92PTQxNTU2Mzg5ODg0Mzc3MSIsICJleHBlY3RlZCI6IHRydWV9'

    def test_diversity_10(self):
        return 'eyJ1cmwiOiAiaHR0cHM6Ly93d3cuZmFjZWJvb2suY29tL3Bob3RvLnBocD92PTU5NDY2OTI3NDMxMDE3MSIsICJleHBlY3RlZCI6IHRydWV9'
