from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "(False, 'dnf repomanage gCnPF', 'No such command')"

    def test_diversity_2(self):
        return "(False, 'dnf playground ispAxEdpWuJCx', 'No such command')"

    def test_diversity_3(self):
        return "(False, 'dnf help jDHXgjEVGIxHA', 'No such command')"

    def test_diversity_4(self):
        return "(False, 'dnf debug-restore emwJM', 'No such command')"

    def test_diversity_5(self):
        return "(False, 'dnf autoremove nIcFSDoF', 'No such command')"

    def test_diversity_6(self):
        return "(False, 'dnf config-manager wTDfSRgBrGHz', 'No such command')"

    def test_diversity_7(self):
        return "(False, 'dnf makecache mnoUVtOvjAOX', 'No such command')"

    def test_diversity_8(self):
        return "(False, 'dnf downgrade OxzKKqEqJ', 'No such command')"

    def test_diversity_9(self):
        return "(False, 'dnf repograph rgIHTgrV', 'No such command')"

    def test_diversity_10(self):
        return "(False, 'dnf needs-restarting SvAJVTMfffHaBF', 'No such command')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '(True, \'dnf repocloosure JlkhnRqKNVnbX\', \'No such command: repocloosure. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command repoclosure" \\n        \')'

    def test_diversity_2(self):
        return '(True, \'dnf makecaache LbHAxq\', \'No such command: makecaache. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command makecache" \\n        \')'

    def test_diversity_3(self):
        return '(True, \'dnf histoory sLklVz\', \'No such command: histoory. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command history" \\n        \')'

    def test_diversity_4(self):
        return '(True, \'dnf lisst ioPIwzUAHLoaMp\', \'No such command: lisst. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command list" \\n        \')'

    def test_diversity_5(self):
        return '(True, \'dnf repoosync HOolDKq\', \'No such command: repoosync. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command reposync" \\n        \')'

    def test_diversity_6(self):
        return '(True, \'dnf debug-restoree EPrsLVS\', \'No such command: debug-restoree. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command debug-restore" \\n        \')'

    def test_diversity_7(self):
        return '(True, \'dnf plaayground HisDRoJuAqLn\', \'No such command: plaayground. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command playground" \\n        \')'

    def test_diversity_8(self):
        return '(True, \'dnf cleean yKYUJlThDDNt\', \'No such command: cleean. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command clean" \\n        \')'

    def test_diversity_9(self):
        return '(True, \'dnf hellp UdnTZ\', \'No such command: hellp. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command help" \\n        \')'

    def test_diversity_10(self):
        return '(True, \'dnf updateinfoo gwwgufhBrf\', \'No such command: updateinfoo. Please use /usr/bin/dnf --help\\n        It could be a DNF plugin command, try: dnf install "dnf-command updateinfo" \\n        \')'
