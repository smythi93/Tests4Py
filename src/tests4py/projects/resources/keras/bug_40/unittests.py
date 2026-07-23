import unittest


def _t4p_stacked_output_shape(u1, u2, ts, emb, rs):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    from keras.layers import recurrent

    cells = [recurrent.LSTMCell(u1), recurrent.LSTMCell(u2)]
    layer = recurrent.RNN(
        cells, return_state=True, return_sequences=(rs == "seq")
    )
    return str(layer.compute_output_shape((None, ts, emb)))


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('[(None, 5, 6), (None, 6), (None, 6), (None, 3), (None, 3)]',
                         _t4p_stacked_output_shape(3, 6, 5, 7, 'seq'))

    def test_diversity_2(self):
        self.assertEqual('[(None, 4, 5), (None, 5), (None, 5), (None, 2), (None, 2)]',
                         _t4p_stacked_output_shape(2, 5, 4, 3, 'seq'))

    def test_diversity_3(self):
        self.assertEqual('[(None, 3), (None, 3), (None, 3), (None, 6), (None, 6)]',
                         _t4p_stacked_output_shape(6, 3, 7, 4, 'last'))

    def test_diversity_4(self):
        self.assertEqual('[(None, 3, 8), (None, 8), (None, 8), (None, 4), (None, 4)]',
                         _t4p_stacked_output_shape(4, 8, 3, 5, 'seq'))

    def test_diversity_5(self):
        self.assertEqual('[(None, 2), (None, 2), (None, 2), (None, 5), (None, 5)]',
                         _t4p_stacked_output_shape(5, 2, 6, 6, 'last'))

    def test_diversity_6(self):
        self.assertEqual('[(None, 2, 4), (None, 4), (None, 4), (None, 8), (None, 8)]',
                         _t4p_stacked_output_shape(8, 4, 2, 8, 'seq'))

    def test_diversity_7(self):
        self.assertEqual('[(None, 7), (None, 7), (None, 7), (None, 3), (None, 3)]',
                         _t4p_stacked_output_shape(3, 7, 5, 5, 'last'))

    def test_diversity_8(self):
        self.assertEqual('[(None, 4, 3), (None, 3), (None, 3), (None, 7), (None, 7)]',
                         _t4p_stacked_output_shape(7, 3, 4, 2, 'seq'))

    def test_diversity_9(self):
        self.assertEqual('[(None, 8), (None, 8), (None, 8), (None, 2), (None, 2)]',
                         _t4p_stacked_output_shape(2, 8, 8, 3, 'last'))

    def test_diversity_10(self):
        self.assertEqual('[(None, 3, 5), (None, 5), (None, 5), (None, 6), (None, 6)]',
                         _t4p_stacked_output_shape(6, 5, 3, 6, 'seq'))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual('[(None, 5, 4), (None, 4), (None, 4), (None, 4), (None, 4)]',
                         _t4p_stacked_output_shape(4, 4, 5, 7, 'seq'))

    def test_diversity_2(self):
        self.assertEqual('[(None, 4, 3), (None, 3), (None, 3), (None, 3), (None, 3)]',
                         _t4p_stacked_output_shape(3, 3, 4, 3, 'seq'))

    def test_diversity_3(self):
        self.assertEqual('[(None, 5), (None, 5), (None, 5), (None, 5), (None, 5)]',
                         _t4p_stacked_output_shape(5, 5, 7, 4, 'last'))

    def test_diversity_4(self):
        self.assertEqual('[(None, 3, 6), (None, 6), (None, 6), (None, 6), (None, 6)]',
                         _t4p_stacked_output_shape(6, 6, 3, 5, 'seq'))

    def test_diversity_5(self):
        self.assertEqual('[(None, 2), (None, 2), (None, 2), (None, 2), (None, 2)]',
                         _t4p_stacked_output_shape(2, 2, 6, 6, 'last'))

    def test_diversity_6(self):
        self.assertEqual('[(None, 2, 7), (None, 7), (None, 7), (None, 7), (None, 7)]',
                         _t4p_stacked_output_shape(7, 7, 2, 8, 'seq'))

    def test_diversity_7(self):
        self.assertEqual('[(None, 8), (None, 8), (None, 8), (None, 8), (None, 8)]',
                         _t4p_stacked_output_shape(8, 8, 5, 5, 'last'))

    def test_diversity_8(self):
        self.assertEqual('[(None, 4, 3), (None, 3), (None, 3), (None, 3), (None, 3)]',
                         _t4p_stacked_output_shape(3, 3, 4, 2, 'seq'))

    def test_diversity_9(self):
        self.assertEqual('[(None, 4), (None, 4), (None, 4), (None, 4), (None, 4)]',
                         _t4p_stacked_output_shape(4, 4, 8, 3, 'last'))

    def test_diversity_10(self):
        self.assertEqual('[(None, 3, 5), (None, 5), (None, 5), (None, 5), (None, 5)]',
                         _t4p_stacked_output_shape(5, 5, 3, 6, 'seq'))
