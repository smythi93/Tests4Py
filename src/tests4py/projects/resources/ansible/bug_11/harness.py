import sys
from types import SimpleNamespace

from ansible.modules.network.ios.ios_banner import map_obj_to_commands


def build_text(mode, word):
    if mode == "pad":
        return "  " + word + "  "
    if mode == "nl":
        return "\n" + word + "\n"
    return word


if __name__ == "__main__":
    mode = sys.argv[1]
    word = sys.argv[2]
    text = build_text(mode, word)
    module = SimpleNamespace(params={"state": "present", "banner": "login"})
    cmds = map_obj_to_commands(({"text": text}, {"text": None}), module)
    print(cmds[0] if cmds else "NONE")
