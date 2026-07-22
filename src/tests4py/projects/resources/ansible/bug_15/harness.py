import sys

from ansible.modules.network.eos.eos_eapi import map_obj_to_commands

KEYS = [
    "http",
    "http_port",
    "https",
    "https_port",
    "local_http",
    "local_http_port",
    "socket",
]


def val(x):
    return None if x == "none" else x


if __name__ == "__main__":
    ws, wv, hs, hv = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    want = {k: None for k in KEYS}
    want["state"], want["vrf"] = val(ws), val(wv)
    have = {k: None for k in KEYS}
    have["state"], have["vrf"] = val(hs), val(hv)
    commands = map_obj_to_commands((want, have), None, [])
    print("|".join(commands))
