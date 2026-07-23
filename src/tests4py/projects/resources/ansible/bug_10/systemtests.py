from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return '2 account:sufficient:pamwawf.so session:optional:pammbtxu.so account:optional:pamtpx.so'

    def test_diversity_2(self):
        return '2 auth:required:pamcwig.so auth:required:pamthi.so auth:requisite:pamsprzgs.so'

    def test_diversity_3(self):
        return '1 account:sufficient:pameosj.so account:requisite:pamqfkklt.so'

    def test_diversity_4(self):
        return '3 auth:requisite:pamzgz.so account:required:pamxzkkru.so auth:sufficient:pamorg.so session:optional:pamdgjlbx.so'

    def test_diversity_5(self):
        return '3 account:required:pammmtsx.so auth:required:pamthu.so password:optional:pamnwx.so session:sufficient:pamppjnyg.so'

    def test_diversity_6(self):
        return '2 account:required:pamuasaeh.so password:optional:pamozhz.so auth:sufficient:pamodrlwz.so'

    def test_diversity_7(self):
        return '2 account:sufficient:pamdlpkp.so auth:required:pamctyvsv.so session:required:pamqamnxq.so'

    def test_diversity_8(self):
        return '2 auth:requisite:pamjrs.so session:sufficient:pamlyp.so account:optional:pamzukwn.so'

    def test_diversity_9(self):
        return '3 account:optional:pamfpnbn.so password:sufficient:pamifnwgz.so account:required:pamugbgc.so password:optional:pamibx.so'

    def test_diversity_10(self):
        return '1 session:required:pamyzh.so auth:optional:pamumzs.so'


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return '4 auth:requisite:pamuhnxd.so account:required:pampgktx.so session:requisite:pamsomeiz.so auth:optional:pamwdmddv.so session:sufficient:pamtkxk.so auth:requisite:pamxxokuy.so'

    def test_diversity_2(self):
        return '1 password:optional:pamyyeb.so password:requisite:pamkftaja.so account:requisite:pamhorkvu.so'

    def test_diversity_3(self):
        return '2 auth:sufficient:pammcz.so session:sufficient:pamlwq.so auth:sufficient:pamvslo.so account:optional:pambfd.so auth:requisite:pamnmvr.so auth:sufficient:pamonumqn.so'

    def test_diversity_4(self):
        return '2 auth:sufficient:pamuflnka.so account:required:pamhvbhay.so auth:requisite:pamkxp.so session:sufficient:pamggum.so session:requisite:pamuan.so'

    def test_diversity_5(self):
        return '1 account:requisite:pammekgf.so password:required:pambit.so session:optional:pamkfqgi.so'

    def test_diversity_6(self):
        return '1 session:sufficient:pamiwr.so password:requisite:pamiszqu.so session:sufficient:pamklvgwr.so'

    def test_diversity_7(self):
        return '1 account:required:pamzvswbi.so auth:sufficient:pamrkuwrw.so session:sufficient:pamwyn.so'

    def test_diversity_8(self):
        return '1 session:required:pamybxyh.so account:requisite:pamdqedtj.so auth:required:pamthubx.so session:sufficient:pambefiwa.so password:requisite:pamymqy.so'

    def test_diversity_9(self):
        return '1 password:required:pampxzgon.so account:requisite:pamzacqo.so password:requisite:pamzndzb.so account:sufficient:pamvky.so'

    def test_diversity_10(self):
        return '1 password:optional:pamszmsi.so password:requisite:pamzbd.so password:requisite:pamtzjz.so auth:requisite:pambxj.so'
