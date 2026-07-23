import unittest


def _t4p_stack_state_size(u1, u2):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    from keras.layers import recurrent

    layer = recurrent.RNN([recurrent.LSTMCell(u1), recurrent.LSTMCell(u2)])
    return str(tuple(layer.cell.state_size))


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('(3, 3, 6, 6)', _t4p_stack_state_size(3, 6))

    def test_diversity_2(self):
        self.assertEqual('(2, 2, 5, 5)', _t4p_stack_state_size(2, 5))

    def test_diversity_3(self):
        self.assertEqual('(6, 6, 3, 3)', _t4p_stack_state_size(6, 3))

    def test_diversity_4(self):
        self.assertEqual('(4, 4, 8, 8)', _t4p_stack_state_size(4, 8))

    def test_diversity_5(self):
        self.assertEqual('(5, 5, 2, 2)', _t4p_stack_state_size(5, 2))

    def test_diversity_6(self):
        self.assertEqual('(8, 8, 4, 4)', _t4p_stack_state_size(8, 4))

    def test_diversity_7(self):
        self.assertEqual('(3, 3, 7, 7)', _t4p_stack_state_size(3, 7))

    def test_diversity_8(self):
        self.assertEqual('(7, 7, 3, 3)', _t4p_stack_state_size(7, 3))

    def test_diversity_9(self):
        self.assertEqual('(2, 2, 8, 8)', _t4p_stack_state_size(2, 8))

    def test_diversity_10(self):
        self.assertEqual('(6, 6, 5, 5)', _t4p_stack_state_size(6, 5))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('(2, 2, 2, 2)', _t4p_stack_state_size(2, 2))

    def test_diversity_2(self):
        self.assertEqual('(3, 3, 3, 3)', _t4p_stack_state_size(3, 3))

    def test_diversity_3(self):
        self.assertEqual('(4, 4, 4, 4)', _t4p_stack_state_size(4, 4))

    def test_diversity_4(self):
        self.assertEqual('(5, 5, 5, 5)', _t4p_stack_state_size(5, 5))

    def test_diversity_5(self):
        self.assertEqual('(6, 6, 6, 6)', _t4p_stack_state_size(6, 6))

    def test_diversity_6(self):
        self.assertEqual('(7, 7, 7, 7)', _t4p_stack_state_size(7, 7))

    def test_diversity_7(self):
        self.assertEqual('(8, 8, 8, 8)', _t4p_stack_state_size(8, 8))

    def test_diversity_8(self):
        self.assertEqual('(9, 9, 9, 9)', _t4p_stack_state_size(9, 9))

    def test_diversity_9(self):
        self.assertEqual('(10, 10, 10, 10)', _t4p_stack_state_size(10, 10))

    def test_diversity_10(self):
        self.assertEqual('(11, 11, 11, 11)', _t4p_stack_state_size(11, 11))
