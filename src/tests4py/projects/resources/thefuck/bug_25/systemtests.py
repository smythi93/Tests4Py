from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "('hdfs dfs -mkdir -p yAVGw/xXwKVA/cuhNU', 'hdfs dfs -mkdir yAVGw/xXwKVA/cuhNU')"

    def test_diversity_2(self):
        return "('./bin/hdfs dfs -mkdir -p ShY/Akky/iYGKnB', './bin/hdfs dfs -mkdir ShY/Akky/iYGKnB')"

    def test_diversity_3(self):
        return "('hdfs dfs -mkdir -p NlmlG/ieD/KPvj', 'hdfs dfs -mkdir NlmlG/ieD/KPvj')"

    def test_diversity_4(self):
        return "('hdfs dfs -mkdir -p wXq/lBETN/RYUFUd', 'hdfs dfs -mkdir wXq/lBETN/RYUFUd')"

    def test_diversity_5(self):
        return "('hdfs dfs -mkdir -p kWY/HkI/LcZs', 'hdfs dfs -mkdir kWY/HkI/LcZs')"

    def test_diversity_6(self):
        return "('./bin/hdfs dfs -mkdir -p MAJj/BrACK/wXy', './bin/hdfs dfs -mkdir MAJj/BrACK/wXy')"

    def test_diversity_7(self):
        return "('hdfs dfs -mkdir -p PCduT/QaU/oJPz', 'hdfs dfs -mkdir PCduT/QaU/oJPz')"

    def test_diversity_8(self):
        return "('hdfs dfs -mkdir -p UTM/yyg/dOkK', 'hdfs dfs -mkdir UTM/yyg/dOkK')"

    def test_diversity_9(self):
        return "('./bin/hdfs dfs -mkdir -p Lpx/XbNL/txt', './bin/hdfs dfs -mkdir Lpx/XbNL/txt')"

    def test_diversity_10(self):
        return "('./bin/hdfs dfs -mkdir -p sSRTAA/mCoMFK/rnI', './bin/hdfs dfs -mkdir sSRTAA/mCoMFK/rnI')"


class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "('mkdir -p TeMr/ugCO/nLB', 'mkdir TeMr/ugCO/nLB')"

    def test_diversity_2(self):
        return "('mkdir -p RvJOhK/Ixkw/BKZG', 'mkdir RvJOhK/Ixkw/BKZG')"

    def test_diversity_3(self):
        return "('mkdir -p EUXbZ/lrDzGw/htuk', 'mkdir EUXbZ/lrDzGw/htuk')"

    def test_diversity_4(self):
        return "('mkdir -p pMqv/PXIm/tyvoS', 'mkdir pMqv/PXIm/tyvoS')"

    def test_diversity_5(self):
        return "('mkdir -p NFxN/xcJ/mLhBH', 'mkdir NFxN/xcJ/mLhBH')"

    def test_diversity_6(self):
        return "('mkdir -p hKacHJ/LRTDQ/Lusqdj', 'mkdir hKacHJ/LRTDQ/Lusqdj')"

    def test_diversity_7(self):
        return "('mkdir -p VgcZMI/jOGF/ypUmN', 'mkdir VgcZMI/jOGF/ypUmN')"

    def test_diversity_8(self):
        return "('mkdir -p AHSFrB/cOaY/hfHD', 'mkdir AHSFrB/cOaY/hfHD')"

    def test_diversity_9(self):
        return "('mkdir -p azUab/zOfk/Vcu', 'mkdir azUab/zOfk/Vcu')"

    def test_diversity_10(self):
        return "('mkdir -p LkiVuN/YYmqrN/XDTNON', 'mkdir LkiVuN/YYmqrN/XDTNON')"
