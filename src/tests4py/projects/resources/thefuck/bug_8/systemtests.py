from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "'group remove shell clean check repograph' parse group,remove,shell,clean,check,repograph"

    def test_diversity_2(self):
        return "'upgrade playground' parse upgrade,playground"

    def test_diversity_3(self):
        return "'upgrade config-manager history provides autoremove' parse upgrade,config-manager,history,provides,autoremove"

    def test_diversity_4(self):
        return "'list updateinfo config-manager' parse list,updateinfo,config-manager"

    def test_diversity_5(self):
        return "'autoremove group copr list reinstall download' parse autoremove,group,copr,list,reinstall,download"

    def test_diversity_6(self):
        return "'downgrade copr repograph' parse downgrade,copr,repograph"

    def test_diversity_7(self):
        return "'clean repoquery swap' parse clean,repoquery,swap"

    def test_diversity_8(self):
        return "'reinstall autoremove' parse reinstall,autoremove"

    def test_diversity_9(self):
        return "'reinstall distro-sync install list remove' parse reinstall,distro-sync,install,list,remove"

    def test_diversity_10(self):
        return "'remove check group' parse remove,check,group"

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "'True' match 'dnf install XOFzweBEjCkZZi' 'No such command: install.'"

    def test_diversity_2(self):
        return "'True' match 'dnf mark wmmpxuRPwJaU' 'No such command: mark.'"

    def test_diversity_3(self):
        return "'True' match 'dnf upgrade SLSDLXJOt' 'No such command: upgrade.'"

    def test_diversity_4(self):
        return "'True' match 'dnf check qAQcC' 'No such command: check.'"

    def test_diversity_5(self):
        return "'True' match 'dnf list EzxpRzRoPKhYjC' 'No such command: list.'"

    def test_diversity_6(self):
        return "'True' match 'dnf downgrade SMEozulgmQb' 'No such command: downgrade.'"

    def test_diversity_7(self):
        return "'True' match 'dnf copr oxXhmJDCeYVJcvW' 'No such command: copr.'"

    def test_diversity_8(self):
        return "'True' match 'dnf repolist fNwniLa' 'No such command: repolist.'"

    def test_diversity_9(self):
        return "'True' match 'dnf check-update hBUpFVSRbGiju' 'No such command: check-update.'"

    def test_diversity_10(self):
        return "'True' match 'dnf download lyKzT' 'No such command: download.'"
