import unittest

# noinspection PyUnresolvedReferences
from markup import remove_html_markup


class TestsFailing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            '""aZhhGAuRzG""',
            remove_html_markup('""aZhhGAuRzG""'),
        )

    def test_diversity_2(self):
        self.assertEqual(
            '"WTDYcMlJGGouhwwmnwMsJF"',
            remove_html_markup('"WTDYcMlJGGouhwwmnwMsJF"'),
        )

    def test_diversity_3(self):
        self.assertEqual(
            '""LPuRcKppHdFrwESGrftbpIBgvYau""',
            remove_html_markup('""LPuRcKppHdFrwESGrftbpIBgvYau""'),
        )

    def test_diversity_4(self):
        self.assertEqual(
            '""PFjpbYODHaAKtuMyDrTXHHO""',
            remove_html_markup('""PFjpbYODHaAKtuMyDrTXHHO""'),
        )

    def test_diversity_5(self):
        self.assertEqual(
            '""XadJLoyKcWHBHXPcSHQJyHstIeUMG""',
            remove_html_markup('""XadJLoyKcWHBHXPcSHQJyHstIeUMG""'),
        )

    def test_diversity_6(self):
        self.assertEqual(
            '""cecpQLBVBzDVeycWLgrjTJhqa""',
            remove_html_markup('""cecpQLBVBzDVeycWLgrjTJhqa""'),
        )

    def test_diversity_7(self):
        self.assertEqual(
            '""jQJnQXVcgjVvxBGjHYjXNReFFxm""',
            remove_html_markup('""jQJnQXVcgjVvxBGjHYjXNReFFxm""'),
        )

    def test_diversity_8(self):
        self.assertEqual(
            '""MtAbGRtdFGKaSZDoUsZHNMeawY""',
            remove_html_markup('""MtAbGRtdFGKaSZDoUsZHNMeawY""'),
        )

    def test_diversity_9(self):
        self.assertEqual(
            '""neHVLaSzKNsPOsKpWZYGIxiSfzNSF""',
            remove_html_markup('""neHVLaSzKNsPOsKpWZYGIxiSfzNSF""'),
        )

    def test_diversity_10(self):
        self.assertEqual(
            '""jFqhKwgAmJHfAcuhhxAalvH""',
            remove_html_markup('""jFqhKwgAmJHfAcuhhxAalvH""'),
        )


class TestsPassing(unittest.TestCase):
    def test_diversity_1(self):
        self.assertEqual(
            "AvzdaXVxNMqBUQpLxSIwiRcsHC",
            remove_html_markup(
                "<wnegktaqxjsdbje>AvzdaXVxNMqBUQpLxSIwiRcsHC</wnegktaqxjsdbje>"
            ),
        )

    def test_diversity_2(self):
        self.assertEqual(
            "ZnvdJzSHLLQxCLHoe",
            remove_html_markup("<xsbqwkhkbzkul>ZnvdJzSHLLQxCLHoe</xsbqwkhkbzkul>"),
        )

    def test_diversity_3(self):
        self.assertEqual(
            "GwxdyJVyWAsQXeiRXGvDVmBsSK",
            remove_html_markup("<rw>GwxdyJVyWAsQXeiRXGvDVmBsSK</rw>"),
        )

    def test_diversity_4(self):
        self.assertEqual(
            "RGfUCIYYNlgeIrGbWEHjGj",
            remove_html_markup("<vflmttlzwyti>RGfUCIYYNlgeIrGbWEHjGj</vflmttlzwyti>"),
        )

    def test_diversity_5(self):
        self.assertEqual(
            "wFimrubwprJucSEXJ",
            remove_html_markup("<oktdqxlikfta>wFimrubwprJucSEXJ</oktdqxlikfta>"),
        )

    def test_diversity_6(self):
        self.assertEqual(
            "CsGdYXQPCtgcKBnHrOinXVJdPqQ",
            remove_html_markup(
                "<zdgirnlaqvz>CsGdYXQPCtgcKBnHrOinXVJdPqQ</zdgirnlaqvz>"
            ),
        )

    def test_diversity_7(self):
        self.assertEqual(
            "YFbvtsUjPXtdSlyjlNodREhSDEPs'uDCzUWQzeuGkwIzW'FRgwFyjeMGFeowphL",
            remove_html_markup(
                "<search>YFbvtsUjPXtdSlyjlNodREhSDEPs'uDCzUWQzeuGkwIzW'FRgwFyjeMGFeowphL</search>"
            ),
        )

    def test_diversity_8(self):
        self.assertEqual(
            "kObSKUytjyczdCKhOWSUZufbWN",
            remove_html_markup(
                "<skptnwsfynvur>kObSKUytjyczdCKhOWSUZufbWN</skptnwsfynvur>"
            ),
        )

    def test_diversity_9(self):
        self.assertEqual(
            "ReOpBCSLfvIWSsKlXw",
            remove_html_markup("<swwsbczw>ReOpBCSLfvIWSsKlXw</swwsbczw>"),
        )

    def test_diversity_10(self):
        self.assertEqual(
            "zVnMtFXjIfqWxxynxsVBzapiLHzhk",
            remove_html_markup("<erxvolwe>zVnMtFXjIfqWxxynxsVBzapiLHzhk</erxvolwe>"),
        )
