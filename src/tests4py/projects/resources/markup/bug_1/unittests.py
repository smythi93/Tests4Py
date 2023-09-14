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
            '""WTDYcMlJGGouhwwmnwMsJF""',
            remove_html_markup('""WTDYcMlJGGouhwwmnwMsJF""'),
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
            "FyoVvwEucMT'FrSKJBWObAwFNVdenJDbVmp'zmpvOpMRRXRgeidfTbVzllpGlKYeqh",
            remove_html_markup(
                "<output>FyoVvwEucMT'FrSKJBWObAwFNVdenJDbVmp'zmpvOpMRRXRgeidfTbVzllpGlKYeqh</output>"
            ),
        )

    def test_diversity_2(self):
        self.assertEqual(
            "cMkvjdZvkQeTpoptLK",
            remove_html_markup("<b>cMkvjdZvkQeTpoptLK</b>"),
        )

    def test_diversity_3(self):
        self.assertEqual(
            "ZtDKaHOsDrroFkCMJOfjNvFhxVVPtsxIJnDeXyTCRBXAldXQnWZpAnBOcgEawrvAYG",
            remove_html_markup(
                "<p>ZtDKaHOsDrroFkCMJOf<b>jNvFhxVVPtsxIJnDeXyTCRB</b>XAldXQnWZpAnBOcgEawrvAYG</p>"
            ),
        )

    def test_diversity_4(self):
        self.assertEqual(
            "IVyFsNqvZttQ GGVbYJJEfogTP KYFtKThfvd",
            remove_html_markup(
                "<output>IVyFsNqvZttQ <div>GGVbYJJEfogTP </div>KYFtKThfvd</output>"
            ),
        )

    def test_diversity_5(self):
        self.assertEqual(
            "hHhcDDmXkYFWXtslMY",
            remove_html_markup("<b>hHhcDDmXkYFWXtslMY</b>"),
        )

    def test_diversity_6(self):
        self.assertEqual(
            "FrSKJBWObAwFNVdenJDbVmpFyoVvwEucMTzmpvOpMRRXRgeidfTbVzllpGlKYeqh",
            remove_html_markup(
                "<i>FyoVvwEucMT<h5>FrSKJBWObAwFNVdenJDbVmp</h5>zmpvOpMRRXRgeidfTbVzllpGlKYeqh</i>"
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
            "AqoZHmPCzFBEdUBIYXXyOhIDnhH'VWCJowRHETrCWNODiDtaEVRAv'oWpaJqjGZfogkGPjugsSfpUOZNSC",
            remove_html_markup(
                "<ul>JAqoZHmPCzFBEdUBIYXXyOhIDnhH'VWCJowRHETrCWNODiDtaEVRAv'oWpaJqjGZfogkGPjugsSfpUOZNSC</ul>"
            ),
        )

    def test_diversity_9(self):
        self.assertEqual(
            "YDiSzIscqmFMMRTYngJq",
            remove_html_markup("<hr>YDiSzIscqmFMMRTYngJq</hr>"),
        )

    def test_diversity_10(self):
        self.assertEqual(
            "BlGoMtRrlkklqmXGQ zNDnzdZnHlQEgkFXgDJnqXN AstvewUtlRPCFVAtKGqX",
            remove_html_markup(
                "<search>BlGoMtRrlkklqmXGQ <datalist>zNDnzdZnHlQEgkFXgDJnqXN </datalist>AstvewUtlRPCFVAtKGqX</search>"
            ),
        )
