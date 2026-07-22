import sys
from unittest import mock

from ansible.module_utils.facts.hardware import linux


def build_cpuinfo(arch, n):
    lines = []
    if arch.startswith(("ppc", "powerpc")):
        for k in range(n):
            lines.append("processor : %d" % k)
            lines.append("cpu : POWER8 (architected), altivec supported")
        lines.append("timebase : 512000000")
    else:
        for k in range(n):
            lines.append("processor : %d" % k)
            lines.append("vendor_id : GenuineIntel")
            lines.append("model name : Intel(R) Xeon(R) CPU")
    return lines


if __name__ == "__main__":
    arch = sys.argv[1]
    n = int(sys.argv[2])
    inst = linux.LinuxHardware(mock.Mock())
    cpuinfo = build_cpuinfo(arch, n)
    with mock.patch("os.path.exists", return_value=False), mock.patch(
        "os.access", return_value=True
    ), mock.patch(
        "ansible.module_utils.facts.hardware.linux.get_file_lines",
        side_effect=[[], cpuinfo],
    ):
        facts = inst.get_cpu_facts(collected_facts={"ansible_architecture": arch})
    print(facts.get("processor_count"))
