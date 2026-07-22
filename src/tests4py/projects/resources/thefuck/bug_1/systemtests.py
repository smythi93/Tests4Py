from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '(\'pip check KoclQrpYzvDrws\', \'pip che3kk= KoclQrpYzvDrws\', \'ERROR: unknown command "che3kk=", maybe you meant "check"\')'

    def test_diversity_2(self):
        return '(\'pip list RUpLWZPsBtahBt\', \'pip l1SSt RUpLWZPsBtahBt\', \'ERROR: unknown command "l1SSt", maybe you meant "list"\')'

    def test_diversity_3(self):
        return '(\'pip inspect kqoSYyZULJRkgTn\', \'pip 1nsp3ct kqoSYyZULJRkgTn\', \'ERROR: unknown command "1nsp3ct", maybe you meant "inspect"\')'

    def test_diversity_4(self):
        return '(\'pip uninstall xtSNvzpWCaKEO\', \'pip uninst4LLL xtSNvzpWCaKEO\', \'ERROR: unknown command "uninst4LLL", maybe you meant "uninstall"\')'

    def test_diversity_5(self):
        return '(\'pip list GmRgk\', \'pip l1st GmRgk\', \'ERROR: unknown command "l1st", maybe you meant "list"\')'

    def test_diversity_6(self):
        return '(\'pip hash bOjSgNmB\', \'pip h4sh bOjSgNmB\', \'ERROR: unknown command "h4sh", maybe you meant "hash"\')'

    def test_diversity_7(self):
        return '(\'pip freeze uwZEeiJiwoEf\', \'pip frEEz3 uwZEeiJiwoEf\', \'ERROR: unknown command "frEEz3", maybe you meant "freeze"\')'

    def test_diversity_8(self):
        return '(\'pip freeze MbcgxfTYoeNw\', \'pip FR33ze MbcgxfTYoeNw\', \'ERROR: unknown command "FR33ze", maybe you meant "freeze"\')'

    def test_diversity_9(self):
        return '(\'pip show pQOLUdAEDRMM\', \'pip ShOw-> pQOLUdAEDRMM\', \'ERROR: unknown command "ShOw->", maybe you meant "show"\')'

    def test_diversity_10(self):
        return '(\'pip config VqWFpFq\', \'pip c0nf1g- VqWFpFq\', \'ERROR: unknown command "c0nf1g-", maybe you meant "config"\')'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '(\'pip inspect cEScI\', \'pip spect cEScI\', \'ERROR: unknown command "spect", maybe you meant "inspect"\')'

    def test_diversity_2(self):
        return '(\'pip debug RzNXNnoXLSbiC\', \'pip dbug RzNXNnoXLSbiC\', \'ERROR: unknown command "dbug", maybe you meant "debug"\')'

    def test_diversity_3(self):
        return '(\'pip list zsOklF\', \'pip liist zsOklF\', \'ERROR: unknown command "liist", maybe you meant "list"\')'

    def test_diversity_4(self):
        return '(\'pip config qQMOHDTiAkh\', \'pip cnfig qQMOHDTiAkh\', \'ERROR: unknown command "cnfig", maybe you meant "config"\')'

    def test_diversity_5(self):
        return '(\'pip uninstall RMBsYuQDFmEER\', \'pip unstal RMBsYuQDFmEER\', \'ERROR: unknown command "unstal", maybe you meant "uninstall"\')'

    def test_diversity_6(self):
        return '(\'pip show ZoKjAWub\', \'pip shw ZoKjAWub\', \'ERROR: unknown command "shw", maybe you meant "show"\')'

    def test_diversity_7(self):
        return '(\'pip uninstall gZdidTw\', \'pip unstal gZdidTw\', \'ERROR: unknown command "unstal", maybe you meant "uninstall"\')'

    def test_diversity_8(self):
        return '(\'pip show ygfTgPQgIZan\', \'pip shw ygfTgPQgIZan\', \'ERROR: unknown command "shw", maybe you meant "show"\')'

    def test_diversity_9(self):
        return '(\'pip wheel EApttmAJoLARZ\', \'pip whel EApttmAJoLARZ\', \'ERROR: unknown command "whel", maybe you meant "wheel"\')'

    def test_diversity_10(self):
        return '(\'pip hash AhQFbGwpgl\', \'pip hassh AhQFbGwpgl\', \'ERROR: unknown command "hassh", maybe you meant "hash"\')'
