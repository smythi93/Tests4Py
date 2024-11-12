import unittest
import os
from six.moves.urllib.parse import urljoin
from six.moves.urllib.request import pathname2url
from keras.utils.data_utils import get_file
from six.moves import reload_module
from keras import backend as K


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.KjFDTMUH.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_2(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.qxuSb.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_3(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.YfUcDhyQFr.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_4(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.JfkjGL.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_5(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.FNvBaIQtxgmvsz.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_6(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.oNmuzIcfm.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_7(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.OjzlZBzdcdi.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_8(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.vQKRnUDFjZe.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_9(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.HXSYBhM.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_10(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        _keras_home = os.path.join(os.path.abspath('.'), '.keras')
        if not os.path.exists(_keras_home):
            os.makedirs(_keras_home)
        os.environ['KERAS_HOME'] = _keras_home
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.JzyMxEKBxegO.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.YyxByaNaEZM.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_2(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.LIAifQMHPI.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_3(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.hLgGWseVQJnK.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_4(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.GQeKoGbzifem.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_5(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.cRdBKBvHD.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_6(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.MpRqUMUElB.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_7(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.dxmosJ.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_8(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.iPONfkHwWn.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_9(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.LVmLEIHRt.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)

    def test_diversity_10(self):
        original_keras_home = os.environ.get('KERAS_HOME')
        if 'KERAS_HOME' in os.environ:
            del os.environ['KERAS_HOME']
        reload_module(K)
        dirname = 'data_utils'
        origin = urljoin('file://', pathname2url(os.path.abspath('test.eROfPp.gz')))
        path = get_file(dirname, origin, untar=True)
        filepath = path + '.tar.gz'
        data_keras_home = os.path.dirname(os.path.dirname(os.path.abspath(filepath)))
        assert data_keras_home == os.path.dirname(K._config_path)
        if original_keras_home is not None:
            os.environ['KERAS_HOME'] = original_keras_home
        else:
            os.environ.pop('KERAS_HOME', None)
        reload_module(K)
