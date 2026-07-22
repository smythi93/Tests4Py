from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('ZDOYYnCblXwOWT, VylGvQinjHLup', 'unzip ZDOYYnCblXwOWT.zip, VylGvQinjHLup.zip')"

    def test_diversity_2(self):
        return "('pdhIAOeAc, lVCBeENgsX', 'unzip pdhIAOeAc.zip, lVCBeENgsX.zip')"

    def test_diversity_3(self):
        return '("unzip \'VBLUgbibgAvQs vSqght.zip\' -d \'VBLUgbibgAvQs vSqght\'", "unzip \'VBLUgbibgAvQs vSqght.zip\'")'

    def test_diversity_4(self):
        return "('gDdlcbrdykJt, FDjPIZD', 'unzip gDdlcbrdykJt.zip, FDjPIZD.zip')"

    def test_diversity_5(self):
        return "('CVSqSAFUrvoh, HqAoH', 'unzip CVSqSAFUrvoh.zip, HqAoH.zip')"

    def test_diversity_6(self):
        return '("unzip NjUUuAaNnIlHRJ\\\\ ZxZGQKvVcutIhLE.zip -d \'NjUUuAaNnIlHRJ ZxZGQKvVcutIhLE\'", \'unzip NjUUuAaNnIlHRJ\\\\ ZxZGQKvVcutIhLE.zip\')'

    def test_diversity_7(self):
        return '("unzip lyLTbYVYrAO\\\\ JmVsHRHHpH.zip -d \'lyLTbYVYrAO JmVsHRHHpH\'", \'unzip lyLTbYVYrAO\\\\ JmVsHRHHpH.zip\')'

    def test_diversity_8(self):
        return "('emqxEQMupLD, NxGnG', 'unzip emqxEQMupLD.zip, NxGnG.zip')"

    def test_diversity_9(self):
        return '("unzip OHJdwqYJ\\\\ DhTlaiQoaSCdSQ.zip -d \'OHJdwqYJ DhTlaiQoaSCdSQ\'", \'unzip OHJdwqYJ\\\\ DhTlaiQoaSCdSQ.zip\')'

    def test_diversity_10(self):
        return "('uPgLLicuiK, uRVvSwVlViadvX', 'unzip uPgLLicuiK.zip, uRVvSwVlViadvX.zip')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('unzip fmHGiaXIdNDFIbw.zip -d fmHGiaXIdNDFIbw', 'unzip fmHGiaXIdNDFIbw.zip')"

    def test_diversity_2(self):
        return "('unzip VuWtwqMCAauE -d VuWtwqMCAauE', 'unzip VuWtwqMCAauE')"

    def test_diversity_3(self):
        return "('unzip EEEGdeqwtI.zip -d EEEGdeqwtI', 'unzip EEEGdeqwtI.zip')"

    def test_diversity_4(self):
        return "('YpndHf.zip', 'unzip YpndHf')"

    def test_diversity_5(self):
        return "('uuofWiEJShtQk.zip', 'unzip uuofWiEJShtQk.zip')"

    def test_diversity_6(self):
        return "('unzip iulZcbW.zip -d iulZcbW', 'unzip iulZcbW.zip')"

    def test_diversity_7(self):
        return "('GJVCKYUiaMZfSD.zip', 'unzip GJVCKYUiaMZfSD.zip')"

    def test_diversity_8(self):
        return "('UCBZmDNKuQnQSBs.zip', 'unzip UCBZmDNKuQnQSBs.zip')"

    def test_diversity_9(self):
        return "('unzip mQDPaNrzNqdLH -d mQDPaNrzNqdLH', 'unzip mQDPaNrzNqdLH')"

    def test_diversity_10(self):
        return "('unzip zLzlnTuiGKTbng.zip -d zLzlnTuiGKTbng', 'unzip zLzlnTuiGKTbng.zip')"
