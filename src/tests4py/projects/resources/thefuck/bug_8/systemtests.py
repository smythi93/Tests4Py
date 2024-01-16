from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):

    def test_diversity_1(self):
        return "dnf upgrade '@Web Server', No such command"

    def test_diversity_2(self):
        return 'dnf downgrade gimp, No such command'

    def test_diversity_3(self):
        return 'dnf needs-restarting firefox, No such command'

    def test_diversity_4(self):
        return 'dnf install vlc, No such command'

    def test_diversity_5(self):
        return 'dnf debuginfo-install nginx, No such command'

    def test_diversity_6(self):
        return "dnf help '@Web Server', No such command"

    def test_diversity_7(self):
        return 'dnf repomanage git, No such command'

    def test_diversity_8(self):
        return 'dnf repomanage tito, No such command'

    def test_diversity_9(self):
        return 'dnf downgrade tito, No such command'

    def test_diversity_10(self):
        return 'dnf list git, No such command'


class TestsPassing(PassingSystemtests):

    def test_diversity_1(self):
        return 'dnf cheeck httpd, No such command: cheeck. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install "dnf-command check" \n'

    def test_diversity_2(self):
        return 'dnf instaall firefox, No such command: instaall. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install "dnf-command install" \n'

    def test_diversity_3(self):
        return 'dnf upgrade-minimale vlc, No such command: upgrade-minimale. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install "dnf-command upgrade-minimal" \n'

    def test_diversity_4(self):
        return 'dnf repooquery nano, No such command: repooquery. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install "dnf-command repoquery" \n'

    def test_diversity_5(self):
        return 'dnf upgrade-minimale httpd, No such command: upgrade-minimale. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install "dnf-command upgrade-minimal" \n'

    def test_diversity_6(self):
        return 'dnf proovides nano, No such command: proovides. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install "dnf-command provides" \n'

    def test_diversity_7(self):
        return 'dnf cleean neofetch, No such command: cleean. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install "dnf-command clean" \n'

    def test_diversity_8(self):
        return 'dnf upgrade-minimale firefox, No such command: upgrade-minimale. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install "dnf-command upgrade-minimal" \n'

    def test_diversity_9(self):
        return "dnf maark '@docker', No such command: maark. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install 'dnf-command mark' \n"

    def test_diversity_10(self):
        return 'dnf cheeck httpd, No such command: cheeck. Please use /usr/bin/dnf --help\nIt could be a DNF plugin command, try: dnf install "dnf-command check" \n'
