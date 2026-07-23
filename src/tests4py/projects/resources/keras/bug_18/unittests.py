import unittest


def _t4p_function_runs(mode, a, b):
    import os

    os.environ.setdefault("KERAS_BACKEND", "tensorflow")
    import keras.backend as K

    K.clear_session()
    try:
        from tensorflow.core.protobuf import config_pb2

        x = K.placeholder(shape=())
        y = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        kwargs = {}
        if mode == "withmeta":
            kwargs["options"] = config_pb2.RunOptions(output_partition_graphs=True)
            kwargs["run_metadata"] = run_metadata
        f = K.function(inputs=[x, y], outputs=[x + y], **kwargs)
        out = f([float(a), float(b)])
        ok = abs(float(out[0]) - (a + b)) < 1e-4
        if mode == "withmeta":
            ok = ok and len(run_metadata.partition_graphs) > 0
        return ok
    except Exception:
        return False


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_function_runs('withmeta', 10, 20))

    def test_diversity_2(self):
        self.assertTrue(_t4p_function_runs('withmeta', 3, 4))

    def test_diversity_3(self):
        self.assertTrue(_t4p_function_runs('withmeta', 100, 1))

    def test_diversity_4(self):
        self.assertTrue(_t4p_function_runs('withmeta', 7, 8))

    def test_diversity_5(self):
        self.assertTrue(_t4p_function_runs('withmeta', 50, 50))

    def test_diversity_6(self):
        self.assertTrue(_t4p_function_runs('withmeta', 2, 9))

    def test_diversity_7(self):
        self.assertTrue(_t4p_function_runs('withmeta', 15, 5))

    def test_diversity_8(self):
        self.assertTrue(_t4p_function_runs('withmeta', 33, 11))

    def test_diversity_9(self):
        self.assertTrue(_t4p_function_runs('withmeta', 6, 6))

    def test_diversity_10(self):
        self.assertTrue(_t4p_function_runs('withmeta', 21, 4))


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertTrue(_t4p_function_runs('plain', 10, 20))

    def test_diversity_2(self):
        self.assertTrue(_t4p_function_runs('plain', 3, 4))

    def test_diversity_3(self):
        self.assertTrue(_t4p_function_runs('plain', 100, 1))

    def test_diversity_4(self):
        self.assertTrue(_t4p_function_runs('plain', 7, 8))

    def test_diversity_5(self):
        self.assertTrue(_t4p_function_runs('plain', 50, 50))

    def test_diversity_6(self):
        self.assertTrue(_t4p_function_runs('plain', 2, 9))

    def test_diversity_7(self):
        self.assertTrue(_t4p_function_runs('plain', 15, 5))

    def test_diversity_8(self):
        self.assertTrue(_t4p_function_runs('plain', 33, 11))

    def test_diversity_9(self):
        self.assertTrue(_t4p_function_runs('plain', 6, 6))

    def test_diversity_10(self):
        self.assertTrue(_t4p_function_runs('plain', 21, 4))
