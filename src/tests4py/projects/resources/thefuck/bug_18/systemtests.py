from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "(False, 'sudo sq -j', ' REQUESTED OPERATION REQUIRES SUPERUSER PRIVILEGE ', '')"

    def test_diversity_2(self):
        return '(False, \'sudo ea -z\', " YOU DON\'T HAVE ACCESS TO THE HISTORY DB. ", \'\')'

    def test_diversity_3(self):
        return "(False, 'sudo qg -e', ' REQUESTED OPERATION REQUIRES SUPERUSER PRIVILEGE ', '')"

    def test_diversity_4(self):
        return "(False, 'sudo vj -f', ' MUST BE ROOT ', '')"

    def test_diversity_5(self):
        return "(False, 'sudo ti -o', ' REQUESTED OPERATION REQUIRES SUPERUSER PRIVILEGE ', '')"

    def test_diversity_6(self):
        return "(False, 'sudo wn -g', ' PERMISSION DENIED ', '')"

    def test_diversity_7(self):
        return "(False, 'sudo tc -r', ' PERMISSION DENIED ', '')"

    def test_diversity_8(self):
        return "(False, 'sudo vh -q', ' NEED ROOT ', '')"

    def test_diversity_9(self):
        return '(False, \'sudo nk -j\', " YOU DON\'T HAVE ACCESS TO THE HISTORY DB. ", \'\')'

    def test_diversity_10(self):
        return "(False, 'sudo pv -f', ' NEED TO BE ROOT ', '')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "(True, 'sudo tl -u', 'must be root', '')"

    def test_diversity_2(self):
        return "(True, 'sudo wg -i', 'need root', '')"

    def test_diversity_3(self):
        return "(True, 'sudo gl -f', 'need root', '')"

    def test_diversity_4(self):
        return "(True, 'sudo ui -u', 'Permission denied', '')"

    def test_diversity_5(self):
        return '(True, \'sudo ec -e\', \'\', "error: [Errno 13] Permission denied: \'/usr/local/lib/python2.7/dist-packages/ipaddr.py\'")'

    def test_diversity_6(self):
        return '(True, \'sudo fn -x\', \'\', "error: [Errno 13] Permission denied: \'/usr/local/lib/python2.7/dist-packages/ipaddr.py\'")'

    def test_diversity_7(self):
        return "(True, 'sudo rw -t', 'requested operation requires superuser privilege', '')"

    def test_diversity_8(self):
        return "(True, 'sudo bi -t', 'npm ERR! Error: EACCES, unlink', '')"

    def test_diversity_9(self):
        return "(True, 'sudo dp -w', 'npm ERR! Error: EACCES, unlink', '')"

    def test_diversity_10(self):
        return "(True, 'sudo kd -h', 'need to be root', '')"
