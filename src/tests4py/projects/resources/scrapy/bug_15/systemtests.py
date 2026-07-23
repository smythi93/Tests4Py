from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'aHR0cDovL3d3dy54b25td3FxcXZxdmR6YnVrdXl2a2h5cXdmd2l5Y3dweHlqcm1hYnpzcmt4d2p4ZXZscHVmY2JhcWRtaW1jdWtjamMuY29tL2huL2JxeGJsL3Jn'

    def test_diversity_2(self):
        return 'aHR0cDovL3d3dy50eWJkbWh1dWpvbmFrbnRkYmZoZ25qdHViamhvY2t1a2tyZWJncnd4em9reHRraXVvaWZwb2VhdXRmeWhwcWlya2J6LmNvbS9leGt1bC9kc3Ryd3UvZ2Z3c3dq'

    def test_diversity_3(self):
        return 'aHR0cDovLy5zbXpyZS5jb20vaHI='

    def test_diversity_4(self):
        return 'aHR0cDovLy50dmdlLmNvbS9xZnls'

    def test_diversity_5(self):
        return 'aHR0cDovL3d3dy52cHB4YWh5bGlpcm1pcnVvanZuZHNnY3FzdnZidHBocG11bmlxdnZ3aWNvaWhvZHRhd3Nicm5lcnJsdWRndHl4anptanFlbWRrYnZyemtjYXZpYi5jb20vdnJrZXluL2Fybw=='

    def test_diversity_6(self):
        return 'aHR0cDovL3d3dy5ybW56aXBqY2xhZmF2dnBzcnNiZmNvZmRpcmFya293YWNtYWZ6ZGxtbHlncHVhamJ1a2J6aWV6ZG5oZmljZHlva210a3d0YS5jb20vZmJjeWI='

    def test_diversity_7(self):
        return 'aHR0cDovLy5vdmRjY3BpbS5jb20vdGIva3pmdmwva2t1'

    def test_diversity_8(self):
        return 'aHR0cDovLy5pZXZvLmNvbS9mcw=='

    def test_diversity_9(self):
        return 'aHR0cDovLy5paHguY29tL3BjaGEvYm9rL3dj'

    def test_diversity_10(self):
        return 'aHR0cDovL3d3dy5kbGNiaHh2dmF5bnV4enNnb2Vqa21iZ2xmdHlsZ250ZHV1c3dsb3FrbGtkYW5wbmtncWRvb2lwamtuenN1d2NucHB6ZXppbWZxbHJoa2guY29tL2NtYWhqL2lvbC9jaQ=='


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'aHR0cDovL3h3by5uZXQvdWtsYno='

    def test_diversity_2(self):
        return 'aHR0cDovL3Z4ZHYub3JnL3FiL3lobnVtei9nZg=='

    def test_diversity_3(self):
        return 'aHR0cDovL25lYi5jb20va3pxaGNoL21mdHU='

    def test_diversity_4(self):
        return 'aHR0cDovL2p6Yi5jb20vdmZobA=='

    def test_diversity_5(self):
        return 'aHR0cDovL2JtZS5pby91cG54L2lhZQ=='

    def test_diversity_6(self):
        return 'aHR0cDovL3hqbWljanRzLmNvbS9oY2hia2sveWtoL3pucmJv'

    def test_diversity_7(self):
        return 'aHR0cDovL25jZ3F6Lm5ldC9qZXh4dnovaHE='

    def test_diversity_8(self):
        return 'aHR0cDovL3Nzb2UuY29tL3BsYWZ2L3B0dHhxL3JuaXlpbQ=='

    def test_diversity_9(self):
        return 'aHR0cDovL2JtaXRzdW0uaW8vbWE='

    def test_diversity_10(self):
        return 'aHR0cDovL3d0anV6Lm9yZy9saA=='
