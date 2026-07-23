import contextlib
import io
import json
import sys
from unittest import mock

from ansible.module_utils import basic
from ansible.module_utils._text import to_bytes
from ansible.modules.packaging.os import redhat_subscription


def set_module_args(args):
    basic._ANSIBLE_ARGS = to_bytes(json.dumps({"ANSIBLE_MODULE_ARGS": args}))


if __name__ == "__main__":
    # argv: mode poolid [quantity]
    mode = sys.argv[1]
    poolid = sys.argv[2]
    quantity = sys.argv[3] if len(sys.argv) > 3 else None

    if mode == "withq":
        pool_ids = [{poolid: int(quantity)}]
    else:
        pool_ids = [poolid]

    set_module_args(
        {
            "state": "present",
            "username": "admin",
            "password": "admin",
            "org_id": "admin",
            "pool_ids": pool_ids,
        }
    )

    available = "\n".join(
        [
            "+-------------------------------------------+",
            "    Available Subscriptions",
            "+-------------------------------------------+",
            "",
            "Subscription Name:   SP Server",
            "Pool ID:             %s" % poolid,
            "Available:           5",
            "",
        ]
    )

    calls = []

    def fake_run_command(args, *a, **kw):
        calls.append(args)
        joined = " ".join(args) if isinstance(args, (list, tuple)) else args
        if "identity" in joined:
            return (1, "This system is not yet registered.", "")
        if "list" in joined and "--available" in joined:
            return (0, available, "")
        return (0, "", "")

    with mock.patch.object(
        redhat_subscription.RegistrationBase, "REDHAT_REPO", create=True
    ), mock.patch.object(
        redhat_subscription, "isfile", return_value=False
    ), mock.patch.object(
        redhat_subscription, "unlink", return_value=True
    ), mock.patch.object(
        basic.AnsibleModule, "get_bin_path", return_value="/testbin/subscription-manager"
    ), mock.patch.object(
        basic.AnsibleModule, "run_command", side_effect=fake_run_command
    ):
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                redhat_subscription.main()
        except SystemExit:
            pass

    attach = None
    for c in calls:
        if isinstance(c, (list, tuple)) and "attach" in c and "--pool" in c:
            attach = list(c)
            break
    print(json.dumps(attach))
