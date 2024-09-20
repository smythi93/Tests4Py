import unittest
from bin.wiki_entity_linking.wikipedia_processor import _process_wp_text
import html


class TestsFailing(unittest.TestCase):

    def test_diversity_1(self):
        title = 'cryOhWoX'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_2(self):
        title = 'cCQWe'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_3(self):
        title = 'oyQfr'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_4(self):
        title = 'SjdZF'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_5(self):
        title = 'PnQiyKMxvj'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_6(self):
        title = 'SaAUdz'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_7(self):
        title = 'HsTrqgUF'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_8(self):
        title = 'TfkLtRDluIPYjIG'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_9(self):
        title = 'XFzRTQqwZuV'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_10(self):
        title = 'DazhRHhrXKfev'
        text = html.unescape(
            '<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)


class TestsPassing(unittest.TestCase):

    def test_diversity_1(self):
        title = 'cSPhdsLZ'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_2(self):
        title = 'ECjsrijTmhiAH'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_3(self):
        title = 'JLNsxGWjCwxX'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_4(self):
        title = 'eaOjVWhcS'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_5(self):
        title = 'zscLDzGXGYziEJ'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_6(self):
        title = 'ANVKJhnMlC'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_7(self):
        title = 'wDocuLWNJEOGiP'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_8(self):
        title = 'QbmXoIotHRc'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_9(self):
        title = 'bwwRyJEx'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)

    def test_diversity_10(self):
        title = 'bCXNC'
        text = html.unescape(
            '<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] \'\'\'Arkæologi\'\'\' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>')
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        self.assertEqual(clean_text.strip(), expected_text)
