import unittest
from keras.layers import recurrent


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(1082), recurrent.LSTMCell(8719)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 8719), (None, 1082), (None, 1082), (None, 8719), (None, 8719)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 8719), (None, 8719), (None, 8719), (None, 1082), (None, 1082)]
        assert output_shape == expected_output_shape

    def test_diversity_2(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(5250), recurrent.LSTMCell(9762)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9762), (None, 5250), (None, 5250), (None, 9762), (None, 9762)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9762), (None, 9762), (None, 9762), (None, 5250), (None, 5250)]
        assert output_shape == expected_output_shape

    def test_diversity_3(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(3400), recurrent.LSTMCell(3236)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 3236), (None, 3400), (None, 3400), (None, 3236), (None, 3236)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 3236), (None, 3236), (None, 3236), (None, 3400), (None, 3400)]
        assert output_shape == expected_output_shape

    def test_diversity_4(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(2103), recurrent.LSTMCell(9347)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9347), (None, 2103), (None, 2103), (None, 9347), (None, 9347)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9347), (None, 9347), (None, 9347), (None, 2103), (None, 2103)]
        assert output_shape == expected_output_shape

    def test_diversity_5(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(8495), recurrent.LSTMCell(9505)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9505), (None, 8495), (None, 8495), (None, 9505), (None, 9505)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9505), (None, 9505), (None, 9505), (None, 8495), (None, 8495)]
        assert output_shape == expected_output_shape

    def test_diversity_6(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(288), recurrent.LSTMCell(6206)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 6206), (None, 288), (None, 288), (None, 6206), (None, 6206)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 6206), (None, 6206), (None, 6206), (None, 288), (None, 288)]
        assert output_shape == expected_output_shape

    def test_diversity_7(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(4479), recurrent.LSTMCell(53)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 53), (None, 4479), (None, 4479), (None, 53), (None, 53)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 53), (None, 53), (None, 53), (None, 4479), (None, 4479)]
        assert output_shape == expected_output_shape

    def test_diversity_8(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(6454), recurrent.LSTMCell(9440)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9440), (None, 6454), (None, 6454), (None, 9440), (None, 9440)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9440), (None, 9440), (None, 9440), (None, 6454), (None, 6454)]
        assert output_shape == expected_output_shape

    def test_diversity_9(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(841), recurrent.LSTMCell(2365)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 2365), (None, 841), (None, 841), (None, 2365), (None, 2365)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 2365), (None, 2365), (None, 2365), (None, 841), (None, 841)]
        assert output_shape == expected_output_shape

    def test_diversity_10(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(2876), recurrent.LSTMCell(7768)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 7768), (None, 2876), (None, 2876), (None, 7768), (None, 7768)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells, reverse_state_order=True)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 7768), (None, 7768), (None, 7768), (None, 2876), (None, 2876)]
        assert output_shape == expected_output_shape


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(4896), recurrent.LSTMCell(9115)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9115), (None, 9115), (None, 9115), (None, 4896), (None, 4896)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9115), (None, 9115), (None, 9115), (None, 4896), (None, 4896)]
        assert output_shape == expected_output_shape

    def test_diversity_2(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(392), recurrent.LSTMCell(6645)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 6645), (None, 6645), (None, 6645), (None, 392), (None, 392)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 6645), (None, 6645), (None, 6645), (None, 392), (None, 392)]
        assert output_shape == expected_output_shape

    def test_diversity_3(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(3967), recurrent.LSTMCell(5711)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 5711), (None, 5711), (None, 5711), (None, 3967), (None, 3967)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 5711), (None, 5711), (None, 5711), (None, 3967), (None, 3967)]
        assert output_shape == expected_output_shape

    def test_diversity_4(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(4073), recurrent.LSTMCell(6475)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 6475), (None, 6475), (None, 6475), (None, 4073), (None, 4073)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 6475), (None, 6475), (None, 6475), (None, 4073), (None, 4073)]
        assert output_shape == expected_output_shape

    def test_diversity_5(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(2339), recurrent.LSTMCell(1906)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 1906), (None, 1906), (None, 1906), (None, 2339), (None, 2339)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 1906), (None, 1906), (None, 1906), (None, 2339), (None, 2339)]
        assert output_shape == expected_output_shape

    def test_diversity_6(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(2539), recurrent.LSTMCell(3837)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 3837), (None, 3837), (None, 3837), (None, 2539), (None, 2539)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 3837), (None, 3837), (None, 3837), (None, 2539), (None, 2539)]
        assert output_shape == expected_output_shape

    def test_diversity_7(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(1858), recurrent.LSTMCell(9102)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9102), (None, 9102), (None, 9102), (None, 1858), (None, 1858)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 9102), (None, 9102), (None, 9102), (None, 1858), (None, 1858)]
        assert output_shape == expected_output_shape

    def test_diversity_8(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(9957), recurrent.LSTMCell(5871)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 5871), (None, 5871), (None, 5871), (None, 9957), (None, 9957)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 5871), (None, 5871), (None, 5871), (None, 9957), (None, 9957)]
        assert output_shape == expected_output_shape

    def test_diversity_9(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(6954), recurrent.LSTMCell(1240)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 1240), (None, 1240), (None, 1240), (None, 6954), (None, 6954)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 1240), (None, 1240), (None, 1240), (None, 6954), (None, 6954)]
        assert output_shape == expected_output_shape

    def test_diversity_10(self):
        num_samples, timesteps, embedding_dim, units = (2, 5, 4, 3)
        cells = [recurrent.LSTMCell(9663), recurrent.LSTMCell(3281)]
        layer = recurrent.RNN(cells, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 3281), (None, 3281), (None, 3281), (None, 9663), (None, 9663)]
        assert output_shape == expected_output_shape
        stacked_cell = recurrent.StackedRNNCells(cells)
        layer = recurrent.RNN(stacked_cell, return_state=True, return_sequences=True)
        output_shape = layer.compute_output_shape((None, timesteps, embedding_dim))
        expected_output_shape = [(None, timesteps, 3281), (None, 3281), (None, 3281), (None, 9663), (None, 9663)]
        assert output_shape == expected_output_shape
