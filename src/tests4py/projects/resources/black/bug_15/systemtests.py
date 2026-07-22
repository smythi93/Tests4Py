from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'IyBmbXQ6IG9mZgpAcm91dGUoWwogICAgKDksIDUsIDIsIDcpCl0pCmRlZiBycHl1Y3ZoKGhleW8pOgogICAgcGFzcwojIGZtdDogb24K'

    def test_diversity_2(self):
        return 'IyBmbXQ6IG9mZgpAbWFyayhbCiAgICAoNywgOCwgMSkKXSkKZGVmIG92emR6ZWMobW9hc25kdG0pOgogICAgcGFzcwojIGZtdDogb24K'

    def test_diversity_3(self):
        return 'IyBmbXQ6IG9mZgpAZ2l2ZW4oWwogICAgKDIsIDUsIDYpCl0pCmRlZiBwZWR5KGRvb3N0cik6CiAgICBwYXNzCiMgZm10OiBvbgo='

    def test_diversity_4(self):
        return 'IyBmbXQ6IG9mZgpAcmVnaXN0ZXIoWwogICAgKDcsIDgsIDUpCl0pCmRlZiBjcWUodHlteW0pOgogICAgcGFzcwojIGZtdDogb24K'

    def test_diversity_5(self):
        return 'IyBmbXQ6IG9mZgpAZGVjbyhbCiAgICAoOSwgNiwgNCkKXSkKZGVmIGh5cXl3KHl4bmR4eCk6CiAgICBwYXNzCiMgZm10OiBvbgo='

    def test_diversity_6(self):
        return 'IyBmbXQ6IG9mZgpAZGVjbyhbCiAgICAoMywgOCwgMiwgMSkKXSkKZGVmIGFsaXp3Ym0oeXFscWp6enEpOgogICAgcGFzcwojIGZtdDogb24K'

    def test_diversity_7(self):
        return 'IyBmbXQ6IG9mZgpAZGVjbyhbCiAgICAoMywgMywgMiwgMykKXSkKZGVmIHV4ZG4obGNxa3F6dGspOgogICAgcGFzcwojIGZtdDogb24K'

    def test_diversity_8(self):
        return 'IyBmbXQ6IG9mZgpAZ2l2ZW4oWwogICAgKDIsIDApCl0pCmRlZiBydmV1cShhaHF0KToKICAgIHBhc3MKIyBmbXQ6IG9uCg=='

    def test_diversity_9(self):
        return 'IyBmbXQ6IG9mZgpAcmVnaXN0ZXIoWwogICAgKDcsIDEpCl0pCmRlZiBqemxoamZpaSh3YXRkKToKICAgIHBhc3MKIyBmbXQ6IG9uCg=='

    def test_diversity_10(self):
        return 'IyBmbXQ6IG9mZgpAZ2l2ZW4oWwogICAgKDYsIDQsIDYsIDUpCl0pCmRlZiBzYmYodXdvbndhZSk6CiAgICBwYXNzCiMgZm10OiBvbgo='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'ZGVmIHNzbGwoKToKICAgIHJldHVybiAxMjMK'

    def test_diversity_2(self):
        return 'cHJpbnQoImpicW9oIikK'

    def test_diversity_3(self):
        return 'cGFhenMgPSA3Ngo='

    def test_diversity_4(self):
        return 'IyBmbXQ6IG9mZgp1amcgPSBbNSwgICA3XQojIGZtdDogb24K'

    def test_diversity_5(self):
        return 'Z3ZvZ3V5ayA9IHsicnV1bG5oIjogMTF9Cg=='

    def test_diversity_6(self):
        return 'a2h0ID0gWzIwLCA3OSwgMTBdCg=='

    def test_diversity_7(self):
        return 'aW1wb3J0IGl4aWMKCgpkZWYgYXNoKGtzcWtqbCk6CiAgICBwYXNzCg=='

    def test_diversity_8(self):
        return 'IyBmbXQ6IG9mZgp3dm5kID0gWzAsICAgNF0KIyBmbXQ6IG9uCg=='

    def test_diversity_9(self):
        return 'ZGVmIGt0eWcoKToKICAgIHJldHVybiAxMTYK'

    def test_diversity_10(self):
        return 'aW1wb3J0IGt3b21nZmVjCgoKZGVmIHplanMoZ3hydm5qYmUpOgogICAgcGFzcwo='
