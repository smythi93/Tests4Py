import contextlib
import io
import json
import sys
import tempfile
from unittest import mock

import ansible.cli.galaxy
from ansible.cli.galaxy import GalaxyCLI
from ansible.utils import context_objects as co

if __name__ == "__main__":
    # argv: mode collection_input   (mode = url | name)
    mode = sys.argv[1]
    collection_input = sys.argv[2]

    co.GlobalCLIArgs._Singleton__instance = None
    output_dir = tempfile.mkdtemp()
    captured = {}

    def fake_install(requirements, *a, **kw):
        captured["requirements"] = requirements

    with mock.patch.object(
        ansible.cli.galaxy, "install_collections", side_effect=fake_install
    ):
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                GalaxyCLI(
                    args=[
                        "ansible-galaxy",
                        "collection",
                        "install",
                        collection_input,
                        "--collections-path",
                        output_dir,
                    ]
                ).run()
        except SystemExit:
            pass

    print(json.dumps(captured.get("requirements")))
