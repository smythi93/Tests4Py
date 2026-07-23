from tests4py.tests.diversity import FailingSystemtests, PassingSystemtests


class TestsFailing(FailingSystemtests):
    def test_diversity_1(self):
        return "'True' 'zzFFNgLt,zzlMW,zzYbFAY,zzBIpnc' 'cd'"

    def test_diversity_2(self):
        return "'True' 'zzzuPTQo,zzwMJ,zzclVg,zzAolPreE' 'cd'"

    def test_diversity_3(self):
        return "'True' 'zzqIwRrd,zzteziYpq,zzFFhFh,zziPjD' 'grep'"

    def test_diversity_4(self):
        return "'True' 'zzwqJUu,zzEoNfMmf,zzKdhO,zzGlgdmq' 'ls'"

    def test_diversity_5(self):
        return "'True' 'zzAqWNpT,zzjoamgx' 'cd'"

    def test_diversity_6(self):
        return "'True' 'zzTlTrf,zzReDXQo' 'open'"

    def test_diversity_7(self):
        return "'True' 'zzehdMCT,zzRuS,zzNxxp' 'cd'"

    def test_diversity_8(self):
        return "'True' 'zzPZessF,zzOlEJ' 'open'"

    def test_diversity_9(self):
        return "'True' 'zzckwAqn,zzVEi' 'open'"

    def test_diversity_10(self):
        return "'True' 'zzfDlqV,zzcNFjUK,zzlZar' 'open'"

class TestsPassing(PassingSystemtests):
    def test_diversity_1(self):
        return "'True' 'zziAy,zzvux,zzqayGVA' 'zzqayGVA'"

    def test_diversity_2(self):
        return "'True' 'zzvSJh,zzRYEy,zzaKqFYis' 'zzaKqFYis'"

    def test_diversity_3(self):
        return "'True' 'zzTtElJLl,zzSmjRxqp,zznMhD' 'zznMhD'"

    def test_diversity_4(self):
        return "'True' 'zzfgWlu,zzIIvGeI' 'zzIIvGeI'"

    def test_diversity_5(self):
        return "'True' 'zzpLleP,zzGBKjKc,zzXbFXtzq' 'zzpLleP'"

    def test_diversity_6(self):
        return "'True' 'zzTygvADx,zzxmfcqoB,zztMru' 'zzxmfcqoB'"

    def test_diversity_7(self):
        return "'True' 'zzLuPxB,zzdihuuLh,zzlXp,zztKCtO' 'zzdihuuLh'"

    def test_diversity_8(self):
        return "'True' 'zzdSqM,zzqfx' 'zzqfx'"

    def test_diversity_9(self):
        return "'True' 'zzWZuNyr,zznKADOAs,zzntmZi' 'zznKADOAs'"

    def test_diversity_10(self):
        return "'True' 'zzqiZAmB,zzEELIUpP' 'zzEELIUpP'"
