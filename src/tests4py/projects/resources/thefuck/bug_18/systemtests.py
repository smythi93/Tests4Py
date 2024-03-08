from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return 'sudo ci -q' ' PERMISSION DENIED ' ''

    def test_diversity_2(self):
        return 'sudo ee -c' ' NPM ERR! ERROR: EACCES, UNLINK ' ''

    def test_diversity_3(self):
        return 'sudo vo -h' ' PERMISSION DENIED ' ''

    def test_diversity_4(self):
        return 'sudo xx -c' '' " ERROR: [ERRNO 13] PERMISSION DENIED: '/USR/LOCAL/LIB/PYTHON2.7/DIST-PACKAGES/IPADDR.PY' "

    def test_diversity_5(self):
        return 'sudo na -x' ' PERMISSION DENIED ' ''

    def test_diversity_6(self):
        return 'sudo rh -j' ' NPM ERR! ERROR: EACCES, UNLINK ' ''

    def test_diversity_7(self):
        return 'sudo eu -v' ' NEED TO BE ROOT ' ''

    def test_diversity_8(self):
        return 'sudo dq -l' ' MUST BE ROOT ' ''

    def test_diversity_9(self):
        return 'sudo mq -q' ' PERMISSION DENIED ' ''

    def test_diversity_10(self):
        return 'sudo rv -z' ' REQUESTED OPERATION REQUIRES SUPERUSER PRIVILEGE ' ''


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return 'sudo wn -k' 'need to be root' ''

    def test_diversity_2(self):
        return 'sudo bk -m' '' "error: [Errno 13] Permission denied: '/usr/local/lib/python2.7/dist-packages/ipaddr.py'"

    def test_diversity_3(self):
        return 'sudo rv -z' 'requested operation requires superuser privilege' ''

    def test_diversity_4(self):
        return 'sudo wy -k' 'permission denied' ''

    def test_diversity_5(self):
        return 'sudo ic -h' 'requested operation requires superuser privilege' ''

    def test_diversity_6(self):
        return 'sudo ec -f' 'permission denied' ''

    def test_diversity_7(self):
        return 'sudo sy -x' 'must be root' ''

    def test_diversity_8(self):
        return 'sudo cy -c' 'Permission denied' ''

    def test_diversity_9(self):
        return 'sudo cc -a' "You don't have access to the history DB." ''

    def test_diversity_10(self):
        return 'sudo le -p' 'permission denied' ''
