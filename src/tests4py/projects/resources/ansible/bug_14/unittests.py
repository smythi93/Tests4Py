import unittest



class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'gvxu', 5655)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://gvxu/api/v1/roles/5655/versions/?page=2&page_size=50', actual)

    def test_diversity_2(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'saly.io', 694)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://saly.io/api/v1/roles/694/versions/?page=2&page_size=50', actual)

    def test_diversity_3(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'tndlpzel.com', 8237)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://tndlpzel.com/api/v1/roles/8237/versions/?page=2&page_size=50', actual)

    def test_diversity_4(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'ajzcjzp.io', 8130)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://ajzcjzp.io/api/v1/roles/8130/versions/?page=2&page_size=50', actual)

    def test_diversity_5(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'bwdogar.org', 3714)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://bwdogar.org/api/v1/roles/3714/versions/?page=2&page_size=50', actual)

    def test_diversity_6(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'inczyd.org', 4417)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://inczyd.org/api/v1/roles/4417/versions/?page=2&page_size=50', actual)

    def test_diversity_7(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'eqiqeu.com', 8037)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://eqiqeu.com/api/v1/roles/8037/versions/?page=2&page_size=50', actual)

    def test_diversity_8(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'scllkegp.org', 6482)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://scllkegp.org/api/v1/roles/6482/versions/?page=2&page_size=50', actual)

    def test_diversity_9(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'jdpnazg.com', 7286)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://jdpnazg.com/api/v1/roles/7286/versions/?page=2&page_size=50', actual)

    def test_diversity_10(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('page', 'druocbj.com', 2523)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://druocbj.com/api/v1/roles/2523/versions/?page=2&page_size=50', actual)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'lsot.io', 378)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://lsot.io/api/v1/roles/378/versions/?page_size=50', actual)

    def test_diversity_2(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'gceb.org', 3063)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://gceb.org/api/v1/roles/3063/versions/?page_size=50', actual)

    def test_diversity_3(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'qfpjwln', 2361)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://qfpjwln/api/v1/roles/2361/versions/?page_size=50', actual)

    def test_diversity_4(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'byyh.com', 7293)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://byyh.com/api/v1/roles/7293/versions/?page_size=50', actual)

    def test_diversity_5(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'nwnagtrf.com', 8349)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://nwnagtrf.com/api/v1/roles/8349/versions/?page_size=50', actual)

    def test_diversity_6(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'kutj.io', 8743)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://kutj.io/api/v1/roles/8743/versions/?page_size=50', actual)

    def test_diversity_7(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'ktalje', 4998)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://ktalje/api/v1/roles/4998/versions/?page_size=50', actual)

    def test_diversity_8(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'ptmagjxb.com', 1171)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://ptmagjxb.com/api/v1/roles/1171/versions/?page_size=50', actual)

    def test_diversity_9(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'zlysn', 9947)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://zlysn/api/v1/roles/9947/versions/?page_size=50', actual)

    def test_diversity_10(self):
        import json
        from io import StringIO
        from unittest import mock
        from ansible import context
        from ansible.galaxy import api as galaxy_api
        from ansible.galaxy.api import GalaxyAPI
        from ansible.galaxy.token import GalaxyToken
        mode, host, role_id = ('single', 'ajycf.org', 7212)
        context.CLIARGS._store = {'ignore_certs': False}
        api = GalaxyAPI(None, 'test', 'https://%s/api/' % host)
        api._available_api_versions = {'v1': 'v1'}
        api.token = GalaxyToken('my token')
        next_link = '/api/v1/roles/%d/versions/?page=2&page_size=50' % role_id
        if mode == 'page':
            responses = [{'count': 2, 'results': [{'name': '3.5.1'}], 'next_link': next_link, 'next': None, 'previous_link': None, 'previous': None}, {'count': 2, 'results': [{'name': '3.5.2'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        else:
            responses = [{'count': 1, 'results': [{'name': '3.5.1'}], 'next_link': None, 'next': None, 'previous_link': None, 'previous': None}]
        mock_open = mock.MagicMock()
        mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
        with mock.patch.object(galaxy_api, 'open_url', mock_open):
            api.fetch_role_related('versions', role_id)
        urls = [c[0][0] for c in mock_open.call_args_list]
        actual = urls[-1] if urls else 'NOCALL'
        self.assertEqual('https://ajycf.org/api/v1/roles/7212/versions/?page_size=50', actual)
