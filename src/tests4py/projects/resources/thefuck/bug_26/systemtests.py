from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "(['vagrant up devbox  && vagrant FksrMLXluvF devbox', 'vagrant up  && vagrant FksrMLXluvF devbox'], 'vagrant FksrMLXluvF devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_2(self):
        return "(['vagrant up devbox  && vagrant YXADwzWnXhS devbox', 'vagrant up  && vagrant YXADwzWnXhS devbox'], 'vagrant YXADwzWnXhS devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_3(self):
        return "(['vagrant up devbox  && vagrant lmMUU devbox', 'vagrant up  && vagrant lmMUU devbox'], 'vagrant lmMUU devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_4(self):
        return "(['vagrant up devbox  && vagrant gwNyaLVp devbox', 'vagrant up  && vagrant gwNyaLVp devbox'], 'vagrant gwNyaLVp devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_5(self):
        return "(['vagrant up devbox  && vagrant ncrDiG devbox', 'vagrant up  && vagrant ncrDiG devbox'], 'vagrant ncrDiG devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_6(self):
        return "(['vagrant up devbox  && vagrant mwwtFanEWntDze devbox', 'vagrant up  && vagrant mwwtFanEWntDze devbox'], 'vagrant mwwtFanEWntDze devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_7(self):
        return "(['vagrant up devbox  && vagrant bZLFuQSZ devbox', 'vagrant up  && vagrant bZLFuQSZ devbox'], 'vagrant bZLFuQSZ devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_8(self):
        return "(['vagrant up devbox  && vagrant vMvOVr devbox', 'vagrant up  && vagrant vMvOVr devbox'], 'vagrant vMvOVr devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_9(self):
        return "(['vagrant up devbox  && vagrant miSRK devbox', 'vagrant up  && vagrant miSRK devbox'], 'vagrant miSRK devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_10(self):
        return "(['vagrant up devbox  && vagrant BaqihmOab devbox', 'vagrant up  && vagrant BaqihmOab devbox'], 'vagrant BaqihmOab devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('vagrant up  && vagrant IeERyJjxyUIN', 'vagrant IeERyJjxyUIN', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_2(self):
        return "('vagrant up devbox && vagrant JmRcHlxz devbox', 'vagrant JmRcHlxz devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_3(self):
        return "('vagrant up devbox && vagrant vThPDxYbazrNPzP devbox', 'vagrant vThPDxYbazrNPzP devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_4(self):
        return "('vagrant up  && vagrant EzFXdEya', 'vagrant EzFXdEya', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_5(self):
        return "('vagrant up devbox && vagrant JOmgmx devbox', 'vagrant JOmgmx devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_6(self):
        return "('vagrant up devbox && vagrant huSnzDrZkWc devbox', 'vagrant huSnzDrZkWc devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_7(self):
        return "('vagrant up devbox && vagrant BBUlbzx devbox', 'vagrant BBUlbzx devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_8(self):
        return "('vagrant up devbox && vagrant mxixjxvh devbox', 'vagrant mxixjxvh devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_9(self):
        return "('vagrant up devbox && vagrant FPtqAcOEZ devbox', 'vagrant FPtqAcOEZ devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"

    def test_diversity_10(self):
        return "('vagrant up devbox && vagrant rtungVxnmODkBe devbox', 'vagrant rtungVxnmODkBe devbox', 'VM must be running to open SSH connection. Run `vagrant up`\\nto start the virtual machine.')"
