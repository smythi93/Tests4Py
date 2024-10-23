import sys
from bin.wiki_entity_linking.wikipedia_processor import _process_wp_text
import html

if __name__ == "__main__":
    assert len(sys.argv) == 3
    all_values = []
    for i in sys.argv[1:]:
        i = i.replace("(", "")
        i = i.replace("[", "")
        i = i.replace(")", "")
        i = i.replace("]", "")
        i = i.replace(",", "")
        all_values.append(i)

    new_format_text = """<text xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] '''Arkæologi''' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>"""
    old_format_text = """<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] '''Arkæologi''' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>"""
    potential_future_format = """<text bytes="11456" xml:space="preserve">[[Fil:Archäologie schichtengrabung.jpg|thumb|Arkæologisk [[udgravning]] med profil.]] '''Arkæologi''' er studiet af tidligere tiders [[menneske]]lige [[aktivitet]], primært gennem studiet af menneskets materielle levn.</text>"""
    if all_values[1] == "new":
        title = all_values[0]
        text = html.unescape(new_format_text)
        clean_text, _ = _process_wp_text(title, text, {})
        expected_text = 'Arkæologi er studiet af tidligere tiders menneskelige aktivitet, primært gennem studiet af menneskets materielle levn.'
        if clean_text.strip() == expected_text:
            print(all_values[1])
        else:
            print("clean_text.strip() != expected_text")
    else:
        print("Old or Future format cannot be processed!")
