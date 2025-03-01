import unittest
from tensorflow.core.protobuf import config_pb2
from keras import backend as K


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([1898, 1281])
        assert output == [3179]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([1898, 1281])
        assert output == [3179]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_2(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([2234, 2488])
        assert output == [4722]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([2234, 2488])
        assert output == [4722]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_3(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([1215, 1065])
        assert output == [2280]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([1215, 1065])
        assert output == [2280]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_4(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([582, 1398])
        assert output == [1980]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([582, 1398])
        assert output == [1980]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_5(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([1125, 3045])
        assert output == [4170]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([1125, 3045])
        assert output == [4170]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_6(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([3319, 3606])
        assert output == [6925]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([3319, 3606])
        assert output == [6925]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_7(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([4294, 343])
        assert output == [4637]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([4294, 343])
        assert output == [4637]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_8(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([1610, 272])
        assert output == [1882]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([1610, 272])
        assert output == [1882]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_9(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([2829, 2574])
        assert output == [5403]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([2829, 2574])
        assert output == [5403]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_10(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       options=run_options, run_metadata=run_metadata)
        output = f([2967, 4844])
        assert output == [7811]
        assert len(run_metadata.partition_graphs) > 2
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder],
                       run_metadata=run_metadata)
        output = f([2967, 4844])
        assert output == [7811]
        assert len(run_metadata.partition_graphs) == 0


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([4658, 4318])
        assert output == [8976]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([4658, 4318])
        assert output == [8976]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_2(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([1724, 1757])
        assert output == [3481]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([1724, 1757])
        assert output == [3481]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_3(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([4533, 3731])
        assert output == [8264]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([4533, 3731])
        assert output == [8264]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_4(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([3532, 1332])
        assert output == [4864]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([3532, 1332])
        assert output == [4864]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_5(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([2389, 2901])
        assert output == [5290]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([2389, 2901])
        assert output == [5290]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_6(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([1984, 2328])
        assert output == [4312]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([1984, 2328])
        assert output == [4312]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_7(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([2740, 3567])
        assert output == [6307]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([2740, 3567])
        assert output == [6307]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_8(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([3112, 3247])
        assert output == [6359]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([3112, 3247])
        assert output == [6359]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_9(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([1625, 4033])
        assert output == [5658]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([1625, 4033])
        assert output == [5658]
        assert len(run_metadata.partition_graphs) == 0

    def test_diversity_10(self):
        x_placeholder = K.placeholder(shape=())
        y_placeholder = K.placeholder(shape=())
        run_metadata = config_pb2.RunMetadata()
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([2471, 20])
        assert output == [2491]
        assert len(run_metadata.partition_graphs) == 0
        f = K.function(inputs=[x_placeholder, y_placeholder], outputs=[x_placeholder + y_placeholder])
        output = f([2471, 20])
        assert output == [2491]
        assert len(run_metadata.partition_graphs) == 0
