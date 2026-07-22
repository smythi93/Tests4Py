import sys

from ansible.module_utils.facts.system.distribution import DistributionFiles

if __name__ == "__main__":
    distro = sys.argv[1]
    path_kind = sys.argv[2]
    version = sys.argv[3]
    if distro == "kali":
        data = 'NAME="Kali GNU/Linux Rolling" VERSION="%s"' % version
    elif distro == "ubuntu":
        data = 'NAME="Ubuntu" VERSION="%s"' % version
    else:
        data = 'NAME="SteamOS" VERSION="%s"' % version
    path = "/etc/os-release" if path_kind == "os" else "/etc/lsb-release"
    df = DistributionFiles(module=None)
    matched, facts = df.parse_distribution_file_Debian(
        distro, data, path, {"distribution_release": "NA"}
    )
    print("%s %s" % (matched, facts.get("distribution")))
