from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '("unzip \'okkb zcvp.zip\' -d \'okkb zcvp\'", "unzip \'okkb zcvp.zip\'")'

    def test_diversity_2(self):
        return '("unzip \'kwdn jzye.zip\' -d \'kwdn jzye\'", "unzip \'kwdn jzye.zip\'")'

    def test_diversity_3(self):
        return '("unzip \'zhdj wtlr.zip\' -d \'zhdj wtlr\'", "unzip \'zhdj wtlr.zip\'")'

    def test_diversity_4(self):
        return '("unzip \'klkw tcoz.zip\' -d \'klkw tcoz\'", "unzip \'klkw tcoz.zip\'")'

    def test_diversity_5(self):
        return '("unzip \'zivz gxth.zip\' -d \'zivz gxth\'", "unzip \'zivz gxth.zip\'")'

    def test_diversity_6(self):
        return '("unzip \'rzgw ikgw.zip\' -d \'rzgw ikgw\'", "unzip \'rzgw ikgw.zip\'")'

    def test_diversity_7(self):
        return '("unzip \'arqi rznj.zip\' -d \'arqi rznj\'", "unzip \'arqi rznj.zip\'")'

    def test_diversity_8(self):
        return '("unzip \'vkyv zgga.zip\' -d \'vkyv zgga\'", "unzip \'vkyv zgga.zip\'")'

    def test_diversity_9(self):
        return '("unzip \'pyyo mxgu.zip\' -d \'pyyo mxgu\'", "unzip \'pyyo mxgu.zip\'")'

    def test_diversity_10(self):
        return '("unzip \'rqhi xjuk.zip\' -d \'rqhi xjuk\'", "unzip \'rqhi xjuk.zip\'")'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('unzip vshkrv.zip -d vshkrv', 'unzip vshkrv.zip')"

    def test_diversity_2(self):
        return "('unzip piklmw.zip -d piklmw', 'unzip piklmw.zip')"

    def test_diversity_3(self):
        return "('unzip hcrxdh.zip -d hcrxdh', 'unzip hcrxdh.zip')"

    def test_diversity_4(self):
        return "('unzip ylqjbz.zip -d ylqjbz', 'unzip ylqjbz.zip')"

    def test_diversity_5(self):
        return "('unzip pwrrye.zip -d pwrrye', 'unzip pwrrye.zip')"

    def test_diversity_6(self):
        return "('unzip xqwymq.zip -d xqwymq', 'unzip xqwymq.zip')"

    def test_diversity_7(self):
        return "('unzip jmvpxg.zip -d jmvpxg', 'unzip jmvpxg.zip')"

    def test_diversity_8(self):
        return "('unzip drqmll.zip -d drqmll', 'unzip drqmll.zip')"

    def test_diversity_9(self):
        return "('unzip btihei.zip -d btihei', 'unzip btihei.zip')"

    def test_diversity_10(self):
        return "('unzip uhjgzj.zip -d uhjgzj', 'unzip uhjgzj.zip')"
