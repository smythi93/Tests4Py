import json
import sys
from io import StringIO
from unittest import mock

from ansible import context
from ansible.galaxy import api as galaxy_api
from ansible.galaxy.api import GalaxyAPI
from ansible.galaxy.token import GalaxyToken

if __name__ == "__main__":
    # argv: mode host role_id   (mode = page | single)
    mode = sys.argv[1]
    host = sys.argv[2]
    role_id = int(sys.argv[3])

    context.CLIARGS._store = {"ignore_certs": False}

    server = "https://%s/api/" % host
    api = GalaxyAPI(None, "test", server)
    api._available_api_versions = {"v1": "v1"}
    api.token = GalaxyToken("my token")

    next_link = "/api/v1/roles/%d/versions/?page=2&page_size=50" % role_id
    if mode == "page":
        responses = [
            {"count": 2, "results": [{"name": "3.5.1"}], "next_link": next_link,
             "next": None, "previous_link": None, "previous": None},
            {"count": 2, "results": [{"name": "3.5.2"}], "next_link": None,
             "next": None, "previous_link": None, "previous": None},
        ]
    else:
        responses = [
            {"count": 1, "results": [{"name": "3.5.1"}], "next_link": None,
             "next": None, "previous_link": None, "previous": None},
        ]

    mock_open = mock.MagicMock()
    mock_open.side_effect = [StringIO(json.dumps(r)) for r in responses]
    with mock.patch.object(galaxy_api, "open_url", mock_open):
        api.fetch_role_related("versions", role_id)

    urls = [c[0][0] for c in mock_open.call_args_list]
    print(urls[-1] if urls else "NOCALL")
