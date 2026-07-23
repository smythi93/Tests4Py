import sys
from unittest import mock

from ansible.module_utils.facts.hardware import linux

if __name__ == "__main__":
    mode = sys.argv[1]
    name1 = sys.argv[2]
    name2 = sys.argv[3]
    if mode == "esc":
        mount_raw = "/mnt/" + name1 + chr(92) + "040" + name2
    else:
        mount_raw = "/mnt/" + name1 + name2
    entries = [["/dev/sdz", mount_raw, "ext4", "rw,relatime", "0", "0"]]
    lh = linux.LinuxHardware(module=mock.Mock(), load_on_init=False)
    with mock.patch.object(
        linux.LinuxHardware, "_mtab_entries", return_value=entries
    ), mock.patch.object(
        linux.LinuxHardware, "_find_bind_mounts", return_value=[]
    ), mock.patch.object(
        linux.LinuxHardware, "_lsblk_uuid", return_value={}
    ), mock.patch.object(
        linux.LinuxHardware, "_udevadm_uuid", return_value=""
    ):
        result = lh.get_mount_facts()
    mounts = result["mounts"]
    print(mounts[0]["mount"] if mounts else "NO_MOUNT")
